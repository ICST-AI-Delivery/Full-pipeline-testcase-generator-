"""
Image Analyzer Module

This module handles CLIP-based image classification and Vision API analysis.
It provides functionality to classify images into technical categories and
extract detailed technical information from images.

Main Components:
- CLIPClassifier: Image classification using CLIP models
- VisionAnalyzer: Detailed image analysis using Vision APIs
- BatchProcessor: Batch processing of multiple images
- ImageAnalyzer: Main interface combining classification and analysis
"""

from .interfaces import ImageAnalyzerInterface
from .clip_classifier import CLIPClassifier
from .vision_analyzer import VisionAnalyzer
from .batch_processor import BatchProcessor
from .image_analyzer import ImageAnalyzer

__all__ = [
    'ImageAnalyzerInterface',
    'CLIPClassifier',
    'VisionAnalyzer', 
    'BatchProcessor',
    'ImageAnalyzer'
]

__version__ = "1.0.0"
