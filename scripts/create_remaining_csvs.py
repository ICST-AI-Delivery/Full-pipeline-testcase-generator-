import pandas as pd
from pathlib import Path
import subprocess
import sys

# List of remaining features to process
features = [
    ("KEY-1_Keyboard", "Pre-FineTuneLearning Model/SRS FPI export/SRS_System Architecture/KEY-1_Keyboard"),
    ("VEH-F200_Gear_and_Status_Indication", "Pre-FineTuneLearning Model/SRS FPI export/SRS_Instrument Cluster/VEH-F200_Gear_and_Status_Indication"),
    ("VFI-F200_Dependence_on_vehicle_state_conditions", "Pre-FineTuneLearning Model/SRS FPI export/SRS_HMI Software/VFI-F200_Dependence_on_vehicle_state_conditions"),
    ("SET-7_Keyboard_Layout", "Pre-FineTuneLearning Model/SRS FPI export/SRS_HMI Software/SET-7_Keyboard_Layout")
]

def create_csv_and_run_clip(feature_name, feature_path):
    print(f"\n{'='*60}")
    print(f"Processing: {feature_name}")
    print(f"{'='*60}")
    
    feature_dir = Path(feature_path)
    print(f'Looking for directory: {feature_dir}')
    print(f'Directory exists: {feature_dir.exists()}')
    
    if not feature_dir.exists():
        print(f"❌ Directory not found: {feature_dir}")
        return False
    
    # Find all image files
    image_extensions = ['*.png', '*.jpg', '*.jpeg', '*.PNG', '*.JPG', '*.JPEG']
    image_files = []
    
    for ext in image_extensions:
        image_files.extend(feature_dir.glob(ext))
    
    print(f'Found {len(image_files)} images')
    
    if not image_files:
        print('❌ No image files found')
        return False
    
    # Sort files naturally
    image_files.sort(key=lambda x: x.name)
    
    # Create CSV data
    csv_data = []
    for img_file in image_files:
        csv_data.append({
            'Image Path': str(img_file),
            'Image Name': img_file.name,
            'Ground Truth Category': '',
            'Notes': feature_name
        })
    
    # Create DataFrame and save CSV
    df = pd.DataFrame(csv_data)
    csv_output_path = Path('data_files') / f'{feature_name}.csv'
    
    # Create data_files directory if it doesn't exist
    csv_output_path.parent.mkdir(exist_ok=True)
    
    df.to_csv(csv_output_path, index=False)
    print(f'✅ Generated CSV: {csv_output_path}')
    print(f'Contains {len(csv_data)} image entries')
    
    # Show the first few entries
    for i, entry in enumerate(csv_data[:3]):
        print(f'  {i+1}. {entry["Image Name"]}')
    
    # Now run the CLIP pipeline
    print(f"\n🚀 Running CLIP pipeline for {feature_name}...")
    result = subprocess.run([
        sys.executable, 
        'scripts/simple_clip_pipeline_extended.py', 
        str(csv_output_path)
    ], capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"✅ CLIP processing completed for {feature_name}")
        # Show key results
        lines = result.stdout.split('\n')
        for line in lines:
            if 'CLIP Prediction:' in line:
                print(f"  {line.strip()}")
    else:
        print(f"❌ CLIP processing failed for {feature_name}")
        print("STDERR:", result.stderr)
    
    return result.returncode == 0

# Process all features
successful_features = []
failed_features = []

for feature_name, feature_path in features:
    success = create_csv_and_run_clip(feature_name, feature_path)
    if success:
        successful_features.append(feature_name)
    else:
        failed_features.append(feature_name)

print(f"\n{'='*60}")
print("FINAL SUMMARY")
print(f"{'='*60}")
print(f"✅ Successfully processed: {len(successful_features)} features")
for feature in successful_features:
    print(f"  - {feature}")

if failed_features:
    print(f"\n❌ Failed to process: {len(failed_features)} features")
    for feature in failed_features:
        print(f"  - {feature}")
