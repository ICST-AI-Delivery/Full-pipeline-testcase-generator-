"""
Utility functions and data structures for SRS Discovery System
"""

import re
import json
import pickle
import logging
from typing import Dict, List, Set, Tuple, Any, Optional
from dataclasses import dataclass, asdict
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class Requirement:
    """Data structure for individual requirements"""
    id: str
    content: str
    artifact_type: str
    responsible_domain: str
    test_stage: str
    verification_criteria: str
    grooming_status: str
    expert_domains: List[str]
    rqa_score: int
    state: str
    visual_elements: List[str] = None
    can_signals: List[str] = None
    telltale_codes: List[str] = None
    popup_ids: List[str] = None
    
    def __post_init__(self):
        if self.visual_elements is None:
            self.visual_elements = []
        if self.can_signals is None:
            self.can_signals = []
        if self.telltale_codes is None:
            self.telltale_codes = []
        if self.popup_ids is None:
            self.popup_ids = []

@dataclass
class Feature:
    """Data structure for complete features"""
    id: str
    name: str
    domain: str
    requirements: List[Requirement]
    can_signals: Set[str]
    expert_domains: Set[str]
    telltale_codes: Set[str]
    popup_ids: Set[str]
    visual_elements: Set[str]
    file_path: str
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization"""
        return {
            'id': self.id,
            'name': self.name,
            'domain': self.domain,
            'requirements': [asdict(req) for req in self.requirements],
            'can_signals': list(self.can_signals),
            'expert_domains': list(self.expert_domains),
            'telltale_codes': list(self.telltale_codes),
            'popup_ids': list(self.popup_ids),
            'visual_elements': list(self.visual_elements),
            'file_path': self.file_path
        }

@dataclass
class RelationshipScore:
    """Data structure for relationship scoring"""
    related_feature_id: str
    score: int  # -3 to +3 scale
    relationship_type: str
    evidence: List[str]
    confidence: float
    
    @property
    def direction(self) -> str:
        """Get relationship direction"""
        if self.score < 0:
            return "input_dependency"
        elif self.score > 0:
            return "output_importance"
        else:
            return "no_relationship"
    
    @property
    def strength(self) -> str:
        """Get relationship strength"""
        abs_score = abs(self.score)
        if abs_score == 3:
            return "critical"
        elif abs_score == 2:
            return "high"
        elif abs_score == 1:
            return "moderate"
        else:
            return "none"

class TextProcessor:
    """Text processing utilities for automotive domain"""
    
    # Automotive-specific patterns
    CAN_SIGNAL_PATTERN = re.compile(r'([A-Z_]+\.[A-Za-z_]+|[A-Z_]+_[A-Z_]+)')
    TELLTALE_CODE_PATTERN = re.compile(r'(\d{5})')
    POPUP_ID_PATTERN = re.compile(r'(01\d{6})')
    POSITION_PATTERN = re.compile(r'Position_?\d+')
    
    @staticmethod
    def extract_can_signals(text: str) -> List[str]:
        """Extract CAN signal names from text"""
        signals = TextProcessor.CAN_SIGNAL_PATTERN.findall(text)
        # Filter out common false positives
        filtered_signals = []
        for signal in signals:
            if len(signal) > 3 and '_' in signal:
                filtered_signals.append(signal)
        return list(set(filtered_signals))
    
    @staticmethod
    def extract_telltale_codes(text: str) -> List[str]:
        """Extract telltale codes from text"""
        codes = TextProcessor.TELLTALE_CODE_PATTERN.findall(text)
        return list(set(codes))
    
    @staticmethod
    def extract_popup_ids(text: str) -> List[str]:
        """Extract pop-up IDs from text"""
        ids = TextProcessor.POPUP_ID_PATTERN.findall(text)
        return list(set(ids))
    
    @staticmethod
    def extract_visual_elements(text: str) -> List[str]:
        """Extract visual element references from text"""
        # Look for image references
        image_pattern = re.compile(r'image\d+\.png')
        images = image_pattern.findall(text)
        return list(set(images))
    
    @staticmethod
    def extract_expert_domains(text: str) -> List[str]:
        """Extract expert domain references"""
        # Common automotive domains
        domains = [
            'IOC_IOC', 'System Infra', 'Android HMI', 'Audio Processing',
            'ADVNet', 'System Core', 'System Qualification'
        ]
        found_domains = []
        for domain in domains:
            if domain in text:
                found_domains.append(domain)
        return found_domains
    
    @staticmethod
    def clean_text(text: str) -> str:
        """Clean and normalize text for processing"""
        if not text:
            return ""
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Remove special characters but keep automotive-specific ones
        text = re.sub(r'[^\w\s\-\._/()]', ' ', text)
        
        return text.strip()

class CacheManager:
    """Manage caching for expensive operations"""
    
    def __init__(self, cache_dir: str = "data/cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
    
    def save_cache(self, key: str, data: Any) -> None:
        """Save data to cache"""
        cache_file = self.cache_dir / f"{key}.pkl"
        try:
            with open(cache_file, 'wb') as f:
                pickle.dump(data, f)
            logger.info(f"Cached data saved: {key}")
        except Exception as e:
            logger.error(f"Failed to save cache {key}: {e}")
    
    def load_cache(self, key: str) -> Optional[Any]:
        """Load data from cache"""
        cache_file = self.cache_dir / f"{key}.pkl"
        if not cache_file.exists():
            return None
        
        try:
            with open(cache_file, 'rb') as f:
                data = pickle.load(f)
            logger.info(f"Cache loaded: {key}")
            return data
        except Exception as e:
            logger.error(f"Failed to load cache {key}: {e}")
            return None
    
    def clear_cache(self) -> None:
        """Clear all cached data"""
        for cache_file in self.cache_dir.glob("*.pkl"):
            cache_file.unlink()
        logger.info("Cache cleared")

def load_config(config_path: str = "config.json") -> Dict:
    """Load configuration from JSON file"""
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.warning(f"Config file {config_path} not found, using defaults")
        return get_default_config()
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in config file: {e}")
        return get_default_config()

def get_default_config() -> Dict:
    """Get default configuration"""
    return {
        "srs_export_path": "../../SRS Export",
        "cache_enabled": True,
        "cache_dir": "data/cache",
        "semantic_model": "all-MiniLM-L6-v2",
        "similarity_threshold": 0.3,
        "max_results": 50,
        "scoring_weights": {
            "exact_match": 0.4,
            "semantic_match": 0.4,
            "graph_relationship": 0.2
        },
        "relationship_rules": {
            "critical_signals": ["ManettinoSts", "ESCOFFLampRequest", "SuspensionSetupSts"],
            "critical_domains": ["IOC_IOC", "System Core", "Safety Systems"],
            "signal_dependency_score": -3,
            "signal_provider_score": 3,
            "domain_overlap_score": -2,
            "semantic_threshold_high": 0.8,
            "semantic_threshold_moderate": 0.6
        }
    }

# Similarity scoring constants
SIMILARITY_SCALE = {
    "CRITICAL_INPUT": -3,      # Current feature cannot function without this input
    "HIGH_INPUT": -2,          # Current feature significantly degraded without input
    "MODERATE_INPUT": -1,      # Current feature enhanced by input but can work without
    "NO_RELATIONSHIP": 0,      # Features are completely independent
    "MODERATE_OUTPUT": 1,      # Other features enhanced by current but can work without
    "HIGH_OUTPUT": 2,          # Other features significantly degraded without current
    "CRITICAL_OUTPUT": 3       # Other features cannot function without current
}

# Relationship type constants
RELATIONSHIP_TYPES = {
    "DIRECT_SIGNAL": "direct_signal_dependency",
    "SHARED_RESOURCE": "shared_hardware_resource", 
    "FUNCTIONAL_INTEGRATION": "functional_integration",
    "DOMAIN_EXPERTISE": "domain_expertise_overlap",
    "SEMANTIC_SIMILARITY": "semantic_content_similarity",
    "VALIDATION_SYNERGY": "validation_test_synergy",
    "ARCHITECTURAL_CONTEXT": "system_architecture_context"
}
