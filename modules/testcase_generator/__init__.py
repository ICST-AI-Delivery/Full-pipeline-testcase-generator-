"""
Test Case Generator Module

This module handles automated test case generation from SRS analysis and FPI dependencies.
It provides functionality to analyze SRS documents, generate test cases, and create
comprehensive test suites based on feature requirements.

Main Components:
- SRSAnalyzer: Analysis of SRS documents and feature extraction
- TestCaseGenerator: Generation of test cases from requirements
- TestSuiteBuilder: Building comprehensive test suites
- TestCaseManager: Main interface combining all functionality
"""

from .interfaces import TestCaseGeneratorInterface
from .srs_analyzer import SRSAnalyzer
from .testcase_generator import TestCaseGenerator
from .testcase_manager import TestCaseManager

__all__ = [
    'TestCaseGeneratorInterface',
    'SRSAnalyzer',
    'TestCaseGenerator',
    'TestCaseManager'
]

__version__ = "1.0.0"
