#!/usr/bin/env python3
"""
Update CSV files to use correct image paths after project restructuring
"""

import os
import pandas as pd
from pathlib import Path

def update_csv_paths():
    """Update all CSV files in data/raw to use correct image paths"""
    
    data_raw_dir = Path("data/raw")
    if not data_raw_dir.exists():
        print("data/raw directory not found")
        return
    
    # Find all CSV files
    csv_files = list(data_raw_dir.glob("*.csv"))
    print(f"Found {len(csv_files)} CSV files to update")
    
    updated_count = 0
    
    for csv_file in csv_files:
        print(f"\nProcessing: {csv_file}")
        
        try:
            # Read CSV
            df = pd.read_csv(csv_file)
            
            # Check if it has Image Path column
            if 'Image Path' not in df.columns:
                print(f"  Skipping - no 'Image Path' column")
                continue
            
            # Update paths
            original_paths = df['Image Path'].copy()
            updated_paths = []
            changes_made = False
            
            for path in original_paths:
                if pd.isna(path):
                    updated_paths.append(path)
                    continue
                    
                path_str = str(path)
                
                # Replace old path patterns with new ones
                if "Pre-FineTuneLearning Model\\SRS FPI export\\SRS_Instrument Cluster\\" in path_str:
                    new_path = path_str.replace(
                        "Pre-FineTuneLearning Model\\SRS FPI export\\SRS_Instrument Cluster\\",
                        "SRS FPI Export\\SRS_Instrument Cluster\\"
                    )
                    updated_paths.append(new_path)
                    changes_made = True
                elif "Pre-FineTuneLearning Model/SRS FPI export/SRS_Instrument Cluster/" in path_str:
                    new_path = path_str.replace(
                        "Pre-FineTuneLearning Model/SRS FPI export/SRS_Instrument Cluster/",
                        "SRS FPI Export/SRS_Instrument Cluster/"
                    )
                    updated_paths.append(new_path)
                    changes_made = True
                else:
                    updated_paths.append(path_str)
            
            if changes_made:
                # Update the DataFrame
                df['Image Path'] = updated_paths
                
                # Save back to CSV
                df.to_csv(csv_file, index=False)
                print(f"  ✅ Updated {csv_file}")
                updated_count += 1
            else:
                print(f"  No changes needed")
                
        except Exception as e:
            print(f"  ❌ Error processing {csv_file}: {e}")
    
    print(f"\n✅ Updated {updated_count} CSV files")

if __name__ == "__main__":
    update_csv_paths()
