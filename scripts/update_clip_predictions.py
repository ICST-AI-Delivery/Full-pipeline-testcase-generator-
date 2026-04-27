"""
Simple script to update CLIP predictions in ground truth template
Keeps all ground truth data, only updates prediction columns
"""

import csv
import os
from datetime import datetime
from clip_classifier import CLIPImageClassifier

def update_clip_predictions():
    """Update CLIP predictions in existing ground truth template"""
    
    # Initialize CLIP classifier
    print("Initializing CLIP classifier...")
    classifier = CLIPImageClassifier(device="cpu")
    
    # File paths
    input_file = "data_files/ground_truth_template_with_clip_predictions_updated.csv"
    output_file = "data_files/ground_truth_template_with_clip_predictions_final.csv"
    
    # Read existing CSV and update predictions
    print(f"Reading {input_file}...")
    updated_rows = []
    
    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Get header row
        updated_rows.append(header)
        
        for row_num, row in enumerate(reader, 1):
            print(f"Processing row {row_num}: {row[1]}")  # Image name
            
            # Keep original ground truth data (columns 0-3)
            image_path = row[0]
            image_name = row[1]
            ground_truth = row[2]
            notes = row[3]
            
            # Generate new CLIP prediction
            if os.path.exists(image_path):
                category, confidence, description = classifier.classify_image(image_path)
                
                # Determine if correct
                correct_incorrect = "Correct" if category == ground_truth else "Incorrect"
                
                # Create timestamp
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                
                # Create updated row
                updated_row = [
                    image_path,           # Column 0: Image Path
                    image_name,           # Column 1: Image Name  
                    ground_truth,         # Column 2: Ground Truth Category
                    notes,                # Column 3: Notes
                    category,             # Column 4: CLIP Predicted Category
                    confidence,           # Column 5: CLIP Confidence
                    description,          # Column 6: CLIP Description
                    correct_incorrect,    # Column 7: Correct/Incorrect
                    timestamp             # Column 8: Timestamp
                ]
                
            else:
                print(f"Warning: Image not found: {image_path}")
                # Keep original row if image not found
                updated_row = row
            
            updated_rows.append(updated_row)
    
    # Write updated CSV
    print(f"Writing results to {output_file}...")
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(updated_rows)
    
    print(f"Complete! Updated predictions saved to {output_file}")

if __name__ == "__main__":
    update_clip_predictions()
