# Automated Vision Pipeline Guide

This guide explains the complete three-phase workflow for processing technical images with CLIP classification, specialized vision analysis, and consolidated analysis with enhanced table extraction.

## Overview

The pipeline consists of three distinct phases for comprehensive image analysis:

1. **CLIP Classification** (using `simple_clip_pipeline.py`)
   - Scans feature directories for images
   - Auto-generates CSV files with image paths
   - Classifies images using CLIP models
   - Outputs CSV with predictions

2. **Vision Analysis** (using `automated_vision_pipeline.py`)
   - Takes the CLIP-classified CSV as input
   - Applies specialized prompts based on image categories
   - Processes images with Claude API
   - Saves detailed analysis results

3. **Consolidated Analysis** (using `generate_consolidated_analysis.py`) - **NEW!**
   - Combines all individual analyses into comprehensive summary
   - Enhanced table extraction with complete cell capture
   - Cross-image relationship analysis
   - Automotive domain integration

## Quick Start

### Step 1: Run CLIP Classification

```bash
python scripts/simple_clip_pipeline.py --feature-mode VEH-F165_Manettino
```

This command:
- Automatically finds images in the feature directory
- Creates a CSV file in `data_files/VEH-F165_Manettino.csv`
- Runs CLIP classification on all images
- Outputs results to `data_files/VEH-F165_Manettino_with_clip_predictions.csv`

### Step 2: Run Vision Analysis

```bash
python scripts/automated_vision_pipeline.py VEH-F165_Manettino
```

This command:
- Loads the CLIP predictions from Step 1
- Processes each image with specialized prompts based on its category
- Saves analysis results to `analysis_results/VEH-F165_Manettino/`

### Step 3: Run Consolidated Analysis (NEW!)

```bash
python scripts/generate_consolidated_analysis.py --feature VEH-F165_Manettino
```

This command:
- Combines all individual analyses from Step 2
- Extracts complete table structures with every cell
- Identifies cross-image relationships and patterns
- Creates comprehensive consolidated summary in `analysis_results/VEH-F165_Manettino/c.txt`

## Detailed Usage

### CLIP Classification Options

```bash
python scripts/simple_clip_pipeline.py --feature-mode <feature_name> [options]
```

Options:
- `--models`: Comma-separated CLIP models (default: "ViT-B/32,ViT-L/14")
- `--device`: Device to run on (cpu or cuda, default: cpu)
- `--force-reprocess`: Force reprocessing all images
- `--no-update-merged`: Don't update the merged predictions table

You can also process a specific CSV file directly:

```bash
python scripts/simple_clip_pipeline.py path/to/input.csv [path/to/output.csv]
```

### Vision Analysis Options

```bash
python scripts/automated_vision_pipeline.py <feature_name> [api_key]
```

- `feature_name`: Name of the feature to process (e.g., VEH-F165_Manettino)
- `api_key`: Optional API key for Claude API (can also be set in the script or as environment variable)

## Supported Image Categories

The system supports specialized analysis for these image categories:

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

Each category has a specialized prompt template in the `vision_api_prompts/` directory.

## Example Workflow

```bash
# Complete 3-step workflow for VEH-F844_Matrix_State_Event
# Step 1: Run CLIP classification
python scripts/simple_clip_pipeline.py --feature-mode VEH-F844_Matrix_State_Event

# Step 2: Run vision analysis on the classified images
python scripts/automated_vision_pipeline.py VEH-F844_Matrix_State_Event

# Step 3: Generate consolidated analysis with enhanced table extraction
python scripts/generate_consolidated_analysis.py --feature VEH-F844_Matrix_State_Event
```

## Troubleshooting

### Common Issues

1. **Missing CSV file**
   - If `automated_vision_pipeline.py` reports missing CSV, ensure you've run `simple_clip_pipeline.py` first

2. **Missing analysis files**
   - If `generate_consolidated_analysis.py` reports no analysis files, ensure Step 2 completed successfully

3. **Image path errors**
   - The system tries multiple path resolution strategies, but if images aren't found:
     - Check that image paths in the CSV are correct
     - Try running from the project root directory

4. **API key errors**
   - Set the API key in the script, as an environment variable, or pass it as an argument

5. **Incomplete table extraction**
   - Check individual analysis quality before running consolidated analysis
   - Use validation scripts to verify table extraction completeness

## Benefits of the Three-Phase Workflow

1. **Modularity**: Each phase can be run independently
2. **Efficiency**: CLIP classification only needs to be run once
3. **Flexibility**: Different vision models can be used without re-running earlier phases
4. **Clarity**: Clear separation of concerns between classification, analysis, and consolidation
5. **Enhanced Table Extraction**: Complete table structures with cross-image relationships
6. **Quality Assurance**: Built-in validation and quality metrics
7. **Automotive Integration**: Domain-specific analysis for automotive specifications

## Complete Pipeline Reference

For the most comprehensive documentation of the complete pipeline including advanced features, troubleshooting, and best practices, see:
- **`COMPLETE_PIPELINE_WORKFLOW.md`** - Master pipeline documentation
- **`CONSOLIDATED_ANALYSIS_GENERATOR_GUIDE.md`** - Detailed Phase 3 documentation
- **`TABLE_EXTRACTION_ENHANCEMENT_SUMMARY.md`** - Table extraction improvements
