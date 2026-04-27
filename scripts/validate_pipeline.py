#!/usr/bin/env python3
"""
Validation script for the automated vision pipeline
Tests all components without making API calls
"""

import pandas as pd
from pathlib import Path
import sys

def test_csv_files():
    """Test CSV file access and structure"""
    print("=== Testing CSV Files ===")
    
    csv_files = [
        "data_files/VEH-F165_Manettino_with_clip_predictions.csv",
        "data_files/VEH-F844_Matrix_State_Event_with_clip_predictions.csv",
        "data_files/VEH-F001_Immobilizer_images_with_clip_predictions.csv",
        "data_files/DMS-7_DRIVER_GAZE_ESTIMATION_with_clip_predictions.csv"
    ]
    
    required_columns = ['Image Path', 'Image Name', 'CLIP Predicted Category']
    
    for csv_file in csv_files:
        if Path(csv_file).exists():
            try:
                df = pd.read_csv(csv_file)
                print(f"✅ {csv_file}: {len(df)} rows")
                
                # Check columns
                missing_cols = [col for col in required_columns if col not in df.columns]
                if missing_cols:
                    print(f"   ❌ Missing columns: {missing_cols}")
                else:
                    print(f"   ✅ All required columns present")
                
                # Check data quality
                valid_rows = df.dropna(subset=required_columns)
                print(f"   📊 Valid rows: {len(valid_rows)}/{len(df)}")
                
                # Sample categories
                categories = df['CLIP Predicted Category'].dropna().unique()
                print(f"   📋 Categories: {len(categories)} unique")
                
            except Exception as e:
                print(f"   ❌ Error reading {csv_file}: {e}")
        else:
            print(f"❌ {csv_file}: Not found")
    
    print()

def test_prompt_files():
    """Test prompt file access"""
    print("=== Testing Prompt Files ===")
    
    # Import the category mapping
    sys.path.append('scripts')
    try:
        from automated_vision_pipeline import CATEGORY_PROMPTS
        print(f"✅ Category mapping loaded: {len(CATEGORY_PROMPTS)} categories")
    except Exception as e:
        print(f"❌ Error loading category mapping: {e}")
        return
    
    prompt_dir = Path("modules/image_analyzer/prompts")
    if not prompt_dir.exists():
        print("❌ Prompt directory not found")
        return
    
    print(f"✅ Prompt directory found")
    
    # Check each mapped prompt file
    missing_files = []
    found_files = []
    
    for category, prompt_file in CATEGORY_PROMPTS.items():
        prompt_path = prompt_dir / prompt_file
        if prompt_path.exists():
            found_files.append(prompt_file)
            # Test reading the file
            try:
                with open(prompt_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    print(f"   ✅ {prompt_file}: {len(content)} characters")
            except Exception as e:
                print(f"   ⚠️  {prompt_file}: Read error - {e}")
        else:
            missing_files.append(prompt_file)
    
    print(f"📊 Summary: {len(found_files)} found, {len(missing_files)} missing")
    
    if missing_files:
        print("❌ Missing prompt files:")
        for missing in missing_files[:5]:  # Show first 5
            print(f"   - {missing}")
    
    print()

def test_output_structure():
    """Test output directory structure"""
    print("=== Testing Output Structure ===")
    
    analysis_dir = Path("analysis_results")
    if analysis_dir.exists():
        print(f"✅ Analysis results directory exists")
        
        # Count existing feature directories
        feature_dirs = [d for d in analysis_dir.iterdir() if d.is_dir()]
        print(f"📁 Existing feature directories: {len(feature_dirs)}")
        
        for feature_dir in feature_dirs[:3]:  # Show first 3
            analysis_files = list(feature_dir.glob("*.txt"))
            print(f"   📂 {feature_dir.name}: {len(analysis_files)} analysis files")
    else:
        print("📁 Analysis results directory will be created when needed")
    
    print()

def test_dependencies():
    """Test required Python packages"""
    print("=== Testing Dependencies ===")
    
    required_packages = [
        ('pandas', 'pd'),
        ('pathlib', 'Path'),
        ('base64', 'base64'),
        ('anthropic', 'anthropic')
    ]
    
    for package_name, import_name in required_packages:
        try:
            if import_name == 'pd':
                import pandas as pd
            elif import_name == 'Path':
                from pathlib import Path
            elif import_name == 'base64':
                import base64
            elif import_name == 'anthropic':
                import anthropic
            
            print(f"✅ {package_name}: Available")
        except ImportError:
            print(f"❌ {package_name}: Missing - install with 'pip install {package_name}'")
    
    print()

def main():
    """Run all validation tests"""
    print("🔍 AUTOMATED VISION PIPELINE VALIDATION")
    print("=" * 50)
    print()
    
    test_dependencies()
    test_csv_files()
    test_prompt_files()
    test_output_structure()
    
    print("🎯 VALIDATION COMPLETE")
    print("=" * 50)
    print()
    print("If all tests show ✅, your pipeline is ready to use!")
    print("Run with: python scripts/automated_vision_pipeline.py <feature_name>")
    print()

if __name__ == "__main__":
    main()
