"""
Data models for Test Case Generator module.

These models define the structure of data produced by the Test Case Generator
and consumed by other modules.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any, Union
from datetime import datetime
from enum import Enum


class TestCasePriority(Enum):
    """Priority levels for test cases."""
    A = "A"  # Critical functionality
    B = "B"  # Important functionality
    C = "C"  # Standard functionality
    D = "D"  # Edge cases and gaps


class RequirementStatus(Enum):
    """Status of requirements in SRS analysis."""
    ACTIVE = "active"
    OBSOLETE = "obsolete"
    INFORMATIONAL = "informational"
    REFERENCED = "referenced"


class TestabilityLevel(Enum):
    """Testability assessment levels."""
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class ValidationStatus(Enum):
    """Validation status for requirements and test cases."""
    VALID = "valid"
    WARNING = "warning"
    ERROR = "error"
    NOT_VALIDATED = "not_validated"


@dataclass
class RequirementAnalysis:
    """Analysis of a single requirement from SRS."""
    requirement_id: str
    title: str
    description: str
    status: RequirementStatus
    testability: TestabilityLevel
    testability_method: str
    dependencies: List[str] = field(default_factory=list)
    implementation_notes: str = ""
    rqa_score: Optional[float] = None
    rqa_issues: List[str] = field(default_factory=list)
    mitigation_strategy: str = ""
    validation_status: ValidationStatus = ValidationStatus.NOT_VALIDATED
    validation_messages: List[str] = field(default_factory=list)
    
    @property
    def is_testable(self) -> bool:
        """Check if requirement is testable."""
        return self.testability != TestabilityLevel.LOW and self.status == RequirementStatus.ACTIVE


@dataclass
class TestStep:
    """Individual test step within a test case."""
    step_number: int
    description: str
    expected_result: str
    test_data: Optional[str] = None
    preconditions: List[str] = field(default_factory=list)
    notes: str = ""


@dataclass
class TestCase:
    """Complete test case definition."""
    test_case_id: str
    title: str
    description: str
    priority: TestCasePriority
    feature_name: str
    requirements_covered: List[str] = field(default_factory=list)
    preconditions: List[str] = field(default_factory=list)
    test_steps: List[TestStep] = field(default_factory=list)
    expected_results: List[str] = field(default_factory=list)
    postconditions: List[str] = field(default_factory=list)
    test_data: Dict[str, Any] = field(default_factory=dict)
    dependencies: List[str] = field(default_factory=list)
    estimated_duration: Optional[int] = None  # minutes
    automation_feasibility: str = "manual"
    risk_level: str = "medium"
    validation_status: ValidationStatus = ValidationStatus.NOT_VALIDATED
    validation_messages: List[str] = field(default_factory=list)
    
    @property
    def step_count(self) -> int:
        """Get number of test steps."""
        return len(self.test_steps)
    
    @property
    def is_valid(self) -> bool:
        """Check if test case is valid."""
        return (len(self.test_steps) > 0 and 
                len(self.expected_results) > 0 and
                len(self.requirements_covered) > 0)


@dataclass
class RequirementTraceability:
    """Traceability between requirements and test cases."""
    requirement_id: str
    test_cases: List[str] = field(default_factory=list)
    coverage_status: str = "not_covered"
    coverage_notes: str = ""
    
    @property
    def is_covered(self) -> bool:
        """Check if requirement is covered by test cases."""
        return len(self.test_cases) > 0


@dataclass
class TestCaseDependency:
    """Dependency relationship between test cases."""
    dependent_test_case: str
    prerequisite_test_case: str
    dependency_type: str  # "setup", "data", "state"
    description: str
    is_blocking: bool = True


@dataclass
class SRSAnalysisResult:
    """Complete result of SRS analysis for a feature."""
    feature_name: str
    feature_id: str
    domain: str
    approval_status: str
    test_stage: str
    analysis_date: datetime
    requirements_summary: List[RequirementAnalysis] = field(default_factory=list)
    visual_elements_analysis: Dict[str, Any] = field(default_factory=dict)
    data_structure_analysis: Dict[str, Any] = field(default_factory=dict)
    core_functionality: Dict[str, Any] = field(default_factory=dict)
    domain_specific_analysis: Dict[str, Any] = field(default_factory=dict)
    formula_verification: Dict[str, Any] = field(default_factory=dict)
    image_traceability: Dict[str, List[str]] = field(default_factory=dict)
    processing_metadata: Dict[str, Any] = field(default_factory=dict)
    validation_status: ValidationStatus = ValidationStatus.NOT_VALIDATED
    validation_messages: List[str] = field(default_factory=list)
    
    @property
    def total_requirements(self) -> int:
        """Get total number of requirements."""
        return len(self.requirements_summary)
    
    @property
    def testable_requirements(self) -> List[RequirementAnalysis]:
        """Get all testable requirements."""
        return [req for req in self.requirements_summary if req.is_testable]
    
    @property
    def requirements_by_status(self) -> Dict[str, int]:
        """Get count of requirements by status."""
        status_count = {}
        for req in self.requirements_summary:
            status = req.status.value
            status_count[status] = status_count.get(status, 0) + 1
        return status_count


@dataclass
class TestCaseDocument:
    """Complete test case document for a feature."""
    feature_name: str
    srs_analysis: SRSAnalysisResult
    test_cases: List[TestCase] = field(default_factory=list)
    requirement_traceability: List[RequirementTraceability] = field(default_factory=list)
    test_case_dependencies: List[TestCaseDependency] = field(default_factory=list)
    execution_order: List[str] = field(default_factory=list)
    coverage_summary: Dict[str, Any] = field(default_factory=dict)
    document_metadata: Dict[str, Any] = field(default_factory=dict)
    generation_timestamp: datetime = field(default_factory=datetime.now)
    validation_status: ValidationStatus = ValidationStatus.NOT_VALIDATED
    validation_messages: List[str] = field(default_factory=list)
    
    def get_test_cases_by_priority(self, priority: TestCasePriority) -> List[TestCase]:
        """Get test cases by priority level."""
        return [tc for tc in self.test_cases if tc.priority == priority]
    
    def get_requirement_coverage(self, requirement_id: str) -> Optional[RequirementTraceability]:
        """Get coverage information for a specific requirement."""
        for trace in self.requirement_traceability:
            if trace.requirement_id == requirement_id:
                return trace
        return None
    
    @property
    def total_test_cases(self) -> int:
        """Get total number of test cases."""
        return len(self.test_cases)
    
    @property
    def coverage_percentage(self) -> float:
        """Calculate requirement coverage percentage."""
        if not self.srs_analysis.testable_requirements:
            return 0.0
        
        covered_requirements = sum(1 for trace in self.requirement_traceability 
                                 if trace.is_covered)
        total_testable = len(self.srs_analysis.testable_requirements)
        
        return (covered_requirements / total_testable) * 100 if total_testable > 0 else 0.0
    
    @property
    def test_case_distribution(self) -> Dict[str, int]:
        """Get distribution of test cases by priority."""
        distribution = {priority.value: 0 for priority in TestCasePriority}
        for tc in self.test_cases:
            distribution[tc.priority.value] += 1
        return distribution


@dataclass
class ValidationResult:
    """Result of validation operations."""
    validation_type: str  # "requirement", "test_case", "document"
    target_id: str
    status: ValidationStatus
    messages: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    suggestions: List[str] = field(default_factory=list)
    validation_timestamp: datetime = field(default_factory=datetime.now)
    
    @property
    def is_valid(self) -> bool:
        """Check if validation passed."""
        return self.status == ValidationStatus.VALID
    
    @property
    def has_warnings(self) -> bool:
        """Check if validation has warnings."""
        return len(self.warnings) > 0 or self.status == ValidationStatus.WARNING
    
    @property
    def has_errors(self) -> bool:
        """Check if validation has errors."""
        return len(self.errors) > 0 or self.status == ValidationStatus.ERROR


@dataclass
class GenerationPhaseResult:
    """Result of a single phase in multi-phase generation."""
    phase_number: int
    phase_name: str
    success: bool
    content_generated: str
    processing_time: float
    tokens_used: int = 0
    error_message: Optional[str] = None
    warnings: List[str] = field(default_factory=list)
    timestamp: datetime = field(default_factory=datetime.now)


@dataclass
class TestCaseGenerationConfig:
    """Configuration for test case generation operations."""
    srs_template_path: str = "SRS_Analysis_TestCase_Generation.txt"
    output_directory: str = "generated_testcases(final output)"
    enable_multi_phase: bool = True
    max_phases: int = 5
    api_timeout: int = 120  # seconds
    max_tokens_per_phase: int = 4000
    enable_validation: bool = True
    validation_strictness: str = "medium"  # "low", "medium", "high"
    enable_caching: bool = True
    cache_directory: str = "data/cache/testcases"
    parallel_processing: bool = False  # Sequential for consistency
    retry_attempts: int = 3
    retry_delay: int = 5  # seconds
