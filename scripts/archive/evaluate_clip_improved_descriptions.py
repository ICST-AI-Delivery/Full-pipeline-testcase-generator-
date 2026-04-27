"""
Evaluate CLIP Classifier with Improved Descriptions on Ground Truth Template Images
Runs CLIP classification using the updated improved category descriptions
and compares predictions with ground truth labels to calculate accuracy.
"""

import os
import csv
import pandas as pd
from datetime import datetime
from clip_classifier import CLIPImageClassifier
import re

def normalize_category_name(category):
    """
    Normalize category names for comparison by removing extra spaces,
    standardizing punctuation, and handling common variations.
    """
    if not category or pd.isna(category):
        return ""
    
    # Convert to uppercase and strip whitespace
    normalized = str(category).upper().strip()
    
    # Remove extra whitespace and newlines
    normalized = re.sub(r'\s+', ' ', normalized)
    
    # Handle common variations and updated category names
    normalized = normalized.replace('TELLTALES ICONS', 'TELLTALE ICONS')
    normalized = normalized.replace('&&', '&')
    normalized = normalized.replace('TECHNCAL', 'TECHNICAL')
    normalized = normalized.replace('CONFIGURATION TABLE', 'CONFIGURATION TABLES')
    normalized = normalized.replace('TABLE  +', 'TABLE +')
    
    # Handle new category name mappings
    normalized = normalized.replace('TABLE + TELLTALES', 'TABLE WITH TELLTALES')
    normalized = normalized.replace('COLOR & GRADIENTS', 'COLOR AND GRADIENTS')
    normalized = normalized.replace('COLOR && GRADIENTS', 'COLOR AND GRADIENTS')
    
    return normalized

def calculate_accuracy_metrics(results):
    """
    Calculate detailed accuracy metrics from results.
    """
    total_images = len(results)
    correct_predictions = sum(1 for r in results if r['Correct/Incorrect'] == 'Correct')
    overall_accuracy = (correct_predictions / total_images) * 100 if total_images > 0 else 0
    
    # Per-category accuracy
    category_stats = {}
    for result in results:
        gt_category = result['Ground Truth Category']
        is_correct = result['Correct/Incorrect'] == 'Correct'
        
        if gt_category not in category_stats:
            category_stats[gt_category] = {'total': 0, 'correct': 0}
        
        category_stats[gt_category]['total'] += 1
        if is_correct:
            category_stats[gt_category]['correct'] += 1
    
    # Calculate per-category accuracy
    for category in category_stats:
        stats = category_stats[category]
        stats['accuracy'] = (stats['correct'] / stats['total']) * 100 if stats['total'] > 0 else 0
    
    return {
        'total_images': total_images,
        'correct_predictions': correct_predictions,
        'overall_accuracy': overall_accuracy,
        'category_stats': category_stats
    }

def main():
    """
    Main evaluation function
    """
    print("CLIP Classifier Evaluation with Improved Descriptions")
    print("=" * 60)
    
    # Initialize CLIP classifier (will use the updated improved descriptions)
    print("Initializing CLIP classifier with improved descriptions...")
    classifier = CLIPImageClassifier(device="cpu")  # Use "cuda" if GPU available
    
    # Read ground truth template
    ground_truth_file = "data_files/ground_truth_template.csv"
    if not os.path.exists(ground_truth_file):
        print(f"Error: Ground truth file not found: {ground_truth_file}")
        return
    
    print(f"Reading ground truth data from: {ground_truth_file}")
    df = pd.read_csv(ground_truth_file)
    print(f"Found {len(df)} images to evaluate")
    
    # Process each image
    results = []
    processed_count = 0
    
    for idx, row in df.iterrows():
        image_path = row['Image Path']
        filename = row['Filename']
        ground_truth = row['Ground_Truth_Category']
        notes = row.get('Notes', '')
        
        print(f"\nProcessing {idx + 1}/{len(df)}: {filename}")
        
        # Check if image file exists
        if not os.path.exists(image_path):
            print(f"  Warning: Image file not found: {image_path}")
            result = {
                'Image Path': image_path,
                'Image Name': filename,
                'Ground Truth Category': ground_truth,
                'Notes': notes,
                'CLIP Predicted Category': 'FILE_NOT_FOUND',
                'CLIP Confidence': 'N/A',
                'CLIP Description': 'Image file not found',
                'Correct/Incorrect': 'Error',
                'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
        else:
            # Classify the image
            try:
                predicted_category, confidence, description = classifier.classify_image(image_path)
                
                # Normalize categories for comparison
                normalized_gt = normalize_category_name(ground_truth)
                normalized_pred = normalize_category_name(predicted_category)
                
                # Determine if prediction is correct
                is_correct = normalized_gt == normalized_pred
                correct_incorrect = 'Correct' if is_correct else 'Incorrect'
                
                print(f"  Ground Truth: {ground_truth}")
                print(f"  Predicted: {predicted_category} ({confidence})")
                print(f"  Result: {correct_incorrect}")
                
                result = {
                    'Image Path': image_path,
                    'Image Name': filename,
                    'Ground Truth Category': ground_truth,
                    'Notes': notes,
                    'CLIP Predicted Category': predicted_category,
                    'CLIP Confidence': confidence,
                    'CLIP Description': description,
                    'Correct/Incorrect': correct_incorrect,
                    'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                processed_count += 1
                
            except Exception as e:
                print(f"  Error processing image: {e}")
                result = {
                    'Image Path': image_path,
                    'Image Name': filename,
                    'Ground Truth Category': ground_truth,
                    'Notes': notes,
                    'CLIP Predicted Category': 'ERROR',
                    'CLIP Confidence': 'N/A',
                    'CLIP Description': f'Error: {str(e)}',
                    'Correct/Incorrect': 'Error',
                    'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
        
        results.append(result)
    
    # Save results to CSV with descriptive filename
    output_file = f"data_files/clip_ground_truth_evaluation_results_improved_descriptions.csv"
    print(f"\nSaving results to: {output_file}")
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Image Path', 'Image Name', 'Ground Truth Category', 'Notes',
                     'CLIP Predicted Category', 'CLIP Confidence', 'CLIP Description',
                     'Correct/Incorrect', 'Timestamp']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    
    # Calculate and display accuracy metrics
    print("\n" + "=" * 60)
    print("EVALUATION RESULTS - IMPROVED DESCRIPTIONS")
    print("=" * 60)
    
    # Filter out error cases for accuracy calculation
    valid_results = [r for r in results if r['Correct/Incorrect'] in ['Correct', 'Incorrect']]
    
    if valid_results:
        metrics = calculate_accuracy_metrics(valid_results)
        
        print(f"Total Images Processed: {processed_count}")
        print(f"Valid Classifications: {len(valid_results)}")
        print(f"Correct Predictions: {metrics['correct_predictions']}")
        print(f"Overall Accuracy: {metrics['overall_accuracy']:.2f}%")
        
        print("\nPer-Category Accuracy:")
        print("-" * 40)
        for category, stats in sorted(metrics['category_stats'].items()):
            print(f"{category}: {stats['correct']}/{stats['total']} ({stats['accuracy']:.1f}%)")
        
        # Show incorrect predictions for analysis
        incorrect_predictions = [r for r in valid_results if r['Correct/Incorrect'] == 'Incorrect']
        if incorrect_predictions:
            print(f"\nIncorrect Predictions ({len(incorrect_predictions)}):")
            print("-" * 60)
            for result in incorrect_predictions:
                print(f"Image: {result['Image Name']}")
                print(f"  Ground Truth: {result['Ground Truth Category']}")
                print(f"  Predicted: {result['CLIP Predicted Category']} ({result['CLIP Confidence']})")
                print()
    
    print(f"\nDetailed results saved to: {output_file}")
    print("Evaluation with improved descriptions complete!")

if __name__ == "__main__":
    main()
