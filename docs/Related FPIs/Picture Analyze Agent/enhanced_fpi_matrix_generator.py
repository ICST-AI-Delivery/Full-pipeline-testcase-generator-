#!/usr/bin/env python3
"""
Enhanced FPI Relationship Matrix Generator
Uses the SRS Discovery System to analyze real feature dependencies from SRS .txt files
"""

import os
import sys
import json
import logging
from typing import Dict, List, Tuple, Set
from collections import defaultdict
from pathlib import Path

# Add the Picture Analyze Agent directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from srs_discovery.parser import SRSParser
from srs_discovery.indexer import ExactMatchIndexer
from srs_discovery.semantic_engine import SemanticSearchEngine
from srs_discovery.graph_engine import RelationshipGraphEngine
from srs_discovery.utils import Feature, RelationshipScore, SIMILARITY_SCALE, RELATIONSHIP_TYPES, logger

class EnhancedFPIMatrixGenerator:
    """Generate FPI relationship matrix using real SRS analysis"""
    
    def __init__(self, srs_export_path: str = "../SRS Export"):
        self.srs_export_path = srs_export_path
        
        # Initialize SRS Discovery System components
        self.parser = SRSParser(srs_export_path)
        self.indexer = ExactMatchIndexer()
        self.semantic_engine = SemanticSearchEngine()
        self.graph_engine = RelationshipGraphEngine()
        
        # Parsed features
        self.features: Dict[str, Feature] = {}
        self.fpi_to_feature_map: Dict[str, str] = {}
        
        # Relationship matrix
        self.relationship_matrix: Dict[str, Dict[str, int]] = {}
        
        logger.info("Enhanced FPI Matrix Generator initialized")
    
    def analyze_srs_features(self) -> None:
        """Parse and analyze all SRS features"""
        logger.info("Starting SRS feature analysis...")
        
        # Parse all SRS files - use parse_srs_folder to handle .txt files
        self.features = {}
        
        # Find all audio-related folders
        audio_folders = [
            os.path.join(self.srs_export_path, "SRS_Audio", folder)
            for folder in os.listdir(os.path.join(self.srs_export_path, "SRS_Audio"))
            if os.path.isdir(os.path.join(self.srs_export_path, "SRS_Audio", folder))
        ]
        
        # Parse each folder
        for folder in audio_folders:
            logger.info(f"Parsing folder: {folder}")
            folder_features = self.parser.parse_srs_folder(folder)
            self.features.update(folder_features)
        
        logger.info(f"Parsed {len(self.features)} features from SRS files")
        
        # Build indices for exact matching
        self.indexer.build_indices(self.features)
        
        # Build semantic embeddings
        if len(self.features) > 0:
            self.semantic_engine.build_embeddings(self.features)
        
        # Create FPI to feature mapping
        self._create_fpi_mapping()
        
        logger.info("SRS feature analysis completed")
    
    def _create_fpi_mapping(self) -> None:
        """Create mapping between FPI names and feature IDs"""
        for feature_id, feature in self.features.items():
            # Extract FPI name from feature name or file path
            fpi_name = self._extract_fpi_name(feature)
            if fpi_name:
                self.fpi_to_feature_map[fpi_name] = feature_id
        
        logger.info(f"Created FPI mapping for {len(self.fpi_to_feature_map)} FPIs")
    
    def _extract_fpi_name(self, feature: Feature) -> str:
        """Extract FPI name from feature"""
        # Try to extract from file path first
        if feature.file_path:
            path_parts = Path(feature.file_path).parts
            for part in path_parts:
                if part.startswith(('VEH-F', 'BC001', 'AUD-', 'FAD-', 'ESE-', 'VAS-')):
                    return part.split('_')[0] if '_' in part else part
        
        # Try to extract from feature name
        if feature.name:
            if feature.name.startswith(('VEH-F', 'BC001', 'AUD-', 'FAD-', 'ESE-', 'VAS-')):
                return feature.name.split('_')[0] if '_' in feature.name else feature.name
        
        return None
    
    def calculate_fpi_relationships(self, fpi_list: List[str]) -> Dict[str, Dict[str, int]]:
        """Calculate relationship matrix for given FPIs using SRS analysis"""
        logger.info(f"Calculating relationships for {len(fpi_list)} FPIs...")
        
        # Initialize matrix
        matrix = {}
        for fpi1 in fpi_list:
            matrix[fpi1] = {}
            for fpi2 in fpi_list:
                matrix[fpi1][fpi2] = 0
        
        # Calculate relationships using SRS discovery system
        for i, fpi1 in enumerate(fpi_list):
            logger.info(f"Processing FPI {i+1}/{len(fpi_list)}: {fpi1}")
            
            # Get feature ID for this FPI
            feature_id1 = self.fpi_to_feature_map.get(fpi1)
            if not feature_id1:
                logger.warning(f"No feature found for FPI: {fpi1}")
                continue
            
            # Find relationships using all three engines
            exact_relationships = self.indexer.find_exact_matches(feature_id1)
            
            # Only use semantic engine if it's properly initialized
            semantic_relationships = []
            try:
                if hasattr(self.semantic_engine, 'indexed') and self.semantic_engine.indexed:
                    semantic_relationships = self.semantic_engine.find_semantic_matches(feature_id1)
            except Exception as e:
                logger.warning(f"Semantic search failed for {feature_id1}: {e}")
            
            # Combine and score relationships
            all_relationships = self._combine_relationships(exact_relationships, semantic_relationships)
            
            # Map relationships back to FPIs and update matrix
            for rel in all_relationships:
                related_fpi = self._find_fpi_for_feature(rel.related_feature_id)
                if related_fpi and related_fpi in fpi_list:
                    # Convert relationship score to matrix score [-3, +3]
                    matrix_score = self._convert_to_matrix_score(rel)
                    matrix[fpi1][related_fpi] = matrix_score
                    matrix[related_fpi][fpi1] = matrix_score  # Ensure symmetry
        
        self.relationship_matrix = matrix
        logger.info("FPI relationship calculation completed")
        return matrix
    
    def _combine_relationships(self, exact_rels: List[RelationshipScore], 
                             semantic_rels: List[RelationshipScore]) -> List[RelationshipScore]:
        """Combine relationships from different engines"""
        # Create a map to avoid duplicates
        relationship_map = {}
        
        # Add exact relationships (higher priority)
        for rel in exact_rels:
            relationship_map[rel.related_feature_id] = rel
        
        # Add semantic relationships if not already present
        for rel in semantic_rels:
            if rel.related_feature_id not in relationship_map:
                relationship_map[rel.related_feature_id] = rel
            else:
                # Combine scores if both exist (weighted average)
                existing = relationship_map[rel.related_feature_id]
                combined_score = int((existing.score * 0.7) + (rel.score * 0.3))
                combined_confidence = (existing.confidence * 0.7) + (rel.confidence * 0.3)
                
                relationship_map[rel.related_feature_id] = RelationshipScore(
                    related_feature_id=rel.related_feature_id,
                    score=combined_score,
                    relationship_type=existing.relationship_type,
                    evidence=existing.evidence + rel.evidence,
                    confidence=combined_confidence
                )
        
        return list(relationship_map.values())
    
    def _convert_to_matrix_score(self, relationship: RelationshipScore) -> int:
        """Convert RelationshipScore to matrix score [-3, +3]"""
        # The relationship score is already in the correct range
        score = relationship.score
        
        # Apply confidence weighting
        if relationship.confidence < 0.5:
            score = int(score * 0.5)  # Reduce score for low confidence
        elif relationship.confidence < 0.7:
            score = int(score * 0.8)  # Slightly reduce for moderate confidence
        
        # Ensure within bounds
        return max(-3, min(3, score))
    
    def _find_fpi_for_feature(self, feature_id: str) -> str:
        """Find FPI name for a given feature ID"""
        for fpi, fid in self.fpi_to_feature_map.items():
            if fid == feature_id:
                return fpi
        return None
    
    def validate_matrix(self, matrix: Dict[str, Dict[str, int]], fpi_list: List[str]) -> bool:
        """Validate matrix symmetry and score range"""
        logger.info("Validating relationship matrix...")
        
        violations = 0
        
        for fpi1 in fpi_list:
            for fpi2 in fpi_list:
                score1 = matrix[fpi1][fpi2]
                score2 = matrix[fpi2][fpi1]
                
                # Check score range
                if score1 < -3 or score1 > 3:
                    logger.error(f"Score out of range: {fpi1} -> {fpi2} = {score1}")
                    violations += 1
                
                # Check diagonal
                if fpi1 == fpi2 and score1 != 0:
                    logger.error(f"Diagonal not zero: {fpi1} -> {fpi2} = {score1}")
                    violations += 1
                
                # Check symmetry
                if fpi1 != fpi2 and score1 != score2:
                    logger.error(f"Asymmetric: {fpi1} -> {fpi2} = {score1}, {fpi2} -> {fpi1} = {score2}")
                    violations += 1
        
        if violations == 0:
            logger.info("✓ Matrix validation PASSED")
            return True
        else:
            logger.error(f"✗ Matrix validation FAILED with {violations} violations")
            return False
    
    def print_matrix_summary(self, matrix: Dict[str, Dict[str, int]], fpi_list: List[str]) -> None:
        """Print matrix summary statistics"""
        print("\n" + "="*80)
        print("FPI RELATIONSHIP MATRIX SUMMARY")
        print("="*80)
        
        # Count relationship types
        relationship_counts = {-3: 0, -2: 0, -1: 0, 0: 0, 1: 0, 2: 0, 3: 0}
        total_pairs = 0
        
        for fpi1 in fpi_list:
            for fpi2 in fpi_list:
                if fpi1 != fpi2:  # Exclude diagonal
                    score = matrix[fpi1][fpi2]
                    relationship_counts[score] += 1
                    total_pairs += 1
        
        # Adjust for symmetry (each relationship counted twice)
        for score in relationship_counts:
            if score != 0:
                relationship_counts[score] //= 2
        
        total_pairs //= 2
        
        print(f"\nTotal FPIs analyzed: {len(fpi_list)}")
        print(f"Total unique FPI pairs: {total_pairs}")
        print(f"Features parsed from SRS: {len(self.features)}")
        print(f"FPIs mapped to features: {len(self.fpi_to_feature_map)}")
        
        print("\nRelationship Distribution:")
        print(f"  Strong Negative (-3): {relationship_counts[-3]:>4} ({relationship_counts[-3]/total_pairs*100:.1f}%)")
        print(f"  Moderate Negative (-2): {relationship_counts[-2]:>4} ({relationship_counts[-2]/total_pairs*100:.1f}%)")
        print(f"  Weak Negative (-1): {relationship_counts[-1]:>4} ({relationship_counts[-1]/total_pairs*100:.1f}%)")
        print(f"  No Relationship (0): {relationship_counts[0]:>4} ({relationship_counts[0]/total_pairs*100:.1f}%)")
        print(f"  Weak Positive (1): {relationship_counts[1]:>4} ({relationship_counts[1]/total_pairs*100:.1f}%)")
        print(f"  Moderate Positive (2): {relationship_counts[2]:>4} ({relationship_counts[2]/total_pairs*100:.1f}%)")
        print(f"  Strong Positive (3): {relationship_counts[3]:>4} ({relationship_counts[3]/total_pairs*100:.1f}%)")
        
        print("\n" + "="*80)
    
    def print_sample_matrix(self, matrix: Dict[str, Dict[str, int]], fpi_list: List[str], sample_size: int = 8) -> None:
        """Print a sample of the relationship matrix"""
        print(f"\nSAMPLE RELATIONSHIP MATRIX (First {sample_size} FPIs)")
        print("="*100)
        
        sample_fpis = fpi_list[:sample_size]
        
        # Print header
        print(f"{'FPI':<25}", end="")
        for fpi in sample_fpis:
            short_name = fpi.split('-')[-1][:8] if '-' in fpi else fpi[:8]
            print(f"{short_name:>8}", end="")
        print()
        
        # Print separator
        print("-" * (25 + 8 * len(sample_fpis)))
        
        # Print matrix rows
        for fpi1 in sample_fpis:
            display_name = fpi1[:22] + "..." if len(fpi1) > 25 else fpi1
            print(f"{display_name:<25}", end="")
            
            for fpi2 in sample_fpis:
                score = matrix[fpi1][fpi2]
                if score > 0:
                    print(f"{score:>8}", end="")
                elif score < 0:
                    print(f"{score:>8}", end="")
                else:
                    print(f"{'·':>8}", end="")
            print()
        
        print("="*100)
    
    def save_matrix(self, matrix: Dict[str, Dict[str, int]], output_file: str) -> None:
        """Save matrix to JSON file with metadata"""
        output_data = {
            "metadata": {
                "generator": "Enhanced FPI Matrix Generator",
                "version": "2.0",
                "srs_features_analyzed": len(self.features),
                "fpis_mapped": len(self.fpi_to_feature_map),
                "analysis_engines": ["exact_match", "semantic_similarity"],
                "score_range": [-3, 3],
                "description": "FPI relationship matrix generated from real SRS analysis"
            },
            "fpi_feature_mapping": self.fpi_to_feature_map,
            "relationship_matrix": matrix
        }
        
        with open(output_file, 'w') as f:
            json.dump(output_data, f, indent=2)
        
        logger.info(f"Enhanced matrix saved to: {output_file}")

def main():
    """Main function to generate enhanced FPI relationship matrix"""
    print("Enhanced FPI Relationship Matrix Generator")
    print("Using Real SRS Analysis")
    print("=" * 60)
    
    # Sample FPI list (from Instrument Cluster domain)
    sample_fpis = [
        "VEH-F001", "VEH-F002", "VEH-F004", "VEH-F005", "VEH-F006",
        "VEH-F020", "VEH-F022", "VEH-F023", "VEH-F024", "VEH-F025",
        "VEH-F027", "VEH-F030", "VEH-F033", "VEH-F042", "VEH-F047",
        "VEH-F134", "VEH-F135", "VEH-F136", "VEH-F139", "VEH-F140",
        "BC001", "FAD-0", "AUD-1", "ESE-1", "VAS-1"
    ]
    
    try:
        # Initialize generator
        generator = EnhancedFPIMatrixGenerator()
        
        # Analyze SRS features
        print("\nStep 1: Analyzing SRS features...")
        generator.analyze_srs_features()
        
        # Calculate relationships
        print("\nStep 2: Calculating FPI relationships...")
        matrix = generator.calculate_fpi_relationships(sample_fpis)
        
        # Validate matrix
        print("\nStep 3: Validating matrix...")
        is_valid = generator.validate_matrix(matrix, sample_fpis)
        
        # Print results
        generator.print_matrix_summary(matrix, sample_fpis)
        generator.print_sample_matrix(matrix, sample_fpis, sample_size=10)
        
        # Save enhanced matrix
        output_file = "Picture Analyze Agent/enhanced_fpi_relationship_matrix.json"
        generator.save_matrix(matrix, output_file)
        
        print(f"\n{'='*60}")
        print("ENHANCED FPI RELATIONSHIP MATRIX GENERATION COMPLETED")
        print(f"{'='*60}")
        print(f"✓ Matrix validation: {'PASSED' if is_valid else 'FAILED'}")
        print(f"✓ Output saved to: {output_file}")
        print(f"✓ Analysis based on real SRS content")
        print(f"✓ Used advanced relationship discovery engines")
        
    except Exception as e:
        print(f"\nError during matrix generation: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
