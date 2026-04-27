#!/usr/bin/env python3
"""
Extract DMS-7 dependency register from existing analysis results
"""

import pandas as pd
import json
import os

def extract_dms7_register():
    """Extract DMS-7 relationships from analysis results"""
    
    # Input file path
    input_file = 'fpi_matrix_results/feature_analysis_DMS-7_DRIVER_GAZE_ESTIMATION_20260416_124302.json'
    output_file = 'dms7_dependency_register.csv'
    
    try:
        # Load the analysis results
        with open(input_file, 'r') as f:
            data = json.load(f)
        
        # Extract relationships
        if 'relationships' in data:
            relationships = data['relationships']
            
            # Convert to DataFrame
            df = pd.DataFrame(relationships)
            
            # Save to CSV
            df.to_csv(output_file, index=False)
            
            print(f"DMS-7 dependency register generated: {output_file}")
            print(f"Total relationships extracted: {len(relationships)}")
            
            # Display first few relationships
            if len(relationships) > 0:
                print("\nFirst few relationships:")
                print(df.head())
                
        else:
            print("No 'relationships' key found in the analysis file")
            
    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except Exception as e:
        print(f"Error extracting DMS-7 register: {e}")

if __name__ == "__main__":
    extract_dms7_register()
