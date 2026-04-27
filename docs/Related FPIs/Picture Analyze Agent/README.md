# Smart SRS Feature Discovery & Critical Relationship Extraction System

A comprehensive automotive feature relationship discovery and analysis system that combines SRS document analysis with critical dependency extraction tools. This system identifies feature dependencies, generates relationship matrices, and extracts critical relationships using advanced AI and graph analysis techniques.

## 🚗 Overview

This system is designed specifically for automotive development environments to:
- **Discover relationships** between features in SRS documents using multi-stage AI analysis
- **Extract critical dependencies** (±3 relationships) from relationship matrices
- **Generate enhanced matrices** from real SRS data analysis
- **Process relationships in batch** with comprehensive reporting and validation

The system uses a hybrid approach combining exact matching, semantic similarity, graph analysis, and specialized extraction tools for complete relationship analysis.

## 🎯 Key Features

### SRS Discovery System
- **Multi-Stage Discovery**: Combines exact matching, semantic analysis, and graph relationships
- **Directional Scoring**: Uses -3 to +3 scale where negative scores indicate input dependencies and positive scores indicate output importance
- **Automotive Domain Expertise**: Specialized for CAN signals, telltale codes, expert domains, and pop-up IDs
- **High Performance**: Optimized with caching, FAISS indexing, and inverted indices
- **Graceful Degradation**: Core functionality works even without optional AI dependencies

### Critical Relationship Extraction Tools
- **Critical Dependency Extraction**: Identifies ±3 relationships (critical dependencies) from relationship matrices
- **Batch Processing Pipeline**: Processes multiple features simultaneously with comprehensive analysis
- **Enhanced Matrix Generation**: Creates relationship matrices from real SRS data analysis
- **Bidirectional Analysis**: Detects input dependencies, output dependencies, and bidirectional relationships
- **Validation & Reporting**: Built-in matrix validation and detailed summary reports
- **Integration Ready**: Designed to integrate with existing Picture Analyze Agent workflows

## 🏗️ Architecture

### Stage 1: Exact Match Engine
- Lightning-fast inverted indices for instant lookups
- CAN signal dependency analysis with directional scoring
- Expert domain overlap detection
- Telltale code and pop-up ID matching

### Stage 2: Semantic Vector Engine
- AI-powered similarity using sentence-transformers
- FAISS indexing for fast vector search
- Contextual relationship discovery
- Automotive domain concept extraction

### Stage 3: Graph Relationship Engine
- Multi-hop dependency discovery using NetworkX
- Transitive relationship analysis
- Structural similarity detection
- Hub feature identification

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Install core dependencies
pip install pandas numpy

# Install optional AI dependencies (recommended)
pip install sentence-transformers faiss-cpu networkx

# Or install all at once
pip install -r requirements.txt
```

### 2. Run the Test Suite

```bash
cd "Picture Analyze Agent"
python test_srs_discovery.py
```

### 3. Basic Usage

#### SRS Discovery System
```python
from srs_discovery.parser import SRSParser
from srs_discovery.indexer import ExactMatchIndexer

# Parse SRS data
parser = SRSParser()
features = parser.parse_srs_folder("../SRS Export/SRS_Audio")

# Build indices and find relationships
indexer = ExactMatchIndexer()
indexer.build_indices(features)
relationships = indexer.find_exact_matches("your_feature_id")

# Print results
for rel in relationships:
    print(f"{rel.related_feature_id}: {rel.score:+d} ({rel.relationship_type})")
```

#### Critical Relationship Extraction
```bash
# Extract critical dependencies for a single feature
python extract_critical_relationships.py --matrix_path sample_relationship_matrix.json --target_feature "Low_Fuel_Warning"

# Run batch processing pipeline
python integration_pipeline.py --matrix sample_relationship_matrix.json --features "Feature1" "Feature2" --summary

# Generate enhanced matrix from real SRS data
python enhanced_fpi_matrix_generator.py
```

## 📊 Similarity Scale (-3 to +3)

The system uses a bidirectional scoring system:

- **-3 (Critical Input)**: Current feature critically depends on this feature
- **-2 (High Input)**: Current feature has high dependency on this feature  
- **-1 (Moderate Input)**: Current feature has moderate dependency on this feature
- **0**: No significant relationship
- **+1 (Moderate Output)**: This feature has moderate importance for other features
- **+2 (High Output)**: This feature has high importance for other features
- **+3 (Critical Output)**: This feature is critical for other features

## 🔍 Relationship Types

- **`direct_signal`**: Direct CAN signal dependency
- **`shared_resource`**: Shared telltale codes, pop-ups, or visual elements
- **`domain_expertise`**: Shared expert domain knowledge
- **`semantic_similarity`**: AI-detected content similarity
- **`transitive_dependency`**: Multi-hop graph relationship
- **`structural_similarity`**: Similar graph neighborhood structure

## 📁 Project Structure

```
Picture Analyze Agent/
├── srs_discovery/
│   ├── __init__.py                    # Package initialization
│   ├── utils.py                       # Core data structures and utilities
│   ├── parser.py                      # SRS CSV parser
│   ├── indexer.py                     # Exact match engine (Stage 1)
│   ├── semantic_engine.py             # Semantic search engine (Stage 2)
│   └── graph_engine.py                # Graph relationship engine (Stage 3)
├── extract_critical_relationships.py  # Critical dependency extraction tool
├── integration_pipeline.py            # Batch processing pipeline
├── enhanced_fpi_matrix_generator.py   # Enhanced matrix generation from SRS data
├── sample_relationship_matrix.json    # Example automotive relationship matrix
├── results/                           # Output directory for analysis results
├── test_srs_discovery.py             # SRS discovery system test suite
├── test_*.py                          # Additional test files
├── requirements.txt                   # Dependencies
└── README.md                         # This file
```

## 🧪 Testing

The test suite automatically:

1. **Finds your SRS Export data** (looks in current directory and parent directory)
2. **Tests all system components** with real automotive data
3. **Shows relationship discovery results** with scores and evidence
4. **Validates performance** and provides statistics
5. **Handles missing dependencies** gracefully

### Test Output Example

```
🚗 Smart SRS Feature Discovery System - Test Suite
============================================================
✅ Found SRS Export folder: /path/to/SRS Export
✅ Successfully parsed 45 features from SRS_Audio
🎯 Built indices for 45 features
   📊 CAN signals: 12
   📊 Expert domains: 8
✅ Found 7 exact match relationships
   1. VEH-F166_Audio_Control (score: -2, confidence: 0.95)
      Type: direct_signal
      Evidence: Depends on ManettinoSts from VEH-F166_Audio_Control
```

## 🔧 Advanced Usage

### Critical Relationship Extraction Tools

#### Extract Critical Dependencies
```python
# Load and analyze relationship matrix
from extract_critical_relationships import CriticalRelationshipExtractor

extractor = CriticalRelationshipExtractor("sample_relationship_matrix.json")
critical_deps = extractor.extract_critical_relationships("Low_Fuel_Warning")

# Print critical dependencies
for dep in critical_deps:
    print(f"{dep['feature']}: {dep['score']:+d} ({dep['type']})")
```

#### Batch Processing Pipeline
```python
# Process multiple features with comprehensive analysis
from integration_pipeline import IntegrationPipeline

pipeline = IntegrationPipeline("sample_relationship_matrix.json")
results = pipeline.process_features(["Feature1", "Feature2"], generate_summary=True)

# Access detailed results
for feature, analysis in results.items():
    print(f"{feature}: {len(analysis['critical_relationships'])} critical dependencies")
```

#### Enhanced Matrix Generation
```python
# Generate relationship matrix from real SRS data
from enhanced_fpi_matrix_generator import EnhancedFPIMatrixGenerator

generator = EnhancedFPIMatrixGenerator("../SRS Export")
generator.analyze_srs_features()
matrix = generator.calculate_fpi_relationships(["VEH-F001", "VEH-F002"])
generator.save_matrix(matrix, "enhanced_matrix.json")
```

### Custom Semantic Models

```python
from srs_discovery.semantic_engine import SemanticSearchEngine

# Use a different sentence transformer model
semantic_engine = SemanticSearchEngine(model_name="all-mpnet-base-v2")
```

### Graph Analysis

```python
from srs_discovery.graph_engine import RelationshipGraphEngine

graph_engine = RelationshipGraphEngine()
graph_engine.build_graph(features, exact_relationships)

# Get complete dependency chain
dependency_chain = graph_engine.get_dependency_chain("your_feature_id")
print(f"Direct dependencies: {dependency_chain['direct_dependencies']}")
```

### Performance Optimization

The system includes several performance optimizations:

- **Caching**: Semantic embeddings are cached to disk
- **FAISS Indexing**: Fast vector similarity search
- **Inverted Indices**: O(1) exact match lookups
- **Batch Processing**: Efficient embedding generation
- **Matrix Validation**: Built-in validation for relationship matrices
- **Results Caching**: Automated caching of analysis results

## 🎯 Automotive Domain Features

### CAN Signal Analysis
- Automatically detects signal providers vs consumers
- Identifies critical automotive signals (ManettinoSts, ESCOFFLampRequest, etc.)
- Provides directional dependency scoring

### Expert Domain Recognition
- IOC (Input/Output Control) systems
- Audio and connectivity domains
- Safety and diagnostic systems
- Powertrain and chassis control

### Telltale and Visual Elements
- Warning lamp relationships
- Pop-up message dependencies
- HMI element connections
- Visual indicator clustering

## 🚀 Integration

This system is designed to integrate with the existing Picture Analyze Agent pipeline for:

- **SRS Analysis**: Automated requirement relationship discovery
- **Test Case Generation**: Dependency-aware test planning
- **Feature Impact Analysis**: Understanding change propagation
- **System Architecture Validation**: Relationship verification

## 📈 Performance

- **Exact Matching**: Sub-second response for 1000+ features
- **Semantic Search**: ~2-5 seconds for embedding generation, <1s for queries
- **Graph Analysis**: Scales to 10,000+ features with NetworkX optimization
- **Memory Efficient**: Streaming processing for large SRS datasets

## 🛠️ Troubleshooting

### Common Issues

1. **"SRS Export folder not found"**
   - Ensure the SRS Export folder is in the current directory or parent directory
   - Check folder permissions

2. **"Semantic dependencies not available"**
   - Install with: `pip install sentence-transformers faiss-cpu`
   - This is optional - exact matching will still work

3. **"NetworkX not available"**
   - Install with: `pip install networkx`
   - This is optional - other engines will still work

### Performance Tips

- Start with smaller SRS folders for initial testing
- Use caching for repeated semantic analysis
- Consider using GPU-accelerated FAISS for large datasets

## 📝 License

This system is part of the Picture Analyze Agent project for automotive development environments.

---

**Ready to discover automotive feature relationships with AI-powered precision! 🚗🤖**
