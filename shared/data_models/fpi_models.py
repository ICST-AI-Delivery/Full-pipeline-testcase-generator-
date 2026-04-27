"""
Data models for FPI Analyzer module.

These models define the structure of data produced by the FPI Analyzer
and consumed by other modules.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any, Set
from datetime import datetime
from enum import Enum


class DependencyType(Enum):
    """Types of dependencies between FPIs."""
    CRITICAL = "critical"  # ±3
    HIGH_PRIORITY = "high_priority"  # ±2
    OPTIONAL = "optional"  # ±1
    NONE = "none"  # 0


class RelationshipDirection(Enum):
    """Direction of dependency relationship."""
    DEPENDS_ON = "depends_on"  # Positive score
    DEPENDED_BY = "depended_by"  # Negative score
    BIDIRECTIONAL = "bidirectional"
    NONE = "none"


@dataclass
class FPIDependency:
    """Represents a dependency relationship between two FPIs."""
    main_fpi: str
    related_fpi: str
    dependency_score: int  # -3 to +3
    dependency_type: DependencyType
    direction: RelationshipDirection
    justification: str
    evidence: str
    feature_path: str
    confidence: float = 0.0
    timestamp: datetime = field(default_factory=datetime.now)
    
    @property
    def is_critical(self) -> bool:
        """Check if this is a critical dependency."""
        return abs(self.dependency_score) == 3
    
    @property
    def is_significant(self) -> bool:
        """Check if this is a significant dependency (score != 0)."""
        return self.dependency_score != 0


@dataclass
class FeatureMetadata:
    """Metadata about an SRS feature."""
    feature_name: str
    feature_path: str
    domain: str
    description: Optional[str] = None
    requirements_count: int = 0
    file_size: int = 0
    last_modified: Optional[datetime] = None
    approval_status: str = "unknown"
    test_stage: str = "unknown"
    responsible_team: Optional[str] = None
    related_features: List[str] = field(default_factory=list)
    tags: Set[str] = field(default_factory=set)


@dataclass
class DependencyMatrix:
    """Complete dependency matrix for a main FPI against related FPIs."""
    main_fpi: str
    total_features_analyzed: int
    non_zero_dependencies: int
    dependency_relationships: List[FPIDependency] = field(default_factory=list)
    matrix_data: Dict[str, Dict[str, int]] = field(default_factory=dict)  # [main][related] = score
    analysis_metadata: Dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.now)
    
    def get_dependencies_by_type(self, dep_type: DependencyType) -> List[FPIDependency]:
        """Get all dependencies of a specific type."""
        return [dep for dep in self.dependency_relationships if dep.dependency_type == dep_type]
    
    def get_critical_dependencies(self) -> List[FPIDependency]:
        """Get all critical dependencies (±3)."""
        return self.get_dependencies_by_type(DependencyType.CRITICAL)
    
    def get_dependency_score(self, related_fpi: str) -> int:
        """Get the dependency score for a specific related FPI."""
        for dep in self.dependency_relationships:
            if dep.related_fpi == related_fpi:
                return dep.dependency_score
        return 0
    
    @property
    def dependency_summary(self) -> Dict[str, int]:
        """Get a summary of dependencies by type."""
        summary = {dep_type.value: 0 for dep_type in DependencyType}
        for dep in self.dependency_relationships:
            summary[dep.dependency_type.value] += 1
        return summary


@dataclass
class FeatureInventory:
    """Complete inventory of SRS features discovered in the system."""
    total_features: int
    domains: Dict[str, int]  # domain -> feature count
    features: List[FeatureMetadata] = field(default_factory=list)
    feature_paths: List[str] = field(default_factory=list)
    discovery_metadata: Dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.now)
    
    def get_features_by_domain(self, domain: str) -> List[FeatureMetadata]:
        """Get all features for a specific domain."""
        return [feature for feature in self.features if feature.domain == domain]
    
    def find_feature(self, feature_name: str) -> Optional[FeatureMetadata]:
        """Find a specific feature by name."""
        for feature in self.features:
            if feature.feature_name == feature_name:
                return feature
        return None
    
    @property
    def domain_distribution(self) -> Dict[str, float]:
        """Get percentage distribution of features by domain."""
        if self.total_features == 0:
            return {}
        return {domain: (count / self.total_features) * 100 
                for domain, count in self.domains.items()}


@dataclass
class RelationshipMatrix:
    """Matrix showing relationships between multiple FPIs."""
    features: List[str]
    matrix_size: int
    relationships: Dict[str, Dict[str, FPIDependency]] = field(default_factory=dict)
    antisymmetric_validation: bool = False
    matrix_statistics: Dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.now)
    
    def add_relationship(self, dependency: FPIDependency):
        """Add a relationship to the matrix."""
        if dependency.main_fpi not in self.relationships:
            self.relationships[dependency.main_fpi] = {}
        self.relationships[dependency.main_fpi][dependency.related_fpi] = dependency
    
    def get_relationship(self, main_fpi: str, related_fpi: str) -> Optional[FPIDependency]:
        """Get the relationship between two FPIs."""
        return self.relationships.get(main_fpi, {}).get(related_fpi)
    
    def validate_antisymmetric(self) -> bool:
        """Validate that the matrix follows antisymmetric properties."""
        for main_fpi in self.relationships:
            for related_fpi in self.relationships[main_fpi]:
                forward_score = self.relationships[main_fpi][related_fpi].dependency_score
                reverse_rel = self.get_relationship(related_fpi, main_fpi)
                if reverse_rel:
                    reverse_score = reverse_rel.dependency_score
                    if forward_score + reverse_score != 0:
                        return False
        return True
    
    @property
    def total_relationships(self) -> int:
        """Get total number of relationships in the matrix."""
        return sum(len(related) for related in self.relationships.values())


@dataclass
class ContextInjectionSummary:
    """Summary for context injection in test case generation."""
    main_fpi: str
    critical_dependencies: List[Dict[str, Any]] = field(default_factory=list)
    high_priority_dependencies: List[Dict[str, Any]] = field(default_factory=list)
    optional_dependencies: List[Dict[str, Any]] = field(default_factory=list)
    statistics: Dict[str, int] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.now)
    
    @property
    def total_dependencies(self) -> int:
        """Get total number of dependencies."""
        return (len(self.critical_dependencies) + 
                len(self.high_priority_dependencies) + 
                len(self.optional_dependencies))
    
    def get_top_dependencies(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get top dependencies by priority."""
        all_deps = (self.critical_dependencies + 
                   self.high_priority_dependencies + 
                   self.optional_dependencies)
        return all_deps[:limit]


@dataclass
class FPIAnalysisConfig:
    """Configuration for FPI analysis operations."""
    srs_base_path: str = "SRS Export"
    output_directory: str = "fpi_matrix_results"
    enable_antisymmetric_validation: bool = True
    dependency_threshold: int = 1  # Minimum score to consider as dependency
    max_features_per_analysis: int = 1500
    enable_caching: bool = True
    cache_directory: str = "data/cache/fpi"
    parallel_processing: bool = True
    max_workers: int = 4
    analysis_timeout: int = 300  # seconds
