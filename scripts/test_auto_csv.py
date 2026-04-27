#!/usr/bin/env python3
"""
Test script for auto-CSV generation functionality
"""

import sys
import os
from pathlib import Path

# Import the auto_generate_csv function from the main pipeline
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.automated_vision_pipeline import auto_generate_csv

def test_auto_csv_generation():
    """Test the auto-CSV generation functionality"""
    print("=" * 60)
    print("🧪 Testing Auto-CSV Generation")
    print("=" * 60)
    
    # Test features
    test_features = [
        "VEH-F001_Immobilizer",
        "VEH-F020_Speedometer",
        "VEH-F844_Matrix_State_Events"
    ]
    
    for feature in test_features:
        print(f"\n📋 Testing feature: {feature}")
        
        # Check if CSV already exists and rename it temporarily if it does
        csv_path = Path(f"data_files/{feature}.csv")
        backup_path = None
        
        if csv_path.exists():
            backup_path = csv_path.with_suffix('.csv.backup')
            print(f"   ⚠️ CSV already exists, creating backup: {backup_path}")
            csv_path.rename(backup_path)
        
        # Run auto-generation
        success = auto_generate_csv(feature)
        
        # Verify results
        if success:
            if csv_path.exists():
                print(f"   ✅ SUCCESS: CSV file created at {csv_path}")
                
                # Check content
                import pandas as pd
                try:
                    df = pd.read_csv(csv_path)
                    print(f"   📊 CSV contains {len(df)} images")
                    print(f"   📊 Columns: {', '.join(df.columns)}")
                    
                    # Check if required columns exist
                    required_columns = ['Image Path', 'Image Name', 'Ground Truth Category', 'Notes']
                    missing_columns = [col for col in required_columns if col not in df.columns]
                    
                    if missing_columns:
                        print(f"   ❌ ERROR: Missing columns: {', '.join(missing_columns)}")
                    else:
                        print(f"   ✅ All required columns present")
                        
                except Exception as e:
                    print(f"   ❌ ERROR reading CSV: {e}")
            else:
                print(f"   ❌ ERROR: Function reported success but CSV file not found")
        else:
            print(f"   ❌ ERROR: Auto-generation failed for {feature}")
        
        # Restore backup if it exists
        if backup_path and backup_path.exists():
            print(f"   🔄 Restoring original CSV from backup")
            if csv_path.exists():
                csv_path.unlink()
            backup_path.rename(csv_path)

if __name__ == "__main__":
    test_auto_csv_generation()
