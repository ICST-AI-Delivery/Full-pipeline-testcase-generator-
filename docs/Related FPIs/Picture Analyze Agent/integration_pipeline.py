#!/usr/bin/env python3
"""
Integration Pipeline for Critical Relationship Extraction
Integrates with the Picture Analyze Agent's existing pipeline
"""

import json
import os
import sys
from pathlib import Path
from extract_critical_relationships import CriticalRelationshipExtractor

class PipelineIntegrator:
    def __init__(self, config_path=None):
        self.config = self._load_config(config_path)
        self.results_dir = Path(self.config.get('results_dir', 'results'))
        self.results_dir.mkdir(exist_ok=True)
    
    def _load_config(self, config_path):
        """Load pipeline configuration"""
        default_config = {
            'matrix_path': 'relationship_matrix.json',
            'results_dir': 'results',
            'output_format': 'json',
            'target_features': []
        }
        
        if config_path and os.path.exists(config_path):
            with open(config_path, 'r') as f:
                user_config = json.load(f)
                default_config.update(user_config)
        
        return default_config
    
    def process_single_feature(self, target_feature, matrix_path=None):
        """Process a single feature and extract critical relationships"""
        matrix_path = matrix_path or self.config['matrix_path']
        
        if not os.path.exists(matrix_path):
            raise FileNotFoundError(f"Relationship matrix not found: {matrix_path}")
        
        extractor = CriticalRelationshipExtractor(matrix_path)
        relationships = extractor.extract_critical_relationships(target_feature)
        
        # Add metadata
        result = {
            'target_feature': target_feature,
            'matrix_source': matrix_path,
            'critical_relationships': relationships,
            'analysis_summary': {
                'total_input_dependencies': len(relationships['input_dependencies']),
                'total_output_dependencies': len(relationships['output_dependencies']),
                'bidirectional_dependencies': list(set(relationships['input_dependencies']) & 
                                                 set(relationships['output_dependencies']))
            }
        }
        
        return result
    
    def process_batch_features(self, target_features=None, matrix_path=None):
        """Process multiple features in batch"""
        target_features = target_features or self.config['target_features']
        
        if not target_features:
            print("No target features specified. Please provide features to analyze.")
            return []
        
        results = []
        for feature in target_features:
            try:
                result = self.process_single_feature(feature, matrix_path)
                results.append(result)
                print(f"✓ Processed: {feature}")
            except Exception as e:
                print(f"✗ Error processing {feature}: {str(e)}")
                results.append({
                    'target_feature': feature,
                    'error': str(e)
                })
        
        return results
    
    def save_results(self, results, output_filename=None):
        """Save results to file"""
        if not output_filename:
            output_filename = f"critical_relationships_analysis.{self.config['output_format']}"
        
        output_path = self.results_dir / output_filename
        
        with open(output_path, 'w') as f:
            if self.config['output_format'] == 'json':
                json.dump(results, f, indent=2)
            else:
                # Default to JSON if format not recognized
                json.dump(results, f, indent=2)
        
        print(f"Results saved to: {output_path}")
        return output_path
    
    def generate_summary_report(self, results):
        """Generate a summary report of the analysis"""
        summary = {
            'total_features_analyzed': len([r for r in results if 'error' not in r]),
            'total_errors': len([r for r in results if 'error' in r]),
            'features_with_bidirectional_deps': [],
            'most_connected_features': [],
            'isolated_features': []
        }
        
        for result in results:
            if 'error' in result:
                continue
                
            feature = result['target_feature']
            analysis = result['analysis_summary']
            
            # Track bidirectional dependencies
            if analysis['bidirectional_dependencies']:
                summary['features_with_bidirectional_deps'].append({
                    'feature': feature,
                    'bidirectional_deps': analysis['bidirectional_dependencies']
                })
            
            # Track connectivity
            total_connections = (analysis['total_input_dependencies'] + 
                               analysis['total_output_dependencies'])
            
            if total_connections == 0:
                summary['isolated_features'].append(feature)
            elif total_connections >= 4:  # Threshold for "highly connected"
                summary['most_connected_features'].append({
                    'feature': feature,
                    'total_connections': total_connections
                })
        
        return summary

def main():
    """Main execution function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Integration Pipeline for Critical Relationship Extraction')
    parser.add_argument('--config', type=str, help='Path to configuration file')
    parser.add_argument('--matrix', type=str, help='Path to relationship matrix JSON file')
    parser.add_argument('--feature', type=str, help='Single feature to analyze')
    parser.add_argument('--features', nargs='+', help='Multiple features to analyze')
    parser.add_argument('--output', type=str, help='Output filename')
    parser.add_argument('--summary', action='store_true', help='Generate summary report')
    
    args = parser.parse_args()
    
    # Initialize pipeline
    integrator = PipelineIntegrator(args.config)
    
    # Process features
    if args.feature:
        # Single feature processing
        result = integrator.process_single_feature(args.feature, args.matrix)
        results = [result]
    elif args.features:
        # Multiple features processing
        results = integrator.process_batch_features(args.features, args.matrix)
    else:
        # Use config file features
        results = integrator.process_batch_features(matrix_path=args.matrix)
    
    # Save results
    output_path = integrator.save_results(results, args.output)
    
    # Generate summary if requested
    if args.summary:
        summary = integrator.generate_summary_report(results)
        summary_path = integrator.save_results(summary, 'analysis_summary.json')
        print(f"Summary report saved to: {summary_path}")
    
    print(f"\nPipeline completed successfully!")
    print(f"Processed {len(results)} features")

if __name__ == "__main__":
    main()
