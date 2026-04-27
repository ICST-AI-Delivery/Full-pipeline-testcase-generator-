"""
FPI Analyzer Module

This module handles Feature dependency analysis and matrix generation.
It provides functionality to analyze SRS features, create dependency matrices,
and generate relationship data between different FPIs.

Main Components:
- FeatureInventory: Discovery and cataloging of SRS features
- DependencyAnalyzer: Analysis of feature dependencies
- MatrixGenerator: Generation of dependency matrices
- ComprehensiveMatrixGenerator: Advanced matrix generation with enhanced analysis
- ComprehensiveDependencyAnalyzer: Comprehensive dependency analysis
- CompleteDependencyAnalyzer: Complete FPI dependency analysis
- TestcaseAnalyzer: FPI testcase context analysis
- AntisymmetricAnalyzer: Antisymmetric dependency analysis
- Processor: Universal FPI processing pipeline
- FPIAnalyzer: Main interface combining all functionality
"""

from .interfaces import FPIAnalyzerInterface
from .feature_inventory import FeatureInventory
from .dependency_analyzer import DependencyAnalyzer
from .matrix_generator import MatrixGenerator

# Import the reorganized analyzers
try:
    from .comprehensive_matrix_generator import *
except ImportError:
    pass

try:
    from .comprehensive_dependency_analyzer import *
except ImportError:
    pass

try:
    from .complete_dependency_analyzer import *
except ImportError:
    pass

try:
    from .testcase_analyzer import *
except ImportError:
    pass

try:
    from .antisymmetric_analyzer import *
except ImportError:
    pass

try:
    from .processor import *
except ImportError:
    pass

try:
    from .fpi_analyzer import FPIAnalyzer
except ImportError:
    pass

# Import utilities
from . import utils

__all__ = [
    'FPIAnalyzerInterface',
    'FeatureInventory',
    'DependencyAnalyzer',
    'MatrixGenerator',
    'utils'
]

__version__ = "1.0.0"
