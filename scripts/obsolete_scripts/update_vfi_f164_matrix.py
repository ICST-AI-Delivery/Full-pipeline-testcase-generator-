#!/usr/bin/env python3
"""
VFI-F164 Energy Manettino Matrix Update Script

This script updates the placeholder FPI dependency matrix with computed scores
for VFI-F164_Energy_Manettino relationships and applies antisymmetric properties.
"""

import pandas as pd
import numpy as np
from datetime import datetime
import json
import os

def load_dependency_register(register_file):
    """Load the VFI-F164 dependency register CSV"""
    print(f"Loading dependency register: {register_file}")
    df = pd.read_csv(register_file)
    print(f"Loaded {len(df)} dependency relationships")
    return df

def load_placeholder_matrix(matrix_file):
    """Load the placeholder matrix CSV"""
    print(f"Loading placeholder matrix: {matrix_file}")
    df = pd.read_csv(matrix_file, index_col=0)
    print(f"Matrix dimensions: {df.shape}")
    return df

def update_matrix_with_scores(matrix_df, register_df, main_fpi):
    """Update matrix with computed scores and apply antisymmetric property"""
    print(f"Updating matrix for main FPI: {main_fpi}")
    
    # Track updates
    updates_made = 0
    score_distribution = {-3: 0, -2: 0, -1: 0, 0: 0, 1: 0, 2: 0, 3: 0}
    
    # Find the main FPI in matrix (should be both row and column)
    if main_fpi not in matrix_df.index:
        print(f"ERROR: Main FPI '{main_fpi}' not found in matrix rows")
        return matrix_df, updates_made, score_distribution
    
    if main_fpi not in matrix_df.columns:
        print(f"ERROR: Main FPI '{main_fpi}' not found in matrix columns")
        return matrix_df, updates_made, score_distribution
    
    print(f"Found main FPI in matrix at position: row={list(matrix_df.index).index(main_fpi)}, col={list(matrix_df.columns).index(main_fpi)}")
    
    # Process each relationship in the register
    for _, row in register_df.iterrows():
        related_fpi = row['Related_FPI']
        score = int(row['Score'])
        
        # Update main FPI -> related FPI (row perspective)
        if related_fpi in matrix_df.columns:
            matrix_df.loc[main_fpi, related_fpi] = score
            updates_made += 1
            score_distribution[score] += 1
            
            # Apply antisymmetric property: related FPI -> main FPI = -score
            if main_fpi in matrix_df.columns:
                antisymmetric_score = -score
                matrix_df.loc[related_fpi, main_fpi] = antisymmetric_score
                updates_made += 1
                score_distribution[antisymmetric_score] += 1
        else:
            print(f"WARNING: Related FPI '{related_fpi}' not found in matrix columns")
    
    # Ensure diagonal is 0 (no self-dependencies)
    matrix_df.loc[main_fpi, main_fpi] = 0
    
    print(f"Matrix updates completed: {updates_made} cells updated")
    return matrix_df, updates_made, score_distribution

def validate_antisymmetric_property(matrix_df, main_fpi):
    """Validate that antisymmetric property is maintained"""
    print("Validating antisymmetric property...")
    
    violations = 0
    total_checks = 0
    
    # Check all relationships involving main FPI
    for other_fpi in matrix_df.columns:
        if other_fpi != main_fpi:
            val_ab = matrix_df.loc[main_fpi, other_fpi]
            val_ba = matrix_df.loc[other_fpi, main_fpi]
            
            # Skip if either value is still "X" (uncomputed)
            if val_ab != "X" and val_ba != "X":
                total_checks += 1
                if val_ab != -val_ba:
                    violations += 1
                    print(f"VIOLATION: {main_fpi} -> {other_fpi} = {val_ab}, but {other_fpi} -> {main_fpi} = {val_ba} (should be {-val_ab})")
    
    print(f"Antisymmetric validation: {violations} violations out of {total_checks} checks")
    return violations == 0

def generate_score_distribution_report(score_distribution, main_fpi):
    """Generate detailed score distribution report"""
    total_relationships = sum(abs(count) for count in score_distribution.values()) // 2  # Divide by 2 due to antisymmetric pairs
    
    report = {
        "main_fpi": main_fpi,
        "timestamp": datetime.now().isoformat(),
        "total_relationships": total_relationships,
        "score_distribution": score_distribution,
        "critical_upstream": score_distribution[-3],
        "high_upstream": score_distribution[-2],
        "low_upstream": score_distribution[-1],
        "no_dependency": score_distribution[0],
        "low_downstream": score_distribution[1],
        "high_downstream": score_distribution[2],
        "critical_downstream": score_distribution[3],
        "upstream_total": score_distribution[-3] + score_distribution[-2] + score_distribution[-1],
        "downstream_total": score_distribution[1] + score_distribution[2] + score_distribution[3]
    }
    
    return report

def main():
    # File paths
    register_file = "vfi_f164_energy_manettino_register_20260416_150457.csv"
    placeholder_file = "fpi_dependency_matrix_placeholder_20260416_145904.csv"
    
    # Main FPI being analyzed
    main_fpi = "SRS Export/SRS Export/SRS_HMI Software/VFI-F164_Energy_Manettino/"
    
    # Generate timestamp for backup and report files
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    try:
        # Create backup of original placeholder matrix
        backup_file = f"fpi_dependency_matrix_placeholder_backup_{timestamp}.csv"
        
        # Load data
        register_df = load_dependency_register(register_file)
        matrix_df = load_placeholder_matrix(placeholder_file)
        
        # Create backup before updating
        matrix_df.to_csv(backup_file)
        print(f"Backup of original placeholder created: {backup_file}")
        
        print(f"\nOriginal matrix info:")
        print(f"- Shape: {matrix_df.shape}")
        print(f"- Unique values: {matrix_df.values.flatten()}")
        unique_vals, counts = np.unique(matrix_df.values.flatten(), return_counts=True)
        for val, count in zip(unique_vals, counts):
            print(f"  '{val}': {count} cells")
        
        # Update matrix with scores
        updated_matrix, updates_made, score_distribution = update_matrix_with_scores(
            matrix_df, register_df, main_fpi
        )
        
        # Validate antisymmetric property
        is_valid = validate_antisymmetric_property(updated_matrix, main_fpi)
        
        # Generate report
        report = generate_score_distribution_report(score_distribution, main_fpi)
        report["matrix_validation"] = {
            "antisymmetric_property_valid": is_valid,
            "total_updates_made": updates_made
        }
        report["files"] = {
            "original_placeholder": placeholder_file,
            "backup_created": backup_file,
            "updated_placeholder": placeholder_file
        }
        
        # Update the original placeholder matrix file
        updated_matrix.to_csv(placeholder_file)
        print(f"\nOriginal placeholder matrix updated: {placeholder_file}")
        
        # Save report
        report_file = f"vfi_f164_matrix_update_report_{timestamp}.json"
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"Update report saved to: {report_file}")
        
        # Print summary
        print(f"\n=== VFI-F164 MATRIX UPDATE SUMMARY ===")
        print(f"Main FPI: {main_fpi}")
        print(f"Total updates made: {updates_made}")
        print(f"Antisymmetric property valid: {is_valid}")
        print(f"\nScore Distribution:")
        print(f"  Critical Upstream (-3): {score_distribution[-3]}")
        print(f"  High Upstream (-2): {score_distribution[-2]}")
        print(f"  Low Upstream (-1): {score_distribution[-1]}")
        print(f"  No Dependency (0): {score_distribution[0]}")
        print(f"  Low Downstream (+1): {score_distribution[1]}")
        print(f"  High Downstream (+2): {score_distribution[2]}")
        print(f"  Critical Downstream (+3): {score_distribution[3]}")
        
        print(f"\nUpstream Dependencies: {report['upstream_total']}")
        print(f"Downstream Dependencies: {report['downstream_total']}")
        print(f"Total Unique Relationships: {report['total_relationships']}")
        
        # Check final matrix state
        print(f"\nFinal matrix info:")
        unique_vals, counts = np.unique(updated_matrix.values.flatten(), return_counts=True)
        for val, count in zip(unique_vals, counts):
            print(f"  '{val}': {count} cells")
        
        print(f"\nMatrix update completed successfully!")
        
    except Exception as e:
        print(f"ERROR: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
