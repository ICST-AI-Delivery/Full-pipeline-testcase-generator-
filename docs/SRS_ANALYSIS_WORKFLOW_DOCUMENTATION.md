# SRS Analysis Workflow Documentation

## Overview
This document provides complete workflow documentation for the SRS Analysis and Test Case Generation system, based on the analysis of `SRS_Analysis_TestCase_Generation.txt` and the `optimize_ai_analysis.ps1` script.

## Workflow Components

### 1. Core Prompt File: `SRS_Analysis_TestCase_Generation.txt`
**Purpose**: Comprehensive AI prompt for analyzing SRS (Software Requirements Specification) documents and generating test cases.

**Structure**:
- **Phase 1**: Detailed Analysis (11 mandatory sections)
- **Phase 2**: Test Case Generation
- **Quality Assurance Checklist**
- **Example Output Structure**

### 2. Automation Script: `optimize_ai_analysis.ps1`
**Purpose**: PowerShell script that automates the SRS analysis workflow by:
- Creating structured placeholder files
- Generating AI prompts with feature-specific content
- Providing browser_action instructions for image analysis
- Managing output file organization

## Complete 11-Section Analysis Structure

The workflow generates analysis documents with the following mandatory sections:

1. **Feature Overview and Approval Status**
2. **Requirements Summary**
3. **Visual Elements Analysis**
   - 3.1 Individual Image Analysis
   - 3.2 Consolidated Visual Elements Analysis
   - 3.3 Image-to-Requirement Traceability
4. **Data Structure and Signal Analysis**
5. **Core Functionality and Gaps**
6. **Domain-Specific Analysis**
7. **Formula and Calculation Verification**
8. **Image-to-Test Case Traceability Matrix**
9. **Test Cases**
10. **Test Case Dependency Mapping**
11. **Requirement Matrix**

## Usage Instructions

### Basic Usage
```powershell
.\optimize_ai_analysis.ps1 -Feature "VEH-F165"
```

### Advanced Options
```powershell
# Custom output directory
.\optimize_ai_analysis.ps1 -Feature "VEH-F001" -OutputDir "Custom_Output"

# Skip task description loading
.\optimize_ai_analysis.ps1 -Feature "VEH-F844" -NoTaskDescription

# Display help
.\optimize_ai_analysis.ps1 -Help
```

## Workflow Process

### Step 1: Script Execution
1. Script searches for feature directory in predefined paths
2. Extracts feature name from directory structure
3. Creates timestamped output file with proper naming convention
4. Generates comprehensive AI prompt including:
   - Task description (from README_SRS_ANALYSIS.md)
   - Feature-specific content from .txt files
   - Image analysis instructions with browser_action commands

### Step 2: Placeholder Generation
- Creates structured placeholder file with all 11 mandatory sections
- Includes specific instructions for image analysis using browser_action tool
- Provides clear markers for AI to fill in analysis content

### Step 3: AI Analysis (Manual)
Since no AI CLI tool is available, the workflow provides:
1. Temporary prompt file path for manual AI interface input
2. Clear instructions for performing the analysis
3. Output file path for saving results
4. Cache clearing reminders for memory optimization

## Key Features

### Image Analysis Integration
- Automatic detection of image files in feature directories
- Generation of browser_action tool instructions
- Emphasis on mandatory image viewing and analysis
- Integration with Visual Elements Analysis section

### File Organization
- Standardized naming convention: `{FEATURE}_{FEATURE}_{FEATURE_NAME}_{DATE}_TC Analyze.txt`
- Organized output in "SRS FPI TestCase" directory
- Prevents overwriting existing analysis files

### Verbosity Control
- Configurable output levels (minimal, normal, detailed)
- User-specific configuration support
- Appropriate messaging for different use cases

## Quality Assurance

### Validation Checks
- ✅ All 11 mandatory sections included in placeholder
- ✅ Proper section numbering and structure
- ✅ Image analysis instructions properly integrated
- ✅ Browser_action tool usage emphasized
- ✅ Output file naming convention standardized

### Error Handling
- Feature directory not found validation
- Existing output file detection
- Temporary file cleanup
- Clear error messaging

## Integration with SRS_Analysis_TestCase_Generation.txt

The workflow is fully aligned with the comprehensive prompt requirements:

### Phase 1 Alignment
- All 11 sections from the example output structure are included
- Visual elements analysis emphasizes browser_action tool usage
- Proper traceability matrices are structured

### Phase 2 Alignment
- Test case generation follows the specified format
- Dependency mapping is included as a separate section
- Quality assurance checklist requirements are met

## Best Practices

### For Users
1. Always use the script to ensure consistent structure
2. Follow the manual analysis instructions when AI CLI is unavailable
3. Clear AI cache/context after each analysis to optimize performance
4. Verify all 11 sections are completed before finalizing analysis

### For Maintenance
1. Keep the 11-section structure synchronized with SRS_Analysis_TestCase_Generation.txt
2. Update search paths as needed for different environments
3. Maintain verbosity configuration options
4. Ensure browser_action instructions remain current

## File Dependencies

### Required Files
- `SRS_Analysis_TestCase_Generation.txt` - Core analysis prompt
- `optimize_ai_analysis.ps1` - Automation script
- `README_SRS_ANALYSIS.md` - Task description (optional)

### Generated Files
- Placeholder analysis documents in "SRS FPI TestCase" directory
- Temporary prompt files (automatically cleaned up)

## Conclusion

This workflow provides a complete, automated approach to SRS analysis and test case generation. The integration between the comprehensive prompt file and the PowerShell automation script ensures consistent, high-quality analysis outputs while maintaining flexibility for different features and use cases.

The corrected 11-section structure ensures full compliance with the SRS_Analysis_TestCase_Generation.txt requirements, making this workflow ready for production use.
