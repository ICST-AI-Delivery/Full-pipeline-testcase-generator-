"""
Run Updated CLIP Classifier on Evaluation Set
Processes all images from additional_images_for_evaluation.csv with new categories
"""

import os
import csv
import pandas as pd
from clip_classifier import CLIPImageClassifier
from datetime import datetime

def load_evaluation_data(csv_path):
    """Load evaluation data from CSV file"""
    df = pd.read_csv(csv_path)
    return df

def run_updated_classification(evaluation_csv_path, output_csv_path):
    """
    Run updated CLIP classifier on evaluation images and calculate accuracy
    
    Args:
        evaluation_csv_path (str): Path to evaluation CSV file
        output_csv_path (str): Path for output CSV file
    """
    print("Loading evaluation data...")
    df = load_evaluation_data(evaluation_csv_path)
    
    print("Initializing updated CLIP classifier...")
    classifier = CLIPImageClassifier(device="cpu")  # Use "cuda" if GPU available
    
    results = []
    correct_predictions = 0
    total_with_ground_truth = 0
    
    print(f"Processing {len(df)} images...")
    
    for idx, row in df.iterrows():
        image_path = row['Image Path']
        filename = row['Filename']
        ground_truth = row['Ground_Truth_Category']
        notes = row['Notes']
        
        print(f"Processing {idx+1}/{len(df)}: {filename}")
        
        # Check if image file exists
        if not os.path.exists(image_path):
            print(f"  Warning: Image not found: {image_path}")
            category = "FILE_NOT_FOUND"
            confidence = "N/A"
            description = "Image file not found"
            is_correct = "N/A"
        else:
            # Classify image with updated classifier
            category, confidence, description = classifier.classify_image(image_path)
            
            # Check accuracy if ground truth is available
            if pd.notna(ground_truth) and ground_truth.strip() != "":
                total_with_ground_truth += 1
                # Normalize category names for comparison
                predicted_normalized = category.upper().strip()
                ground_truth_normalized = ground_truth.upper().strip()
                
                # Handle some common variations
                if ground_truth_normalized == "TELLTALES ICONS & INDICATORS":
                    ground_truth_normalized = "TELLTALE ICONS & INDICATORS"
                if ground_truth_normalized == "TECHNICAL SPEC":
                    ground_truth_normalized = "TECHNICAL SPECIFICATIONS"
                if ground_truth_normalized == "CONFIG TABLE":
                    ground_truth_normalized = "CONFIGURATION TABLES"
                
                is_correct = "CORRECT" if predicted_normalized == ground_truth_normalized else "WRONG"
                if is_correct == "CORRECT":
                    correct_predictions += 1
            else:
                is_correct = "NO_GROUND_TRUTH"
        
        # Prepare result row
        result = {
            'Image Path': image_path,
            'Filename': filename,
            'Ground_Truth_Category': ground_truth,
            'Notes': notes,
            'Updated_CLIP_Category': category,
            'Updated_CLIP_Confidence': confidence,
            'Updated_CLIP_Description': description,
            'Classification_Correct': is_correct,
            'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        results.append(result)
    
    # Save results to CSV
    print(f"Saving results to {output_csv_path}...")
    results_df = pd.DataFrame(results)
    results_df.to_csv(output_csv_path, index=False)
    
    # Calculate and display accuracy
    if total_with_ground_truth > 0:
        accuracy = (correct_predictions / total_with_ground_truth) * 100
        print(f"\n=== ACCURACY RESULTS ===")
        print(f"Total images with ground truth: {total_with_ground_truth}")
        print(f"Correct predictions: {correct_predictions}")
        print(f"Accuracy: {accuracy:.2f}%")
        
        # Show breakdown by category
        print(f"\n=== CATEGORY BREAKDOWN ===")
        category_stats = {}
        for result in results:
            if result['Classification_Correct'] in ['CORRECT', 'WRONG']:
                gt_cat = result['Ground_Truth_Category']
                if pd.notna(gt_cat) and gt_cat.strip() != "":
                    if gt_cat not in category_stats:
                        category_stats[gt_cat] = {'correct': 0, 'total': 0}
                    category_stats[gt_cat]['total'] += 1
                    if result['Classification_Correct'] == 'CORRECT':
                        category_stats[gt_cat]['correct'] += 1
        
        for category, stats in category_stats.items():
            cat_accuracy = (stats['correct'] / stats['total']) * 100 if stats['total'] > 0 else 0
            print(f"{category}: {stats['correct']}/{stats['total']} ({cat_accuracy:.1f}%)")
    else:
        print("No ground truth labels found for accuracy calculation")
    
    print(f"\nResults saved to: {output_csv_path}")
    return results_df

def main():
    """Main execution function"""
    evaluation_csv = "data_files/additional_images_for_evaluation.csv"
    output_csv = "data_files/updated_clip_evaluation_results.csv"
    
    if not os.path.exists(evaluation_csv):
        print(f"Error: Evaluation file not found: {evaluation_csv}")
        return
    
    print("Starting updated CLIP evaluation...")
    results_df = run_updated_classification(evaluation_csv, output_csv)
    print("Evaluation complete!")

if __name__ == "__main__":
    main()
