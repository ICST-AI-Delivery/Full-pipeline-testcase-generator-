# Picture Analyze Agent - Project Structure

## Overview
This document describes the reorganized structure of the Picture Analyze Agent project, designed to improve maintainability, scalability, and development workflow.

## Directory Structure

```
Picture Analyze Agent/
├── .env                          # Environment variables (local)
├── .env.example                  # Environment variables template
├── .gitignore                    # Git ignore rules
├── README.md                     # Main project documentation
├── requirements.txt              # Python dependencies
├── PROJECT_STRUCTURE.md          # This file
│
├── src/                          # Source code
│   ├── analyzers/                # Analysis modules
│   │   ├── complete_fpi_dependency_analyzer.py
│   │   ├── comprehensive_fpi_dependency_analyzer.py
│   │   ├── corrected_antisymmetric_fpi_analyzer.py
│   │   └── corrected_fpi_testcase_analyzer.py
│   ├── classifiers/              # Classification modules
│   │   └── copy_and_run_clip.py
│   ├── processors/               # Data processing modules
│   │   └── universal_fpi_processor.py
│   └── utils/                    # Utility functions
│
├── scripts/                      # Utility and automation scripts
│   ├── comprehensive_fpi_matrix_generator.py
│   ├── copy_power_csv.py
│   ├── count_srs_features.py
│   ├── create_feature_inventory.py
│   ├── create_fpi_dependency_matrix_placeholder.py
│   ├── create_power_management_csv.py
│   ├── create_remaining_csvs.py
│   ├── optimize_ai_analysis.ps1
│   ├── process_veh_f200.py
│   ├── obsolete_scripts/         # Deprecated scripts
│   └── processes/                # Process automation
│
├── templates/                    # Analysis templates and prompts
│   ├── picture_centric/          # Picture-centric analysis templates
│   ├── system_architecture/      # System architecture templates
│   ├── flowchart/               # Flowchart analysis templates
│   └── vision_api_prompts/       # Vision API prompt templates
│
├── data/                         # Data files and results
│   ├── raw/                      # Raw input data
│   │   ├── images/               # Image files
│   │   └── srs_export/           # SRS export data
│   ├── processed/                # Processed data files
│   │   ├── *.json                # JSON data files
│   │   ├── *.csv                 # CSV data files
│   │   └── *.txt                 # Text data files
│   └── results/                  # Analysis results
│       ├── fpi_matrix_results/   # FPI matrix analysis results
│       ├── generated_testcases(final output)/  # Generated test cases
│       └── SRS FPI TestCase/     # SRS FPI test cases
│
├── models/                       # Machine learning models
│   └── Pre-FineTuneLearning Model/  # Pre-trained models
│
├── docs/                         # Documentation
│   ├── *.md                      # Markdown documentation files
│   ├── Multi phase implementation/  # Implementation phases
│   ├── reference_materials/      # Reference documentation
│   └── Related FPIs/            # FPI-related documentation
│
└── utils/                        # Project utilities (existing)
```

## Key Improvements

### 1. **Logical Separation**
- **src/**: Core application code organized by functionality
- **scripts/**: Utility and automation scripts
- **templates/**: Reusable analysis templates
- **data/**: All data files with clear raw/processed/results separation
- **docs/**: Comprehensive documentation

### 2. **Source Code Organization**
- **analyzers/**: FPI analysis and dependency analysis modules
- **classifiers/**: Image classification and ML-related code
- **processors/**: Data processing and transformation modules
- **utils/**: Common utility functions

### 3. **Data Management**
- **raw/**: Original, unmodified data files
- **processed/**: Cleaned and transformed data
- **results/**: Analysis outputs and generated content

### 4. **Template System**
- **picture_centric/**: Templates for image-focused analysis
- **system_architecture/**: System design analysis templates
- **flowchart/**: Process flow analysis templates
- **vision_api_prompts/**: AI vision API prompt templates

## Benefits

1. **Maintainability**: Clear separation of concerns makes code easier to maintain
2. **Scalability**: Modular structure supports project growth
3. **Collaboration**: Standardized organization improves team collaboration
4. **Development**: Easier to locate and modify specific functionality
5. **Testing**: Isolated modules are easier to test independently

## Usage Guidelines

### Adding New Code
- **Analysis modules**: Add to `src/analyzers/`
- **Classification models**: Add to `src/classifiers/`
- **Data processing**: Add to `src/processors/`
- **Utility scripts**: Add to `scripts/`
- **Templates**: Add to appropriate `templates/` subdirectory

### Data Management
- **Raw data**: Place in `data/raw/` with appropriate subdirectories
- **Processed data**: Output to `data/processed/`
- **Results**: Save analysis results to `data/results/`

### Documentation
- **Technical docs**: Add to `docs/`
- **API documentation**: Include in relevant source files
- **User guides**: Add to `docs/` with clear naming

## Migration Notes

All files have been moved to their appropriate locations while maintaining their functionality. The reorganization focused on:

1. Grouping related files together
2. Separating code from data and documentation
3. Creating clear hierarchies for different file types
4. Maintaining backward compatibility where possible

## Next Steps

1. Update import statements in Python files to reflect new structure
2. Create `__init__.py` files in Python packages
3. Update configuration files with new paths
4. Create automated tests for the reorganized structure
5. Update CI/CD pipelines to work with new structure
