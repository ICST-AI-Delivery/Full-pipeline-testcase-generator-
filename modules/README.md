# Picture Analyze Agent - Modules Documentation

## Overview

The `modules/` directory contains the core processing components of the Picture Analyze Agent system, designed for automotive SRS (Software Requirements Specification) analysis and test case generation. The system integrates CLIP-based image classification, Vision API analysis, and automated test case generation for automotive features.

## Architecture

```
modules/
├── fpi_analyzer/           # Feature dependency analysis
├── image_analyzer/         # Image processing & vision analysis
└── testcase_generator/     # SRS analysis & test case generation
```

## Quick Start

### Prerequisites
```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your HARMAN_API_KEY
```

### Basic Workflow
```bash
# 1. CLIP Classification
python modules/image_analyzer/simple_clip_pipeline.py --feature-mode VEH-F165_Manettino

# 2. Vision API Analysis
python modules/image_analyzer/vision_analyzer.py VEH-F165_Manettino

# 3. Generate Test Cases
python modules/testcase_generator/generate_srs_analysis.py --feature VEH-F165_Manettino
```

---

## Module 1: Image Analyzer

### Purpose
Processes automotive technical images through a two-stage pipeline:
1. **CLIP Classification** - Categorizes images into 13+ technical categories
2. **Vision API Analysis** - Applies specialized prompts for detailed analysis

### Structure
```
image_analyzer/
├── interfaces.py                    # Abstract interfaces
├── simple_clip_pipeline.py         # CLIP classification pipeline
├── vision_analyzer.py              # Vision API analysis
├── batch_processor.py              # Batch processing utilities
└── prompts/                        # 25+ specialized analysis prompts
    ├── 01_HMI_DISPLAY_LAYOUTS_v1.0.md
    ├── 02_CONFIGURATION_TABLES_v1.0.md
    ├── 03_SYSTEM_ARCHITECTURE_DIAGRAMS_v2.0_ENHANCED.md
    ├── 04_STATE_FLOW_DIAGRAMS_v2.1_SEQUENTIAL_MATRIX.md
    ├── 05_TIMING_DIAGRAMS_v6.0_SYSTEMATIC_STATE_MATRIX.md
    └── [20+ more specialized prompts...]
```

### Key Components

#### 1. CLIP Classification Pipeline (`simple_clip_pipeline.py`)
- **Purpose**: Categorizes images using CLIP model
- **Categories**: 13 technical categories (HMI Displays, Configuration Tables, System Architecture, etc.)
- **Output**: CSV with image paths and predicted categories

#### 2. Vision Analyzer (`vision_analyzer.py`)
- **Purpose**: Detailed analysis using category-specific prompts
- **Integration**: HARMAN LLM API with specialized prompts
- **Output**: Detailed text analysis files organized by feature

#### 3. Batch Processor (`batch_processor.py`)
- **Purpose**: Process multiple features simultaneously
- **Features**: Progress tracking, error handling, result consolidation

### Commands

#### CLIP Classification
```bash
# Single feature processing
python modules/image_analyzer/simple_clip_pipeline.py --feature-mode VEH-F165_Manettino

# Batch processing multiple features
python modules/image_analyzer/simple_clip_pipeline.py --batch-mode

# Custom image directory
python modules/image_analyzer/simple_clip_pipeline.py --feature-mode VEH-F165_Manettino --image-dir custom_images/

# Debug mode with detailed output
python modules/image_analyzer/simple_clip_pipeline.py --feature-mode VEH-F165_Manettino --debug
```

#### Vision API Analysis
```bash
# Analyze feature with CLIP predictions
python modules/image_analyzer/vision_analyzer.py VEH-F165_Manettino

# Process specific CSV file
python modules/image_analyzer/vision_analyzer.py VEH-F165_Manettino --csv-file custom_predictions.csv

# Custom API configuration
python modules/image_analyzer/vision_analyzer.py VEH-F165_Manettino --api-key YOUR_KEY
```

#### Batch Processing
```bash
# Process all features in data_files/
python modules/image_analyzer/batch_processor.py --input data_files/ --output analysis_results/

# Process specific features
python modules/image_analyzer/batch_processor.py --features VEH-F165_Manettino,VEH-F040_Key_Status

# Resume interrupted processing
python modules/image_analyzer/batch_processor.py --resume --checkpoint batch_checkpoint.json
```

### Supported Image Categories

| Category | Prompt Version | Description |
|----------|----------------|-------------|
| HMI DISPLAY LAYOUTS | v1.0 | Dashboard and interface layouts |
| CONFIGURATION TABLES | v1.0 | System configuration matrices |
| SYSTEM ARCHITECTURE DIAGRAMS | v2.0 | System component relationships |
| STATE FLOW DIAGRAMS | v2.1 | State transition workflows |
| TIMING DIAGRAMS | v6.0 | Signal timing and sequences |
| PROCESS FLOW DIAGRAMS | v5.0 | Process workflows with arrows |
| TELLTALE ICONS & INDICATORS | v1.0 | Warning lights and indicators |
| DECISION LOGIC TABLES | v1.0 | Logic decision matrices |
| INTERFACE SPECIFICATIONS | v1.0 | Interface definitions |
| REQUIREMENT SPECIFICATIONS | v1.0 | Requirement documentation |
| ERROR HANDLING DIAGRAMS | v1.0 | Error flow and handling |
| NETWORK TOPOLOGY DIAGRAMS | v1.0 | Network architecture |
| SIGNAL FLOW DIAGRAMS | v1.0 | Signal routing and flow |

### Output Structure
```
analysis_results/
└── [FEATURE_NAME]/
    ├── image1_HMI_DISPLAY_LAYOUTS_analysis.txt
    ├── image2_CONFIGURATION_TABLES_analysis.txt
    ├── image3_SYSTEM_ARCHITECTURE_analysis.txt
    └── c.txt                                    # Consolidated analysis
```

---

## Module 2: FPI Analyzer

### Purpose
Analyzes Feature Performance Indicators (FPI) and generates dependency matrices for automotive features.

### Structure
```
fpi_analyzer/
├── interfaces.py                    # Abstract interfaces
├── dependency_analyzer.py           # Basic dependency analysis
├── complete_fpi_dependency_analyzer.py    # Complete analysis
├── comprehensive_fpi_dependency_analyzer.py    # Comprehensive analysis
├── corrected_antisymmetric_fpi_analyzer.py    # Antisymmetric analysis
└── corrected_fpi_testcase_analyzer.py         # Test case analysis
```

### Key Components

#### 1. Dependency Analyzer (`dependency_analyzer.py`)
- **Purpose**: Creates placeholder dependency matrices
- **Output**: CSV matrices with feature relationships
- **Format**: 1426x1426 matrix with dependency scores (-3 to +3)

#### 2. Complete FPI Analyzer (`complete_fpi_dependency_analyzer.py`)
- **Purpose**: Full feature inventory and dependency analysis
- **Features**: Context injection, relationship mapping
- **Output**: JSON summaries and CSV matrices

#### 3. Comprehensive Matrix Generator (`comprehensive_fpi_matrix_generator.py`)
- **Purpose**: Advanced matrix generation with validation
- **Features**: Antisymmetric validation, progress tracking
- **Output**: Validated dependency matrices

### Commands

#### Basic Dependency Analysis
```bash
# Generate placeholder matrix
python modules/fpi_analyzer/dependency_analyzer.py

# Custom feature inventory
python modules/fpi_analyzer/dependency_analyzer.py --inventory custom_inventory.json
```

#### Complete FPI Analysis
```bash
# Full analysis with default settings
python modules/fpi_analyzer/complete_fpi_dependency_analyzer.py

# Custom configuration
python modules/fpi_analyzer/complete_fpi_dependency_analyzer.py --config analysis_config.json

# Specific feature subset
python modules/fpi_analyzer/complete_fpi_dependency_analyzer.py --features VEH-F165,VEH-F040
```

#### Comprehensive Matrix Generation
```bash
# Generate comprehensive matrix
python modules/fpi_analyzer/comprehensive_fpi_matrix_generator.py

# Validate existing matrix
python modules/fpi_analyzer/comprehensive_fpi_matrix_generator.py --validate existing_matrix.csv

# Resume interrupted analysis
python modules/fpi_analyzer/comprehensive_fpi_matrix_generator.py --resume checkpoint.json
```

#### Antisymmetric Analysis
```bash
# Corrected antisymmetric analysis
python modules/fpi_analyzer/corrected_antisymmetric_fpi_analyzer.py

# Validate antisymmetric properties
python modules/fpi_analyzer/corrected_antisymmetric_fpi_analyzer.py --validate-only
```

### Output Files

#### Matrix Files
- `fpi_dependency_matrix_[timestamp].csv` - Main dependency matrix
- `fpi_dependency_register_[timestamp].csv` - Feature register
- `corrected_antisymmetric_matrix_[timestamp].json` - Antisymmetric analysis

#### Analysis Reports
- `complete_fpi_context_injection_summary_[timestamp].json` - Context analysis
- `corrected_fpi_analysis_report_[timestamp].json` - Validation report
- `fpi_dependency_matrix_stats_[timestamp].json` - Matrix statistics

---

## Module 3: Test Case Generator

### Purpose
Generates comprehensive SRS analysis documents and test cases using a 5-phase approach to manage context limits effectively.

### Structure
```
testcase_generator/
├── interfaces.py                    # Abstract interfaces
├── generate_srs_analysis.py        # Main SRS analysis generator
├── testcase_generator.py           # Test case generation utilities
└── SRS_Analysis_TestCase_Generation.txt    # Analysis template
```

### Key Components

#### 1. SRS Analysis Generator (`generate_srs_analysis.py`)
- **Purpose**: 5-phase SRS analysis and test case generation
- **Features**: Context management, progressive document building
- **Integration**: HARMAN LLM API with specialized templates

#### 2. Test Case Generator (`testcase_generator.py`)
- **Purpose**: Utility functions for test case creation
- **Features**: Template management, validation, formatting

### 5-Phase Analysis Process

| Phase | Focus | Sections | Purpose |
|-------|-------|----------|---------|
| **Phase 1** | Foundation Setup | 1-2 | Feature overview, requirements summary |
| **Phase 2** | Technical Analysis | 3-4 | Visual elements, data structure analysis |
| **Phase 3** | Functionality Analysis | 5-8 | Core functionality, domain analysis |
| **Phase 4** | Test Case Generation | 9 | Comprehensive test cases |
| **Phase 5** | Final Integration | 10-11 | Dependency mapping, requirement matrix |

### Commands

#### Single Phase Execution
```bash
# Phase 1: Foundation Setup
python modules/testcase_generator/generate_srs_analysis.py --phase 1 --feature VEH-F165_Manettino

# Phase 2: Technical Analysis
python modules/testcase_generator/generate_srs_analysis.py --phase 2 --feature VEH-F165_Manettino

# Phase 3: Functionality Analysis
python modules/testcase_generator/generate_srs_analysis.py --phase 3 --feature VEH-F165_Manettino

# Phase 4: Test Case Generation
python modules/testcase_generator/generate_srs_analysis.py --phase 4 --feature VEH-F165_Manettino

# Phase 5: Final Integration
python modules/testcase_generator/generate_srs_analysis.py --phase 5 --feature VEH-F165_Manettino
```

#### Complete Analysis
```bash
# Run all phases sequentially
python modules/testcase_generator/generate_srs_analysis.py --feature VEH-F165_Manettino

# Custom API key
python modules/testcase_generator/generate_srs_analysis.py --feature VEH-F165_Manettino --api-key YOUR_KEY

# Debug mode with detailed logging
python modules/testcase_generator/generate_srs_analysis.py --feature VEH-F165_Manettino --debug
```

#### Batch Processing
```bash
# Process multiple features
for feature in VEH-F165_Manettino VEH-F040_Key_Status VEH-F247_External_Lights_Management; do
    python modules/testcase_generator/generate_srs_analysis.py --feature $feature
done

# Parallel processing (Linux/Mac)
parallel python modules/testcase_generator/generate_srs_analysis.py --feature {} ::: VEH-F165_Manettino VEH-F040_Key_Status
```

### Input Requirements

#### SRS Files Location
The system searches for SRS files in the following order:
1. `SRS FPI Export/[FEATURE_NAME].txt`
2. `SRS FPI Export/SRS Export/[Domain]/[FEATURE_NAME]/[requirements].txt`
3. `models/Pre-FineTuneLearning Model/SRS FPI export/[Domain]/[FEATURE_NAME]/[requirements].txt`

#### Supported Domains
- SRS_Instrument Cluster
- SRS_Audio
- SRS_Connectivity
- SRS_Diagnostics
- SRS_DMS
- SRS_HMI Software
- SRS_Navigation
- SRS_System Architecture
- SRS_Tuner

#### Visual Analysis Integration
- Consolidated analysis: `analysis_results/[FEATURE_NAME]/c.txt`
- Individual analyses: `analysis_results/[FEATURE_NAME]/*.txt`

### Output Structure
```
generated_testcases(final output)/
└── [FEATURE_NAME]_SRS_Analysis_and_TestCases.md
```

---

## Complete Workflow Examples

### End-to-End Feature Analysis
```bash
#!/bin/bash
# Complete analysis workflow for a single feature

FEATURE="VEH-F165_Manettino"

echo "Starting complete analysis for $FEATURE"

# Step 1: CLIP Classification
echo "Step 1: CLIP Classification"
python modules/image_analyzer/simple_clip_pipeline.py --feature-mode $FEATURE

# Step 2: Vision API Analysis
echo "Step 2: Vision API Analysis"
python modules/image_analyzer/vision_analyzer.py $FEATURE

# Step 3: Generate Test Cases
echo "Step 3: SRS Analysis and Test Case Generation"
python modules/testcase_generator/generate_srs_analysis.py --feature $FEATURE

echo "Analysis complete for $FEATURE"
echo "Results available in:"
echo "  - analysis_results/$FEATURE/"
echo "  - generated_testcases(final output)/${FEATURE}_SRS_Analysis_and_TestCases.md"
```

### Batch Processing Multiple Features
```bash
#!/bin/bash
# Batch processing script

FEATURES=(
    "VEH-F165_Manettino"
    "VEH-F040_Key_Status"
    "VEH-F247_External_Lights_Management"
    "DMS-7_DRIVER_GAZE_ESTIMATION"
)

for FEATURE in "${FEATURES[@]}"; do
    echo "Processing $FEATURE..."
    
    # CLIP Classification
    python modules/image_analyzer/simple_clip_pipeline.py --feature-mode $FEATURE
    
    # Vision Analysis
    python modules/image_analyzer/vision_analyzer.py $FEATURE
    
    # Test Case Generation
    python modules/testcase_generator/generate_srs_analysis.py --feature $FEATURE
    
    echo "Completed $FEATURE"
done
```

### FPI Dependency Analysis Workflow
```bash
#!/bin/bash
# FPI dependency analysis workflow

echo "Starting FPI dependency analysis"

# Step 1: Generate feature inventory
python modules/fpi_analyzer/dependency_analyzer.py

# Step 2: Complete dependency analysis
python modules/fpi_analyzer/complete_fpi_dependency_analyzer.py

# Step 3: Comprehensive matrix generation
python modules/fpi_analyzer/comprehensive_fpi_matrix_generator.py

# Step 4: Antisymmetric validation
python modules/fpi_analyzer/corrected_antisymmetric_fpi_analyzer.py

echo "FPI analysis complete"
echo "Results available in:"
echo "  - fpi_dependency_matrix_*.csv"
echo "  - corrected_antisymmetric_matrix_*.json"
echo "  - complete_fpi_context_injection_summary_*.json"
```

---

## Troubleshooting

### Common Issues

#### 1. API Key Issues
```bash
# Check if API key is set
python -c "from utils.env_manager import env_manager; print('API Key:', 'SET' if env_manager.get_config_value('HARMAN_API_KEY') else 'NOT SET')"

# Test API connection
python modules/image_analyzer/vision_analyzer.py --test-api
```

#### 2. Missing Dependencies
```bash
# Install missing packages
pip install -r requirements.txt

# Check specific dependencies
python -c "import clip, litellm, pandas; print('Dependencies OK')"
```

#### 3. File Path Issues
```bash
# Verify SRS file structure
find "SRS FPI Export" -name "*.txt" | head -10

# Check analysis results
ls -la analysis_results/*/
```

#### 4. Memory Issues
```bash
# Monitor memory usage during processing
python modules/image_analyzer/simple_clip_pipeline.py --feature-mode VEH-F165_Manettino --memory-monitor

# Process in smaller batches
python modules/image_analyzer/batch_processor.py --batch-size 10
```

### Debug Commands

#### Enable Debug Logging
```bash
# Set debug environment variable
export DEBUG=1

# Run with verbose output
python modules/testcase_generator/generate_srs_analysis.py --feature VEH-F165_Manettino --debug
```

#### Validate Pipeline
```bash
# Test complete pipeline with sample data
python scripts/validate_pipeline.py --feature VEH-F165_Manettino

# Check individual components
python scripts/test_single_image.py --image sample_image.png --category "HMI DISPLAY LAYOUTS"
```

---

## Integration with External Tools

### GitHub Copilot Optimization

This documentation structure is optimized for GitHub Copilot integration:

- **Clear module boundaries** - Helps AI understand component separation
- **Consistent command patterns** - Enables better code completion
- **Comprehensive examples** - Provides context for AI suggestions
- **Interface documentation** - Supports type-aware completions

### IDE Integration

#### VS Code Configuration
```json
{
    "python.defaultInterpreterPath": "./venv/bin/python",
    "python.analysis.extraPaths": ["./modules", "./utils"],
    "files.associations": {
        "*.md": "markdown"
    }
}
```

#### PyCharm Configuration
- Mark `modules/` as Sources Root
- Mark `utils/` as Sources Root
- Configure Python interpreter to project virtual environment

### CI/CD Integration

#### GitHub Actions Example
```yaml
name: Picture Analyze Agent Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.8
    - name: Install dependencies
      run: pip install -r requirements.txt
    - name: Run tests
      run: python -m pytest tests/
    - name: Validate pipeline
      run: python scripts/validate_pipeline.py --test-mode
```

---

## Performance Optimization

### Batch Processing Tips

#### Optimal Batch Sizes
- **CLIP Classification**: 50-100 images per batch
- **Vision API Analysis**: 10-20 images per batch (API rate limits)
- **Test Case Generation**: 1 feature per process (memory intensive)

#### Parallel Processing
```bash
# Process multiple features in parallel (Linux/Mac)
parallel -j 4 python modules/testcase_generator/generate_srs_analysis.py --feature {} ::: \
    VEH-F165_Manettino VEH-F040_Key_Status VEH-F247_External_Lights_Management DMS-7_DRIVER_GAZE_ESTIMATION

# Windows PowerShell parallel processing
$features = @("VEH-F165_Manettino", "VEH-F040_Key_Status", "VEH-F247_External_Lights_Management")
$features | ForEach-Object -Parallel {
    python modules/testcase_generator/generate_srs_analysis.py --feature $_
} -ThrottleLimit 4
```

### Memory Management

#### Large Dataset Processing
```bash
# Process with memory constraints
python modules/image_analyzer/batch_processor.py --max-memory 8GB --swap-threshold 6GB

# Monitor resource usage
python modules/image_analyzer/simple_clip_pipeline.py --feature-mode VEH-F165_Manettino --profile
```

---

## Maintenance Commands

### Data Cleanup
```bash
# Clean temporary files
find . -name "*.tmp" -delete
find . -name "__pycache__" -type d -exec rm -rf {} +

# Archive old results
mkdir -p archive/$(date +%Y%m%d)
mv analysis_results/* archive/$(date +%Y%m%d)/
mv generated_testcases/* archive/$(date +%Y%m%d)/
```

### System Health Checks
```bash
# Check disk space
df -h

# Verify all modules can be imported
python -c "
import modules.image_analyzer.simple_clip_pipeline
import modules.fpi_analyzer.dependency_analyzer
import modules.testcase_generator.generate_srs_analysis
print('All modules imported successfully')
"

# Test API connectivity
python -c "
from utils.env_manager import env_manager
from litellm import completion
api_key = env_manager.get_config_value('HARMAN_API_KEY')
if api_key:
    print('API key configured')
else:
    print('API key missing')
"
```

### Log Analysis
```bash
# View recent logs
tail -f logs/pipeline.log

# Search for errors
grep -i error logs/*.log

# Analyze processing times
grep "Processing time" logs/pipeline.log | awk '{print $NF}' | sort -n
```

---

## Contributing

### Development Setup
```bash
# Clone repository
git clone <repository-url>
cd Picture-Analyze-Agent

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Install development dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Set up pre-commit hooks
pre-commit install
```

### Code Style
- Follow PEP 8 for Python code
- Use type hints where possible
- Document all public functions and classes
- Include docstrings for modules

### Testing
```bash
# Run unit tests
python -m pytest tests/

# Run integration tests
python -m pytest tests/integration/

# Run with coverage
python -m pytest --cov=modules tests/
```

---

## Support

### Documentation
- **Project Overview**: `docs/PROJECT_STRUCTURE_REORGANIZED.md`
- **API Documentation**: `docs/api/`
- **Examples**: `examples/`

### Common Resources
- **Environment Setup**: `ENVIRONMENT_SETUP_GUIDE.md`
- **Pipeline Workflow**: `COMPLETE_PIPELINE_WORKFLOW.md`
- **Vision API Guide**: `VISION_API_EXTRACTION_SYSTEM_SUMMARY.md`

### Contact
For technical support or questions about the Picture Analyze Agent system, please refer to the project documentation or contact the development team.

---

*Last Updated: April 2026*
*Version: 1.0*
