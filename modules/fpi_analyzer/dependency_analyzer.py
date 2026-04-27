#!/usr/bin/env python3
"""
FPI Testcase Context Dependency Matrix Placeholder Generator

This script creates a placeholder matrix for the FPI testcase context dependency analysis.
- Dimensions: 1426x1426 (all features as both rows and columns)
- Format: CSV file with feature names as headers
- Initial Values: "X" for all uncomputed relationships, "0" for diagonal (self-references)
- Compliance: Follows the FPI testcase context dependency matrix prompt methodology

The matrix will serve as a baseline for tracking computation progress, where:
- "X" markers will be replaced with dependency scores (-3 to +3) as relationships are computed
- Progress tracking: Count of "X" vs computed scores
"""

import json
import csv
import os
from datetime import datetime

def load_feature_inventory(file_path):
    """Load the complete feature inventory from JSON file."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            # Extract all feature paths from the inventory
            all_features = data.get("all_features", [])
            print(f"Loaded {len(all_features)} features from inventory.")
            return all_features
    except Exception as e:
        print(f"Error loading feature inventory: {e}")
        return []

def create_matrix_placeholder(features):
    """Create a placeholder matrix with all features as rows and columns."""
    # Initialize matrix with "X" for all cells
    matrix = {}
    
    # Use feature paths as keys
    for feature in features:
        # Extract feature name from path for cleaner display
        feature_name = os.path.basename(os.path.dirname(feature))
        matrix[feature] = {}
        
        for other_feature in features:
            if feature == other_feature:
                # Diagonal elements (self-references) are set to "0"
                matrix[feature][other_feature] = "0"
            else:
                # Off-diagonal elements (uncomputed relationships) are set to "X"
                matrix[feature][other_feature] = "X"
    
    return matrix

def export_matrix_to_csv(matrix, features, output_file):
    """Export the matrix to a CSV file."""
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            
            # Write header row with feature names
            header = ["Feature_Name"] + features
            writer.writerow(header)
            
            # Write matrix rows
            for feature in features:
                row = [feature]
                for other_feature in features:
                    row.append(matrix[feature][other_feature])
                writer.writerow(row)
                
        print(f"Matrix exported to {output_file}")
        return True
    except Exception as e:
        print(f"Error exporting matrix to CSV: {e}")
        return False

def generate_matrix_stats(matrix, features):
    """Generate statistics about the matrix."""
    total_cells = len(features) * len(features)
    diagonal_cells = len(features)
    uncomputed_cells = sum(1 for f1 in features for f2 in features if matrix[f1][f2] == "X")
    computed_cells = total_cells - uncomputed_cells - diagonal_cells
    
    stats = {
        "total_features": len(features),
        "total_cells": total_cells,
        "diagonal_cells": diagonal_cells,
        "uncomputed_cells": uncomputed_cells,
        "computed_cells": computed_cells,
        "completion_percentage": round((computed_cells / (total_cells - diagonal_cells)) * 100, 2)
    }
    
    return stats

def main():
    # Configuration
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    inventory_file = "complete_srs_feature_inventory_20260416_142136.json"
    output_file = f"fpi_dependency_matrix_placeholder_{timestamp}.csv"
    stats_file = f"fpi_dependency_matrix_stats_{timestamp}.json"
    
    # Load feature inventory
    features = load_feature_inventory(inventory_file)
    if not features:
        print("Failed to load features. Exiting.")
        return
    
    # Create matrix placeholder
    print(f"Creating {len(features)}x{len(features)} matrix placeholder...")
    matrix = create_matrix_placeholder(features)
    
    # Export matrix to CSV
    print(f"Exporting matrix to {output_file}...")
    export_success = export_matrix_to_csv(matrix, features, output_file)
    
    if export_success:
        # Generate and save matrix statistics
        stats = generate_matrix_stats(matrix, features)
        with open(stats_file, 'w') as f:
            json.dump(stats, f, indent=2)
        
        print("\nMatrix Placeholder Generation Complete!")
        print(f"Total Features: {stats['total_features']}")
        print(f"Total Matrix Cells: {stats['total_cells']}")
        print(f"Diagonal Cells (0): {stats['diagonal_cells']}")
        print(f"Uncomputed Cells (X): {stats['uncomputed_cells']}")
        print(f"Computed Cells: {stats['computed_cells']}")
        print(f"Completion Percentage: {stats['completion_percentage']}%")
        print(f"\nMatrix saved to: {output_file}")
        print(f"Statistics saved to: {stats_file}")
    else:
        print("Failed to export matrix. Exiting.")

if __name__ == "__main__":
    main()
