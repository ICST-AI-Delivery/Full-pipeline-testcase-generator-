"""
Evaluation script to compare original and enhanced classifiers against ground truth
"""

import os
import csv
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

def load_ground_truth(csv_path):
    """
    Load ground truth data from CSV
    """
    ground_truth = {}
    with open(csv_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if len(row) >= 3 and row[2].strip():  # Check if ground truth category exists
                image_path = row[0]
                category = row[2].strip()
                ground_truth[image_path] = category
    
    print(f"Loaded {len(ground_truth)} ground truth entries")
    return ground_truth

def load_classification_results(csv_path):
    """
    Load classification results from CSV
    """
    results = {}
    with open(csv_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        
        # Find column indices
        clip_idx = header.index('CLIP Category') if 'CLIP Category' in header else -1
        siglip_idx = header.index('SigLIP Category') if 'SigLIP Category' in header else -1
        enhanced_clip_idx = header.index('Enhanced CLIP Category') if 'Enhanced CLIP Category' in header else -1
        enhanced_siglip_idx = header.index('Enhanced SigLIP Category') if 'Enhanced SigLIP Category' in header else -1
        
        for row in reader:
            image_path = row[0]
            result = {}
            
            if clip_idx >= 0 and clip_idx < len(row):
                result['CLIP'] = row[clip_idx]
            
            if siglip_idx >= 0 and siglip_idx < len(row):
                result['SigLIP'] = row[siglip_idx]
            
            if enhanced_clip_idx >= 0 and enhanced_clip_idx < len(row):
                result['Enhanced CLIP'] = row[enhanced_clip_idx]
            
            if enhanced_siglip_idx >= 0 and enhanced_siglip_idx < len(row):
                result['Enhanced SigLIP'] = row[enhanced_siglip_idx]
            
            results[image_path] = result
    
    print(f"Loaded classification results for {len(results)} images")
    return results

def calculate_metrics(ground_truth, predictions):
    """
    Calculate classification metrics
    """
    if not predictions:
        return {
            'accuracy': 0.0,
            'precision': 0.0,
            'recall': 0.0,
            'f1': 0.0,
            'count': 0
        }
    
    # Get common image paths
    common_paths = set(ground_truth.keys()) & set(predictions.keys())
    if not common_paths:
        print("No common images found between ground truth and predictions")
        return {
            'accuracy': 0.0,
            'precision': 0.0,
            'recall': 0.0,
            'f1': 0.0,
            'count': 0
        }
    
    # Prepare lists for metrics calculation
    y_true = []
    y_pred = []
    
    for path in common_paths:
        # Normalize categories for comparison (remove extra spaces, uppercase)
        true_category = ground_truth[path].strip().upper()
        pred_category = predictions[path].strip().upper()
        
        # Handle special cases
        if true_category == "TELLTALES ICONS &INDICATORS":
            true_category = "TELLTALE ICONS & INDICATORS"
        if true_category == "PROCESS FLOW DIAGRAM":
            true_category = "PROCESS FLOW DIAGRAMS"
        if true_category == "TECHNCAL SPECIFICATIONS":
            true_category = "TECHNICAL SPECIFICATIONS"
        if true_category == "SYSTEM ARCHITECTURE":
            true_category = "SYSTEM ARCHITECTURE DIAGRAMS"
        if true_category == "TABLE  + TELLTALES":
            true_category = "TABLE + TELLTALES"
        
        y_true.append(true_category)
        y_pred.append(pred_category)
    
    # Calculate metrics
    unique_categories = sorted(list(set(y_true + y_pred)))
    
    try:
        accuracy = accuracy_score(y_true, y_pred)
        precision = precision_score(y_true, y_pred, average='weighted', labels=unique_categories, zero_division=0)
        recall = recall_score(y_true, y_pred, average='weighted', labels=unique_categories, zero_division=0)
        f1 = f1_score(y_true, y_pred, average='weighted', labels=unique_categories, zero_division=0)
        
        return {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1': f1,
            'count': len(common_paths)
        }
    except Exception as e:
        print(f"Error calculating metrics: {e}")
        return {
            'accuracy': 0.0,
            'precision': 0.0,
            'recall': 0.0,
            'f1': 0.0,
            'count': len(common_paths)
        }

def evaluate_classifiers(ground_truth_path, results_path):
    """
    Evaluate classifier performance against ground truth
    """
    # Load data
    ground_truth = load_ground_truth(ground_truth_path)
    results = load_classification_results(results_path)
    
    # Extract predictions for each classifier
    clip_predictions = {}
    siglip_predictions = {}
    enhanced_clip_predictions = {}
    enhanced_siglip_predictions = {}
    
    for path, result in results.items():
        if 'CLIP' in result:
            clip_predictions[path] = result['CLIP']
        if 'SigLIP' in result:
            siglip_predictions[path] = result['SigLIP']
        if 'Enhanced CLIP' in result:
            enhanced_clip_predictions[path] = result['Enhanced CLIP']
        if 'Enhanced SigLIP' in result:
            enhanced_siglip_predictions[path] = result['Enhanced SigLIP']
    
    # Calculate metrics
    clip_metrics = calculate_metrics(ground_truth, clip_predictions)
    siglip_metrics = calculate_metrics(ground_truth, siglip_predictions)
    enhanced_clip_metrics = calculate_metrics(ground_truth, enhanced_clip_predictions)
    enhanced_siglip_metrics = calculate_metrics(ground_truth, enhanced_siglip_predictions)
    
    # Print results
    print("\nClassifier Performance Metrics:")
    print("-" * 80)
    print(f"{'Classifier':<20} {'Accuracy':<10} {'Precision':<10} {'Recall':<10} {'F1 Score':<10} {'Count':<10}")
    print("-" * 80)
    
    if clip_metrics['count'] > 0:
        print(f"{'CLIP':<20} {clip_metrics['accuracy']:.4f}     {clip_metrics['precision']:.4f}     {clip_metrics['recall']:.4f}     {clip_metrics['f1']:.4f}     {clip_metrics['count']}")
    
    if siglip_metrics['count'] > 0:
        print(f"{'SigLIP':<20} {siglip_metrics['accuracy']:.4f}     {siglip_metrics['precision']:.4f}     {siglip_metrics['recall']:.4f}     {siglip_metrics['f1']:.4f}     {siglip_metrics['count']}")
    
    if enhanced_clip_metrics['count'] > 0:
        print(f"{'Enhanced CLIP':<20} {enhanced_clip_metrics['accuracy']:.4f}     {enhanced_clip_metrics['precision']:.4f}     {enhanced_clip_metrics['recall']:.4f}     {enhanced_clip_metrics['f1']:.4f}     {enhanced_clip_metrics['count']}")
    
    if enhanced_siglip_metrics['count'] > 0:
        print(f"{'Enhanced SigLIP':<20} {enhanced_siglip_metrics['accuracy']:.4f}     {enhanced_siglip_metrics['precision']:.4f}     {enhanced_siglip_metrics['recall']:.4f}     {enhanced_siglip_metrics['f1']:.4f}     {enhanced_siglip_metrics['count']}")
    
    print("-" * 80)
    
    # Calculate improvement percentages
    if clip_metrics['count'] > 0 and enhanced_clip_metrics['count'] > 0:
        clip_improvement = (enhanced_clip_metrics['accuracy'] - clip_metrics['accuracy']) / clip_metrics['accuracy'] * 100 if clip_metrics['accuracy'] > 0 else float('inf')
        print(f"CLIP accuracy improvement: {clip_improvement:.2f}%")
    
    if siglip_metrics['count'] > 0 and enhanced_siglip_metrics['count'] > 0:
        siglip_improvement = (enhanced_siglip_metrics['accuracy'] - siglip_metrics['accuracy']) / siglip_metrics['accuracy'] * 100 if siglip_metrics['accuracy'] > 0 else float('inf')
        print(f"SigLIP accuracy improvement: {siglip_improvement:.2f}%")
    
    # Return metrics for further analysis
    return {
        'CLIP': clip_metrics,
        'SigLIP': siglip_metrics,
        'Enhanced CLIP': enhanced_clip_metrics,
        'Enhanced SigLIP': enhanced_siglip_metrics
    }

def main():
    """
    Main function
    """
    ground_truth_path = "data_files/ground_truth_template.csv"
    results_path = "data_files/ground_truth_template_enhanced_clip.csv"
    
    if os.path.exists(ground_truth_path) and os.path.exists(results_path):
        evaluate_classifiers(ground_truth_path, results_path)
    else:
        print(f"Required files not found. Please ensure both files exist:")
        print(f"  - Ground truth: {ground_truth_path}")
        print(f"  - Results: {results_path}")

if __name__ == "__main__":
    main()
