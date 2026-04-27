"""
Data models for inter-module communication.

This module defines the data structures used for communication
between the Image Analyzer, FPI Analyzer, and Test Case Generator modules.
"""

from .image_models import (
    ImageAnalysisResult,
    VisionAnalysisResult,
    BatchProcessResult,
    ImageClassification,
    TechnicalElement
)

from .fpi_models import (
    DependencyMatrix,
    FeatureInventory,
    RelationshipMatrix,
    FPIDependency,
    FeatureMetadata
)

from .testcase_models import (
    SRSAnalysisResult,
    TestCaseDocument,
    ValidationResult,
    RequirementAnalysis,
    TestCase
)

__all__ = [
    # Image models
    'ImageAnalysisResult',
    'VisionAnalysisResult', 
    'BatchProcessResult',
    'ImageClassification',
    'TechnicalElement',
    
    # FPI models
    'DependencyMatrix',
    'FeatureInventory',
    'RelationshipMatrix',
    'FPIDependency',
    'FeatureMetadata',
    
    # Test case models
    'SRSAnalysisResult',
    'TestCaseDocument',
    'ValidationResult',
    'RequirementAnalysis',
    'TestCase'
]
