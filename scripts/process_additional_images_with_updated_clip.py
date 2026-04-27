"""
Process Additional Images with Updated CLIP Classifier
Creates a new file with the same structure as additional_images_with_old_clip_descriptions.csv
but using the updated CLIP classifier with improved category descriptions
"""

import os
import csv
import pandas as pd
from datetime import datetime
from clip_classifier import CLIPImageClassifier

def process_additional_images_with_updated_clip():
    """
    Process additional images using updated CLIP classifier and create new CSV
    with same structure as the original file
    """
    
    # Initialize updated CLIP classifier
    print("Initializing updated CLIP classifier...")
    classifier = CLIPImageClassifier(device="cpu")  # Use "cuda" if GPU available
    
    # Input and output files
    input_file = "data_files/additional_images_with_old_clip_descriptions.csv"
    output_file = "data_files/additional_images_with_updated_clip_descriptions.csv"
    
    print(f"Reading additional images from: {input_file}")
    
    try:
        # Read the original CSV
        df = pd.read_csv(input_file)
        print(f"Found {len(df)} images to process")
        
        # Prepare results list
        results = []
        
        # Process each image
        for idx, row in df.iterrows():
            image_path = row['Image Path']
            filename = row['Filename']
            ground_truth_category = row['Ground_Truth_Category'] if pd.notna(row['Ground_Truth_Category']) else ""
            notes = row['Notes'] if pd.notna(row['Notes']) else ""
            original_clip_category = row['Original CLIP Category']
            original_clip_confidence = row['Original CLIP Confidence']
            original_clip_description = row['Original CLIP Description']
            classification_correct = row['Classification_Correct']
            
            print(f"Processing {idx + 1}/{len(df)}: {filename}")
            
            # Check if image exists
            if not os.path.exists(image_path):
                print(f"  Warning: Image not found at {image_path}")
                # Still add to results with error
                results.append([
                    image_path,
                    filename,
                    ground_truth_category,
                    notes,
                    original_clip_category,
                    original_clip_confidence,
                    original_clip_description,
                    classification_correct,
                    "FILE NOT FOUND",
                    "Low",
                    "Error: Image file not found",
                    "N/A",
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                ])
                continue
            
            # Run updated CLIP classification
            try:
                updated_clip_category, updated_clip_confidence, updated_clip_description = classifier.classify_image(image_path)
                
                # Determine if updated prediction is correct (if we have ground truth)
                updated_classification_correct = "N/A"
                if ground_truth_category and ground_truth_category.strip():
                    # Handle category mapping differences
                    ground_truth_normalized = ground_truth_category.replace("TABLE + TELLTALES", "TABLE WITH TELLTALES")
                    ground_truth_normalized = ground_truth_normalized.replace("COLOR && GRADIENTS", "COLOR AND GRADIENTS")
                    ground_truth_normalized = ground_truth_normalized.replace("TECHNICAL SPEC", "TECHNICAL SPECIFICATIONS")
                    ground_truth_normalized = ground_truth_normalized.replace("HMI DISPLAY LAYOUT", "HMI DISPLAY LAYOUTS")
                    
                    if updated_clip_category == ground_truth_normalized:
                        updated_classification_correct = "CORRECT"
                    else:
                        updated_classification_correct = "WRONG"
                
                # Add result with both original and updated predictions
                results.append([
                    image_path,
                    filename,
                    ground_truth_category,
                    notes,
                    original_clip_category,
                    original_clip_confidence,
                    original_clip_description,
                    classification_correct,
                    updated_clip_category,
                    updated_clip_confidence,
                    updated_clip_description,
                    updated_classification_correct,
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                ])
                
                print(f"  Original CLIP: {original_clip_category}")
                print(f"  Updated CLIP: {updated_clip_category} ({updated_clip_confidence})")
                if ground_truth_category:
                    print(f"  Ground Truth: {ground_truth_category}")
                    print(f"  Updated Result: {updated_classification_correct}")
                
            except Exception as e:
                print(f"  Error processing image: {e}")
                results.append([
                    image_path,
                    filename,
                    ground_truth_category,
                    notes,
                    original_clip_category,
                    original_clip_confidence,
                    original_clip_description,
                    classification_correct,
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
            # Write header with both original and updated columns
            writer.writerow([
                'Image Path',
                'Filename',
                'Ground_Truth_Category',
                'Notes',
                'Original CLIP Category',
                'Original CLIP Confidence',
                'Original CLIP Description',
                'Original Classification_Correct',
                'Updated CLIP Category',
                'Updated CLIP Confidence',
                'Updated CLIP Description',
                'Updated Classification_Correct',
                'Timestamp'
            ])
            # Write all results
            writer.writerows(results)
        
        # Calculate and display accuracy comparison
        # Count only images with ground truth and a clear CORRECT/WRONG assessment
        images_with_assessment = []
        original_correct = 0
        updated_correct = 0
        
        for result in results:
            ground_truth = result[2]
            original_assessment = result[7]
            updated_assessment = result[11]
            
            # Only count images with ground truth and clear assessment
            if ground_truth and ground_truth.strip():
                if original_assessment == "CORRECT":
                    original_correct += 1
                if updated_assessment == "CORRECT":
                    updated_correct += 1
                if original_assessment in ["CORRECT", "WRONG"] or updated_assessment in ["CORRECT", "WRONG"]:
                    images_with_assessment.append(result)
        
        total_with_assessment = len(images_with_assessment)
        
        print(f"\nClassification Results Comparison:")
        print(f"Total images processed: {len(results)}")
        print(f"Images with ground truth and assessment: {total_with_assessment}")
        
        if total_with_assessment > 0:
            original_accuracy = (original_correct / total_with_assessment) * 100
            updated_accuracy = (updated_correct / total_with_assessment) * 100
            
            print(f"Original CLIP accuracy: {original_correct}/{total_with_assessment} = {original_accuracy:.2f}%")
            print(f"Updated CLIP accuracy: {updated_correct}/{total_with_assessment} = {updated_accuracy:.2f}%")
            
            improvement = updated_accuracy - original_accuracy
            print(f"Improvement: {improvement:.2f} percentage points")
            
            # List images where classification changed
            print("\nClassification Changes:")
            changes = 0
            improvements = 0
            regressions = 0
            
            for result in images_with_assessment:
                original_category = result[4]
                updated_category = result[8]
                ground_truth = result[2]
                filename = result[1]
                
                if original_category != updated_category:
                    changes += 1
                    change_type = ""
                    
                    # Normalize ground truth for comparison
                    ground_truth_normalized = ground_truth.replace("TABLE + TELLTALES", "TABLE WITH TELLTALES")
                    ground_truth_normalized = ground_truth_normalized.replace("COLOR && GRADIENTS", "COLOR AND GRADIENTS")
                    ground_truth_normalized = ground_truth_normalized.replace("TECHNICAL SPEC", "TECHNICAL SPECIFICATIONS")
                    ground_truth_normalized = ground_truth_normalized.replace("HMI DISPLAY LAYOUT", "HMI DISPLAY LAYOUTS")
                    ground_truth_normalized = ground_truth_normalized.replace("CONFIG TABLE", "CONFIGURATION TABLES")
                    
                    # Check if it's an improvement or regression
                    if original_category == ground_truth_normalized and updated_category != ground_truth_normalized:
                        change_type = "REGRESSION"
                        regressions += 1
                    elif original_category != ground_truth_normalized and updated_category == ground_truth_normalized:
                        change_type = "IMPROVEMENT"
                        improvements += 1
                    else:
                        change_type = "CHANGE"
                    
                    print(f"  {filename}: {original_category} -> {updated_category} ({change_type})")
            
            print(f"\nTotal classification changes: {changes}")
            print(f"Improvements: {improvements}")
            print(f"Regressions: {regressions}")
        
        print(f"\nResults saved to: {output_file}")
        print("File structure matches original with added updated CLIP columns")
        
    except Exception as e:
        print(f"Error reading input file: {e}")
        return

def main():
    """
    Main function to process additional images with updated CLIP classifier
    """
    print("=" * 70)
    print("Process Additional Images with Updated CLIP Classifier")
    print("=" * 70)
    
    process_additional_images_with_updated_clip()
    
    print("\nProcess completed!")

if __name__ == "__main__":
    main()
