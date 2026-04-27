"""
Data models for Image Analyzer module.

These models define the structure of data produced by the Image Analyzer
and consumed by other modules.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any
from datetime import datetime
from enum import Enum


class ImageCategory(Enum):
    """Enumeration of image categories for classification."""
    CONFIG_TABLE = "config_table"
    HMI_DISPLAY = "hmi_display"
    PROCESS_FLOW = "process_flow"
    SYSTEM_ARCHITECTURE = "system_architecture"
    TELLTALES = "telltales"
    FLOWCHART = "flowchart"
    STATE_MATRIX = "state_matrix"
    SIGNAL_DIAGRAM = "signal_diagram"
    WIRING_DIAGRAM = "wiring_diagram"
    COMPONENT_LAYOUT = "component_layout"
    USER_INTERFACE = "user_interface"
    DIAGNOSTIC_SCREEN = "diagnostic_screen"
    OTHER = "other"


@dataclass
class TechnicalElement:
    """Represents a technical element extracted from an image."""
    element_type: str  # e.g., "table", "signal", "component"
    name: str
    properties: Dict[str, Any] = field(default_factory=dict)
    coordinates: Optional[Dict[str, int]] = None  # x, y, width, height
    confidence: float = 0.0


@dataclass
class ImageClassification:
    """Result of CLIP-based image classification."""
    image_path: str
    predicted_category: ImageCategory
    confidence_scores: Dict[str, float] = field(default_factory=dict)
    top_predictions: List[tuple] = field(default_factory=list)  # [(category, score), ...]
    processing_time: float = 0.0
    model_version: str = "unknown"


@dataclass
class VisionAnalysisResult:
    """Result of Vision API analysis for a single image."""
    image_path: str
    category: ImageCategory
    analysis_text: str
    technical_elements: List[TechnicalElement] = field(default_factory=list)
    extracted_tables: List[Dict[str, Any]] = field(default_factory=list)
    signals_identified: List[str] = field(default_factory=list)
    processing_metadata: Dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.now)
    success: bool = True
    error_message: Optional[str] = None


@dataclass
class ImageAnalysisResult:
    """Complete analysis result for a single image including both classification and vision analysis."""
    image_path: str
    filename: str
    classification: ImageClassification
    vision_analysis: Optional[VisionAnalysisResult] = None
    file_metadata: Dict[str, Any] = field(default_factory=dict)  # size, format, etc.
    processing_summary: Dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.now)
    
    @property
    def category(self) -> ImageCategory:
        """Get the predicted category from classification."""
        return self.classification.predicted_category
    
    @property
    def confidence(self) -> float:
        """Get the confidence score for the predicted category."""
        return self.classification.confidence_scores.get(
            self.classification.predicted_category.value, 0.0
        )


@dataclass
class BatchProcessResult:
    """Result of batch processing multiple images."""
    total_images: int
    successful_analyses: int
    failed_analyses: int
    results: List[ImageAnalysisResult] = field(default_factory=list)
    processing_summary: Dict[str, Any] = field(default_factory=dict)
    category_distribution: Dict[str, int] = field(default_factory=dict)
    average_confidence: float = 0.0
    total_processing_time: float = 0.0
    timestamp: datetime = field(default_factory=datetime.now)
    errors: List[Dict[str, str]] = field(default_factory=list)  # [{"image": path, "error": msg}, ...]
    
    def get_results_by_category(self, category: ImageCategory) -> List[ImageAnalysisResult]:
        """Get all results for a specific category."""
        return [result for result in self.results if result.category == category]
    
    def get_high_confidence_results(self, threshold: float = 0.8) -> List[ImageAnalysisResult]:
        """Get results with confidence above threshold."""
        return [result for result in self.results if result.confidence >= threshold]
    
    @property
    def success_rate(self) -> float:
        """Calculate the success rate of the batch processing."""
        if self.total_images == 0:
            return 0.0
        return self.successful_analyses / self.total_images


@dataclass
class ImageProcessingConfig:
    """Configuration for image processing operations."""
    clip_model_name: str = "ViT-B/32"
    vision_api_endpoint: str = ""
    batch_size: int = 32
    confidence_threshold: float = 0.5
    max_image_size: tuple = (1024, 1024)
    supported_formats: List[str] = field(default_factory=lambda: ['.jpg', '.jpeg', '.png', '.bmp'])
    enable_caching: bool = True
    cache_directory: str = "data/cache"
    parallel_processing: bool = True
    max_workers: int = 4
