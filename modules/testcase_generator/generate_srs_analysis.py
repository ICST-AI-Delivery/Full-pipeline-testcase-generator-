#!/usr/bin/env python3
"""
Sequential SRS Analysis and Test Case Generation Script

This script implements a phased approach to generate comprehensive SRS analysis
and test cases while managing context limits effectively. Each phase appends
to the same output file, building a complete document progressively.

Usage:
    python modules/testcase_generator/generate_srs_analysis.py --phase 1 --feature VEH-F165_Manettino
    python modules/testcase_generator/generate_srs_analysis.py --phase 2 --feature VEH-F165_Manettino
    python modules/testcase_generator/generate_srs_analysis.py --phase 3 --feature VEH-F165_Manettino
    python modules/testcase_generator/generate_srs_analysis.py --phase 4 --feature VEH-F165_Manettino
    python modules/testcase_generator/generate_srs_analysis.py --phase 5 --feature VEH-F165_Manettino
"""

import argparse
import os
import sys
import json
from pathlib import Path
from litellm import completion
from datetime import datetime
import csv
import glob
import re

# Add utils to path for environment management
sys.path.append(str(Path(__file__).parent.parent.parent))
from utils.env_manager import env_manager

def clean_text_for_api(text):
    """Clean text to handle encoding issues for API calls"""
    if not text:
        return text
    
    # Handle common problematic characters
    replacements = {
        '\xa0': ' ',  # Non-breaking space
        '\u2022': '•',  # Bullet point
        '\u2013': '-',  # En dash
        '\u2014': '--',  # Em dash
        '\u2018': "'",  # Left single quotation mark
        '\u2019': "'",  # Right single quotation mark
        '\u201c': '"',  # Left double quotation mark
        '\u201d': '"',  # Right double quotation mark
        '\u2026': '...',  # Horizontal ellipsis
        '\u00d7': 'x',  # Multiplication sign
        '\u00b0': '°',  # Degree symbol
        '\u2192': '->',  # Right arrow
        '\u2190': '<-',  # Left arrow
        '\u2194': '<->',  # Left-right arrow
        '\u2265': '>=',  # Greater than or equal to
        '\u2264': '<=',  # Less than or equal to
        '\u00b1': '+/-',  # Plus-minus sign
        '\u03bc': 'μ',  # Greek letter mu
        '\u03b1': 'α',  # Greek letter alpha
        '\u03b2': 'β',  # Greek letter beta
        '\u03b3': 'γ',  # Greek letter gamma
        '\u03b4': 'δ',  # Greek letter delta
        '\u03c9': 'ω',  # Greek letter omega
        '\u2080': '0',  # Subscript zero
        '\u2081': '1',  # Subscript one
        '\u2082': '2',  # Subscript two
        '\u2083': '3',  # Subscript three
        '\u2084': '4',  # Subscript four
        '\u2085': '5',  # Subscript five
        '\u2086': '6',  # Subscript six
        '\u2087': '7',  # Subscript seven
        '\u2088': '8',  # Subscript eight
        '\u2089': '9',  # Subscript nine
    }
    
    # Apply replacements
    for old_char, new_char in replacements.items():
        text = text.replace(old_char, new_char)
    
    # Remove any remaining non-ASCII characters that might cause issues
    # Keep common extended ASCII characters but remove problematic ones
    text = re.sub(r'[^\x00-\x7F\u00A0-\u00FF\u0100-\u017F\u0180-\u024F]', '?', text)
    
    # Clean up multiple spaces
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()

class SRSAnalysisGenerator:
    def __init__(self, api_key=None):
        """Initialize the SRS Analysis Generator"""
        self.api_key = api_key or env_manager.get_config_value('HARMAN_API_KEY')
        if not self.api_key:
            raise ValueError("HARMAN_API_KEY not found in environment variables")
        # Note: We'll pass api_key directly to completion() calls, no need to set env var
        self.project_root = Path(__file__).parent.parent.parent
        self.analysis_results_dir = self.project_root / "data" / "results"
        self.data_files_dir = self.project_root / "data_files"
        self.srs_export_dir = self.project_root / "SRS FPI Export"
        self.generated_testcases_dir = self.project_root / "generated_testcases(final output)"
        
        # Ensure output directory exists
        self.generated_testcases_dir.mkdir(exist_ok=True)
        
    def find_srs_file(self, feature_name):
        """Find the SRS requirements file for the given feature"""
        # First try direct file paths (legacy structure)
        possible_paths = [
            self.srs_export_dir / f"{feature_name}.txt",
            self.project_root / f"{feature_name}.txt",
            self.project_root / f"{feature_name}_requirements.txt",
        ]
        
        for path in possible_paths:
            if path.exists():
                return path
        
        # Try hierarchical directory structure
        srs_domains = [
            "SRS_Instrument Cluster",
            "SRS_Audio", 
            "SRS_Connectivity",
            "SRS_Diagnostics",
            "SRS_DMS",
            "SRS_HMI Software",
            "SRS_Navigation",
            "SRS_System Architecture",
            "SRS_Tuner"
        ]
        
        searched_paths = []
        
        # Try multiple SRS directory structures
        srs_base_dirs = [
            self.srs_export_dir,  # SRS FPI Export/
            self.srs_export_dir / "SRS Export",  # SRS FPI Export/SRS Export/
            self.project_root / "models" / "Pre-FineTuneLearning Model" / "SRS FPI export"  # models/Pre-FineTuneLearning Model/SRS FPI export/
        ]
        
        for srs_base in srs_base_dirs:
            if not srs_base.exists():
                continue
                
            for domain in srs_domains:
                domain_dir = srs_base / domain / feature_name
                searched_paths.append(str(domain_dir))
                
                if domain_dir.exists() and domain_dir.is_dir():
                    # Look for any .txt files in the feature directory
                    txt_files = list(domain_dir.glob("*.txt"))
                    if txt_files:
                        print(f"Found SRS file in hierarchical structure: {txt_files[0]}")
                        return txt_files[0]
                    
                    # Look for files with feature name
                    for txt_file in txt_files:
                        if feature_name.lower() in txt_file.name.lower():
                            return txt_file
        
        # Search for files containing the feature name in project root
        for txt_file in self.project_root.glob("*.txt"):
            if feature_name.lower() in txt_file.name.lower():
                return txt_file
        
        # Enhanced error message with all searched paths
        error_msg = f"""Could not find SRS requirements file for {feature_name}.

Searched locations:
1. Direct file paths:
   - {self.srs_export_dir / f'{feature_name}.txt'}
   - {self.project_root / f'{feature_name}.txt'}
   - {self.project_root / f'{feature_name}_requirements.txt'}

2. Hierarchical directory structure:"""
        
        for path in searched_paths:
            error_msg += f"\n   - {path}/"
            
        error_msg += f"""

Expected structure: SRS Export/[Domain]/{feature_name}/[requirements_file].txt

Available domains: {', '.join(srs_domains)}

Please ensure the SRS requirements file is placed in the correct location."""
        
        raise FileNotFoundError(error_msg)
    
    def find_consolidated_analysis(self, feature_name):
        """Find the consolidated analysis file (c.txt) for the feature"""
        feature_dir = self.analysis_results_dir / feature_name
        consolidated_file = feature_dir / "c.txt"
        
        if consolidated_file.exists():
            return consolidated_file
        
        # Alternative naming patterns
        alt_files = [
            feature_dir / f"c_{feature_name}.txt",
            feature_dir / f"{feature_name}_consolidated.txt",
        ]
        
        for alt_file in alt_files:
            if alt_file.exists():
                return alt_file
                
        return None
    
    def find_individual_analysis_files(self, feature_name):
        """Find all individual image analysis files for the feature"""
        feature_dir = self.analysis_results_dir / feature_name
        
        if not feature_dir.exists():
            return []
            
        # Find all analysis files except consolidated ones
        analysis_files = []
        for txt_file in feature_dir.glob("*.txt"):
            if txt_file.name not in ["c.txt", f"c_{feature_name}.txt", f"{feature_name}_consolidated.txt"]:
                analysis_files.append(txt_file)
                
        return sorted(analysis_files)
    
    def get_output_file_path(self, feature_name):
        """Get the output file path for the SRS analysis document"""
        return self.generated_testcases_dir / f"{feature_name}_SRS_Analysis_and_TestCases.md"
    
    def load_existing_analysis(self, feature_name):
        """Load existing analysis content if it exists"""
        output_file = self.get_output_file_path(feature_name)
        
        if output_file.exists():
            with open(output_file, 'r', encoding='utf-8') as f:
                return f.read()
        
        return None
    
    def load_srs_prompt_template(self):
        """Load the SRS analysis prompt template"""
        # Template file is in the same directory as this script
        template_file = Path(__file__).parent / "SRS_Analysis_TestCase_Generation.txt"
        
        if not template_file.exists():
            raise FileNotFoundError(f"SRS_Analysis_TestCase_Generation.txt not found at {template_file}")
            
        with open(template_file, 'r', encoding='utf-8') as f:
            return f.read()
    
    def count_requirements_in_srs(self, srs_content):
        """Count the number of requirements in the SRS content"""
        if not srs_content:
            return 0
        
        # Look for requirement patterns - common formats include:
        # - Req. ID: 12345
        # - Requirement ID: 12345
        # - REQ-12345
        # - [12345]
        # - ID: 12345
        
        patterns = [
            r'Req\.\s*ID\s*:\s*(\d+)',  # Req. ID: 12345
            r'Requirement\s*ID\s*:\s*(\d+)',  # Requirement ID: 12345
            r'REQ-(\d+)',  # REQ-12345
            r'ID\s*:\s*(\d+)',  # ID: 12345
            r'\[(\d+)\]',  # [12345]
            r'^\s*(\d{7,})',  # 7+ digit numbers at start of line (common requirement ID format)
        ]
        
        requirement_ids = set()
        
        for pattern in patterns:
            matches = re.findall(pattern, srs_content, re.MULTILINE | re.IGNORECASE)
            for match in matches:
                # Filter out obviously non-requirement numbers (like years, small numbers, etc.)
                if len(match) >= 4:  # Requirement IDs are typically 4+ digits
                    requirement_ids.add(match)
        
        # If no patterns found, try counting lines that look like requirements
        if not requirement_ids:
            # Look for lines that start with numbers or contain "requirement"
            lines = srs_content.split('\n')
            for line in lines:
                line = line.strip()
                if (line and 
                    (re.match(r'^\d+\.', line) or  # Lines starting with number.
                     'requirement' in line.lower() or
                     re.match(r'^\d+\s+', line))):  # Lines starting with number space
                    requirement_ids.add(line[:20])  # Use first 20 chars as unique identifier
        
        count = len(requirement_ids)
        print(f"Found {count} requirements in SRS content")
        return count if count > 0 else 25  # Default fallback if counting fails
    
    def create_phase_prompt(self, phase, feature_name, srs_content, consolidated_analysis, 
                          individual_analyses, existing_content):
        """Create the prompt for a specific phase"""
        
        base_template = self.load_srs_prompt_template()
        
        phase_prompts = {
            1: self.create_phase1_prompt,
            2: self.create_phase2_prompt,
            3: self.create_phase3_prompt,
            4: self.create_phase4_prompt,
            5: self.create_phase5_prompt
        }
        
        if phase not in phase_prompts:
            raise ValueError(f"Invalid phase: {phase}. Must be 1-5.")
            
        return phase_prompts[phase](feature_name, srs_content, consolidated_analysis, 
                                  individual_analyses, existing_content, base_template)
    
    def create_phase1_prompt(self, feature_name, srs_content, consolidated_analysis, 
                           individual_analyses, existing_content, base_template):
        """Create Phase 1 prompt: Foundation Setup using perfected main template sections"""
        
        # Count requirements in SRS content for validation
        requirement_count = self.count_requirements_in_srs(srs_content)
        
        prompt = f"""
# SRS Analysis Phase 1: Foundation Setup

You are tasked with creating the foundation of a comprehensive SRS analysis document for {feature_name}.

## Phase 1 Objectives:
- Create sections 1-2 of the SRS analysis document
- Focus on Feature Overview and Requirements Summary
- Establish the document structure and basic analysis
- **MANDATORY**: Process ALL {requirement_count} requirements found in the SRS document

## Available Inputs:

### SRS Requirements Document:
```
{srs_content}
```

### Consolidated Visual Analysis (if available):
"""
        
        if consolidated_analysis:
            prompt += f"```\n{consolidated_analysis}\n```\n"
        else:
            prompt += "No consolidated visual analysis available for this feature.\n"
        
        prompt += f"""

## Instructions:
Using the SRS Analysis Template, create the initial analysis document with:

### 2.1. Req Feature Overview and Approval Status

-   **Feature ID and Name**: Extract from the source document.
-   **Brief Description**: Write a concise summary of the feature's purpose and functionality. This should clearly explain what the feature does, its main purpose, and how it contributes to the overall system.
-   **Responsible Domain**: Extract from the source document.
-   **Test Stage**: Extract from the source document.
-   **Approval Status**: Check the "Grooming Status" field. If it is not "Approved", mark the feature as "NOT APPROVED" and **stop all further analysis and test case creation for this feature.**
-   **Requirements Approval**: Include a count of approved requirements vs. total requirements (e.g., "15/17 requirements approved (2 obsolete)")
-   **Analysis Date**: Include the current date in YYYY-MM-DD format.

### 2.2. Requirements Summary

-   Summarize all key functional requirements from the source document in a methodical manner using technical approaches
-   Clearly distinguish between active requirements, informational items, Referenced Requirements and exclude the obsolete requirements.

#### 2.2.1 CRITICAL REQUIREMENT ANALYSIS FORMAT (MANDATORY COMPLIANCE)

**ABSOLUTE REQUIREMENT**: You __must__ create **INDIVIDUAL ENTRIES** for each requirement ID. **NO GROUPING OR COMBINING ALLOWED**.

**MANDATORY REQUIREMENT COVERAGE**: You __must__ process ALL {requirement_count} requirements found in the SRS document. Each requirement must have its own individual analysis entry.

**MANDATORY FORMAT FOR EACH REQUIREMENT**:
```
**Req. ID**: [EXACT_REQUIREMENT_ID] - [SPECIFIC_REQUIREMENT_TITLE]
- **Testability**: [High/Medium/Low] - [SPECIFIC_VERIFICATION_METHOD]
- **Dependencies**: [LIST_SPECIFIC_DEPENDENCIES]
- **Implementation**: [SPECIFIC_IMPLEMENTATION_DETAILS]
```

**VALIDATION CHECKPOINTS**:
- [ ] **Individual Entry Check**: Each requirement ID has its own separate entry
- [ ] **Complete Coverage Check**: All {requirement_count} requirements from the SRS document are processed
- [ ] **No Combined Entries**: No entries like "3828029, 3793745, 3793757 - Combined Description"
- [ ] **Specific Titles**: Each entry has a specific, unique title describing that requirement only
- [ ] **Complete Information**: Each entry includes testability, dependencies, and implementation
- [ ] **Source Verification**: Each requirement ID matches exactly with the source SRS document

**FORBIDDEN PRACTICES**:
- ❌ **Combined requirement entries** (e.g., "3828029, 3793745 - Area 1 Specifications")
- ❌ **Generic descriptions** that could apply to multiple requirements
- ❌ **Placeholder requirement IDs** not found in the source document
- ❌ **Grouped functional areas** instead of individual requirement analysis
- ❌ **Incomplete coverage** - skipping any requirements from the SRS document

-   For each requirement, you __must__ include:
    * Testability assessment (how the requirement can be verified)
    * Dependencies on other requirements or signals
    * Implementation considerations or challenges
    * Note any obsolete or problematic requirements with clear marking

### 2.2.1 Requirement Quality Assessment

-   For each requirement with RQA issues:
    * Analyze the specific issues identified (e.g., compound requirements, missing units)
    * Create a mitigation strategy for each issue type:
        - For compound requirements: Break down into atomic test steps
        - For missing units: Define appropriate units and tolerances for testing
        - For negative statements: Convert to positive verification criteria
        - For unclear terms: Define specific, measurable criteria
    * Flag requirements with low RQA scores (<70) for additional test coverage
    * Document how the test cases will address these quality issues

## Output Format:
Create a markdown document starting with:

```markdown
# {feature_name} - SRS Analysis and Test Cases Document

## 1. Feature Overview and Approval Status
[Complete analysis following section 2.1 requirements]

## 2. Requirements Summary
[Individual requirement entries with mandatory format - ALL {requirement_count} requirements must be included]
```

## CRITICAL VALIDATION BEFORE COMPLETION:
Before completing Phase 1, you __must__ verify:
- [ ] All {requirement_count} requirements from the SRS document have individual entries
- [ ] Each requirement follows the mandatory format exactly
- [ ] No requirements are grouped or combined
- [ ] All validation checkpoints are satisfied
- [ ] No forbidden practices are present in the analysis

Focus ONLY on sections 1-2. Do not include any other sections as they will be added in subsequent phases.

**MANDATORY COMPLIANCE**: This phase will be validated for complete requirement coverage. Incomplete processing will require re-execution.
"""
        
        return prompt
    
    def create_phase2_prompt(self, feature_name, srs_content, consolidated_analysis, 
                           individual_analyses, existing_content, base_template):
        """Create Phase 2 prompt: Technical Analysis - Enhanced to preserve individual image distinctions"""
        
        prompt = f"""
# SRS Analysis Phase 2: Technical Analysis

You are continuing the SRS analysis document for {feature_name} by adding technical analysis sections.

## Phase 2 Objectives:
- Add sections 3-4 to the existing document
- Focus on Visual Elements Analysis and Data Structure Analysis
- Leverage consolidated visual analysis while preserving individual image distinctions

## Existing Document Content:
```markdown
{existing_content}
```

## Available Inputs:

### Consolidated Visual Analysis:
"""
        
        if consolidated_analysis:
            prompt += f"```\n{consolidated_analysis}\n```\n"
        else:
            prompt += "No consolidated visual analysis available.\n"
        
        prompt += f"""

## CRITICAL INDIVIDUAL IMAGE PRESERVATION REQUIREMENTS:

### MANDATORY IMAGE SEPARATION PROTOCOL:
1. **Individual Image Analysis**: Each image mentioned in the consolidated analysis MUST be analyzed separately
2. **Distinct Content Preservation**: Maintain unique content for each image - DO NOT combine or merge similar images
3. **Specific Image References**: Use exact image identifiers (e.g., "IMAGE 119", "IMAGE 120") throughout the analysis
4. **Separate Subsections**: Create individual subsections for each image with distinct content
5. **Content Validation**: Ensure each image's unique characteristics, tables, and specifications are preserved

### FORBIDDEN PRACTICES:
- ❌ Combining multiple images into single descriptions (e.g., "Images 119-120 show...")
- ❌ Generic descriptions that could apply to multiple images
- ❌ Merging distinct table content from different images
- ❌ Using placeholder or summary content instead of specific image details

## Instructions:
APPEND the following sections to the existing document using the consolidated visual analysis above with STRICT individual image separation:

3. **Visual Elements Analysis** (Section 2.3)
   - **MANDATORY**: Create separate analysis subsections for each individual image
   - Apply CLIP-based image classification integration per image
   - Use category-specific analysis methodology for each image
   - Extract real content only (no placeholder data) for each specific image
   - Reference specific images individually (e.g., "### IMAGE 119 Analysis", "### IMAGE 120 Analysis")
   - Include human validation visual context integration per image
   - Utilize all visual elements, colors, shapes, and technical specifications from each image's specific data
   - **VALIDATION CHECKPOINT**: Ensure each image has its own distinct subsection with unique content

4. **Data Structure and Signal Analysis** (Section 2.4)
   - **MANDATORY**: Analyze tables and signals from each image separately
   - Document all CAN/Internal signals with complete information per image
   - Create systematic tables for each image's logic using extracted table data
   - Include CAN signal detailed analysis from each image's specific visual data
   - Map signal-to-function relationships using image-specific cross-table relationships
   - Utilize all technical specifications and signal names from each individual image
   - **VALIDATION CHECKPOINT**: Ensure distinct table analysis for each image

## ENHANCED QUALITY VALIDATION REQUIREMENTS:
- [ ] **Individual Image Check**: Each image has its own separate analysis section
- [ ] **Content Uniqueness Check**: No two images share identical descriptions
- [ ] **Specific Reference Check**: All image references use exact identifiers
- [ ] **Table Separation Check**: Tables from different images are analyzed separately
- [ ] **Technical Detail Check**: Each image's unique technical specifications are preserved

## Output Format:
Provide ONLY the new sections to be appended with MANDATORY individual image separation:

```markdown
## 3. Visual Elements Analysis

### IMAGE [X] Analysis
[Specific analysis for this individual image]

### IMAGE [Y] Analysis  
[Specific analysis for this individual image]

[Continue for each image...]

## 4. Data Structure and Signal Analysis

### IMAGE [X] Data Analysis
[Specific data/signal analysis for this individual image]

### IMAGE [Y] Data Analysis
[Specific data/signal analysis for this individual image]

[Continue for each image...]
```

**CRITICAL VALIDATION**: Before completing, verify that each image mentioned in the consolidated analysis has its own individual section with unique, specific content. NO COMBINING OR MERGING OF IMAGES ALLOWED.
"""
        
        return prompt
    
    def create_phase3_prompt(self, feature_name, srs_content, consolidated_analysis, 
                           individual_analyses, existing_content, base_template):
        """Create Phase 3 prompt: Functionality Analysis"""
        
        prompt = f"""
# SRS Analysis Phase 3: Functionality Analysis

You are continuing the SRS analysis document for {feature_name} by adding functionality analysis sections.

## Phase 3 Objectives:
- Add sections 5-8 to the existing document
- Focus on Core Functionality, Domain-Specific Analysis, and Traceability
- Prepare foundation for test case generation

## Existing Document Content:
```markdown
{existing_content}
```

## Instructions:
APPEND the following sections to the existing document:

5. **Core Functionality and Gaps** (Section 2.5)
   - Define validation methods and test design methodology
   - Identify key test scenarios (Priority A)
   - Document main components (Priority B)
   - Note functional gaps (Priority D)

6. **Domain-Specific Analysis** (Section 2.8)
   - Apply appropriate domain-specific analysis based on the feature's domain
   - Include domain-specific verification methods and requirements

7. **Formula and Calculation Verification** (Section 2.7)
   - Create formula validation tables with test inputs
   - Document expected outputs and verification methods
   - Include boundary value and edge case testing

8. **Image-to-Test Case Traceability Matrix** (Section 2.6)
   - Create comprehensive traceability between images and future test cases
   - Include coverage assessment for each image

## Output Format:
Provide ONLY the new sections to be appended:

```markdown
## 5. Core Functionality and Gaps
[Complete functionality analysis]

## 6. Domain-Specific Analysis
[Domain-specific analysis based on feature domain]

## 7. Formula and Calculation Verification
[Formula validation tables and verification methods]

## 8. Image-to-Test Case Traceability Matrix
[Complete image-to-test case traceability]
```

Follow all quality validation requirements from the template.
"""
        
        return prompt
    
    def create_phase4_prompt(self, feature_name, srs_content, consolidated_analysis, 
                           individual_analyses, existing_content, base_template):
        """Create Phase 4 prompt: Test Case Generation"""
        
        prompt = f"""
# SRS Analysis Phase 4: Test Case Generation

You are continuing the SRS analysis document for {feature_name} by adding the test cases section.

## Phase 4 Objectives:
- Add section 9 (Test Cases) to the existing document
- Generate comprehensive, optimized test cases
- Apply all test case design methodologies from the template

## Existing Document Content:
```markdown
{existing_content}
```

## Instructions:
APPEND the test cases section to the existing document:

9. **Test Cases** (Section 3)
   - Apply test case optimization strategy to minimize redundancy
   - Follow the mandatory test case template structure
   - Ensure perfect alignment between test steps and expected results
   - Include visual verification steps from analysis files
   - Apply appropriate priorities (A, B, C, D)
   - Create comprehensive test coverage for all requirements

## Critical Requirements:
- Each test case must follow the exact template structure
- Test Step Description and Expected Results must have 1:1 correspondence
- Include specific CAN signal values and timing information
- Apply test case consolidation rules to optimize efficiency
- Ensure complete requirement coverage

## Output Format:
Provide ONLY the new section to be appended:

```markdown
## 9. Test Cases

### TC_{feature_name}_01_[FUNCTIONALITY]
[Complete test case following template]

### TC_{feature_name}_02_[FUNCTIONALITY]
[Complete test case following template]

[Continue with all necessary test cases...]
```

Follow all quality validation requirements and test case design methodologies from the template.
"""
        
        return prompt
    
    def create_phase5_prompt(self, feature_name, srs_content, consolidated_analysis, 
                           individual_analyses, existing_content, base_template):
        """Create Phase 5 prompt: Final Integration"""
        
        prompt = f"""
# SRS Analysis Phase 5: Final Integration

You are completing the SRS analysis document for {feature_name} by adding the final integration sections.

## Phase 5 Objectives:
- Add sections 10-11 to complete the document
- Create test case dependency mapping and requirement matrix
- Perform final quality validation

## Existing Document Content:
```markdown
{existing_content}
```

## Instructions:
APPEND the final sections to complete the document:

10. **Test Case Dependency Mapping** (Section 3.5)
    - Create comprehensive dependency mapping framework
    - Include execution order optimization
    - Document risk assessment and mitigation strategies

11. **Requirement Matrix** (Section 3.3)
    - Create traceability matrix mapping test cases to requirements
    - Ensure every testable requirement is covered exactly once
    - Apply critical traceability matrix safeguards

## Critical Requirements:
- Validate that all requirements from section 2 appear in the matrix
- Ensure test case names match exactly with section 9
- Apply all mandatory validation checkpoints
- Perform complete quality assurance validation

## Output Format:
Provide ONLY the new sections to be appended:

```markdown
## 10. Test Case Dependency Mapping
[Complete dependency mapping with visual graph]

## 11. Requirement Matrix
[Complete traceability matrix with validation]
```

Apply the strengthened quality assurance framework to ensure document completeness and accuracy.
"""
        
        return prompt
    
    def call_llm_api(self, prompt):
        """Call LLM API using LiteLLM with HARMAN configuration"""
        try:
            # Ensure prompt is properly encoded
            if isinstance(prompt, str):
                # Convert to bytes and back to ensure clean UTF-8
                prompt = prompt.encode('utf-8', errors='replace').decode('utf-8')
            
            response = completion(
                model="openai/sonnet-4-asia",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                api_key=self.api_key,
                base_url="https://brllm.harman.com",
                max_tokens=8000,
                temperature=0.1
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            print(f"Error calling HARMAN LLM API: {e}")
            # Print more details about the error
            import traceback
            print(f"Full error traceback: {traceback.format_exc()}")
            return None
    
    def append_to_file(self, file_path, content):
        """Append content to the analysis file"""
        try:
            with open(file_path, 'a', encoding='utf-8') as f:
                f.write("\n\n" + content)
            print(f"Successfully appended content to {file_path}")
            return True
        except Exception as e:
            print(f"Error appending to file {file_path}: {e}")
            return False
    
    def create_new_file(self, file_path, content):
        """Create a new analysis file"""
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Successfully created new file {file_path}")
            return True
        except Exception as e:
            print(f"Error creating file {file_path}: {e}")
            return False
    
    def run_phase(self, phase, feature_name):
        """Run a specific phase of the SRS analysis"""
        print(f"\n=== Running Phase {phase} for {feature_name} ===")
        
        try:
            # Load SRS requirements file
            srs_file = self.find_srs_file(feature_name)
            print(f"Found SRS file: {srs_file}")
            
            with open(srs_file, 'r', encoding='utf-8') as f:
                srs_content = clean_text_for_api(f.read())
            
            # Load consolidated analysis if available
            consolidated_analysis = None
            consolidated_file = self.find_consolidated_analysis(feature_name)
            if consolidated_file:
                print(f"Found consolidated analysis: {consolidated_file}")
                with open(consolidated_file, 'r', encoding='utf-8') as f:
                    consolidated_analysis = clean_text_for_api(f.read())
            else:
                print("No consolidated analysis found")
            
            # Load individual analysis files
            individual_analyses = self.find_individual_analysis_files(feature_name)
            print(f"Found {len(individual_analyses)} individual analysis files")
            
            # Load existing content for phases 2-5
            existing_content = None
            if phase > 1:
                existing_content = self.load_existing_analysis(feature_name)
                if not existing_content:
                    print(f"Error: No existing analysis found for phase {phase}. Run phase 1 first.")
                    return False
            
            # Create phase-specific prompt
            prompt = self.create_phase_prompt(
                phase, feature_name, srs_content, consolidated_analysis,
                individual_analyses, existing_content
            )
            
            # Clean the final prompt before sending to API
            prompt = clean_text_for_api(prompt)
            
            print("Calling LLM API...")
            response = self.call_llm_api(prompt)
            
            if not response:
                print("Error: No response from LLM API")
                return False
            
            # Save the response
            output_file = self.get_output_file_path(feature_name)
            
            if phase == 1:
                # Create new file for phase 1
                success = self.create_new_file(output_file, response)
            else:
                # Append to existing file for phases 2-5
                success = self.append_to_file(output_file, response)
            
            if success:
                print(f"Phase {phase} completed successfully!")
                print(f"Output saved to: {output_file}")
                return True
            else:
                print(f"Error saving phase {phase} output")
                return False
                
        except Exception as e:
            print(f"Error in phase {phase}: {e}")
            return False
    
    def run_all_phases(self, feature_name):
        """Run all phases sequentially"""
        print(f"\n=== Running All Phases for {feature_name} ===")
        
        for phase in range(1, 6):
            success = self.run_phase(phase, feature_name)
            if not success:
                print(f"Failed at phase {phase}. Stopping execution.")
                return False
            
            # Brief pause between phases
            print(f"Phase {phase} completed. Continuing to next phase...")
        
        print(f"\nAll phases completed successfully for {feature_name}!")
        return True

def main():
    """Main function to handle command line arguments"""
    parser = argparse.ArgumentParser(
        description="Generate SRS Analysis and Test Cases in phases"
    )
    parser.add_argument(
        "--phase", 
        type=int, 
        choices=[1, 2, 3, 4, 5], 
        help="Phase to run (1-5). If not specified, runs all phases."
    )
    parser.add_argument(
        "--feature", 
        type=str, 
        required=True,
        help="Feature name (e.g., VEH-F165_Manettino)"
    )
    parser.add_argument(
        "--api-key",
        type=str,
        help="OpenAI API key (optional, can be set in environment)"
    )
    
    args = parser.parse_args()
    
    # Get API key from argument or environment
    api_key = args.api_key
    
    try:
        # Initialize generator (will get API key from environment if not provided)
        generator = SRSAnalysisGenerator(api_key=api_key)
    except ValueError as e:
        print(f"Error: {e}")
        print("Please add HARMAN_API_KEY=your_api_key_here to your .env file")
        return 1
    
    # Run specified phase or all phases
    if args.phase:
        success = generator.run_phase(args.phase, args.feature)
    else:
        success = generator.run_all_phases(args.feature)
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())
