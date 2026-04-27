import pandas as pd
from pathlib import Path
import subprocess
import sys

# Process the final feature
feature_name = "VEH-F200_Gear_and_Status_Indication"
feature_path = "Pre-FineTuneLearning Model/SRS FPI export/SRS_Instrument Cluster/VEH-F200_Gear_and_Status_Indication_by_AutomaticRobotized_Gearbox"

print(f"Processing: {feature_name}")
print(f"Path: {feature_path}")

feature_dir = Path(feature_path)
print(f'Directory exists: {feature_dir.exists()}')

if not feature_dir.exists():
    print(f"❌ Directory not found: {feature_dir}")
    exit(1)

# Find all image files
image_extensions = ['*.png', '*.jpg', '*.jpeg', '*.PNG', '*.JPG', '*.JPEG']
image_files = []

for ext in image_extensions:
    image_files.extend(feature_dir.glob(ext))

print(f'Found {len(image_files)} images')

if not image_files:
    print('❌ No image files found')
    exit(1)

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
for i, entry in enumerate(csv_data[:5]):
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
    prediction_count = 0
    for line in lines:
        if 'CLIP Prediction:' in line:
            prediction_count += 1
            if prediction_count <= 5:  # Show first 5 predictions
                print(f"  {line.strip()}")
    if prediction_count > 5:
        print(f"  ... and {prediction_count - 5} more predictions")
else:
    print(f"❌ CLIP processing failed for {feature_name}")
    print("STDERR:", result.stderr)

print(f"\n✅ Final feature {feature_name} processing complete!")
