#!/usr/bin/env python3
"""
Clean merged predictions file by removing FILE NOT FOUND entries
"""

import pandas as pd
from pathlib import Path

def clean_merged_predictions():
    """Remove FILE NOT FOUND entries from merged predictions"""
    
    merged_file = Path("data/processed/merged_clip_predictions.csv")
    
    if not merged_file.exists():
        print("Merged predictions file not found")
        return
    
    print(f"Cleaning: {merged_file}")
    
    # Read the file
    df = pd.read_csv(merged_file)
    print(f"Original entries: {len(df)}")
    
    # Count FILE NOT FOUND entries
    file_not_found_count = len(df[df['CLIP Predicted Category'] == 'FILE NOT FOUND'])
    print(f"FILE NOT FOUND entries: {file_not_found_count}")
    
    # Remove FILE NOT FOUND entries
    df_cleaned = df[df['CLIP Predicted Category'] != 'FILE NOT FOUND'].copy()
    print(f"Entries after cleaning: {len(df_cleaned)}")
    
    # Save the cleaned file
    df_cleaned.to_csv(merged_file, index=False)
    print(f"✅ Cleaned merged predictions file")
    print(f"Removed {file_not_found_count} FILE NOT FOUND entries")

if __name__ == "__main__":
    clean_merged_predictions()
