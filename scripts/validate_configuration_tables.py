#!/usr/bin/env python3
"""
CONFIGURATION_TABLES Analysis Validation Script

Purpose: Validate CONFIGURATION_TABLES analyses for compliance with standardized structure
Author: Picture Analyze Agent Development Team
Version: 1.0
Created: 2026-03-24
"""

import os
import re
from typing import Dict, List, Tuple
from pathlib import Path

class ConfigurationTablesValidator:
    """Validates CONFIGURATION_TABLES analysis files for compliance with standards."""
    
    def __init__(self):
        self.validation_criteria = {
            "required_sections": [
                "=== CONFIGURATION TABLE ANALYSIS REPORT ===",
                "=== TABLE STRUCTURE ANALYSIS ===",
                "=== PARAMETER EXTRACTION ===",
                "=== STATE EVENT MATRIX ANALYSIS ===",
                "=== EXTRACTED TABLE DATA ===",
                "=== CSV FORMAT READY DATA ===",
                "=== AUTOMOTIVE CONTEXT INTEGRATION ==="
            ],
            "technical_depth_indicators": [
                "CAN Signal:",
                "State Transition Matrix:",
                "Boolean Logic Extraction:",
                "Parameter Combination Matrix:",
                "Data Type:",
                "Possible Values:"
            ],
            "formatting_requirements": [
                "├─", "│", "└─",  # Tree structure formatting
                "**", "```",      # Markdown formatting
                "|", "---"        # Table formatting
            ]
        }
        
        self.section_quality_requirements = {
            "TABLE STRUCTURE ANALYSIS": [
                "TABLE DIMENSIONS:",
                "COLUMN STRUCTURE:",
                "ROW STRUCTURE:",
                "TABLE RELATIONSHIPS:"
            ],
            "PARAMETER EXTRACTION": [
                "COMPLETE TABLE DATA EXTRACTION",
                "PARAMETER DEFINITIONS",
                "CONFIGURATION COMBINATIONS"
            ],
            "STATE EVENT MATRIX ANALYSIS": [
                "System States Identified:",
                "State Transition Matrix:",
                "CAN Signal Mapping:",
                "Decision Logic Tables:"
            ]
        }
    
    def validate_file(self, file_path: str) -> Dict:
        """Validate a single CONFIGURATION_TABLES analysis file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            results = {
                'file_path': file_path,
                'section_completeness': self._check_section_completeness(content),
                'technical_depth': self._check_technical_depth(content),
                'format_consistency': self._check_format_consistency(content),
                'section_quality': self._check_section_quality(content),
                'overall_score': 0,
                'compliance_status': 'UNKNOWN',
                'missing_elements': [],
                'recommendations': []
            }
            
            # Calculate overall score
            results['overall_score'] = self._calculate_score(results)
            results['compliance_status'] = self._determine_compliance(results['overall_score'])
            results['missing_elements'] = self._identify_missing_elements(content)
            results['recommendations'] = self._generate_recommendations(results)
            
            return results
            
        except Exception as e:
            return {
                'file_path': file_path,
                'error': f"Validation failed: {str(e)}",
                'compliance_status': 'ERROR'
            }
    
    def _check_section_completeness(self, content: str) -> Dict:
        """Check if all required sections are present."""
        results = {
            'score': 0,
            'total_sections': len(self.validation_criteria['required_sections']),
            'present_sections': 0,
            'missing_sections': []
        }
        
        for section in self.validation_criteria['required_sections']:
            if section in content:
                results['present_sections'] += 1
            else:
                results['missing_sections'].append(section)
        
        results['score'] = (results['present_sections'] / results['total_sections']) * 100
        return results
    
    def _check_technical_depth(self, content: str) -> Dict:
        """Check for technical depth indicators."""
        results = {
            'score': 0,
            'total_indicators': len(self.validation_criteria['technical_depth_indicators']),
            'present_indicators': 0,
            'missing_indicators': []
        }
        
        for indicator in self.validation_criteria['technical_depth_indicators']:
            if indicator in content:
                results['present_indicators'] += 1
            else:
                results['missing_indicators'].append(indicator)
        
        results['score'] = (results['present_indicators'] / results['total_indicators']) * 100
        return results
    
    def _check_format_consistency(self, content: str) -> Dict:
        """Check for proper formatting elements."""
        results = {
            'score': 0,
            'total_formats': len(self.validation_criteria['formatting_requirements']),
            'present_formats': 0,
            'missing_formats': []
        }
        
        for format_req in self.validation_criteria['formatting_requirements']:
            if format_req in content:
                results['present_formats'] += 1
            else:
                results['missing_formats'].append(format_req)
        
        results['score'] = (results['present_formats'] / results['total_formats']) * 100
        return results
    
    def _check_section_quality(self, content: str) -> Dict:
        """Check quality of specific sections."""
        results = {}
        
        for section_name, requirements in self.section_quality_requirements.items():
            section_results = {
                'score': 0,
                'total_requirements': len(requirements),
                'met_requirements': 0,
                'missing_requirements': []
            }
            
            for requirement in requirements:
                if requirement in content:
                    section_results['met_requirements'] += 1
                else:
                    section_results['missing_requirements'].append(requirement)
            
            section_results['score'] = (section_results['met_requirements'] / section_results['total_requirements']) * 100
            results[section_name] = section_results
        
        return results
    
    def _calculate_score(self, results: Dict) -> float:
        """Calculate overall compliance score."""
        section_score = results['section_completeness']['score'] * 0.4
        technical_score = results['technical_depth']['score'] * 0.3
        format_score = results['format_consistency']['score'] * 0.1
        
        # Average section quality scores
        quality_scores = [section['score'] for section in results['section_quality'].values()]
        quality_score = (sum(quality_scores) / len(quality_scores)) * 0.2 if quality_scores else 0
        
        return section_score + technical_score + format_score + quality_score
    
    def _determine_compliance(self, score: float) -> str:
        """Determine compliance status based on score."""
        if score >= 95:
            return "EXCELLENT"
        elif score >= 85:
            return "COMPLIANT"
        elif score >= 70:
            return "NEEDS_IMPROVEMENT"
        else:
            return "NON_COMPLIANT"
    
    def _identify_missing_elements(self, content: str) -> List[str]:
        """Identify specific missing elements."""
        missing = []
        
        # Check for specific patterns that should be present
        patterns = {
            "Complete Data Matrix": r"\*\*Complete Data Matrix:\*\*",
            "CAN Signal Mapping": r"CAN_Signal",
            "State Transition Matrix": r"State_Transition_Matrix|Current_State.*Next_State",
            "CSV Format Data": r"\.csv:",
            "Parameter Definitions": r"PARAMETER \d+:",
            "Boolean Logic": r"AND Conditions:|OR Conditions:"
        }
        
        for element, pattern in patterns.items():
            if not re.search(pattern, content, re.IGNORECASE):
                missing.append(element)
        
        return missing
    
    def _generate_recommendations(self, results: Dict) -> List[str]:
        """Generate specific recommendations for improvement."""
        recommendations = []
        
        if results['section_completeness']['score'] < 100:
            recommendations.append("Add missing required sections to achieve full compliance")
        
        if results['technical_depth']['score'] < 80:
            recommendations.append("Increase technical depth with more CAN signal mapping and state analysis")
        
        if results['format_consistency']['score'] < 90:
            recommendations.append("Improve formatting consistency with proper markdown and tree structures")
        
        # Section-specific recommendations
        for section_name, section_data in results['section_quality'].items():
            if section_data['score'] < 80:
                recommendations.append(f"Enhance {section_name} section with missing requirements")
        
        if results['overall_score'] < 85:
            recommendations.append("Re-analyze using enhanced CONFIGURATION_TABLES template for full compliance")
        
        return recommendations

def validate_configuration_tables_directory(directory_path: str) -> Dict:
    """Validate all CONFIGURATION_TABLES analysis files in a directory."""
    validator = ConfigurationTablesValidator()
    results = {
        'validation_summary': {
            'total_files': 0,
            'compliant_files': 0,
            'non_compliant_files': 0,
            'error_files': 0,
            'average_score': 0
        },
        'file_results': []
    }
    
    # Find all CONFIGURATION_TABLES analysis files
    config_files = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if 'CONFIGURATION_TABLES_analysis' in file and file.endswith('.txt'):
                config_files.append(os.path.join(root, file))
    
    if not config_files:
        print(f"No CONFIGURATION_TABLES analysis files found in {directory_path}")
        return results
    
    scores = []
    for file_path in config_files:
        print(f"Validating: {file_path}")
        file_result = validator.validate_file(file_path)
        results['file_results'].append(file_result)
        
        if 'error' in file_result:
            results['validation_summary']['error_files'] += 1
        else:
            if file_result['compliance_status'] in ['COMPLIANT', 'EXCELLENT']:
                results['validation_summary']['compliant_files'] += 1
            else:
                results['validation_summary']['non_compliant_files'] += 1
            scores.append(file_result['overall_score'])
    
    results['validation_summary']['total_files'] = len(config_files)
    results['validation_summary']['average_score'] = sum(scores) / len(scores) if scores else 0
    
    return results

def generate_validation_report(results: Dict, output_file: str = None):
    """Generate a detailed validation report."""
    report = []
    report.append("# CONFIGURATION_TABLES Analysis Validation Report")
    report.append(f"**Generated:** {os.popen('date').read().strip()}")
    report.append("")
    
    # Summary
    summary = results['validation_summary']
    report.append("## Validation Summary")
    report.append(f"- **Total Files Analyzed:** {summary['total_files']}")
    report.append(f"- **Compliant Files:** {summary['compliant_files']}")
    report.append(f"- **Non-Compliant Files:** {summary['non_compliant_files']}")
    report.append(f"- **Error Files:** {summary['error_files']}")
    report.append(f"- **Average Score:** {summary['average_score']:.1f}%")
    report.append("")
    
    # Detailed results
    report.append("## Detailed File Results")
    for file_result in results['file_results']:
        if 'error' in file_result:
            report.append(f"### ❌ {os.path.basename(file_result['file_path'])}")
            report.append(f"**Status:** ERROR - {file_result['error']}")
        else:
            status_emoji = {
                'EXCELLENT': '🟢',
                'COMPLIANT': '✅',
                'NEEDS_IMPROVEMENT': '🟡',
                'NON_COMPLIANT': '❌'
            }
            
            report.append(f"### {status_emoji.get(file_result['compliance_status'], '❓')} {os.path.basename(file_result['file_path'])}")
            report.append(f"**Overall Score:** {file_result['overall_score']:.1f}%")
            report.append(f"**Status:** {file_result['compliance_status']}")
            report.append("")
            
            # Section scores
            report.append("**Section Scores:**")
            report.append(f"- Section Completeness: {file_result['section_completeness']['score']:.1f}%")
            report.append(f"- Technical Depth: {file_result['technical_depth']['score']:.1f}%")
            report.append(f"- Format Consistency: {file_result['format_consistency']['score']:.1f}%")
            report.append("")
            
            # Missing elements
            if file_result['missing_elements']:
                report.append("**Missing Elements:**")
                for element in file_result['missing_elements']:
                    report.append(f"- {element}")
                report.append("")
            
            # Recommendations
            if file_result['recommendations']:
                report.append("**Recommendations:**")
                for rec in file_result['recommendations']:
                    report.append(f"- {rec}")
                report.append("")
    
    report_text = "\n".join(report)
    
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report_text)
        print(f"Validation report saved to: {output_file}")
    
    return report_text

if __name__ == "__main__":
    import sys
    
    # Default to analysis_results directory
    directory = sys.argv[1] if len(sys.argv) > 1 else "analysis_results"
    
    print("🔍 Starting CONFIGURATION_TABLES Analysis Validation...")
    print(f"📁 Scanning directory: {directory}")
    print("=" * 60)
    
    results = validate_configuration_tables_directory(directory)
    
    # Generate and display report
    report = generate_validation_report(results, "CONFIGURATION_TABLES_VALIDATION_REPORT.md")
    
    print("\n" + "=" * 60)
    print("📊 VALIDATION COMPLETE")
    print(f"✅ Compliant: {results['validation_summary']['compliant_files']}")
    print(f"❌ Non-Compliant: {results['validation_summary']['non_compliant_files']}")
    print(f"📈 Average Score: {results['validation_summary']['average_score']:.1f}%")
    print("📄 Full report saved to: CONFIGURATION_TABLES_VALIDATION_REPORT.md")
