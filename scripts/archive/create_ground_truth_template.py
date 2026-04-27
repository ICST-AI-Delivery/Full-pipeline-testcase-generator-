"""
Script to create ground truth template CSV from image list
"""

import csv
import os

def create_ground_truth_template():
    """Create ground truth template CSV from image_list.txt"""
    
    # Read image paths from image_list.txt
    image_paths = []
    with open('image_list.txt', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            # Skip empty lines and comments
            if line and not line.startswith('#'):
                image_paths.append(line)
    
    print(f"Found {len(image_paths)} images to include in template")
    
    # Create ground truth template CSV
    with open('ground_truth_template.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write header
        writer.writerow(['Image Path', 'Filename', 'Ground_Truth_Category', 'Notes'])
        
        # Write each image path with empty ground truth fields
        for image_path in image_paths:
            filename = os.path.basename(image_path)
            writer.writerow([image_path, filename, '', ''])
    
    print("Ground truth template created: ground_truth_template.csv")
    print("\nInstructions:")
    print("1. Open ground_truth_template.csv")
    print("2. Fill in the 'Ground_Truth_Category' column with the correct category for each image")
    print("3. Optionally add notes in the 'Notes' column")
    print("4. Save the file when complete")

if __name__ == "__main__":
    create_ground_truth_template()
