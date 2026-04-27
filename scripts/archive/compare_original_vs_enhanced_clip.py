"""
Compare Original CLIP vs Enhanced CLIP performance on ground truth dataset
"""

import os
import csv
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def normalize_category(category):
    """Normalize category names for comparison"""
    if not category:
        return ""
    
    category = category.strip().upper()
    
    # Handle common variations
    if category == "TELLTALES ICONS &INDICATORS":
        return "TELLTALE ICONS & INDICATORS"
    if category == "PROCESS FLOW DIAGRAM":
        return "PROCESS FLOW DIAGRAMS"
    if category == "TECHNCAL SPECIFICATIONS":
        return "TECHNICAL SPECIFICATIONS"
    if category == "SYSTEM ARCHITECTURE":
        return "SYSTEM ARCHITECTURE DIAGRAMS"
    if category == "TABLE  + TELLTALES":
        return "TABLE + TELLTALES"
    
    return category

def calculate_metrics(ground_truth, predictions):
    """Calculate classification metrics"""
    if not predictions:
        return {'accuracy': 0.0, 'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'count': 0}
    
    # Get common image paths
    common_paths = set(ground_truth.keys()) & set(predictions.keys())
    if not common_paths:
        return {'accuracy': 0.0, 'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'count': 0}
    
    # Prepare lists for metrics calculation
    y_true = []
    y_pred = []
    
    for path in common_paths:
        true_category = normalize_category(ground_truth[path])
        pred_category = normalize_category(predictions[path])
        
        if true_category:  # Only include if ground truth exists
            y_true.append(true_category)
            y_pred.append(pred_category)
    
    if not y_true:
        return {'accuracy': 0.0, 'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'count': 0}
    
    try:
        accuracy = accuracy_score(y_true, y_pred)
        precision = precision_score(y_true, y_pred, average='weighted', zero_division=0)
        recall = recall_score(y_true, y_pred, average='weighted', zero_division=0)
        f1 = f1_score(y_true, y_pred, average='weighted', zero_division=0)
        
        return {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1': f1,
            'count': len(y_true)
        }
    except Exception as e:
        print(f"Error calculating metrics: {e}")
        return {'accuracy': 0.0, 'precision': 0.0, 'recall': 0.0, 'f1': 0.0, 'count': len(y_true)}

def load_comparison_data():
    """Load and merge all CLIP comparison data"""
    
    # Load original CLIP results
    original_clip_path = "data_files/ground_truth_template_original_clip.csv"
    enhanced_clip_path = "data_files/ground_truth_template_enhanced_clip.csv"
    
    merged_data = {}
    ground_truth = {}
    original_clip_predictions = {}
    enhanced_clip_predictions = {}
    
    # Load original CLIP results
    if os.path.exists(original_clip_path):
        with open(original_clip_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)
            
            # Find column indices
            original_clip_idx = header.index('Original CLIP Category') if 'Original CLIP Category' in header else -1
            
            for row in reader:
                if len(row) > 0:
                    image_path = row[0]
                    ground_truth_cat = row[2] if len(row) > 2 else ''
                    
                    if ground_truth_cat.strip():
                        ground_truth[image_path] = ground_truth_cat
                    
                    if original_clip_idx >= 0 and original_clip_idx < len(row):
                        original_clip_predictions[image_path] = row[original_clip_idx]
                    
                    merged_data[image_path] = {
                        'Image Path': row[0],
                        'Image Name': row[1] if len(row) > 1 else '',
                        'Ground Truth Category': ground_truth_cat,
                        'Original CLIP Category': row[original_clip_idx] if original_clip_idx >= 0 and original_clip_idx < len(row) else '',
                        'Original CLIP Confidence': row[original_clip_idx + 1] if original_clip_idx >= 0 and original_clip_idx + 1 < len(row) else ''
                    }
    
    # Load enhanced CLIP results
    if os.path.exists(enhanced_clip_path):
        with open(enhanced_clip_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)
            
            # Find column indices
            enhanced_clip_idx = header.index('Enhanced CLIP Category') if 'Enhanced CLIP Category' in header else -1
            
            for row in reader:
                if len(row) > 0:
                    image_path = row[0]
                    
                    if enhanced_clip_idx >= 0 and enhanced_clip_idx < len(row):
                        enhanced_clip_predictions[image_path] = row[enhanced_clip_idx]
                    
                    if image_path in merged_data:
                        merged_data[image_path]['Enhanced CLIP Category'] = row[enhanced_clip_idx] if enhanced_clip_idx >= 0 and enhanced_clip_idx < len(row) else ''
                        merged_data[image_path]['Enhanced CLIP Confidence'] = row[enhanced_clip_idx + 1] if enhanced_clip_idx >= 0 and enhanced_clip_idx + 1 < len(row) else ''
    
    return ground_truth, original_clip_predictions, enhanced_clip_predictions, merged_data

def analyze_differences(ground_truth, original_predictions, enhanced_predictions):
    """Analyze specific differences between original and enhanced CLIP"""
    
    print("\nDETAILED COMPARISON ANALYSIS:")
    print("=" * 80)
    
    # Find cases where predictions differ
    different_predictions = []
    original_correct = 0
    enhanced_correct = 0
    both_correct = 0
    both_wrong = 0
    
    for path in ground_truth.keys():
        if path in original_predictions and path in enhanced_predictions:
            gt_norm = normalize_category(ground_truth[path])
            orig_norm = normalize_category(original_predictions[path])
            enh_norm = normalize_category(enhanced_predictions[path])
            
            orig_correct = (gt_norm == orig_norm)
            enh_correct = (gt_norm == enh_norm)
            
            if orig_correct and enh_correct:
                both_correct += 1
            elif orig_correct and not enh_correct:
                original_correct += 1
                different_predictions.append({
                    'path': path,
                    'ground_truth': gt_norm,
                    'original': orig_norm,
                    'enhanced': enh_norm,
                    'type': 'Original correct, Enhanced wrong'
                })
            elif not orig_correct and enh_correct:
                enhanced_correct += 1
                different_predictions.append({
                    'path': path,
                    'ground_truth': gt_norm,
                    'original': orig_norm,
                    'enhanced': enh_norm,
                    'type': 'Enhanced correct, Original wrong'
                })
            else:
                both_wrong += 1
                if orig_norm != enh_norm:  # Different wrong answers
                    different_predictions.append({
                        'path': path,
                        'ground_truth': gt_norm,
                        'original': orig_norm,
                        'enhanced': enh_norm,
                        'type': 'Both wrong, different answers'
                    })
    
    print(f"Both correct: {both_correct}")
    print(f"Only Original correct: {original_correct}")
    print(f"Only Enhanced correct: {enhanced_correct}")
    print(f"Both wrong: {both_wrong}")
    
    print(f"\nCases where predictions differ ({len(different_predictions)} cases):")
    print("-" * 80)
    
    for diff in different_predictions:
        print(f"\nImage: {diff['path']}")
        print(f"Ground Truth: {diff['ground_truth']}")
        print(f"Original CLIP: {diff['original']}")
        print(f"Enhanced CLIP: {diff['enhanced']}")
        print(f"Analysis: {diff['type']}")

def main():
    """Main comparison function"""
    
    print("ORIGINAL CLIP vs ENHANCED CLIP COMPARISON")
    print("=" * 60)
    
    # Load data
    ground_truth, original_predictions, enhanced_predictions, merged_data = load_comparison_data()
    
    if not ground_truth:
        print("No ground truth data found!")
        return
    
    # Calculate metrics
    original_metrics = calculate_metrics(ground_truth, original_predictions)
    enhanced_metrics = calculate_metrics(ground_truth, enhanced_predictions)
    
    # Print comparison results
    print(f"\nPERFORMANCE COMPARISON:")
    print("-" * 60)
    print(f"{'Metric':<15} {'Original CLIP':<15} {'Enhanced CLIP':<15} {'Difference':<15}")
    print("-" * 60)
    
    accuracy_diff = enhanced_metrics['accuracy'] - original_metrics['accuracy']
    precision_diff = enhanced_metrics['precision'] - original_metrics['precision']
    recall_diff = enhanced_metrics['recall'] - original_metrics['recall']
    f1_diff = enhanced_metrics['f1'] - original_metrics['f1']
    
    print(f"{'Accuracy':<15} {original_metrics['accuracy']:.4f}          {enhanced_metrics['accuracy']:.4f}          {accuracy_diff:+.4f}")
    print(f"{'Precision':<15} {original_metrics['precision']:.4f}          {enhanced_metrics['precision']:.4f}          {precision_diff:+.4f}")
    print(f"{'Recall':<15} {original_metrics['recall']:.4f}          {enhanced_metrics['recall']:.4f}          {recall_diff:+.4f}")
    print(f"{'F1 Score':<15} {original_metrics['f1']:.4f}          {enhanced_metrics['f1']:.4f}          {f1_diff:+.4f}")
    print(f"{'Images':<15} {original_metrics['count']:<15} {enhanced_metrics['count']:<15}")
    
    # Calculate percentage change
    if original_metrics['accuracy'] > 0:
        accuracy_change = (accuracy_diff / original_metrics['accuracy']) * 100
        print(f"\nAccuracy change: {accuracy_change:+.2f}%")
        
        if accuracy_change < 0:
            print("⚠️  WARNING: Enhanced prompts REDUCED accuracy!")
        else:
            print("✅ Enhanced prompts improved accuracy")
    
    # Detailed analysis
    analyze_differences(ground_truth, original_predictions, enhanced_predictions)
    
    # Save comprehensive comparison
    output_path = "data_files/clip_comparison_results.csv"
    with open(output_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write header
        header = ['Image Path', 'Image Name', 'Ground Truth Category',
                 'Original CLIP Category', 'Original CLIP Confidence',
                 'Enhanced CLIP Category', 'Enhanced CLIP Confidence',
                 'Original Correct', 'Enhanced Correct', 'Agreement']
        writer.writerow(header)
        
        # Write data
        for path, data in merged_data.items():
            gt_norm = normalize_category(data.get('Ground Truth Category', ''))
            orig_norm = normalize_category(data.get('Original CLIP Category', ''))
            enh_norm = normalize_category(data.get('Enhanced CLIP Category', ''))
            
            orig_correct = 'Yes' if gt_norm and gt_norm == orig_norm else 'No'
            enh_correct = 'Yes' if gt_norm and gt_norm == enh_norm else 'No'
            agreement = 'Yes' if orig_norm == enh_norm else 'No'
            
            row = [
                data.get('Image Path', ''),
                data.get('Image Name', ''),
                data.get('Ground Truth Category', ''),
                data.get('Original CLIP Category', ''),
                data.get('Original CLIP Confidence', ''),
                data.get('Enhanced CLIP Category', ''),
                data.get('Enhanced CLIP Confidence', ''),
                orig_correct,
                enh_correct,
                agreement
            ]
            writer.writerow(row)
    
    print(f"\nDetailed comparison saved to: {output_path}")

if __name__ == "__main__":
    main()
