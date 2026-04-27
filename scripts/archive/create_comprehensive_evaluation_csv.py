"""
Create comprehensive evaluation CSV combining CLIP results with comprehensive_evaluation_results.csv
This script creates a new CSV file that includes:
- Images from comprehensive_evaluation_results.csv
- Ground truth categories
- CLIP predictions (using improved descriptions)
- Enhanced SigLIP predictions
- Correct/Incorrect labels for both models
"""

import pandas as pd
import os

def main():
    print("Creating Comprehensive Evaluation CSV")
    print("=" * 50)
    
    # Read the comprehensive evaluation results (contains Enhanced SigLIP results)
    comprehensive_file = "data_files/comprehensive_evaluation_results.csv"
    if not os.path.exists(comprehensive_file):
        print(f"Error: {comprehensive_file} not found")
        return
    
    print(f"Reading comprehensive evaluation results from: {comprehensive_file}")
    comprehensive_df = pd.read_csv(comprehensive_file)
    
    # Read the CLIP improved descriptions results
    clip_file = "data_files/clip_ground_truth_evaluation_results_improved_descriptions.csv"
    if not os.path.exists(clip_file):
        print(f"Error: {clip_file} not found")
        return
    
    print(f"Reading CLIP results from: {clip_file}")
    clip_df = pd.read_csv(clip_file)
    
    # Create mapping from image name to CLIP results
    clip_results = {}
    for _, row in clip_df.iterrows():
        image_name = row['Image Name']
        clip_results[image_name] = {
            'CLIP_Predicted_Category': row['CLIP Predicted Category'],
            'CLIP_Confidence': row['CLIP Confidence'],
            'CLIP_Correct_Incorrect': row['Correct/Incorrect']
        }
    
    # Create the final results list
    final_results = []
    
    for _, row in comprehensive_df.iterrows():
        image_name = row['Image Name']
        ground_truth = row['Ground Truth Category']
        enhanced_siglip_pred = row['Enhanced SigLIP Predicted Category']
        enhanced_siglip_conf = row['Enhanced SigLIP Confidence']
        
        # Determine Enhanced SigLIP correctness
        siglip_correct = 'Correct' if ground_truth.strip().upper() == enhanced_siglip_pred.strip().upper() else 'Incorrect'
        
