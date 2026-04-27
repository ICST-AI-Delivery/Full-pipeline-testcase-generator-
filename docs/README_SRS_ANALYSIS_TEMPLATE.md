# SRS Analysis Template Documentation

## Overview

This repository contains a comprehensive template system for analyzing Software Requirements Specification (SRS) features and generating detailed test cases. The system consists of two main components:

1. **SRS_ANALYSIS_TEMPLATE_COMPLETE.md** - A structured template with placeholders for all analysis sections
2. **optimize_ai_analysis.ps1** - A PowerShell script that automates the analysis process

## Template Structure

The template is organized into 11 main sections, each focusing on a specific aspect of the SRS analysis:

1. **Feature Overview and Approval Status** - Basic feature information and approval metrics
2. **Requirements Summary** - Detailed breakdown of individual requirements
3. **Visual Elements Analysis** - Analysis of images and visual components
4. **Data Structure and Signal Analysis** - Signal architecture and system components
5. **Test Case Dependency Tree** - Hierarchical test dependencies
6. **Comprehensive Test Cases** - Detailed test cases with priorities
7. **Critical Gaps and Recommendations** - Identified gaps and improvement suggestions
8. **Final Validation Criteria** - Acceptance criteria and feature summary
9. **Image-to-Test Case Traceability** - Mapping between visual elements and test cases
10. **Test Case Dependency Mapping** - Execution order and dependencies
11. **Requirement Matrix** - Bidirectional mapping between requirements and test cases

## How the System Works

### 1. Script Execution

When you run the `optimize_ai_analysis.ps1` script with a feature ID parameter:

```powershell
.\optimize_ai_analysis.ps1 -Feature VEH-F165
```

The script performs the following operations:

- Searches for the feature directory in predefined paths
- Extracts the feature name from the directory
- Creates a dated output file in the specified output directory
- Generates a placeholder file based on the template structure
- Adds task description and feature content to the analysis prompt
- Provides instructions for image analysis using browser_action

### 2. Template Integration

The script creates a placeholder file with the structure from `SRS_ANALYSIS_TEMPLATE_COMPLETE.md`, which is then filled in during the analysis process. The template ensures:

- Consistent structure across all feature analyses
- Comprehensive coverage of all required analysis aspects
- Clear instructions for image analysis using browser_action
- Proper traceability between requirements, visual elements, and test cases

### 3. Image Analysis Integration

The template includes special instructions for image analysis using the browser_action tool:

- Each image in the feature directory must be analyzed using browser_action
- The analysis results are documented in Section 3 (Visual Elements Analysis)
- Visual elements are cross-referenced with requirements and test cases
- A traceability matrix is created to ensure complete coverage

## Using the Template System

### For Analysts

1. Run the script with the desired feature ID:
   ```powershell
   .\optimize_ai_analysis.ps1 -Feature <FEATURE_ID>
   ```

2. The script will generate a placeholder file in the output directory
3. Follow the instructions in the placeholder file to complete the analysis
4. Use browser_action to analyze any images in the feature directory
5. Fill in all sections of the template with appropriate content

### For Developers

If you need to modify the template system:

1. Edit `SRS_ANALYSIS_TEMPLATE_COMPLETE.md` to update the template structure
2. Modify `optimize_ai_analysis.ps1` to change the script behavior
3. Ensure that any changes maintain compatibility between the script and template

## Best Practices

- Always use the browser_action tool to analyze images as instructed
- Fill in all sections of the template, even if some are marked as optional
- Maintain traceability between requirements, visual elements, and test cases
- Document any critical gaps or recommendations in Section 7
- Follow the test case dependency structure in Sections 5 and 10

## Output Format

The final output file will be named according to the following pattern:

```
[FEATURE_ID]_[FEATURE_ID]_[FEATURE_NAME]_[DATE]_TC Analyze.txt
```

For example:
```
VEH-F165_VEH-F165_VEH-F165_Manettino_20260310_TC Analyze.txt
```

## Troubleshooting

If you encounter issues with the script or template:

- Ensure that the feature directory exists in one of the search paths
- Check that the feature ID is correctly specified
- Verify that the template file is accessible to the script
- Ensure that any images are properly referenced with file:// URLs

## Version History

- **v1.0** - Initial release with comprehensive template and script integration
- **v1.1** - Added enhanced browser_action integration for image analysis
- **v1.2** - Improved traceability between requirements and test cases

## Contact

For questions or support, please contact the SRS Analysis Team.
