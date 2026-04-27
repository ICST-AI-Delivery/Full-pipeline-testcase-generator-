# Picture Analyze Agent - Modular Architecture Implementation

## Overview
This document outlines the restructuring of the Picture Analyze Agent into three distinct, modular components:

1. **Image Analyzer Module** - CLIP classification and vision analysis
2. **FPI Analyzer Module** - Feature dependency analysis and matrix generation  
3. **Test Case Generator Module** - SRS analysis and test case generation

## New Project Structure

```
picture_analyze_agent/
├── modules/
│   ├── image_analyzer/
│   │   ├── __init__.py
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── clip_classifier.py
│   │   │   ├── vision_api_client.py
│   │   │   └── image_processor.py
│   │   ├── prompts/
│   │   │   ├── __init__.py
│   │   │   ├── category_prompts/
│   │   │   └── prompt_manager.py
│   │   ├── pipelines/
│   │   │   ├── __init__.py
│   │   │   ├── clip_pipeline.py
│   │   │   └── vision_pipeline.py
│   │   └── interfaces/
│   │       ├── __init__.py
│   │       ├── image_analyzer_api.py
│   │       └── result_formatter.py
│   ├── fpi_analyzer/
│   │   ├── __init__.py
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── dependency_analyzer.py
│   │   │   ├── matrix_generator.py
│   │   │   └── feature_inventory.py
│   │   ├── search/
│   │   │   ├── __init__.py
│   │   │   ├── srs_searcher.py
│   │   │   ├── relationship_mapper.py
│   │   │   └── content_loader.py
│   │   ├── analysis/
│   │   │   ├── __init__.py
│   │   │   ├── antisymmetric_analyzer.py
│   │   │   └── scoring_engine.py
│   │   └── interfaces/
│   │       ├── __init__.py
│   │       ├── fpi_analyzer_api.py
│   │       └── matrix_exporter.py
│   └── testcase_generator/
│       ├── __init__.py
│       ├── core/
│       │   ├── __init__.py
│       │   ├── srs_analyzer.py
│       │   ├── template_processor.py
│       │   └── phase_manager.py
│       ├── generators/
│       │   ├── __init__.py
│       │   ├── requirement_analyzer.py
│       │   ├── testcase_builder.py
│       │   └── validation_engine.py
│       ├── templates/
│       │   ├── srs_templates/
│       │   └── testcase_templates/
│       └── interfaces/
│           ├── __init__.py
│           ├── testcase_generator_api.py
│           └── document_exporter.py
├── shared/
│   ├── __init__.py
│   ├── data_models/
│   │   ├── __init__.py
│   │   ├── image_models.py
│   │   ├── fpi_models.py
│   │   └── testcase_models.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── file_utils.py
│   │   ├── path_utils.py
│   │   └── validation_utils.py
│   └── config/
│       ├── __init__.py
│       ├── settings.py
│       └── env_manager.py
├── orchestrator/
│   ├── __init__.py
│   ├── workflow_manager.py
│   ├── pipeline_orchestrator.py
│   └── api_gateway.py
├── cli/
│   ├── __init__.py
│   ├── image_analyzer_cli.py
│   ├── fpi_analyzer_cli.py
│   ├── testcase_generator_cli.py
│   └── main_cli.py
├── legacy/
│   └── [existing scripts moved here for reference]
├── data/
│   ├── input/
│   ├── output/
│   ├── cache/
│   └── temp/
├── docs/
│   ├── api/
│   ├── modules/
│   └── migration/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── fixtures/
├── requirements.txt
├── setup.py
├── README.md
└── .env.example
```

## Module Interfaces

### Image Analyzer API
```python
class ImageAnalyzerAPI:
    def classify_images(self, image_paths: List[str]) -> List[ImageAnalysisResult]
    def analyze_with_vision_api(self, image_path: str, category: str) -> VisionAnalysisResult
    def batch_process(self, csv_path: str) -> BatchProcessResult
```

### FPI Analyzer API
```python
class FPIAnalyzerAPI:
    def analyze_dependencies(self, main_fpi: str, related_fpis: List[str]) -> DependencyMatrix
    def generate_feature_inventory(self, srs_path: str) -> FeatureInventory
    def create_relationship_matrix(self, features: List[str]) -> RelationshipMatrix
```

### Test Case Generator API
```python
class TestCaseGeneratorAPI:
    def generate_srs_analysis(self, feature_name: str, phase: int = None) -> SRSAnalysisResult
    def create_test_cases(self, srs_content: str, image_analyses: List[dict]) -> TestCaseDocument
    def validate_requirements(self, requirements: List[dict]) -> ValidationResult
```

## Migration Benefits

1. **Separation of Concerns**: Each module has a single, well-defined responsibility
2. **Independent Development**: Teams can work on different modules simultaneously
3. **Scalable Architecture**: Individual modules can be scaled based on demand
4. **Testability**: Each module can be thoroughly unit tested in isolation
5. **Reusability**: Modules can be reused across different projects
6. **Maintainability**: Clear boundaries make maintenance and updates easier
7. **API-First Design**: Clean interfaces enable integration with external systems

## Implementation Phases

### Phase 1: Foundation Setup
- Create directory structure
- Implement shared data models
- Set up configuration management
- Create base interfaces

### Phase 2: Image Analyzer Module
- Extract CLIP classification logic
- Implement vision API client
- Create image processing pipeline
- Build unified API interface

### Phase 3: FPI Analyzer Module
- Extract dependency analysis logic
- Implement matrix generation
- Create SRS search capabilities
- Build analysis API interface

### Phase 4: Test Case Generator Module
- Extract SRS analysis logic
- Implement multi-phase generation
- Create template processing system
- Build generation API interface

### Phase 5: Orchestration Layer
- Implement workflow manager
- Create pipeline orchestrator
- Build CLI interfaces
- Add API gateway

### Phase 6: Migration and Testing
- Migrate existing functionality
- Comprehensive testing
- Documentation updates
- Legacy cleanup

## Data Flow Architecture

```
Input Data → Image Analyzer → Image Analysis Results
                ↓
Input Data → FPI Analyzer → Dependency Matrices
                ↓
SRS Data + Image Results + FPI Results → Test Case Generator → Test Cases
```

This modular approach will transform the current monolithic structure into a maintainable, scalable, and professional software architecture.
