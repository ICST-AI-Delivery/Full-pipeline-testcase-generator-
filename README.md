# Full Pipeline Testcase Generator

A comprehensive automotive SRS (Software Requirements Specification) analysis system that automatically generates test cases from technical documentation and images using AI-powered analysis pipelines.

## 🚀 Overview

The Full Pipeline Testcase Generator transforms automotive technical documentation into comprehensive test cases through a sophisticated 3-module pipeline:

1. **🔍 Image Analyzer** - CLIP classification and Vision API analysis of technical images
2. **🔗 FPI Analyzer** - Feature dependency analysis and relationship mapping
3. **📋 Test Case Generator** - SRS analysis and comprehensive test case generation using a 5-phase approach

## 📁 Project Structure

```
Full Pipeline Testcase Generator/
├── modules/                     # Core processing modules
│   ├── image_analyzer/         # Module 1: Image processing & vision analysis
│   ├── fpi_analyzer/          # Module 2: Feature dependency analysis
│   └── testcase_generator/    # Module 3: SRS analysis & test case generation
├── data/                       # Data storage and processing
│   ├── raw/                   # Raw CSV files with image paths
│   ├── processed/             # CLIP predictions and processed data
│   └── results/               # Vision API analysis results
├── scripts/                    # Utility and processing scripts
├── shared/                     # Shared data models and utilities
├── templates/                  # Analysis templates and prompts
├── docs/                       # Comprehensive documentation
├── generated_testcases(final output)/  # Final test case documents
└── SRS FPI Export/            # SRS requirements documents
```

## ⚡ Quick Start

### Prerequisites
```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your HARMAN_API_KEY
```

### Complete Pipeline Workflow
```bash
# Module 1: Image Analysis (categorize and analyze technical images)
python modules/image_analyzer/simple_clip_pipeline.py --feature-mode VEH-F165_Manettino
python modules/image_analyzer/vision_analyzer.py VEH-F165_Manettino

# Module 2: FPI Analysis (feature dependency mapping)
python modules/fpi_analyzer/complete_fpi_dependency_analyzer.py

# Module 3: Test Case Generation (5-phase SRS analysis and test case creation)
python modules/testcase_generator/generate_srs_analysis.py --feature VEH-F165_Manettino
```

## 🏗️ Core Modules

### Module 1: Image Analyzer (`modules/image_analyzer/`)
**Purpose**: Processes automotive technical images to extract visual context for test case generation

- **CLIP Classification**: Categorizes images using CLIP model into 13+ technical categories
- **Vision API Analysis**: Applies 25+ specialized prompts based on image category
- **Batch Processing**: Handles multiple features simultaneously

**Key Features**:
- 13+ technical image categories (HMI Displays, Configuration Tables, System Architecture, etc.)
- Category-specific analysis prompts optimized for automotive documentation
- Integration with HARMAN LLM API for detailed analysis
- Feeds visual context to downstream modules

### Module 2: FPI Analyzer (`modules/fpi_analyzer/`)
**Purpose**: Analyzes Feature Performance Indicators (FPI) and generates dependency matrices

- **Dependency Analysis**: Creates feature relationship matrices (1426x1426)
- **Antisymmetric Validation**: Ensures mathematical consistency
- **Context Injection**: Advanced relationship mapping between automotive features
- **Matrix Generation**: Comprehensive dependency analysis for test planning

**Key Features**:
- Complete feature inventory analysis
- Dependency scoring (-3 to +3 scale)
- Antisymmetric matrix validation
- Context injection summaries

### Module 3: Test Case Generator (`modules/testcase_generator/`)
**Purpose**: The **final output module** that generates comprehensive test cases using inputs from Modules 1 & 2

The `generate_srs_analysis.py` script transforms SRS requirements, visual analysis, and dependency data into comprehensive test documentation.

#### 🔄 5-Phase Process
| Phase | Focus | Output | Key Features |
|-------|-------|--------|--------------|
| **Phase 1** | Foundation Setup | Feature overview, requirements summary | Counts all requirements, creates individual entries |
| **Phase 2** | Technical Analysis | Visual elements, data structure analysis | Preserves individual image distinctions |
| **Phase 3** | Functionality Analysis | Core functionality, domain analysis | Prepares foundation for test cases |
| **Phase 4** | Test Case Generation | Comprehensive test cases | Creates actual test procedures with CAN signals |
| **Phase 5** | Final Integration | Dependency mapping, requirement matrix | Ensures complete traceability |

#### 🔧 How It Works
1. **Loads SRS requirements** from multiple search locations
2. **Finds visual analysis files** (consolidated + individual analyses)
3. **Progressive document building** - each phase builds on the previous one
4. **API Integration** - Uses HARMAN LLM API (`openai/sonnet-4.6-asia`)
5. **Context management** - 4000 tokens per phase to avoid timeouts

#### ⚠️ Gateway Timeout Prevention
The system splits work into phases because sending everything at once would exceed token limits:

| Phase | Payload Size | Content |
|-------|--------------|---------|
| Phase 1 | Small | SRS content + prompt |
| Phase 2 | Medium | Phase 1 output + visual analysis + prompt |
| Phase 3 | Large | Phases 1-2 output + prompt |
| Phase 4 | Very Large | Phases 1-3 output + prompt |
| Phase 5 | Largest | Phases 1-4 output + prompt |

**Solutions for timeouts**:
- Reduced `max_tokens` from 8000 to 4000
- Run phases individually: `--phase 1`, `--phase 2`, etc.
- Wait and retry - often just temporary server load


## 📊 Supported Image Categories

| Category | Description | Prompt Version |
|----------|-------------|----------------|
| HMI DISPLAY LAYOUTS | Dashboard and interface layouts | v1.0 |
| CONFIGURATION TABLES | System configuration matrices | v1.0 |
| SYSTEM ARCHITECTURE DIAGRAMS | System component relationships | v2.0 |
| STATE FLOW DIAGRAMS | State transition workflows | v2.1 |
| TIMING DIAGRAMS | Signal timing and sequences | v6.0 |
| PROCESS FLOW DIAGRAMS | Process workflows with arrows | v5.0 |
| TELLTALE ICONS & INDICATORS | Warning lights and indicators | v1.0 |
| DECISION LOGIC TABLES | Logic decision matrices | v1.0 |
| INTERFACE SPECIFICATIONS | Interface definitions | v1.0 |
| REQUIREMENT SPECIFICATIONS | Requirement documentation | v1.0 |
| ERROR HANDLING DIAGRAMS | Error flow and handling | v1.0 |
| NETWORK TOPOLOGY DIAGRAMS | Network architecture | v1.0 |
| SIGNAL FLOW DIAGRAMS | Signal routing and flow | v1.0 |

## 🎯 Key Features

### Automated Analysis Pipeline
- **CLIP-based Classification**: Intelligent image categorization
- **Vision API Integration**: HARMAN LLM API with specialized prompts
- **Progressive Processing**: 5-phase approach manages context limits effectively

### Test Case Generation
- **Comprehensive Coverage**: Every requirement gets individual analysis
- **CAN Signal Integration**: Includes specific signal values and timing
- **Traceability Matrix**: Maps requirements to test cases
- **Priority Classification**: A/B/C/D priority assignments

### Dependency Analysis
- **FPI Matrix Generation**: 1426x1426 feature dependency matrices
- **Antisymmetric Validation**: Mathematical consistency checks
- **Context Injection**: Advanced relationship mapping

### Batch Processing
- **Multi-feature Support**: Process multiple automotive features
- **Progress Tracking**: Monitor processing status
- **Error Handling**: Robust error recovery and logging

## 📋 Usage Examples

### Single Feature Analysis
```bash
# Complete end-to-end analysis
FEATURE="VEH-F165_Manettino"

# Step 1: CLIP Classification
python modules/image_analyzer/simple_clip_pipeline.py --feature-mode $FEATURE

# Step 2: Vision API Analysis  
python modules/image_analyzer/vision_analyzer.py $FEATURE

# Step 3: Generate Test Cases
python modules/testcase_generator/generate_srs_analysis.py --feature $FEATURE
```

### Phase-by-Phase Test Case Generation
```bash
# Run individual phases (useful for debugging timeouts)
python modules/testcase_generator/generate_srs_analysis.py --phase 1 --feature VEH-F165_Manettino
python modules/testcase_generator/generate_srs_analysis.py --phase 2 --feature VEH-F165_Manettino
python modules/testcase_generator/generate_srs_analysis.py --phase 3 --feature VEH-F165_Manettino
python modules/testcase_generator/generate_srs_analysis.py --phase 4 --feature VEH-F165_Manettino
python modules/testcase_generator/generate_srs_analysis.py --phase 5 --feature VEH-F165_Manettino
```

### Batch Processing
```bash
# Process multiple features
FEATURES=("VEH-F165_Manettino" "VEH-F040_Key_Status" "DMS-7_DRIVER_GAZE_ESTIMATION")

for FEATURE in "${FEATURES[@]}"; do
    echo "Processing $FEATURE..."
    python modules/image_analyzer/simple_clip_pipeline.py --feature-mode $FEATURE
    python modules/image_analyzer/vision_analyzer.py $FEATURE
    python modules/testcase_generator/generate_srs_analysis.py --feature $FEATURE
done
```

## 📂 Input Requirements

### SRS Files
The system searches for SRS files in this order:
1. `SRS FPI Export/[FEATURE_NAME].txt`
2. `SRS FPI Export/[Domain]/[FEATURE_NAME]/*.txt`
3. `models/Pre-FineTuneLearning Model/SRS FPI export/[Domain]/[FEATURE_NAME]/*.txt`

### Supported SRS Domains
- SRS_Instrument Cluster
- SRS_Audio  
- SRS_Connectivity
- SRS_Diagnostics
- SRS_DMS
- SRS_HMI Software
- SRS_Navigation
- SRS_System Architecture
- SRS_Tuner

### Image Data
- **CSV files**: `data/raw/[FEATURE_NAME].csv` with image paths
- **Images**: Referenced in CSV files, typically in project subdirectories
- **CLIP predictions**: Generated in `data/processed/[FEATURE_NAME]_with_clip_predictions.csv`

## 📤 Output Structure

```
# Analysis Results
data/results/[FEATURE_NAME]/
├── image1_HMI_DISPLAY_LAYOUTS_analysis.txt
├── image2_CONFIGURATION_TABLES_analysis.txt  
├── image3_SYSTEM_ARCHITECTURE_analysis.txt
└── c.txt                                    # Consolidated analysis

# Final Test Cases
generated_testcases(final output)/
└── [FEATURE_NAME]_SRS_Analysis_and_TestCases.md

# FPI Analysis
├── fpi_dependency_matrix_[timestamp].csv
├── corrected_antisymmetric_matrix_[timestamp].json
└── complete_fpi_context_injection_summary_[timestamp].json
```

## 🔧 Configuration

### Environment Variables
```bash
# Required
HARMAN_API_KEY=your_harman_api_key_here

# Optional
DEBUG=1                    # Enable debug logging
MAX_TOKENS=4000           # API token limit per request
BATCH_SIZE=10             # Batch processing size
```

### API Configuration
- **Model**: `openai/sonnet-4.6-asia`
- **Base URL**: `https://brllm.harman.com`
- **Max Tokens**: 4000 per phase (optimized to avoid timeouts)
- **Temperature**: 0.1 (for consistent output)

## 🚨 Troubleshooting

### Common Issues

#### Gateway Timeout Errors
**Symptoms**: 504 Gateway Timeout on HARMAN API
**Solutions**:
1. Wait 5-10 minutes and retry (often temporary server load)
2. Run phases individually instead of all at once
3. Reduce `max_tokens` in the script (already set to 4000)
4. Process during off-peak hours

#### Missing SRS Files
**Symptoms**: "SRS file not found" errors
**Solutions**:
1. Check file exists in `SRS FPI Export/` directory
2. Verify feature name matches exactly (case-sensitive)
3. Check supported domain list above

#### API Key Issues
**Symptoms**: Authentication errors
**Solutions**:
```bash
# Check if API key is set
python -c "from utils.env_manager import env_manager; print('API Key:', 'SET' if env_manager.get_config_value('HARMAN_API_KEY') else 'NOT SET')"

# Test API connection
python scripts/test_api.py
```

### Debug Commands
```bash
# Enable debug logging
export DEBUG=1

# Test individual components
python scripts/test_single_image.py --image sample.png --category "HMI DISPLAY LAYOUTS"

# Validate complete pipeline
python scripts/validate_pipeline.py --feature VEH-F165_Manettino
```

## 📚 Documentation

Comprehensive documentation is available:

- **`modules/README.md`** - Detailed module documentation with technical implementation
- **`docs/PROJECT_STRUCTURE_REORGANIZED.md`** - Complete project structure overview
- **`docs/PROCESSING_GUIDELINES.md`** - Processing workflows and best practices
- **`docs/ENVIRONMENT_SETUP_GUIDE.md`** - Environment setup and configuration
- **`templates/vision_api_prompts/`** - All 25+ specialized analysis prompts

## 🤝 Contributing

### Development Setup
```bash
# Clone and setup
git clone <repository-url>
cd Picture-Analyze-Agent
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

### Code Organization
- **New analyzers**: Add to `modules/fpi_analyzer/`
- **New image processors**: Add to `modules/image_analyzer/`
- **New test generators**: Add to `modules/testcase_generator/`
- **Utility scripts**: Add to `scripts/`
- **Documentation**: Update in `docs/`

### Testing
```bash
# Run validation tests
python scripts/validate_pipeline.py --test-mode

# Test individual components
python -m pytest tests/ --cov=modules
```

## 📄 License

This project is part of the HARMAN automotive software development toolkit.

---

## 🎯 System Highlights

### Why 5-Phase Processing?
The test case generation uses a 5-phase approach because:
- **Token Limits**: Single requests would exceed API limits
- **Context Management**: Each phase builds on previous results
- **Error Recovery**: Failed phases can be rerun individually
- **Quality Control**: Progressive validation at each stage

### Advanced Features
- **Antisymmetric Matrix Validation**: Ensures mathematical consistency in dependency analysis
- **Context Injection**: Advanced relationship mapping between features
- **Progressive Document Building**: Intelligent content accumulation across phases
- **Category-Specific Prompts**: 25+ specialized prompts optimized for automotive documentation

### Integration Ready
- **GitHub Copilot Optimized**: Clear module boundaries and consistent patterns
- **CI/CD Compatible**: Validation scripts and automated testing
- **Scalable Architecture**: Modular design supports easy extension

*Last Updated: April 2026*
*Version: 2.0 - Enhanced with detailed 5-phase test case generation*