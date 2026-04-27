"""
Evaluate Visual-First CLIP Classifier Performance
Compare visual-first approach against ground truth data
"""

import csv
import pandas as pd
from collections import defaultdict

def evaluate_visual_first_classifier():
    """
    Evaluate the visual-first CLIP classifier performance against ground truth
    """
    # Read the results
    csv_path = "data_files/ground_truth_template_visual_first_clip.csv"
    
    try:
        df = pd.read_csv(csv_path)
        print("Visual-First CLIP Classifier Evaluation Report")
        print("=" * 60)
        
        # Get column indices
        ground_truth_col = "Ground_Truth_Category"
        visual_first_col = "Visual-First CLIP Category"
        confidence_col = "Visual-First CLIP Confidence"
        
        if ground_truth_col not in df.columns or visual_first_col not in df.columns:
            print("Error: Required columns not found in CSV")
            return
        
        # Calculate accuracy
        correct_predictions = (df[ground_truth_col] == df[visual_first_col]).sum()
        total_predictions = len(df)
        accuracy = correct_predictions / total_predictions
        
        print(f"Overall Accuracy: {accuracy:.3f} ({correct_predictions}/{total_predictions})")
        print()
        
        # Confidence distribution
        confidence_counts = df[confidence_col].value_counts()
        print("Confidence Distribution:")
        for conf, count in confidence_counts.items():
            print(f"  {conf}: {count} ({count/total_predictions:.1%})")
        print()
        
        # Accuracy by confidence level
        print("Accuracy by Confidence Level:")
        for conf in ['High', 'Medium', 'Low']:
            if conf in confidence_counts:
                conf_df = df[df[confidence_col] == conf]
                conf_correct = (conf_df[ground_truth_col] == conf_df[visual_first_col]).sum()
                conf_total = len(conf_df)
                conf_accuracy = conf_correct / conf_total if conf_total > 0 else 0
                print(f"  {conf}: {conf_accuracy:.3f} ({conf_correct}/{conf_total})")
        print()
        
        # Category-wise performance
        print("Category-wise Performance:")
        print("-" * 40)
        
        category_stats = defaultdict(lambda: {'correct': 0, 'total': 0, 'predicted_as': defaultdict(int)})
        
        for _, row in df.iterrows():
            true_cat = row[ground_truth_col]
            pred_cat = row[visual_first_col]
            
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
        for idx, row in df.iterrows():
            image_path = row['Image Path']
            true_cat = row[ground_truth_col]
            pred_cat = row[visual_first_col]
            confidence = row[confidence_col]
            
            status = "✓" if true_cat == pred_cat else "✗"
            print(f"{status} {image_path}")
            print(f"  Ground Truth: {true_cat}")
            print(f"  Predicted: {pred_cat} ({confidence})")
            if true_cat != pred_cat:
                print(f"  *** MISMATCH ***")
            print()
        
        return accuracy
        
    except Exception as e:
        print(f"Error evaluating classifier: {e}")
        return None

if __name__ == "__main__":
    evaluate_visual_first_classifier()
