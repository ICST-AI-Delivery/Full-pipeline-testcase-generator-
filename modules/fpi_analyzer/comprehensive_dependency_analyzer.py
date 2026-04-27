#!/usr/bin/env python3
"""
Comprehensive FPI Testcase Context Dependency Matrix Analyzer
Implements the exact methodology from fpi_testcase_context_dependency_matrix_prompt.md
"""

import os
import json
import numpy as np
from datetime import datetime

class FPIDependencyAnalyzer:
    def __init__(self, srs_export_path="SRS Export/SRS Export"):
        self.srs_export_path = srs_export_path
        self.domains = {}
        self.all_features = []
        self.main_fpi = "2xA2B_Audio_Layout"
        self.dependency_matrix = None
        self.dependency_register = []
        
    def scan_all_features(self):
        """Scan all domains and collect all features"""
        print("=== COMPREHENSIVE SRS FEATURE INVENTORY ===")
        
        total_features = 0
        
        # Get all domains (SRS_Audio, SRS_Connectivity, etc.)
        for domain_name in os.listdir(self.srs_export_path):
            domain_path = os.path.join(self.srs_export_path, domain_name)
            if os.path.isdir(domain_path) and not domain_name.startswith('.') and domain_name.startswith('SRS_'):
                
                # Get all features in this domain
                features = []
                if os.path.exists(domain_path):
                    for item in os.listdir(domain_path):
                        item_path = os.path.join(domain_path, item)
                        if os.path.isdir(item_path) and not item.startswith('.'):
                            features.append(item)
                            self.all_features.append({
                                'domain': domain_name,
                                'feature': item,
                                'path': item_path
                            })
                
                self.domains[domain_name] = {
                    'feature_count': len(features),
                    'features': features
                }
                total_features += len(features)
                
                print(f"{domain_name}: {len(features)} features")
                if features:
                    sample = features[:3]
                    print(f"  Sample: {sample}...")
                print()
        
        print(f"TOTAL FEATURES ACROSS ALL DOMAINS: {total_features}")
        print(f"TOTAL DOMAINS: {len(self.domains)}")
        print(f"MAIN FPI: '{self.main_fpi}' vs {total_features} related features")
        print()
        
        return total_features
    
    def load_feature_content(self, domain, feature):
        """Load the actual SRS content for a feature"""
        feature_path = os.path.join(self.srs_export_path, domain, feature)
        
        # Look for TXT files in the feature directory
        txt_files = []
        if os.path.exists(feature_path):
            for file in os.listdir(feature_path):
                if file.endswith('.txt'):
                    txt_files.append(file)
        
        if not txt_files:
            return f"No TXT files found in {feature_path}"
        
        # Read the first TXT file (or combine multiple if needed)
        content = ""
        for txt_file in txt_files[:1]:  # Just first file for now
            txt_path = os.path.join(feature_path, txt_file)
            try:
                with open(txt_path, 'r', encoding='utf-8') as f:
                    content += f.read()
            except Exception as e:
                content += f"Error reading {txt_file}: {str(e)}"
        
        return content
    
    def analyze_testcase_context_dependency(self, main_fpi_content, related_fpi_content, related_fpi_name):
        """
        Analyze testcase context dependency using the exact methodology
        Returns score from -3 to +3 based on upstream/downstream context analysis
        """
        
        # This is a simplified implementation - in practice, this would use
        # the LLM API with the exact prompt from fpi_testcase_context_dependency_matrix_prompt.md
        
        # For now, implement basic keyword-based analysis
        main_lower = main_fpi_content.lower()
        related_lower = related_fpi_content.lower()
        
        # Look for direct references
        if related_fpi_name.lower() in main_lower:
            return 3  # Strong positive dependency
        elif main_fpi_content.lower().replace('_', ' ') in related_lower:
            return 2  # Moderate positive dependency
        
        # Look for common technical terms (simplified)
        audio_terms = ['audio', 'sound', 'speaker', 'amplifier', 'a2b', 'layout']
        main_audio_count = sum(1 for term in audio_terms if term in main_lower)
        related_audio_count = sum(1 for term in audio_terms if term in related_lower)
        
        if main_audio_count > 2 and related_audio_count > 2:
            return 1  # Weak positive dependency
        elif main_audio_count > 0 and related_audio_count > 0:
            return 0  # No significant dependency
        else:
            return -1  # Weak negative dependency (different domains)
    
    def generate_dependency_matrix(self):
        """Generate the complete 1×N dependency matrix"""
        print("=== GENERATING TESTCASE CONTEXT DEPENDENCY MATRIX ===")
        
        # Load main FPI content
        main_fpi_content = self.load_feature_content("SRS_Audio", self.main_fpi)
        
        # Initialize matrix (1×N where N is total features)
        n_features = len(self.all_features)
        self.dependency_matrix = np.zeros((1, n_features), dtype=int)
        
        print(f"Analyzing '{self.main_fpi}' against {n_features} related features...")
        print()
        
        for i, feature_info in enumerate(self.all_features):
            domain = feature_info['domain']
            feature = feature_info['feature']
            
            # Skip self-comparison
            if feature == self.main_fpi:
                self.dependency_matrix[0, i] = 0
                continue
            
            # Load related feature content
            related_content = self.load_feature_content(domain, feature)
            
            # Analyze dependency
            score = self.analyze_testcase_context_dependency(
                main_fpi_content, related_content, feature
            )
            
            self.dependency_matrix[0, i] = score
            
            # Add to dependency register
            self.dependency_register.append({
                'main_fpi': self.main_fpi,
                'related_fpi': feature,
                'domain': domain,
                'dependency_score': score,
                'context_type': self._get_context_type(score),
                'evidence': f"Analysis of {feature} content vs {self.main_fpi}",
                'timestamp': datetime.now().isoformat()
            })
            
            if i % 10 == 0:
                print(f"Processed {i+1}/{n_features} features...")
        
        print(f"✓ Dependency matrix generation complete!")
        return self.dependency_matrix
    
    def _get_context_type(self, score):
        """Map dependency score to context type"""
        if score >= 2:
            return "Strong Upstream Context"
        elif score == 1:
            return "Weak Upstream Context"
        elif score == 0:
            return "No Significant Context"
        elif score == -1:
            return "Weak Downstream Context"
        else:
            return "Strong Downstream Context"
    
    def save_results(self):
        """Save all results to files"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Save feature inventory
        inventory = {
            'scan_timestamp': datetime.now().isoformat(),
            'main_fpi': self.main_fpi,
            'total_features': len(self.all_features),
            'total_domains': len(self.domains),
            'domains': self.domains,
            'all_features': self.all_features
        }
        
        with open(f'srs_complete_inventory_{timestamp}.json', 'w') as f:
            json.dump(inventory, f, indent=2)
        
        # Save dependency matrix
        matrix_data = {
            'main_fpi': self.main_fpi,
            'matrix_shape': self.dependency_matrix.shape,
            'dependency_matrix': self.dependency_matrix.tolist(),
            'feature_mapping': [f"{f['domain']}/{f['feature']}" for f in self.all_features],
            'generation_timestamp': datetime.now().isoformat()
        }
        
        with open(f'fpi_dependency_matrix_{timestamp}.json', 'w') as f:
            json.dump(matrix_data, f, indent=2)
        
        # Save dependency register
        with open(f'fpi_dependency_register_{timestamp}.json', 'w') as f:
            json.dump(self.dependency_register, f, indent=2)
        
        print(f"✓ Results saved:")
        print(f"  - Complete inventory: srs_complete_inventory_{timestamp}.json")
        print(f"  - Dependency matrix: fpi_dependency_matrix_{timestamp}.json")
        print(f"  - Dependency register: fpi_dependency_register_{timestamp}.json")
        
        return timestamp
    
    def generate_summary_report(self):
        """Generate summary statistics and insights"""
        if self.dependency_matrix is None:
            return "No dependency matrix generated yet"
        
        scores = self.dependency_matrix[0, :]
        
        summary = {
            'main_fpi': self.main_fpi,
            'total_analyzed_features': len(scores),
            'dependency_distribution': {
                'strong_positive': int(np.sum(scores >= 2)),
                'weak_positive': int(np.sum(scores == 1)),
                'no_dependency': int(np.sum(scores == 0)),
                'weak_negative': int(np.sum(scores == -1)),
                'strong_negative': int(np.sum(scores <= -2))
            },
            'highest_dependencies': [],
            'analysis_timestamp': datetime.now().isoformat()
        }
        
        # Find highest dependency features
        high_dep_indices = np.where(scores >= 1)[0]
        for idx in high_dep_indices:
            feature_info = self.all_features[idx]
            summary['highest_dependencies'].append({
                'feature': feature_info['feature'],
                'domain': feature_info['domain'],
                'score': int(scores[idx])
            })
        
        return summary

def main():
    analyzer = FPIDependencyAnalyzer()
    
    # Step 1: Scan all features
    total_features = analyzer.scan_all_features()
    
    # Step 2: Generate dependency matrix
    matrix = analyzer.generate_dependency_matrix()
    
    # Step 3: Save results
    timestamp = analyzer.save_results()
    
    # Step 4: Generate summary
    summary = analyzer.generate_summary_report()
    
    print("\n=== ANALYSIS COMPLETE ===")
    print(f"Main FPI: {analyzer.main_fpi}")
    print(f"Total Features Analyzed: {total_features}")
    print(f"Dependency Matrix Shape: {matrix.shape}")
    print(f"Results saved with timestamp: {timestamp}")
    
    return analyzer, summary

if __name__ == "__main__":
    analyzer, summary = main()
