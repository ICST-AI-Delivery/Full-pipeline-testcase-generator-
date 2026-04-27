"""
Accuracy Evaluation Tool
Compares ground truth labels with classifier predictions and generates accuracy metrics
"""

import csv
import pandas as pd
from collections import defaultdict, Counter
import numpy as np

def load_ground_truth(ground_truth_file):
    """Load ground truth labels from CSV file"""
    ground_truth = {}
    
    try:
        with open(ground_truth_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                image_path = row['Image Path']
                true_category = row['Ground_Truth_Category'].strip()
                if true_category:  # Only include rows with ground truth labels
                    ground_truth[image_path] = true_category
        
        print(f"Loaded {len(ground_truth)} ground truth labels")
        return ground_truth
    
    except FileNotFoundError:
        print(f"Error: Ground truth file '{ground_truth_file}' not found")
        return {}
    except Exception as e:
        print(f"Error loading ground truth: {e}")
        return {}

def load_predictions(predictions_file):
    """Load classifier predictions from CSV file"""
    predictions = {}
    
    try:
        with open(predictions_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                image_path = row['Image Path']
                clip_pred = row.get('CLIP Category', 'N/A')
                cv_pred = row.get('CV Category', 'N/A')
                predictions[image_path] = {
                    'CLIP': clip_pred,
                    'CV': cv_pred
                }
        
        print(f"Loaded predictions for {len(predictions)} images")
        return predictions
    
    except FileNotFoundError:
        print(f"Error: Predictions file '{predictions_file}' not found")
        return {}
    except Exception as e:
        print(f"Error loading predictions: {e}")
        return {}

def calculate_accuracy(ground_truth, predictions, classifier_name):
    """Calculate accuracy metrics for a specific classifier"""
    
    correct = 0
    total = 0
    category_stats = defaultdict(lambda: {'correct': 0, 'total': 0, 'predictions': []})
    
    for image_path, true_category in ground_truth.items():
        if image_path in predictions:
            pred_category = predictions[image_path][classifier_name]
            
            if pred_category != 'N/A' and pred_category != 'Error':
                total += 1
                category_stats[true_category]['total'] += 1
                category_stats[true_category]['predictions'].append(pred_category)
                
                if pred_category == true_category:
                    correct += 1
                    category_stats[true_category]['correct'] += 1
    
    overall_accuracy = (correct / total * 100) if total > 0 else 0
    
    return overall_accuracy, category_stats, correct, total

def create_confusion_matrix(ground_truth, predictions, classifier_name):
    """Create confusion matrix for the classifier"""
    
    # Get all unique categories
    all_categories = set(ground_truth.values())
    for image_path in ground_truth:
        if image_path in predictions:
            pred_cat = predictions[image_path][classifier_name]
            if pred_cat not in ['N/A', 'Error']:
                all_categories.add(pred_cat)
    
    all_categories = sorted(list(all_categories))
    
    # Initialize confusion matrix
    confusion_matrix = defaultdict(lambda: defaultdict(int))
    
    # Fill confusion matrix
    for image_path, true_category in ground_truth.items():
        if image_path in predictions:
            pred_category = predictions[image_path][classifier_name]
            if pred_category not in ['N/A', 'Error']:
                confusion_matrix[true_category][pred_category] += 1
    
    return confusion_matrix, all_categories

def print_results(classifier_name, accuracy, category_stats, correct, total):
    """Print detailed results for a classifier"""
    
    print(f"\n{'='*60}")
    print(f"{classifier_name.upper()} CLASSIFIER RESULTS")
    print(f"{'='*60}")
    print(f"Overall Accuracy: {accuracy:.2f}% ({correct}/{total})")
    
    print(f"\nPer-Category Results:")
    print(f"{'Category':<35} {'Accuracy':<10} {'Correct/Total'}")
    print("-" * 60)
    
    for category in sorted(category_stats.keys()):
        stats = category_stats[category]
        cat_accuracy = (stats['correct'] / stats['total'] * 100) if stats['total'] > 0 else 0
        print(f"{category:<35} {cat_accuracy:>7.1f}% {stats['correct']:>6}/{stats['total']:<6}")
    
    # Show most common misclassifications
    print(f"\nMost Common Misclassifications:")
    misclassifications = Counter()
    
    for category, stats in category_stats.items():
        for pred in stats['predictions']:
            if pred != category:
                misclassifications[(category, pred)] += 1
    
    if misclassifications:
        for (true_cat, pred_cat), count in misclassifications.most_common(5):
            print(f"  {true_cat} → {pred_cat}: {count} times")
    else:
        print("  No misclassifications found!")

def save_detailed_results(ground_truth, predictions, output_file="accuracy_analysis.csv"):
    """Save detailed comparison results to CSV"""
    
    results = []
    
    for image_path, true_category in ground_truth.items():
        if image_path in predictions:
            clip_pred = predictions[image_path]['CLIP']
            cv_pred = predictions[image_path]['CV']
            
            clip_correct = "Yes" if clip_pred == true_category else "No"
            cv_correct = "Yes" if cv_pred == true_category else "No"
            
            results.append({
                'Image Path': image_path,
                'Filename': image_path.split('/')[-1],
                'Ground Truth': true_category,
                'CLIP Prediction': clip_pred,
                'CLIP Correct': clip_correct,
                'CV Prediction': cv_pred,
                'CV Correct': cv_correct,
                'Both Correct': "Yes" if clip_correct == "Yes" and cv_correct == "Yes" else "No"
            })
    
    # Save to CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        if results:
            writer = csv.DictWriter(file, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)
    
    print(f"\nDetailed results saved to: {output_file}")

def main():
    """Main evaluation function"""
    
    print("ACCURACY EVALUATION TOOL")
    print("=" * 60)
    
    # File paths
    ground_truth_file = "ground_truth_template.csv"  # User should fill this in
    predictions_file = "complete_image_inventory.csv"
    
    # Load data
    ground_truth = load_ground_truth(ground_truth_file)
    predictions = load_predictions(predictions_file)
    
    if not ground_truth:
        print("\nError: No ground truth labels found.")
        print("Please fill in the 'Ground_Truth_Category' column in ground_truth_template.csv")
        return
    
    if not predictions:
        print("\nError: No predictions found.")
        print("Please ensure complete_image_inventory.csv exists with classifier predictions")
        return
    
    # Calculate accuracy for both classifiers
    clip_accuracy, clip_stats, clip_correct, clip_total = calculate_accuracy(
        ground_truth, predictions, 'CLIP'
    )
    
    cv_accuracy, cv_stats, cv_correct, cv_total = calculate_accuracy(
        ground_truth, predictions, 'CV'
    )
    
    # Print results
    print_results("CLIP", clip_accuracy, clip_stats, clip_correct, clip_total)
    print_results("CV", cv_accuracy, cv_stats, cv_correct, cv_total)
    
    # Comparison summary
    print(f"\n{'='*60}")
    print("COMPARISON SUMMARY")
    print(f"{'='*60}")
    print(f"CLIP Accuracy: {clip_accuracy:.2f}%")
    print(f"CV Accuracy:   {cv_accuracy:.2f}%")
    
    if clip_accuracy > cv_accuracy:
        print(f"CLIP performs better by {clip_accuracy - cv_accuracy:.2f} percentage points")
    elif cv_accuracy > clip_accuracy:
        print(f"CV performs better by {cv_accuracy - clip_accuracy:.2f} percentage points")
    else:
        print("Both classifiers perform equally well")
    
    # Save detailed results
    save_detailed_results(ground_truth, predictions)
    
    print(f"\nEvaluation complete!")

if __name__ == "__main__":
    main()
