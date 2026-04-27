"""
Evaluate Original CLIP Classifier Performance
Run original CLIP classifier on ground truth dataset and calculate accuracy
"""

import csv
import pandas as pd
from collections import defaultdict
import sys
import os

# Add the scripts directory to the path to import the classifier
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from clip_classifier import CLIPImageClassifier

def run_original_clip_on_ground_truth():
    """
    Run original CLIP classifier on ground truth dataset
    """
    # Initialize the original CLIP classifier
    print("Initializing Original CLIP Classifier...")
    classifier = CLIPImageClassifier(device="cpu")
    
    # Read ground truth data
    ground_truth_path = "data_files/ground_truth_template.csv"
    
    try:
        df = pd.read_csv(ground_truth_path)
        print(f"Loaded ground truth dataset with {len(df)} images")
        
        # Process each image
        results = []
        for idx, row in df.iterrows():
            image_path = row['Image Path']
            filename = row['Filename']
            ground_truth = row['Ground_Truth_Category']
            notes = row.get('Notes', '')
            
            print(f"Processing {idx+1}/{len(df)}: {filename}")
            
            # Classify with original CLIP
            category, confidence, description = classifier.classify_image(image_path)
            
            # Store result
            result = {
                'Image Path': image_path,
                'Filename': filename,
                'Ground_Truth_Category': ground_truth,
                'Notes': notes,
                'Original CLIP Category': category,
                'Original CLIP Confidence': confidence,
                'Original CLIP Description': description
            }
            results.append(result)
        
        # Save results to CSV
        output_path = "data_files/ground_truth_template_original_clip.csv"
        results_df = pd.DataFrame(results)
        results_df.to_csv(output_path, index=False)
        print(f"Results saved to: {output_path}")
        
        return results_df
        
    except Exception as e:
        print(f"Error processing ground truth dataset: {e}")
        return None

def evaluate_original_clip_accuracy():
    """
    Evaluate the original CLIP classifier accuracy
    """
    # First run the classifier if results don't exist
    results_path = "data_files/ground_truth_template_original_clip.csv"
    
    if not os.path.exists(results_path):
        print("Running original CLIP classifier on ground truth dataset...")
        df = run_original_clip_on_ground_truth()
        if df is None:
            return
    else:
        print("Loading existing original CLIP results...")
        df = pd.read_csv(results_path)
    
    print("\nOriginal CLIP Classifier Evaluation Report")
    print("=" * 60)
    
    # Get column names
    ground_truth_col = "Ground_Truth_Category"
    original_clip_col = "Original CLIP Category"
    confidence_col = "Original CLIP Confidence"
    
    # Filter out rows with missing ground truth
    df_filtered = df[df[ground_truth_col].notna() & (df[ground_truth_col] != '')]
    
    if len(df_filtered) == 0:
        print("No valid ground truth data found for evaluation")
        return
    
    # Calculate accuracy
    correct_predictions = (df_filtered[ground_truth_col] == df_filtered[original_clip_col]).sum()
    total_predictions = len(df_filtered)
    accuracy = correct_predictions / total_predictions
    
    print(f"Overall Accuracy: {accuracy:.3f} ({correct_predictions}/{total_predictions})")
    print()
    
    # Confidence distribution
    confidence_counts = df_filtered[confidence_col].value_counts()
    print("Confidence Distribution:")
    for conf, count in confidence_counts.items():
        print(f"  {conf}: {count} ({count/total_predictions:.1%})")
    print()
    
    # Accuracy by confidence level
    print("Accuracy by Confidence Level:")
    for conf in ['High', 'Medium', 'Low']:
        if conf in confidence_counts:
            conf_df = df_filtered[df_filtered[confidence_col] == conf]
            conf_correct = (conf_df[ground_truth_col] == conf_df[original_clip_col]).sum()
            conf_total = len(conf_df)
            conf_accuracy = conf_correct / conf_total if conf_total > 0 else 0
            print(f"  {conf}: {conf_accuracy:.3f} ({conf_correct}/{conf_total})")
    print()
    
    # Category-wise performance
    print("Category-wise Performance:")
    print("-" * 40)
    
    category_stats = defaultdict(lambda: {'correct': 0, 'total': 0, 'predicted_as': defaultdict(int)})
    
    for _, row in df_filtered.iterrows():
        true_cat = row[ground_truth_col]
        pred_cat = row[original_clip_col]
        
        category_stats[true_cat]['total'] += 1
        category_stats[true_cat]['predicted_as'][pred_cat] += 1
        
        if true_cat == pred_cat:
            category_stats[true_cat]['correct'] += 1
    
    for category in sorted(category_stats.keys()):
        stats = category_stats[category]
        accuracy = stats['correct'] / stats['total'] if stats['total'] > 0 else 0
        print(f"{category}:")
        print(f"  Accuracy: {accuracy:.3f} ({stats['correct']}/{stats['total']})")
        
        # Show misclassifications
        if stats['correct'] < stats['total']:
            print("  Misclassified as:")
            for pred_cat, count in stats['predicted_as'].items():
                if pred_cat != category and count > 0:
                    print(f"    {pred_cat}: {count}")
        print()
    
    # Detailed results for each image
    print("Detailed Results:")
    print("-" * 60)
    for idx, row in df_filtered.iterrows():
        image_path = row['Image Path']
        true_cat = row[ground_truth_col]
        pred_cat = row[original_clip_col]
        confidence = row[confidence_col]
        
        status = "✓" if true_cat == pred_cat else "✗"
        print(f"{status} {image_path}")
        print(f"  Ground Truth: {true_cat}")
        print(f"  Predicted: {pred_cat} ({confidence})")
        if true_cat != pred_cat:
            print(f"  *** MISMATCH ***")
        print()
    
    return accuracy

if __name__ == "__main__":
    evaluate_original_clip_accuracy()
