"""
Smart SRS Feature Discovery System

A sophisticated automotive feature relationship discovery system that analyzes
SRS (Software Requirements Specification) documents to identify feature dependencies
and relationships using a -3 to +3 similarity scale.

Similarity Scale:
- -3 to -1: Current feature depends on other features (input dependencies)
- 0: No relationship
- +1 to +3: Other features depend on current feature (output dependencies)
"""

from .parser import SRSParser
from .indexer import ExactMatchIndexer
from .semantic_engine import SemanticSearchEngine
from .graph_engine import RelationshipGraphEngine

__version__ = "1.0.0"
__author__ = "Picture Analyze Agent Team"

__all__ = [
    'SRSParser', 
    'ExactMatchIndexer',
    'SemanticSearchEngine',
    'RelationshipGraphEngine'
]
