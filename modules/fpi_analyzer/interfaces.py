"""
Interface definitions for FPI Analyzer module.
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from shared.data_models.fpi_models import (
    FeatureInventory,
    DependencyMatrix,
    FeatureDependency
)


class FPIAnalyzerInterface(ABC):
    """Abstract interface for FPI analysis operations."""
    
    @abstractmethod
    def create_feature_inventory(self, srs_path: str) -> FeatureInventory:
        """Create a feature inventory from SRS documents."""
        pass
    
    @abstractmethod
    def analyze_dependencies(self, feature_inventory: FeatureInventory) -> List[FeatureDependency]:
        """Analyze dependencies between features."""
        pass
    
    @abstractmethod
    def generate_dependency_matrix(self, dependencies: List[FeatureDependency]) -> DependencyMatrix:
        """Generate a dependency matrix from feature dependencies."""
        pass
    
    @abstractmethod
    def export_matrix(self, matrix: DependencyMatrix, output_path: str) -> str:
        """Export dependency matrix to CSV or JSON format."""
        pass


class FeatureInventoryInterface(ABC):
    """Interface for feature inventory operations."""
    
    @abstractmethod
    def discover_features(self, srs_path: str) -> List[dict]:
        """Discover features from SRS documents."""
        pass
    
    @abstractmethod
    def categorize_features(self, features: List[dict]) -> Dict[str, List[dict]]:
        """Categorize features by type or domain."""
        pass


class DependencyAnalyzerInterface(ABC):
    """Interface for dependency analysis operations."""
    
    @abstractmethod
    def analyze_feature_dependencies(self, features: List[dict]) -> List[FeatureDependency]:
        """Analyze dependencies between features."""
        pass
    
    @abstractmethod
    def validate_dependencies(self, dependencies: List[FeatureDependency]) -> List[str]:
        """Validate dependencies for consistency and correctness."""
        pass


class MatrixGeneratorInterface(ABC):
    """Interface for matrix generation operations."""
    
    @abstractmethod
    def create_matrix(self, dependencies: List[FeatureDependency]) -> DependencyMatrix:
        """Create a dependency matrix from feature dependencies."""
        pass
    
    @abstractmethod
    def export_to_csv(self, matrix: DependencyMatrix, output_path: str) -> str:
        """Export matrix to CSV format."""
        pass
    
    @abstractmethod
    def export_to_json(self, matrix: DependencyMatrix, output_path: str) -> str:
        """Export matrix to JSON format."""
        pass
