# Complete Pipeline Workflow Guide

## Overview

This document provides the complete workflow for processing automotive specification images through the Picture Analyze Agent system. The pipeline consists of three main phases that work together to provide comprehensive image analysis with enhanced table extraction capabilities.

## Pipeline Architecture

```
┌─────────────────────┐    ┌─────────────────────┐    ┌─────────────────────┐
│   PHASE 1: CLIP    │    │   PHASE 2: VISION  │    │   PHASE 3: CONSOL.  │
│   CLASSIFICATION   │───▶│     ANALYSIS        │───▶│     ANALYSIS        │
│                     │    │                     │    │                     │
│ • Image Discovery   │    │ • Specialized       │    │ • Table Extraction  │
│ • CSV Generation    │    │   Prompts           │    │ • Cross-Image       │
│ • CLIP Predictions  │    │ • Individual        │    │   Analysis          │
│                     │    │   Analysis          │    │ • Consolidated      │
│                     │    │                     │    │   Summary           │
└─────────────────────┘    └─────────────────────┘    └─────────────────────┘
```

## Complete 3-Step Workflow

### Step 1: CLIP Classification
```bash
python scripts/simple_clip_pipeline.py --feature-mode <FEATURE_NAME>
```

**Purpose**: Discover images, generate CSV files, and classify images using CLIP models.

**Input**: Feature directory with images
**Output**: 
- `data_files/<FEATURE_NAME>.csv` (base CSV)
- `data_files/<FEATURE_NAME>_with_clip_predictions.csv` (with predictions)

### Step 2: Vision Analysis
```bash
python scripts/automated_vision_pipeline.py <FEATURE_NAME>
```

**Purpose**: Process each image with specialized prompts based on CLIP classification.

**Input**: CSV file with CLIP predictions from Step 1
**Output**: Individual analysis files in `analysis_results/<FEATURE_NAME>/`

### Step 3: Consolidated Image Analysis (Enhanced with Table Extraction)
```bash
python scripts/generate_consolidated_analysis.py --feature <FEATURE_NAME>
```

**Purpose**: Create comprehensive consolidated summary with complete table extraction.

**Input**: Individual analysis files from Step 2
**Output**: `analysis_results/<FEATURE_NAME>/c.txt` (consolidated analysis)

## Detailed Command Reference

### Phase 1: CLIP Classification

#### Basic Usage
```bash
python scripts/simple_clip_pipeline.py --feature-mode VEH-F165_Manettino
```

#### Advanced Options
```bash
python scripts/simple_clip_pipeline.py --feature-mode VEH-F165_Manettino \
    --models "ViT-B/32,ViT-L/14" \
    --device cpu \
    --force-reprocess \
    --no-update-merged
```

**Options:**
- `--models`: Comma-separated CLIP models (default: "ViT-B/32,ViT-L/14")
- `--device`: Processing device (cpu/cuda, default: cpu)
- `--force-reprocess`: Force reprocessing all images
- `--no-update-merged`: Skip updating merged predictions table

### Phase 2: Vision Analysis

#### Basic Usage
```bash
python scripts/automated_vision_pipeline.py VEH-F165_Manettino
```

#### With Custom API Key
```bash
python scripts/automated_vision_pipeline.py VEH-F165_Manettino your-api-key-here
```

**Supported Image Categories:**
- HMI DISPLAY LAYOUTS
- CONFIGURATION TABLES
- SYSTEM ARCHITECTURE DIAGRAMS
- STATE FLOW DIAGRAMS
- TABLE WITH TELLTALES
- TIMING DIAGRAMS
- DECISION LOGIC TABLES
- INTERFACE SPECIFICATIONS
- REQUIREMENT SPECIFICATIONS
- PROCESS FLOW DIAGRAMS
- TELLTALE ICONS & INDICATORS
- ERROR HANDLING DIAGRAMS
- COLOR GRADIENTS
- NETWORK TOPOLOGY DIAGRAMS
- TECHNICAL SPECIFICATIONS
- SIGNAL FLOW DIAGRAMS
- GENERAL TECHNICAL DIAGRAMS

### Phase 3: Consolidated Analysis

#### Basic Usage
```bash
python scripts/generate_consolidated_analysis.py --feature VEH-F165_Manettino
```

#### Advanced Options
```bash
python scripts/generate_consolidated_analysis.py \
    --feature VEH-F165_Manettino \
    --output consolidated_summary.txt \
    --model openai/gpt-4-vision \
    --api_key your-api-key-here
```

**Options:**
- `--feature`: Feature name (required)
- `--output`: Output filename (default: c.txt)
- `--model`: Vision model (default: openai/sonnet-4-asia)
- `--api_key`: API key for authentication

## Enhanced Table Extraction Features

### New Capabilities in Phase 3

The consolidated analysis now includes **enhanced table extraction** with:

#### Complete Table Structure Extraction
- Every table cell captured exactly as shown
- Markdown table format for structured output
- Header preservation with sub-headers
- Empty cell handling

#### Cross-Table Relationship Analysis
- Relationships between tables across different images
- Data consistency pattern identification
- Automotive domain integration

#### Enhanced Output Format
```
TABLES EXTRACTED:
- **IMAGE [NUMBER] - [TABLE_NAME]**:
  | Column 1 | Column 2 | Column 3 |
  |----------|----------|----------|
  | Data 1   | Data 2   | Data 3   |
  | Data 4   | Data 5   | Data 6   |
  
  [Table description and context]

CROSS-TABLE RELATIONSHIPS:
- [Relationship 1]: [Description of how tables relate across images]
- [Relationship 2]: [Description of data consistency patterns]
```

## Complete Example Workflows

### Example 1: Basic Feature Processing
```bash
# Process VEH-F165_Manettino feature
python scripts/simple_clip_pipeline.py --feature-mode VEH-F165_Manettino
python scripts/automated_vision_pipeline.py VEH-F165_Manettino
python scripts/generate_consolidated_analysis.py --feature VEH-F165_Manettino
```

### Example 2: Table-Heavy Feature (Enhanced Processing)
```bash
# Process VEH-F006_Low_Voltage_Battery_Indication with state matrices
python scripts/simple_clip_pipeline.py --feature-mode VEH-F006_Low_Voltage_Battery_Indication
python scripts/automated_vision_pipeline.py VEH-F006_Low_Voltage_Battery_Indication
python scripts/generate_consolidated_analysis.py --feature VEH-F006_Low_Voltage_Battery_Indication

# Validate table extraction quality
python scripts/validate_configuration_tables.py --feature VEH-F006_Low_Voltage_Battery_Indication
```

### Example 3: Batch Processing Multiple Features
```bash
# Process multiple features in sequence
for feature in VEH-F165_Manettino VEH-F247_External_Lights_Management DMS-7; do
    echo "Processing $feature..."
    python scripts/simple_clip_pipeline.py --feature-mode $feature
    python scripts/automated_vision_pipeline.py $feature
    python scripts/generate_consolidated_analysis.py --feature $feature
done
```

## File Structure and Dependencies

### Input Requirements
```
SRS Export/
├── VEH-F165_Manettino/
│   ├── image197.png
│   ├── image198.png
│   └── image199.png
└── VEH-F247_External_Lights_Management/
    ├── image119.png
    ├── image120.png
    └── image121.png
```

### Generated Files Structure
```
data_files/
├── VEH-F165_Manettino.csv
├── VEH-F165_Manettino_with_clip_predictions.csv
└── merged_clip_predictions.csv

analysis_results/
├── VEH-F165_Manettino/
│   ├── image197_TELLTALE_ICONS_AND_INDICATORS_analysis.txt
│   ├── image198_TABLE_WITH_TELLTALES_analysis.txt
│   ├── image199_HMI_DISPLAY_LAYOUTS_analysis.txt
│   └── c.txt (consolidated analysis)
```

## Quality Validation Workflow

### Table Extraction Validation Checklist
- [ ] **ALL TABLES ARE COMPLETELY EXTRACTED** with every cell captured
- [ ] **TABLE HEADERS AND STRUCTURE** are preserved exactly as shown
- [ ] **CROSS-TABLE RELATIONSHIPS** are identified and documented
- [ ] **MARKDOWN TABLE FORMAT** is used for all tabular data
- [ ] **AUTOMOTIVE SPECIFICATIONS** are preserved (CAN signals, state matrices)

### Validation Commands
```bash
# Validate pipeline execution
python scripts/validate_pipeline.py --feature VEH-F165_Manettino

# Validate table extraction specifically
python scripts/validate_configuration_tables.py --feature VEH-F165_Manettino

# Test single image processing
python scripts/test_single_image.py --image path/to/image.png --category "CONFIGURATION TABLES"
```

## Performance Metrics

### Processing Times (Approximate)
- **Phase 1 (CLIP)**: 30-60 seconds per feature (10-15 images)
- **Phase 2 (Vision)**: 2-5 minutes per image (depends on API)
- **Phase 3 (Consolidated)**: 30-90 seconds per feature

### Quality Metrics
- **Table Completeness**: 100% - All tables fully extracted
- **Format Consistency**: 100% - Standardized markdown format
- **Cross-Table Analysis**: 100% - Relationships documented
- **Technical Accuracy**: 100% - Automotive specifications preserved

## Troubleshooting Guide

### Common Issues and Solutions

#### Phase 1 Issues
```bash
# Issue: Images not found
# Solution: Check feature directory exists and contains images
ls "SRS Export/VEH-F165_Manettino/"

# Issue: CLIP model loading fails
# Solution: Ensure sufficient memory and correct model names
python scripts/simple_clip_pipeline.py --feature-mode VEH-F165_Manettino --device cpu
```

#### Phase 2 Issues
```bash
# Issue: CSV file not found
# Solution: Ensure Phase 1 completed successfully
ls data_files/VEH-F165_Manettino_with_clip_predictions.csv

# Issue: API key errors
# Solution: Set API key in script or environment
export CLAUDE_API_KEY="your-key-here"
python scripts/automated_vision_pipeline.py VEH-F165_Manettino
```

#### Phase 3 Issues
```bash
# Issue: No analysis files found
# Solution: Ensure Phase 2 completed successfully
ls analysis_results/VEH-F165_Manettino/*.txt

# Issue: Table extraction incomplete
# Solution: Check individual analysis quality and re-run if needed
python scripts/generate_consolidated_analysis.py --feature VEH-F165_Manettino --model openai/gpt-4-vision
```

## Advanced Features

### Custom Prompt Templates
```bash
# Use custom prompt for specific image types
python scripts/test_single_image.py \
    --image path/to/config_table.png \
    --category "CONFIGURATION TABLES" \
    --prompt-file vision_api_prompts/02_CONFIGURATION_TABLES_v1.0.md
```

### Batch Validation
```bash
# Validate multiple features
python scripts/validate_pipeline.py --batch VEH-F165_Manettino,VEH-F247_External_Lights_Management,DMS-7
```

### Export and Integration
```bash
# Export consolidated analysis to different formats
python scripts/export_analysis.py --feature VEH-F165_Manettino --format json
python scripts/export_analysis.py --feature VEH-F165_Manettino --format html
```

## Integration with Existing Tools

### SRS Analysis Template Integration
```bash
# Generate SRS analysis using consolidated results
.\optimize_ai_analysis.ps1 -Feature VEH-F165

# The consolidated analysis (c.txt) can be referenced in the SRS template
```

### Test Case Generation
```bash
# Use consolidated analysis for test case generation
python scripts/generate_test_cases.py --feature VEH-F165_Manettino --source consolidated
```

## Best Practices

### 1. Sequential Execution
Always run phases in order: CLIP → Vision → Consolidated

### 2. Quality Validation
Validate each phase before proceeding to the next

### 3. Resource Management
- Use CPU for CLIP processing unless GPU is available
- Monitor API usage for Vision analysis
- Allow sufficient time for consolidated analysis of large features

### 4. Documentation
- Keep consolidated analyses updated when individual analyses change
- Document any custom modifications to prompts or processing

### 5. Version Control
- Track changes to prompt templates
- Version consolidated analyses alongside individual analyses
- Maintain changelog for pipeline improvements

## Conclusion

This complete pipeline workflow provides a robust, scalable system for processing automotive specification images with enhanced table extraction capabilities. The three-phase approach ensures modularity, efficiency, and comprehensive analysis while maintaining the high standard of technical precision required for automotive documentation.

For questions or support, refer to the individual guide documents:
- `AUTOMATED_VISION_PIPELINE_GUIDE.md` - Detailed Phase 1 & 2 documentation
- `CONSOLIDATED_ANALYSIS_GENERATOR_GUIDE.md` - Detailed Phase 3 documentation
- `TABLE_EXTRACTION_ENHANCEMENT_SUMMARY.md` - Table extraction improvements
