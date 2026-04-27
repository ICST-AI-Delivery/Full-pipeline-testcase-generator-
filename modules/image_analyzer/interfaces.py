"""
Interface definitions for Image Analyzer module.
"""

from abc import ABC, abstractmethod
from typing import List, Optional
from shared.data_models.image_models import (
    ImageAnalysisResult, 
    BatchProcessResult, 
    ImageProcessingConfig
)


class ImageAnalyzerInterface(ABC):
    """Abstract interface for image analysis operations."""
    
    @abstractmethod
    def analyze_single_image(self, image_path: str) -> ImageAnalysisResult:
        """Analyze a single image and return complete analysis result."""
        pass
    
    @abstractmethod
    def analyze_batch(self, image_paths: List[str]) -> BatchProcessResult:
        """Analyze multiple images in batch."""
        pass
    
    @abstractmethod
    def configure(self, config: ImageProcessingConfig) -> None:
        """Configure the analyzer with processing parameters."""
        pass


class CLIPClassifierInterface(ABC):
    """Interface for CLIP-based image classification."""
    
    @abstractmethod
    def classify_image(self, image_path: str) -> dict:
        """Classify a single image using CLIP model."""
        pass
    
    @abstractmethod
    def classify_batch(self, image_paths: List[str]) -> List[dict]:
        """Classify multiple images in batch."""
        pass


class VisionAnalyzerInterface(ABC):
    """Interface for Vision API analysis."""
    
    @abstractmethod
    def analyze_image(self, image_path: str, category: str) -> dict:
        """Analyze image using appropriate Vision API prompt."""
        pass
    
    @abstractmethod
    def get_prompt_for_category(self, category: str) -> str:
        """Get the appropriate prompt template for image category."""
        pass
