# Picture Analyze Agent

A comprehensive image analysis system for automotive SRS (Software Requirements Specification) documents, featuring automated vision processing, dependency analysis, and test case generation.

## Project Structure

```
Picture Analyze Agent/
├── src/                          # Source code
│   ├── analyzers/               # FPI dependency analyzers
│   ├── classifiers/             # Image classification models (CLIP)
│   ├── processors/              # Data processing utilities
│   └── utils/                   # Utility functions
├── data/                        # Data storage
│   ├── raw/                     # Raw input data
│   │   ├── images/              # Input images
│   │   └── srs_export/          # SRS export files
│   ├── processed/               # Processed data
│   └── results/                 # Analysis results
├── templates/                   # Analysis templates
│   ├── picture_centric/         # Picture-focused analysis
│   ├── system_architecture/     # System architecture analysis
│   └── flowchart/              # Flowchart analysis
├── models/                      # Trained models and weights
├── scripts/                     # Utility scripts
├── docs/                        # Documentation
└── requirements.txt             # Python dependencies
```

## Features

- **Automated Image Analysis**: Vision API integration for comprehensive image understanding
- **FPI Dependency Analysis**: Feature Point Interface dependency mapping and analysis
- **CLIP Classification**: Advanced image classification using CLIP models
- **Template-based Analysis**: Structured analysis templates for different image types
- **Test Case Generation**: Automated generation of test cases from SRS analysis
- **Matrix Generation**: Dependency matrix creation and validation

## Quick Start

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up Environment**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and configuration
   ```

3. **Run Analysis**
   ```bash
   # For FPI dependency analysis
   python src/analyzers/complete_fpi_dependency_analyzer.py
   
   # For CLIP classification
   python src/classifiers/copy_and_run_clip.py
   
   # For universal processing
   python src/processors/universal_fpi_processor.py
   ```

## Key Components

### Analyzers
- `complete_fpi_dependency_analyzer.py` - Complete FPI dependency analysis
- `comprehensive_fpi_dependency_analyzer.py` - Comprehensive dependency mapping
- `corrected_antisymmetric_fpi_analyzer.py` - Antisymmetric relationship analysis

### Classifiers
- `copy_and_run_clip.py` - CLIP-based image classification

### Processors
- `universal_fpi_processor.py` - Universal FPI processing pipeline

### Templates
- Picture-centric analysis templates
- System architecture analysis frameworks
- Flowchart analysis methodologies

## Data Organization

- **Raw Data**: Original SRS exports, images, and input files
- **Processed Data**: Cleaned and preprocessed datasets
- **Results**: Analysis outputs, matrices, and generated reports

## Documentation

Comprehensive documentation is available in the `docs/` directory:
- Application overview and architecture
- Processing summaries and workflows
- Integration guides and best practices

## Contributing

1. Follow the established project structure
2. Place new analyzers in `src/analyzers/`
3. Add utility scripts to `scripts/`
4. Update documentation in `docs/`
5. Include tests for new functionality

## License

This project is part of the HARMAN automotive software development toolkit.
