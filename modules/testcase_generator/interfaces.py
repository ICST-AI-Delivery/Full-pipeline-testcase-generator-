"""
Interface definitions for Test Case Generator module.
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from shared.data_models.testcase_models import (
    TestCase,
    TestSuite,
    TestRequirement
)
from shared.data_models.fpi_models import (
    FeatureInventory,
    DependencyMatrix
)


class TestCaseGeneratorInterface(ABC):
    """Abstract interface for test case generation operations."""
    
    @abstractmethod
    def generate_test_cases(self, feature_id: str, requirements: List[TestRequirement]) -> List[TestCase]:
        """Generate test cases for a specific feature."""
        pass
    
    @abstractmethod
    def generate_test_suite(self, feature_inventory: FeatureInventory, 
                           dependency_matrix: DependencyMatrix) -> TestSuite:
        """Generate a complete test suite from feature inventory and dependencies."""
        pass
    
    @abstractmethod
    def export_test_cases(self, test_cases: List[TestCase], output_path: str) -> str:
        """Export test cases to a file."""
        pass


class SRSAnalyzerInterface(ABC):
    """Interface for SRS analysis operations."""
    
    @abstractmethod
    def extract_requirements(self, srs_path: str) -> List[TestRequirement]:
        """Extract test requirements from SRS documents."""
        pass
    
    @abstractmethod
    def analyze_requirement(self, requirement: TestRequirement) -> Dict:
        """Analyze a requirement for test case generation."""
        pass
    
    @abstractmethod
    def validate_requirements(self, requirements: List[TestRequirement]) -> List[str]:
        """Validate requirements for testability."""
        pass


class TestSuiteBuilderInterface(ABC):
    """Interface for test suite building operations."""
    
    @abstractmethod
    def build_test_suite(self, test_cases: List[TestCase]) -> TestSuite:
        """Build a test suite from test cases."""
        pass
    
    @abstractmethod
    def optimize_test_suite(self, test_suite: TestSuite) -> TestSuite:
        """Optimize a test suite for coverage and efficiency."""
        pass
    
    @abstractmethod
    def export_test_suite(self, test_suite: TestSuite, output_path: str) -> str:
        """Export a test suite to a file."""
        pass


class TestCaseManagerInterface(ABC):
    """Interface for test case management operations."""
    
    @abstractmethod
    def create_test_cases(self, feature_id: str, srs_path: str) -> List[TestCase]:
        """Create test cases for a specific feature from SRS."""
        pass
    
    @abstractmethod
    def create_test_suite(self, feature_ids: List[str], srs_path: str) -> TestSuite:
        """Create a test suite for multiple features."""
        pass
    
    @abstractmethod
    def export_results(self, output_path: str, format: str = "json") -> str:
        """Export test cases or test suite to a file."""
        pass
