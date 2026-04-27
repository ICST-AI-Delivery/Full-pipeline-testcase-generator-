"""
Run CLIP Classifier with Simplified Descriptions Structure
Uses the same structure as clip_ground_truth_evaluation_results_simplified_descriptions.csv
"""

import os
import csv
import pandas as pd
from datetime import datetime
from clip_classifier import CLIPImageClassifier

def run_clip_with_ground_truth_structure():
    """
    Run CLIP classifier using the ground truth template and output in the same format
    as the simplified descriptions file
    """
    
    # Initialize CLIP classifier
    print("Initializing CLIP classifier...")
    classifier = CLIPImageClassifier(device="cpu")  # Use "cuda" if GPU available
    
    # Read the ground truth template
    ground_truth_file = "data_files/ground_truth_template.csv"
    output_file = "data_files/clip_predictions_simplified_structure.csv"
    
    print(f"Reading ground truth template from: {ground_truth_file}")
    
    try:
        # Read ground truth data
        df = pd.read_csv(ground_truth_file)
        print(f"Found {len(df)} images to process")
        
        # Prepare results list
        results = []
        
        # Process each image
        for idx, row in df.iterrows():
            image_path = row['Image Path']
            image_name = row['Filename']
            ground_truth_category = row['Ground_Truth_Category'].strip() if pd.notna(row['Ground_Truth_Category']) else ""
            notes = row['Notes'] if pd.notna(row['Notes']) else "nan"
            
            print(f"Processing {idx + 1}/{len(df)}: {image_name}")
            
            # Check if image exists
            if not os.path.exists(image_path):
                print(f"  Warning: Image not found at {image_path}")
                # Still add to results with error
                results.append([
                    image_path,
                    image_name,
                    ground_truth_category,
                    notes,
                    "FILE NOT FOUND",
                    "Low",
                    "Error: Image file not found",
                    "N/A",
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                ])
                continue
            
            # Run CLIP classification
            try:
                clip_category, clip_confidence, clip_description = classifier.classify_image(image_path)
                
                # Determine if prediction is correct
                # Handle the category mapping differences
                ground_truth_normalized = ground_truth_category.replace("TABLE + TELLTALES", "TABLE WITH TELLTALES")
                ground_truth_normalized = ground_truth_normalized.replace("COLOR && GRADIENTS", "COLOR AND GRADIENTS")
                
                if clip_category == ground_truth_normalized:
                    correct_incorrect = "Correct"
                else:
                    correct_incorrect = "Incorrect"
                
                # Add result
                results.append([
                    image_path,
                    image_name,
                    ground_truth_category,
                    notes,
                    clip_category,
                    clip_confidence,
                    clip_description,
                    correct_incorrect,
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                ])
                
                print(f"  Ground Truth: {ground_truth_category}")
                print(f"  CLIP Prediction: {clip_category} ({clip_confidence})")
                print(f"  Result: {correct_incorrect}")
                
            except Exception as e:
                print(f"  Error processing image: {e}")
                results.append([
                    image_path,
                    image_name,
                    ground_truth_category,
                    notes,
                    "ERROR",
                    "Low",
                    f"Error: {str(e)}",
                    "N/A",
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                ])
        
        # Save results to CSV
        print(f"\nSaving results to: {output_file}")
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            # Write header (same as simplified descriptions file)
            writer.writerow([
                'Image Path',
                'Image Name', 
                'Ground Truth Category',
                'Notes',
                'CLIP Predicted Category',
                'CLIP Confidence',
                'CLIP Description',
                'Correct/Incorrect',
                'Timestamp'
            ])
            # Write all results
            writer.writerows(results)
        
        # Calculate and display accuracy
        correct_count = sum(1 for result in results if result[7] == "Correct")
        total_valid = sum(1 for result in results if result[7] in ["Correct", "Incorrect"])
        
        if total_valid > 0:
            accuracy = (correct_count / total_valid) * 100
            print(f"\nClassification Results:")
            print(f"Total images processed: {len(results)}")
            print(f"Valid classifications: {total_valid}")
            print(f"Correct predictions: {correct_count}")
            print(f"Accuracy: {accuracy:.2f}%")
        
        print(f"\nResults saved to: {output_file}")
        print("File structure matches clip_ground_truth_evaluation_results_simplified_descriptions.csv")
        
    except Exception as e:
        print(f"Error reading ground truth file: {e}")
        return

def main():
    """
    Main function to run the CLIP classifier with simplified structure
    """
    print("=" * 60)
    print("CLIP Classifier with Simplified Descriptions Structure")
    print("=" * 60)
    
    run_clip_with_ground_truth_structure()
    
    print("\nProcess completed!")

if __name__ == "__main__":
    main()
