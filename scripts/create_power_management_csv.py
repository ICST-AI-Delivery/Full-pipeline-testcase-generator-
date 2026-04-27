import pandas as pd
from pathlib import Path
import os

# Create the CSV manually for T_POWER_MANAGEMENT_($0503)
feature_dir = Path('Pre-FineTuneLearning Model/SRS FPI export/SRS_Diagnostics/T_POWER_MANAGEMENT_($0503)')
print(f'Looking for directory: {feature_dir}')
print(f'Directory exists: {feature_dir.exists()}')

if feature_dir.exists():
    # Find all image files
    image_extensions = ['*.png', '*.jpg', '*.jpeg', '*.PNG', '*.JPG', '*.JPEG']
    image_files = []
    
    for ext in image_extensions:
        image_files.extend(feature_dir.glob(ext))
    
    print(f'Found {len(image_files)} images')
    
    if image_files:
        # Sort files naturally
        image_files.sort(key=lambda x: x.name)
        
        # Create CSV data
        csv_data = []
        for img_file in image_files:
            csv_data.append({
                'Image Path': str(img_file),
                'Image Name': img_file.name,
                'Ground Truth Category': '',
                'Notes': 'T POWER MANAGEMENT ($0503)'
            })
        
        # Create DataFrame and save CSV
        df = pd.DataFrame(csv_data)
        csv_output_path = Path('data_files') / 'T_POWER_MANAGEMENT_($0503).csv'
        
        # Create data_files directory if it doesn't exist
        csv_output_path.parent.mkdir(exist_ok=True)
        
        df.to_csv(csv_output_path, index=False)
        print(f'Generated CSV: {csv_output_path}')
        print(f'Contains {len(csv_data)} image entries')
        
        # Show the first few entries
        for i, entry in enumerate(csv_data[:3]):
            print(f'  {i+1}. {entry["Image Name"]}')
    else:
        print('No image files found')
else:
    print('Directory not found')
