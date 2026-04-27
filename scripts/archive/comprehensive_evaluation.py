"""
Comprehensive evaluation script to compare all classifiers against ground truth
"""

import os
import csv
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

def load_ground_truth(csv_path):
    """Load ground truth data from CSV"""
    ground_truth = {}
    with open(csv_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if len(row) >= 3 and row[2].strip():
                image_path = row[0]
                category = row[2].strip()
                ground_truth[image_path] = category
    
    print(f"Loaded {len(ground_truth)} ground truth entries")
    return ground_truth

def merge_classification_results():
    """Merge all classification results into one comprehensive dataset"""
    base_path = "data_files/ground_truth_template"
    files_to_merge = [
        f"{base_path}.csv",  # Original with ground truth
        f"{base_path}_siglip.csv",  # Original SigLIP results
        f"{base_path}_enhanced_clip.csv",  # Enhanced CLIP results
        f"{base_path}_enhanced_siglip.csv"  # Enhanced SigLIP results
    ]
    
    # Start with the base file
    merged_data = {}
    
    # Load base file with ground truth
    if os.path.exists(files_to_merge[0]):
        with open(files_to_merge[0], 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                if len(row) > 0:
                    image_path = row[0]
                    merged_data[image_path] = {
                        'Image Path': row[0],
                        'Image Name': row[1] if len(row) > 1 else '',
                        'Ground Truth Category': row[2] if len(row) > 2 else '',
                        'Notes': row[3] if len(row) > 3 else ''
                    }
    
    # Add SigLIP results
    if os.path.exists(files_to_merge[1]):
        with open(files_to_merge[1], 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)
            siglip_idx = header.index('SigLIP Category') if 'SigLIP Category' in header else -1
            siglip_conf_idx = header.index('SigLIP Confidence') if 'SigLIP Confidence' in header else -1
            
            for row in reader:
                if len(row) > 0:
                    image_path = row[0]
                    if image_path in merged_data:
                        if siglip_idx >= 0 and siglip_idx < len(row):
                            merged_data[image_path]['SigLIP Category'] = row[siglip_idx]
                        if siglip_conf_idx >= 0 and siglip_conf_idx < len(row):
                            merged_data[image_path]['SigLIP Confidence'] = row[siglip_conf_idx]
    
    # Add Enhanced CLIP results
    if os.path.exists(files_to_merge[2]):
        with open(files_to_merge[2], 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)
            clip_idx = header.index('Enhanced CLIP Category') if 'Enhanced CLIP Category' in header else -1
            clip_conf_idx = header.index('Enhanced CLIP Confidence') if 'Enhanced CLIP Confidence' in header else -1
            
            for row in reader:
                if len(row) > 0:
                    image_path = row[0]
                    if image_path in merged_data:
                        if clip_idx >= 0 and clip_idx < len(row):
                            merged_data[image_path]['Enhanced CLIP Category'] = row[clip_idx]
                        if clip_conf_idx >= 0 and clip_conf_idx < len(row):
                            merged_data[image_path]['Enhanced CLIP Confidence'] = row[clip_conf_idx]
    
    # Add Enhanced SigLIP results
    if os.path.exists(files_to_merge[3]):
        with open(files_to_merge[3], 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)
            siglip_enh_idx = header.index('Enhanced SigLIP Category') if 'Enhanced SigLIP Category' in header else -1
            siglip_enh_conf_idx = header.index('Enhanced SigLIP Confidence') if 'Enhanced SigLIP Confidence' in header else -1
            
            for row in reader:
                if len(row) > 0:
                    image_path = row[0]
                    if image_path in merged_data:
                        if siglip_enh_idx >= 0 and siglip_enh_idx < len(row):
                            merged_data[image_path]['Enhanced SigLIP Category'] = row[siglip_enh_idx]
                        if siglip_enh_conf_idx >= 0 and siglip_enh_conf_idx < len(row):
                            merged_data[image_path]['Enhanced SigLIP Confidence'] = row[siglip_enh_conf_idx]
    
    return merged_data

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

def evaluate_all_classifiers():
    """Evaluate all classifiers comprehensively"""
    # Merge all results
    merged_data = merge_classification_results()
    
    if not merged_data:
        print("No data found to evaluate")
        return
    
    # Extract ground truth and predictions
    ground_truth = {}
    siglip_predictions = {}
    enhanced_clip_predictions = {}
    enhanced_siglip_predictions = {}
    
    for path, data in merged_data.items():
        if data.get('Ground Truth Category'):
            ground_truth[path] = data['Ground Truth Category']
        
        if data.get('SigLIP Category'):
            siglip_predictions[path] = data['SigLIP Category']
        
        if data.get('Enhanced CLIP Category'):
            enhanced_clip_predictions[path] = data['Enhanced CLIP Category']
        
        if data.get('Enhanced SigLIP Category'):
            enhanced_siglip_predictions[path] = data['Enhanced SigLIP Category']
    
    # Calculate metrics
    siglip_metrics = calculate_metrics(ground_truth, siglip_predictions)
    enhanced_clip_metrics = calculate_metrics(ground_truth, enhanced_clip_predictions)
    enhanced_siglip_metrics = calculate_metrics(ground_truth, enhanced_siglip_predictions)
    
    # Print comprehensive results
    print("\n" + "="*100)
    print("COMPREHENSIVE CLASSIFIER EVALUATION RESULTS")
    print("="*100)
    print(f"Total images with ground truth: {len(ground_truth)}")
    print(f"SigLIP predictions available: {len(siglip_predictions)}")
    print(f"Enhanced CLIP predictions available: {len(enhanced_clip_predictions)}")
    print(f"Enhanced SigLIP predictions available: {len(enhanced_siglip_predictions)}")
    
    print("\nPERFORMANCE METRICS:")
    print("-" * 100)
    print(f"{'Classifier':<20} {'Accuracy':<10} {'Precision':<10} {'Recall':<10} {'F1 Score':<10} {'Evaluated':<10}")
    print("-" * 100)
    
    if siglip_metrics['count'] > 0:
        print(f"{'SigLIP':<20} {siglip_metrics['accuracy']:.4f}     {siglip_metrics['precision']:.4f}     {siglip_metrics['recall']:.4f}     {siglip_metrics['f1']:.4f}     {siglip_metrics['count']}")
    
    if enhanced_clip_metrics['count'] > 0:
        print(f"{'Enhanced CLIP':<20} {enhanced_clip_metrics['accuracy']:.4f}     {enhanced_clip_metrics['precision']:.4f}     {enhanced_clip_metrics['recall']:.4f}     {enhanced_clip_metrics['f1']:.4f}     {enhanced_clip_metrics['count']}")
    
    if enhanced_siglip_metrics['count'] > 0:
        print(f"{'Enhanced SigLIP':<20} {enhanced_siglip_metrics['accuracy']:.4f}     {enhanced_siglip_metrics['precision']:.4f}     {enhanced_siglip_metrics['recall']:.4f}     {enhanced_siglip_metrics['f1']:.4f}     {enhanced_siglip_metrics['count']}")
    
    print("-" * 100)
    
    # Calculate improvements
    if siglip_metrics['count'] > 0 and enhanced_siglip_metrics['count'] > 0:
        siglip_improvement = (enhanced_siglip_metrics['accuracy'] - siglip_metrics['accuracy']) / siglip_metrics['accuracy'] * 100 if siglip_metrics['accuracy'] > 0 else 0
        print(f"SigLIP Enhancement Improvement: {siglip_improvement:.2f}% accuracy gain")
    
    # Save comprehensive results
    output_path = "data_files/comprehensive_evaluation_results.csv"
    with open(output_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write header
        header = ['Image Path', 'Image Name', 'Ground Truth Category', 'Notes',
                 'SigLIP Category', 'SigLIP Confidence',
                 'Enhanced CLIP Category', 'Enhanced CLIP Confidence',
                 'Enhanced SigLIP Category', 'Enhanced SigLIP Confidence']
        writer.writerow(header)
        
        # Write data
        for path, data in merged_data.items():
            row = [
                data.get('Image Path', ''),
                data.get('Image Name', ''),
                data.get('Ground Truth Category', ''),
                data.get('Notes', ''),
                data.get('SigLIP Category', ''),
                data.get('SigLIP Confidence', ''),
                data.get('Enhanced CLIP Category', ''),
                data.get('Enhanced CLIP Confidence', ''),
                data.get('Enhanced SigLIP Category', ''),
                data.get('Enhanced SigLIP Confidence', '')
            ]
            writer.writerow(row)
    
    print(f"\nComprehensive results saved to: {output_path}")
    
    # Detailed analysis
    print("\nDETAILED ANALYSIS:")
    print("-" * 50)
    
    # Find best performing classifier
    best_accuracy = 0
    best_classifier = ""
    
    for name, metrics in [("SigLIP", siglip_metrics), ("Enhanced CLIP", enhanced_clip_metrics), ("Enhanced SigLIP", enhanced_siglip_metrics)]:
        if metrics['count'] > 0 and metrics['accuracy'] > best_accuracy:
            best_accuracy = metrics['accuracy']
            best_classifier = name
    
    if best_classifier:
        print(f"Best performing classifier: {best_classifier} ({best_accuracy:.4f} accuracy)")
    
    # Category-wise analysis
    print("\nCATEGORY DISTRIBUTION IN GROUND TRUTH:")
    category_counts = {}
    for category in ground_truth.values():
        norm_cat = normalize_category(category)
        category_counts[norm_cat] = category_counts.get(norm_cat, 0) + 1
    
    for category, count in sorted(category_counts.items()):
        print(f"  {category}: {count} images")
    
    return {
        'SigLIP': siglip_metrics,
        'Enhanced CLIP': enhanced_clip_metrics,
        'Enhanced SigLIP': enhanced_siglip_metrics,
        'merged_data': merged_data
    }

if __name__ == "__main__":
    evaluate_all_classifiers()
