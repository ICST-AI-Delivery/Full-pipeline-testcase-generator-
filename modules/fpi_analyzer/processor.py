#!/usr/bin/env python3
"""
Universal FPI Matrix Processor
Handles complete end-to-end workflow for FPI relationship processing:
1. Check if feature analysis exists
2. Generate analysis if missing
3. Extract relationships from analysis
4. Update matrix with relationships
5. Track processing status and audit trail
"""

import os
import json
import pandas as pd
import numpy as np
import subprocess
import sys
from datetime import datetime
from pathlib import Path
import argparse
import glob
import re

class UniversalFPIProcessor:
    def __init__(self, base_dir="."):
        self.base_dir = Path(base_dir)
        self.fpi_matrix_results_dir = self.base_dir / "fpi_matrix_results"
        self.processing_registry_file = self.base_dir / "fpi_processing_registry.json"
        self.placeholder_matrix_file = self.base_dir / "fpi_dependency_matrix_placeholder_20260416_145904.csv"
        
        # Initialize processing registry
        self.processing_registry = self.load_processing_registry()
        
    def load_processing_registry(self):
        """Load or create processing registry"""
        if self.processing_registry_file.exists():
            with open(self.processing_registry_file, 'r') as f:
                return json.load(f)
        else:
            return {
                "processed_features": {},
                "processing_history": [],
                "last_updated": None
            }
    
    def save_processing_registry(self):
        """Save processing registry"""
        self.processing_registry["last_updated"] = datetime.now().isoformat()
        with open(self.processing_registry_file, 'w') as f:
            json.dump(self.processing_registry, f, indent=2)
    
    def check_analysis_exists(self, feature_name):
        """Check if analysis JSON exists for the feature"""
        pattern = f"feature_analysis_{feature_name}_*.json"
        analysis_files = list(self.fpi_matrix_results_dir.glob(pattern))
        
        if analysis_files:
            # Return the most recent analysis file
            latest_file = max(analysis_files, key=lambda x: x.stat().st_mtime)
            return latest_file
        return None
    
    def generate_feature_analysis(self, feature_name):
        """Generate feature analysis using comprehensive FPI analyzer"""
        print(f"Analysis not found for {feature_name}. Generating analysis...")
        
        try:
            # Run the comprehensive FPI analyzer
            cmd = [sys.executable, "comprehensive_fpi_dependency_analyzer.py"]
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=self.base_dir)
            
            if result.returncode != 0:
                print(f"Error generating analysis: {result.stderr}")
                return None
            
            print("Analysis generation completed. Checking for new analysis file...")
            
            # Check if analysis was generated
            analysis_file = self.check_analysis_exists(feature_name)
            if analysis_file:
                print(f"Analysis generated: {analysis_file}")
                return analysis_file
            else:
                print(f"Warning: Analysis generation completed but no file found for {feature_name}")
                return None
                
        except Exception as e:
            print(f"Error running comprehensive FPI analyzer: {e}")
            return None
    
    def extract_relationships_from_analysis(self, analysis_file, feature_name):
        """Extract relationships from analysis JSON"""
        try:
            with open(analysis_file, 'r') as f:
                analysis_data = json.load(f)
            
            relationships = []
            
            # Handle different JSON structures
            if 'dependency_relationships' in analysis_data:
                deps = analysis_data['dependency_relationships']
            elif 'relationships' in analysis_data:
                deps = analysis_data['relationships']
            else:
                # Look for relationship data in the structure
                deps = analysis_data
            
            # Extract relationships based on structure
            if isinstance(deps, dict):
                for target_fpi, relationship_data in deps.items():
                    if isinstance(relationship_data, dict) and 'dependency_score' in relationship_data:
                        score = relationship_data['dependency_score']
                        relationships.append({
                            'source_fpi': feature_name,
                            'target_fpi': target_fpi,
                            'dependency_score': score,
                            'relationship_type': self.classify_relationship_type(score)
                        })
                    elif isinstance(relationship_data, (int, float)):
                        # Direct score mapping
                        score = relationship_data
                        relationships.append({
                            'source_fpi': feature_name,
                            'target_fpi': target_fpi,
                            'dependency_score': score,
                            'relationship_type': self.classify_relationship_type(score)
                        })
            elif isinstance(deps, list):
                # Handle list-based structures
                for rel in deps:
                    if isinstance(rel, dict):
                        # Look for different field names
                        score = None
                        target_fpi = None
                        
                        # Try different score field names
                        if 'score' in rel:
                            score = rel['score']
                        elif 'dependency_score' in rel:
                            score = rel['dependency_score']
                        elif 'relationship_score' in rel:
                            score = rel['relationship_score']
                        
                        # Try different target FPI field names
                        if 'related_fpi' in rel:
                            target_fpi = rel['related_fpi']
                        elif 'target_fpi' in rel:
                            target_fpi = rel['target_fpi']
                        elif 'fpi' in rel:
                            target_fpi = rel['fpi']
                        elif 'feature' in rel:
                            target_fpi = rel['feature']
                        
                        if score is not None and target_fpi is not None:
                            relationships.append({
                                'source_fpi': feature_name,
                                'target_fpi': target_fpi,
                                'dependency_score': score,
                                'relationship_type': self.classify_relationship_type(score)
                            })
            
            print(f"Extracted {len(relationships)} relationships from analysis")
            return relationships
            
        except Exception as e:
            print(f"Error extracting relationships from {analysis_file}: {e}")
            return []
    
    def classify_relationship_type(self, score):
        """Classify relationship type based on score"""
        if score >= 3:
            return "critical_downstream"
        elif score >= 2:
            return "high_downstream"
        elif score >= 1:
            return "low_downstream"
        elif score == 0:
            return "no_dependency"
        elif score >= -1:
            return "low_upstream"
        elif score >= -2:
            return "high_upstream"
        else:
            return "critical_upstream"
    
    def map_fpi_names_to_matrix(self, fpi_name, matrix_index):
        """Map simple FPI names to full matrix path names"""
        # Direct match first
        if fpi_name in matrix_index:
            return fpi_name
        
        # Look for partial matches in matrix index
        matches = [idx for idx in matrix_index if fpi_name in idx]
        
        if len(matches) == 1:
            return matches[0]
        elif len(matches) > 1:
            # Prefer exact substring matches
            exact_matches = [idx for idx in matches if idx.endswith(f"/{fpi_name}/") or idx.endswith(fpi_name)]
            if exact_matches:
                return exact_matches[0]
            else:
                # Return the shortest match (most specific)
                return min(matches, key=len)
        
        # No match found
        return None
    
    def update_matrix_with_relationships(self, relationships, feature_name):
        """Update the placeholder matrix with new relationships"""
        try:
            # Load placeholder matrix
            print(f"Loading placeholder matrix: {self.placeholder_matrix_file}")
            matrix_df = pd.read_csv(self.placeholder_matrix_file, index_col=0)
            
            # Map source feature name
            source_mapped = self.map_fpi_names_to_matrix(feature_name, matrix_df.index)
            if not source_mapped:
                print(f"Warning: Source feature {feature_name} not found in matrix")
                return None
            
            updates_made = 0
            antisymmetric_updates = 0
            skipped_relationships = 0
            missing_fpis = []
            
            print(f"Processing {len(relationships)} relationships...")
            
            for rel in relationships:
                target_fpi = rel['target_fpi']
                score = rel['dependency_score']
                
                # Map target FPI name
                target_mapped = self.map_fpi_names_to_matrix(target_fpi, matrix_df.index)
                
                if not target_mapped:
                    missing_fpis.append(target_fpi)
                    skipped_relationships += 1
                    continue
                
                # Update matrix (source -> target)
                if matrix_df.loc[source_mapped, target_mapped] == 0:
                    matrix_df.loc[source_mapped, target_mapped] = score
                    updates_made += 1
                
                # Update antisymmetric relationship (target -> source)
                antisymmetric_score = -score
                if matrix_df.loc[target_mapped, source_mapped] == 0:
                    matrix_df.loc[target_mapped, source_mapped] = antisymmetric_score
                    antisymmetric_updates += 1
            
            # Update the placeholder matrix in-place (overwrite the same file)
            matrix_df.to_csv(self.placeholder_matrix_file)
            print(f"Updated placeholder matrix: {self.placeholder_matrix_file}")
            
            # Create feature-specific relationships JSON file
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            relationships_json_file = self.base_dir / f"{feature_name.lower()}_relationships_{timestamp}.json"
            
            # Save the extracted relationships for this feature
            feature_relationships_data = {
                "feature_name": feature_name,
                "source_mapped": source_mapped,
                "timestamp": timestamp,
                "total_relationships": len(relationships),
                "processed_relationships": len(relationships) - skipped_relationships,
                "skipped_relationships": skipped_relationships,
                "relationships": relationships,
                "missing_fpis": missing_fpis
            }
            
            with open(relationships_json_file, 'w') as f:
                json.dump(feature_relationships_data, f, indent=2)
            
            # Generate update report
            update_report = {
                "timestamp": timestamp,
                "source_fpi": feature_name,
                "source_mapped": source_mapped,
                "input_matrix": str(self.placeholder_matrix_file),
                "output_matrix": str(self.placeholder_matrix_file),  # Same file updated in-place
                "relationships_json": str(relationships_json_file),
                "total_relationships_processed": len(relationships),
                "updates_made": updates_made,
                "antisymmetric_updates": antisymmetric_updates,
                "skipped_relationships": skipped_relationships,
                "missing_fpis": missing_fpis[:20],  # First 20 missing FPIs
                "total_missing_fpis": len(missing_fpis),
                "matrix_dimensions": {
                    "rows": len(matrix_df.index),
                    "columns": len(matrix_df.columns)
                },
                "update_summary": {
                    "high_confidence_updates": updates_made,
                    "total_matrix_updates": updates_made + antisymmetric_updates
                }
            }
            
            # Save update report
            report_file = self.base_dir / f"{feature_name.lower()}_matrix_update_report_{timestamp}.json"
            with open(report_file, 'w') as f:
                json.dump(update_report, f, indent=2)
            
            print(f"\n=== Matrix Update Complete ===")
            print(f"Placeholder matrix updated in-place: {self.placeholder_matrix_file}")
            print(f"Feature relationships saved: {relationships_json_file}")
            print(f"Update report saved: {report_file}")
            print(f"Total relationships processed: {len(relationships)}")
            print(f"Matrix updates made: {updates_made}")
            print(f"Antisymmetric updates made: {antisymmetric_updates}")
            print(f"Relationships skipped: {skipped_relationships}")
            print(f"Missing FPIs: {len(missing_fpis)}")
            
            if missing_fpis:
                print(f"First few missing FPIs: {missing_fpis[:5]}")
            
            return update_report
            
        except Exception as e:
            print(f"Error updating matrix: {e}")
            return None
    
    def is_feature_processed(self, feature_name):
        """Check if feature has already been processed"""
        return feature_name in self.processing_registry["processed_features"]
    
    def mark_feature_processed(self, feature_name, update_report):
        """Mark feature as processed in registry"""
        self.processing_registry["processed_features"][feature_name] = {
            "processed_at": datetime.now().isoformat(),
            "updates_made": update_report.get("updates_made", 0),
            "total_relationships": update_report.get("total_relationships_processed", 0),
            "output_matrix": update_report.get("output_matrix", ""),
            "report_file": update_report.get("report_file", "")
        }
        
        self.processing_registry["processing_history"].append({
            "feature": feature_name,
            "action": "processed",
            "timestamp": datetime.now().isoformat(),
            "updates": update_report.get("updates_made", 0)
        })
        
        self.save_processing_registry()
    
    def process_feature(self, feature_name, force_reprocess=False):
        """Process a single feature through the complete workflow"""
        print(f"\n{'='*60}")
        print(f"Processing Feature: {feature_name}")
        print(f"{'='*60}")
        
        # Check if already processed
        if not force_reprocess and self.is_feature_processed(feature_name):
            print(f"Feature {feature_name} already processed. Use --force to reprocess.")
            return True
        
        # Step 1: Check if analysis exists
        analysis_file = self.check_analysis_exists(feature_name)
        
        # Step 2: Generate analysis if missing
        if not analysis_file:
            analysis_file = self.generate_feature_analysis(feature_name)
            if not analysis_file:
                print(f"Failed to generate or find analysis for {feature_name}")
                return False
        else:
            print(f"Using existing analysis: {analysis_file}")
        
        # Step 3: Extract relationships
        relationships = self.extract_relationships_from_analysis(analysis_file, feature_name)
        if not relationships:
            print(f"No relationships extracted for {feature_name}")
            return False
        
        # Step 4: Update matrix
        update_report = self.update_matrix_with_relationships(relationships, feature_name)
        if not update_report:
            print(f"Failed to update matrix for {feature_name}")
            return False
        
        # Step 5: Mark as processed
        self.mark_feature_processed(feature_name, update_report)
        
        print(f"Successfully processed {feature_name}")
        return True
    
    def process_multiple_features(self, feature_names, force_reprocess=False):
        """Process multiple features in batch"""
        results = {}
        
        for feature_name in feature_names:
            try:
                success = self.process_feature(feature_name, force_reprocess)
                results[feature_name] = "success" if success else "failed"
            except Exception as e:
                print(f"Error processing {feature_name}: {e}")
                results[feature_name] = f"error: {e}"
        
        # Print summary
        print(f"\n{'='*60}")
        print("BATCH PROCESSING SUMMARY")
        print(f"{'='*60}")
        
        for feature, status in results.items():
            print(f"{feature}: {status}")
        
        return results
    
    def show_processing_status(self):
        """Show current processing status"""
        print(f"\n{'='*60}")
        print("FPI PROCESSING STATUS")
        print(f"{'='*60}")
        
        processed = self.processing_registry["processed_features"]
        print(f"Total processed features: {len(processed)}")
        
        if processed:
            print("\nProcessed Features:")
            for feature, info in processed.items():
                print(f"  {feature}:")
                print(f"    Processed: {info['processed_at']}")
                print(f"    Updates: {info['updates_made']}")
                print(f"    Relationships: {info['total_relationships']}")
        
        # Show available analyses
        analysis_files = list(self.fpi_matrix_results_dir.glob("feature_analysis_*.json"))
        print(f"\nAvailable analyses: {len(analysis_files)}")
        
        # Extract feature names from analysis files
        available_features = set()
        for file in analysis_files:
            match = re.search(r'feature_analysis_(.+?)_\d{8}_\d{6}\.json', file.name)
            if match:
                available_features.add(match.group(1))
        
        unprocessed_features = available_features - set(processed.keys())
        if unprocessed_features:
            print(f"\nUnprocessed features with available analyses:")
            for feature in sorted(unprocessed_features):
                print(f"  {feature}")

def main():
    parser = argparse.ArgumentParser(description="Universal FPI Matrix Processor")
    parser.add_argument("--feature", help="Process single feature")
    parser.add_argument("--batch", action="store_true", help="Process multiple features")
    parser.add_argument("--features", help="Comma-separated list of features for batch processing")
    parser.add_argument("--force", action="store_true", help="Force reprocessing even if already processed")
    parser.add_argument("--status", action="store_true", help="Show processing status")
    parser.add_argument("--list-available", action="store_true", help="List available analyses")
    
    args = parser.parse_args()
    
    # Initialize processor
    processor = UniversalFPIProcessor()
    
    if args.status:
        processor.show_processing_status()
        return
    
    if args.list_available:
        processor.show_processing_status()
        return
    
    if args.feature:
        # Process single feature
        success = processor.process_feature(args.feature, args.force)
        sys.exit(0 if success else 1)
    
    elif args.batch and args.features:
        # Process multiple features
        feature_list = [f.strip() for f in args.features.split(",")]
        results = processor.process_multiple_features(feature_list, args.force)
        
        # Exit with error if any failed
        failed_count = sum(1 for status in results.values() if status != "success")
        sys.exit(0 if failed_count == 0 else 1)
    
    else:
        # Interactive mode - show available features and prompt
        processor.show_processing_status()
        print("\nUsage examples:")
        print("  python universal_fpi_processor.py --feature DMS-7_DRIVER_GAZE_ESTIMATION")
        print("  python universal_fpi_processor.py --batch --features 'DMS-7_DRIVER_GAZE_ESTIMATION,VEH-F247_External_Lights_Management'")
        print("  python universal_fpi_processor.py --status")
        print("  python universal_fpi_processor.py --force --feature DMS-7_DRIVER_GAZE_ESTIMATION")

if __name__ == "__main__":
    main()
