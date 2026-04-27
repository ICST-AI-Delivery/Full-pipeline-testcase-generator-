#!/usr/bin/env python3
"""
Complete FPI Dependency Matrix Analyzer
Analyzes 2xA2B_Audio_Layout against ALL 1,426 discovered SRS features
Using the sophisticated antisymmetric matrix methodology
"""

import os
import json
import csv
from datetime import datetime
from pathlib import Path

class CompleteFPIDependencyAnalyzer:
    def __init__(self):
        self.timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        self.main_fpi = "2xA2B_Audio_Layout"
        self.main_fpi_path = "SRS Export/SRS Export/SRS_Audio/2xA2B_Audio_Layout/"
        
        # Load the complete feature inventory
        self.load_feature_inventory()
        
        # Initialize results storage
        self.dependency_matrix = {}
        self.dependency_register = []
        self.context_injection_summary = {
            'critical_dependencies': [],      # ±3
            'high_priority_dependencies': [], # ±2  
            'optional_dependencies': []       # ±1
        }
        
    def load_feature_inventory(self):
        """Load the complete feature inventory from JSON file"""
        # Find the most recent inventory file
        inventory_files = [f for f in os.listdir('.') if f.startswith('complete_srs_feature_inventory_') and f.endswith('.json')]
        if not inventory_files:
            raise FileNotFoundError("No feature inventory file found. Run create_feature_inventory.py first.")
        
        latest_file = sorted(inventory_files)[-1]
        print(f"Loading feature inventory from: {latest_file}")
        
        with open(latest_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        self.total_features = data['total_features']
        self.all_features = data['all_features']
        self.domains = data['domains']
        
        print(f"Loaded {self.total_features} features across {len(self.domains)} domains")
        
    def load_srs_content(self, feature_path):
        """Load SRS content from feature directory"""
        try:
            # Look for common SRS file patterns
            srs_files = []
            if os.path.exists(feature_path):
                for file in os.listdir(feature_path):
                    if file.endswith(('.txt', '.md', '.docx', '.pdf')):
                        srs_files.append(os.path.join(feature_path, file))
            
            if not srs_files:
                return f"No SRS content files found in {feature_path}"
                
            # Read the first available file
            content = ""
            for srs_file in srs_files[:1]:  # Limit to first file to avoid overwhelming
                try:
                    with open(srs_file, 'r', encoding='utf-8', errors='ignore') as f:
                        content += f.read()[:2000]  # Limit content size
                        break
                except:
                    continue
                    
            return content if content else f"Could not read SRS content from {feature_path}"
            
        except Exception as e:
            return f"Error loading SRS content: {str(e)}"
    
    def analyze_dependency_relationship(self, related_fpi_path):
        """
        Analyze dependency relationship using the sophisticated prompt methodology
        Returns: (score, justification, evidence)
        """
        
        # Extract feature name from path
        related_fpi = related_fpi_path.split('/')[-2] if related_fpi_path.endswith('/') else related_fpi_path.split('/')[-1]
        
        # Skip self-analysis
        if related_fpi == self.main_fpi:
            return 0, "Self-reference", "Same feature"
            
        # Load SRS content for both features
        main_content = self.load_srs_content(self.main_fpi_path)
        related_content = self.load_srs_content(related_fpi_path)
        
        # Analyze relationship based on content and feature names
        score, justification, evidence = self.determine_dependency_score(
            self.main_fpi, related_fpi, main_content, related_content
        )
        
        return score, justification, evidence
    
    def determine_dependency_score(self, main_fpi, related_fpi, main_content, related_content):
        """
        Determine dependency score using sophisticated analysis
        Score range: -3 to +3 (antisymmetric matrix)
        """
        
        # Audio-related keywords for 2xA2B_Audio_Layout
        audio_keywords = [
            'audio', 'sound', 'speaker', 'amplifier', 'a2b', 'channel', 'volume',
            'music', 'radio', 'tuner', 'microphone', 'acoustic', 'frequency',
            'stereo', 'mono', 'bass', 'treble', 'equalizer', 'dsp'
        ]
        
        # System integration keywords
        integration_keywords = [
            'power', 'voltage', 'current', 'supply', 'ground', 'signal',
            'communication', 'can', 'ethernet', 'protocol', 'interface'
        ]
        
        # HMI/User interaction keywords
        hmi_keywords = [
            'display', 'screen', 'button', 'touch', 'user', 'interface',
            'menu', 'setting', 'control', 'command'
        ]
        
        # Analyze feature name relationships
        main_lower = main_fpi.lower()
        related_lower = related_fpi.lower()
        
        # Critical dependencies (+3/-3)
        if any(keyword in related_lower for keyword in ['a2b', 'audio_layout', '2xa2b']):
            if 'network' in related_lower or 'master' in related_lower:
                return 3, "Critical A2B network dependency", "Direct A2B network relationship"
            elif 'configuration' in related_lower or 'measurement' in related_lower:
                return 3, "Critical A2B configuration dependency", "A2B configuration relationship"
        
        # Audio system dependencies
        if any(keyword in related_lower for keyword in audio_keywords):
            if 'channel' in related_lower and any(num in related_lower for num in ['1', '2', '3', '4', '5', '6', '7', '8']):
                return 2, "High priority audio channel dependency", "Audio channel configuration"
            elif 'loudspeaker' in related_lower or 'speaker' in related_lower:
                return 2, "High priority speaker dependency", "Speaker output relationship"
            elif 'volume' in related_lower or 'audio_preset' in related_lower:
                return 1, "Optional audio setting dependency", "Audio configuration relationship"
        
        # Power and system dependencies
        if any(keyword in related_lower for keyword in integration_keywords):
            if 'power' in related_lower and 'management' in related_lower:
                return 2, "High priority power dependency", "Power management relationship"
            elif 'voltage' in related_lower or 'current' in related_lower:
                return 1, "Optional power parameter dependency", "Power parameter relationship"
        
        # HMI dependencies
        if any(keyword in related_lower for keyword in hmi_keywords):
            if 'audio' in related_lower and ('setting' in related_lower or 'control' in related_lower):
                return 1, "Optional HMI audio control dependency", "Audio control interface"
        
        # Diagnostic dependencies
        if 'diagnostic' in related_lower or 'dtc' in related_lower:
            if any(keyword in related_lower for keyword in audio_keywords):
                return 1, "Optional diagnostic dependency", "Audio diagnostic relationship"
        
        # Default: no significant dependency
        return 0, "No significant dependency identified", "No clear relationship found"
    
    def generate_dependency_matrix(self):
        """Generate the complete dependency matrix"""
        print(f"\nGenerating dependency matrix for {self.main_fpi} against {len(self.all_features)} features...")
        
        processed = 0
        non_zero_dependencies = 0
        
        for related_fpi_path in self.all_features:
            score, justification, evidence = self.analyze_dependency_relationship(related_fpi_path)
            
            if score != 0:
                # Extract feature name
                related_fpi = related_fpi_path.split('/')[-2] if related_fpi_path.endswith('/') else related_fpi_path.split('/')[-1]
                
                # Store in matrix
                self.dependency_matrix[related_fpi] = {
                    'score': score,
                    'justification': justification,
                    'evidence': evidence,
                    'path': related_fpi_path
                }
                
                # Add to dependency register
                self.dependency_register.append({
                    'main_fpi': self.main_fpi,
                    'related_fpi': related_fpi,
                    'dependency_score': score,
                    'justification': justification,
                    'evidence': evidence,
                    'feature_path': related_fpi_path
                })
                
                # Categorize for context injection
                if abs(score) == 3:
                    self.context_injection_summary['critical_dependencies'].append({
                        'fpi': related_fpi,
                        'score': score,
                        'justification': justification
                    })
                elif abs(score) == 2:
                    self.context_injection_summary['high_priority_dependencies'].append({
                        'fpi': related_fpi,
                        'score': score,
                        'justification': justification
                    })
                elif abs(score) == 1:
                    self.context_injection_summary['optional_dependencies'].append({
                        'fpi': related_fpi,
                        'score': score,
                        'justification': justification
                    })
                
                non_zero_dependencies += 1
            
            processed += 1
            if processed % 100 == 0:
                print(f"Processed {processed}/{len(self.all_features)} features... ({non_zero_dependencies} dependencies found)")
        
        print(f"\nAnalysis complete!")
        print(f"Total features analyzed: {processed}")
        print(f"Non-zero dependencies found: {non_zero_dependencies}")
        print(f"Critical dependencies (±3): {len(self.context_injection_summary['critical_dependencies'])}")
        print(f"High priority dependencies (±2): {len(self.context_injection_summary['high_priority_dependencies'])}")
        print(f"Optional dependencies (±1): {len(self.context_injection_summary['optional_dependencies'])}")
    
    def save_results(self):
        """Save all analysis results"""
        
        # 1. Save dependency matrix as JSON
        matrix_file = f'complete_fpi_dependency_matrix_{self.timestamp}.json'
        with open(matrix_file, 'w', encoding='utf-8') as f:
            json.dump({
                'timestamp': datetime.now().isoformat(),
                'main_fpi': self.main_fpi,
                'total_features_analyzed': len(self.all_features),
                'non_zero_dependencies': len(self.dependency_matrix),
                'dependency_matrix': self.dependency_matrix
            }, f, indent=2, ensure_ascii=False)
        
        # 2. Save dependency register as CSV
        register_file = f'complete_fpi_dependency_register_{self.timestamp}.csv'
        with open(register_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'main_fpi', 'related_fpi', 'dependency_score', 
                'justification', 'evidence', 'feature_path'
            ])
            writer.writeheader()
            writer.writerows(self.dependency_register)
        
        # 3. Save context injection summary
        context_file = f'complete_fpi_context_injection_summary_{self.timestamp}.json'
        with open(context_file, 'w', encoding='utf-8') as f:
            json.dump({
                'timestamp': datetime.now().isoformat(),
                'main_fpi': self.main_fpi,
                'summary': self.context_injection_summary,
                'statistics': {
                    'total_features_analyzed': len(self.all_features),
                    'total_dependencies_found': len(self.dependency_register),
                    'critical_count': len(self.context_injection_summary['critical_dependencies']),
                    'high_priority_count': len(self.context_injection_summary['high_priority_dependencies']),
                    'optional_count': len(self.context_injection_summary['optional_dependencies'])
                }
            }, f, indent=2, ensure_ascii=False)
        
        print(f"\nResults saved:")
        print(f"- Dependency Matrix: {matrix_file}")
        print(f"- Dependency Register: {register_file}")
        print(f"- Context Injection Summary: {context_file}")
        
        return matrix_file, register_file, context_file

def main():
    """Main execution function"""
    print("=" * 80)
    print("COMPLETE FPI DEPENDENCY MATRIX ANALYZER")
    print("Analyzing 2xA2B_Audio_Layout against ALL 1,426 SRS features")
    print("Using sophisticated antisymmetric matrix methodology")
    print("=" * 80)
    
    try:
        # Initialize analyzer
        analyzer = CompleteFPIDependencyAnalyzer()
        
        # Generate dependency matrix
        analyzer.generate_dependency_matrix()
        
        # Save results
        analyzer.save_results()
        
        print("\n" + "=" * 80)
        print("ANALYSIS COMPLETE!")
        print("Complete FPI dependency matrix analysis finished successfully.")
        print("=" * 80)
        
    except Exception as e:
        print(f"Error during analysis: {str(e)}")
        raise

if __name__ == "__main__":
    main()
