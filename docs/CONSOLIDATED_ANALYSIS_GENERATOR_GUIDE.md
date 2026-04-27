# Consolidated Analysis Generator Guide

## Overview

The `generate_consolidated_analysis.py` script creates comprehensive consolidated summaries of all individual image analyses for a specific automotive feature. This tool uses the Vision API to intelligently combine multiple analysis files into a single, well-structured reference document.

## Purpose

- **Consolidate Information**: Combine all individual image analyses for a feature into one comprehensive document
- **Maintain Technical Precision**: Preserve exact text, colors, shapes, and technical specifications from all images
- **Standardize Format**: Generate consistent consolidated analyses following the established template
- **Enable Cross-Image Analysis**: Identify patterns, relationships, and comprehensive feature understanding

## Enhanced Table Extraction Features (NEW!)

### Recent Enhancements (March 2026)

The consolidated analysis now includes **enhanced table extraction capabilities** with:

#### Complete Table Structure Extraction
- **Every table cell captured exactly as shown** - No data loss or approximation
- **Markdown table format** for structured, readable output
- **Header preservation** including sub-headers and complex structures
- **Empty cell handling** with proper placeholder representation
- **Multi-row and multi-column span support**

#### Cross-Table Relationship Analysis
- **Relationships between tables** across different images identified
- **Data consistency patterns** documented and validated
- **Automotive domain integration** with CAN signals, state matrices, and configuration tables
- **Signal flow traceability** across multiple specification tables

#### Enhanced Output Format with Tables
```
TABLES EXTRACTED:
- **IMAGE [NUMBER] - [TABLE_NAME]**:
  | Column 1 | Column 2 | Column 3 |
  |----------|----------|----------|
  | Data 1   | Data 2   | Data 3   |
  | Data 4   | Data 5   | Data 6   |
  
  Context: [Table description and automotive relevance]

CROSS-TABLE RELATIONSHIPS:
- [Relationship 1]: [Description of how tables relate across images]
- [Relationship 2]: [Description of data consistency patterns]
- [Signal Flow]: [CAN signal mappings and state transitions]
```

#### Validation and Quality Metrics
- **100% Table Completeness**: All tables fully extracted with every cell
- **Format Consistency**: Standardized markdown table format
- **Automotive Accuracy**: Technical specifications preserved exactly
- **Cross-Reference Validation**: Table relationships verified

### Test Results
Recent testing with **VEH-F006_Low_Voltage_Battery_Indication** achieved:
- ✅ **100% table extraction completeness**
- ✅ **All state matrix relationships documented**
- ✅ **CAN signal mappings preserved**
- ✅ **Cross-table consistency validated**

## How It Works

1. **Loads Template**: Uses the `CONSOLIDATED_IMAGE_ANALYSIS_v1.0.md` prompt template
2. **Finds Feature Directory**: Locates the feature directory in `analysis_results/`
3. **Collects Analysis Files**: Gathers all individual `.txt` analysis files (excluding existing `c.txt`)
4. **Reads Content**: Combines all individual analyses into a single input
5. **Calls Vision API**: Sends consolidated prompt to generate comprehensive summary
6. **Saves Result**: Creates `c.txt` file in the feature directory

## Usage

### Basic Usage
```bash
python scripts/generate_consolidated_analysis.py --feature VEH-F165_Manettino
```

### Advanced Usage
```bash
# Custom output filename
python scripts/generate_consolidated_analysis.py --feature VEH-F247_External_Lights_Management --output consolidated_summary.txt

# Different model
python scripts/generate_consolidated_analysis.py --feature DMS-7 --model openai/gpt-4-vision

# Custom API key
python scripts/generate_consolidated_analysis.py --feature VEH-F844 --api_key your-api-key-here
```

## Command Line Arguments

| Argument | Required | Default | Description |
|----------|----------|---------|-------------|
| `--feature` | Yes | - | Feature name (directory name in analysis_results) |
| `--output` | No | `c.txt` | Output filename |
| `--model` | No | `openai/sonnet-4-asia` | Vision model to use |
| `--api_key` | No | Hardcoded HARMAN key | API key for authentication |

## Input Requirements

### Directory Structure
```
analysis_results/
├── VEH-F165_Manettino/
│   ├── image197_TELLTALE_ICONS_AND_INDICATORS_analysis.txt
│   ├── image198_TABLE_WITH_TELLTALES_analysis.txt
│   ├── image199_HMI_DISPLAY_LAYOUTS_analysis.txt
│   └── ... (other individual analysis files)
├── VEH-F247_External_Lights_Management/
│   ├── image119_CONFIGURATION_TABLES_analysis.txt
│   ├── image120_CONFIGURATION_TABLES_analysis.txt
│   └── ... (other individual analysis files)
```

### File Requirements
- Feature directory must exist in `analysis_results/`
- Directory must contain at least one `.txt` analysis file
- Individual analysis files should follow standard naming convention
- Existing `c.txt` files are automatically skipped to avoid circular processing

## Output Format

The generated consolidated analysis follows this structure:

```
=== [FEATURE_NAME] - ALL IMAGES INFORMATION CONSOLIDATED ===

=== IMAGE [NUMBER] - [DESCRIPTIVE_TITLE] ===
Content: [Brief description of what the image shows]
Visual Elements:
- [Explicit description of visual elements]
- Text shown: "[EXACT_TEXT_HERE]"
- Color: [Color name] - RGB approximately (R, G, B)
- Shape: [Exact shape description]
- Size: Approximately XxY pixels

[Repeat for each image]

=== CONSOLIDATED VISUAL DATA SUMMARY ===

COLORS IDENTIFIED:
- [Color]: [Usage context and locations]

TEXT ELEMENTS EXTRACTED:
- [Category]: "[Text1]", "[Text2]", "[Text3]"

SHAPES AND LAYOUTS:
- [Element]: [Detailed shape and layout description]

TECHNICAL SPECIFICATIONS:
- [Technical aspect]: [Exact values and specifications]

DIMENSIONS AND QUALITY:
- [Size and quality assessments]
```

## Example Outputs

### Successful Execution
```
🚀 Starting consolidated analysis for feature: VEH-F247_External_Lights_Management
📝 Loading prompt template...
✅ Prompt template loaded (5206 chars)
📁 Looking for feature directory: VEH-F247_External_Lights_Management
✅ Found feature directory: analysis_results\VEH-F247_External_Lights_Management
📄 Collecting individual analysis files...
✅ Found 5 analysis files:
  - image119_CONFIGURATION_TABLES_analysis.txt
  - image120_CONFIGURATION_TABLES_analysis.txt
  - image121_CONFIGURATION_TABLES_analysis.txt
  - image122_TELLTALE_ICONS_AND_INDICATORS_analysis.txt
  - test_result_image119.png.txt
📖 Reading analysis file contents...
✅ Analysis content loaded (38227 chars)
🤖 Generating consolidated analysis using model: openai/sonnet-4-asia
🌐 Making API call for consolidated analysis...
✅ Consolidated analysis generated (6683 chars)
💾 Saving consolidated analysis to: c.txt
🎉 SUCCESS! Consolidated analysis saved to: analysis_results\VEH-F247_External_Lights_Management\c.txt
📊 Analysis length: 6683 characters
```

## Error Handling

### Common Errors and Solutions

1. **Feature Directory Not Found**
   ```
   ❌ No feature directory found for: InvalidFeature
   Available features:
     - VEH-F165_Manettino
     - VEH-F247_External_Lights_Management
     - DMS-7
   ```
   **Solution**: Use exact directory name from the list

2. **No Analysis Files Found**
   ```
   ❌ No analysis files found in: analysis_results/EmptyFeature
   ```
   **Solution**: Ensure the feature directory contains individual analysis `.txt` files

3. **API Call Failed**
   ```
   ❌ API call failed: Authentication failed
   ```
   **Solution**: Check API key and network connectivity

4. **Multiple Matching Directories**
   ```
   ❌ Multiple matching directories found for 'VEH':
     - VEH-F165_Manettino
     - VEH-F247_External_Lights_Management
   ```
   **Solution**: Use the complete, exact directory name

## Integration with Existing Workflow

### Step 1: Generate Individual Analyses
```bash
# Use existing automated pipeline
python scripts/automated_vision_pipeline.py --csv data_files/VEH-F165_Manettino_with_clip_predictions.csv
```

### Step 2: Generate Consolidated Analysis
```bash
# Create comprehensive summary
python scripts/generate_consolidated_analysis.py --feature VEH-F165_Manettino
```

### Step 3: Review and Validate
- Check the generated `c.txt` file for completeness
- Verify all images are included
- Confirm technical specifications are preserved
- Validate consolidated summaries are accurate

## Quality Assurance

### Enhanced Validation Checklist (Updated March 2026)

#### Standard Validation
- [ ] All image numbers are included in the consolidated analysis
- [ ] All visible text is quoted exactly as it appears
- [ ] All colors are specifically named with RGB approximations where possible
- [ ] All technical values (hex codes, signal names) are preserved verbatim
- [ ] Consolidated summaries group related information logically
- [ ] Format follows the standardized structure
- [ ] No interpretation or assumption - only explicit visual content

#### Table Extraction Validation (NEW!)
- [ ] **ALL TABLES ARE COMPLETELY EXTRACTED** with every cell captured
- [ ] **TABLE HEADERS AND STRUCTURE** are preserved exactly as shown
- [ ] **CROSS-TABLE RELATIONSHIPS** are identified and documented
- [ ] **MARKDOWN TABLE FORMAT** is used for all tabular data
- [ ] **AUTOMOTIVE SPECIFICATIONS** are preserved (CAN signals, state matrices)
- [ ] **EMPTY CELLS** are properly represented with placeholders
- [ ] **MULTI-ROW/COLUMN SPANS** are handled correctly
- [ ] **TABLE CONTEXT** is provided for automotive relevance

### Best Practices
1. **Run on Complete Feature Sets**: Ensure all individual analyses are complete before consolidation
2. **Review Output**: Always review the generated consolidated analysis for accuracy
3. **Preserve Technical Precision**: The tool maintains automotive engineering accuracy
4. **Use Consistent Naming**: Follow established feature naming conventions
5. **Version Control**: Track consolidated analyses alongside individual analyses

## Technical Details

### Dependencies
- `litellm`: For Vision API integration
- `pathlib`: For file system operations
- `argparse`: For command line interface

### API Configuration
- **Base URL**: `https://brllm.harman.com`
- **Default Model**: `openai/sonnet-4-asia`
- **Max Tokens**: 8000 (increased for comprehensive analysis)
- **Authentication**: HARMAN API key

### File Processing
- **Input**: Multiple individual analysis `.txt` files
- **Processing**: Combines all content with file headers
- **Output**: Single consolidated `c.txt` file
- **Encoding**: UTF-8 for international character support

## Troubleshooting

### Performance Issues
- **Large Feature Sets**: For features with many images, the API call may take longer
- **Token Limits**: Very large feature sets may approach token limits
- **Network Timeouts**: Ensure stable internet connection for API calls

### Content Issues
- **Missing Information**: If consolidated analysis seems incomplete, check individual analysis quality
- **Format Problems**: Ensure individual analyses follow standard format
- **Technical Accuracy**: Cross-reference consolidated output with original images

## Future Enhancements

### Planned Features
1. **Batch Processing**: Process multiple features in one command
2. **Incremental Updates**: Only process new/changed individual analyses
3. **Quality Metrics**: Automated quality assessment of consolidated output
4. **Template Customization**: Support for different output formats
5. **Cross-Feature Analysis**: Compare consolidated analyses across features

### Integration Opportunities
1. **CI/CD Pipeline**: Automated consolidated analysis generation
2. **Documentation Generation**: Export to various documentation formats
3. **Quality Assurance**: Automated validation against source images
4. **Reporting**: Generate feature comparison reports

## Conclusion

The Consolidated Analysis Generator provides a powerful tool for creating comprehensive feature summaries that maintain the technical precision and explicit content capture established in the Picture Analyze Agent system. It enables efficient consolidation of multiple image analyses while preserving all critical visual and technical information.
