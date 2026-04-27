#!/usr/bin/env python3
"""
Add More Images to Existing Evaluation Set
==========================================

This script adds 10 more diverse images to the existing evaluation table
while preserving all user-added ground truth categories and correctness assessments.

The script will:
1. Load the existing evaluation CSV with all user annotations
2. Select 10 additional diverse images from underrepresented domains
3. Run CLIP classification on only the new images
4. Append the new results while preserving existing data
"""

import os
import sys
import pandas as pd
import random
from pathlib import Path
import json
from datetime import datetime

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

# Import CLIP classifier
from scripts.original_clip_classifier import classify_image, get_category_descriptions

def find_all_images():
    """Find all PNG images in the project directories."""
    image_paths = []
    
    # Search in static directory
    static_dir = project_root / "static"
    if static_dir.exists():
        for png_file in static_dir.rglob("*.png"):
            image_paths.append(str(png_file.relative_to(project_root)))
    
    # Search in Pre-FineTuneLearning Model directory
    pretrain_dir = project_root / "Pre-FineTuneLearning Model"
    if pretrain_dir.exists():
        for png_file in pretrain_dir.rglob("*.png"):
            image_paths.append(str(png_file.relative_to(project_root)))
    
    return image_paths

def load_existing_evaluation_set():
    """Load existing evaluation set with all user annotations."""
    eval_file = project_root / "data_files" / "additional_images_for_evaluation.csv"
    if eval_file.exists():
        df = pd.read_csv(eval_file)
        existing_images = set(df['Image Path'].tolist())
        print(f"   Loaded {len(df)} existing images with user annotations")
        return df, existing_images
    else:
        print("   No existing evaluation file found")
        return pd.DataFrame(), set()

def load_ground_truth_images():
    """Load ground truth images to avoid duplicates."""
    gt_file = project_root / "data_files" / "ground_truth_template_original_clip.csv"
    if gt_file.exists():
        df = pd.read_csv(gt_file)
        return set(df['Image Path'].tolist())
    return set()

def categorize_by_domain(image_paths):
    """Categorize images by their domain/function area."""
    domains = {
        'Audio_Tuner': [],
        'Navigation': [],
        'Parking_Systems': [],
        'HMI_Software': [],
        'System_Architecture': [],
        'Driver_Assistance': [],
        'Vehicle_Status': [],
        'Safety_Systems': [],
        'Instrument_Cluster': [],
        'Connectivity': [],
        'Diagnostics': [],
        'Other': []
    }
    
    for path in image_paths:
        path_lower = path.lower()
        
        if any(x in path_lower for x in ['rad-', 'tuner', 'audio']):
            domains['Audio_Tuner'].append(path)
        elif any(x in path_lower for x in ['map-', 'navigation', 'navigator']):
            domains['Navigation'].append(path)
        elif any(x in path_lower for x in ['prk-', 'parking', 'camera', 'proximity']):
            domains['Parking_Systems'].append(path)
        elif any(x in path_lower for x in ['vfi-', 'set-', 'hmi', 'profile']):
            domains['HMI_Software'].append(path)
        elif any(x in path_lower for x in ['f244', 'f834', 'pmn-', 'system architecture', 'power', 'ethernet']):
            domains['System_Architecture'].append(path)
        elif any(x in path_lower for x in ['f53', 'f56', 'cruise', 'lane', 'collision', 'adaptive']):
            domains['Driver_Assistance'].append(path)
        elif any(x in path_lower for x in ['f80', 'f81', 'battery', 'charging', 'hybrid', 'performance']):
            domains['Vehicle_Status'].append(path)
        elif any(x in path_lower for x in ['f139', 'f140', 'airbag', 'seatbelt', 'brake']):
            domains['Safety_Systems'].append(path)
        elif any(x in path_lower for x in ['instrument cluster', 'speedometer', 'odometer', 'telltale']):
            domains['Instrument_Cluster'].append(path)
        elif any(x in path_lower for x in ['connectivity', 'usb', 'wireless']):
            domains['Connectivity'].append(path)
        elif any(x in path_lower for x in ['diagnostic', 'test']):
            domains['Diagnostics'].append(path)
        else:
            domains['Other'].append(path)
    
    return domains

def select_additional_images(domains, excluded_images, target_count=10):
    """Select additional images with focus on diversity."""
    selected_images = []
    selection_log = []
    
    # Remove excluded images from domains
    for domain_name, images in domains.items():
        domains[domain_name] = [img for img in images if img not in excluded_images]
    
    # Get non-empty domains
    non_empty_domains = {k: v for k, v in domains.items() if v}
    
    print(f"   Found {len(non_empty_domains)} non-empty domains for additional selection")
    
    # Try to get at least 1 image from each domain, then fill remaining randomly
    domains_list = list(non_empty_domains.keys())
    random.shuffle(domains_list)
    
    # First pass: one image per domain (up to target_count)
    for domain_name in domains_list[:target_count]:
        images = non_empty_domains[domain_name]
        if images:
            selected_img = random.choice(images)
            selected_images.append(selected_img)
            selection_log.append({
                'image': selected_img,
                'domain': domain_name,
                'reason': f'Additional diversity sampling from {domain_name}'
            })
            # Remove selected image to avoid duplicates
            non_empty_domains[domain_name].remove(selected_img)
    
    # Second pass: fill remaining slots randomly
    remaining_slots = target_count - len(selected_images)
    if remaining_slots > 0:
        all_remaining = []
        for images in non_empty_domains.values():
            all_remaining.extend(images)
        
        if all_remaining:
            additional = random.sample(all_remaining, min(remaining_slots, len(all_remaining)))
            for img in additional:
                selected_images.append(img)
                # Find which domain this belongs to
                img_domain = 'Unknown'
                for domain_name, images in non_empty_domains.items():
                    if img in images:
                        img_domain = domain_name
                        break
                selection_log.append({
                    'image': img,
                    'domain': img_domain,
                    'reason': 'Random selection to fill remaining slots'
                })
    
    return selected_images[:target_count], selection_log

def run_clip_on_new_images(image_paths):
    """Run CLIP classifier on new images only."""
    results = []
    
    print(f"   Running CLIP classification on {len(image_paths)} new images...")
    
    for i, image_path in enumerate(image_paths, 1):
        print(f"   Processing {i}/{len(image_paths)}: {Path(image_path).name}")
        
        try:
            # Run CLIP classification
            result = classify_image(image_path)
            
            if result:
                # Convert confidence score to level
                confidence_score = result.get('confidence', 0)
                if confidence_score >= 0.7:
                    confidence_level = 'High'
                elif confidence_score >= 0.4:
                    confidence_level = 'Medium'
                else:
                    confidence_level = 'Low'
                
                results.append({
                    'Image Path': image_path,
                    'Filename': Path(image_path).name,
                    'Ground_Truth_Category': '',  # Empty for manual labeling
                    'Notes': '',  # Empty for manual notes
                    'Original CLIP Category': result['category'],
                    'Original CLIP Confidence': confidence_level,
                    'Original CLIP Description': f"CLIP classification: {result['description']} (score: {confidence_score:.3f})",
                    'Classification_Correct': ''  # Empty for manual validation
                })
            else:
                print(f"     Failed to classify {image_path}")
                results.append({
                    'Image Path': image_path,
                    'Filename': Path(image_path).name,
                    'Ground_Truth_Category': '',
                    'Notes': 'Classification failed',
                    'Original CLIP Category': 'UNKNOWN',
                    'Original CLIP Confidence': 'Low',
                    'Original CLIP Description': 'CLIP classification failed',
                    'Classification_Correct': ''
                })
                
        except Exception as e:
            print(f"     Error processing {image_path}: {e}")
            results.append({
                'Image Path': image_path,
                'Filename': Path(image_path).name,
                'Ground_Truth_Category': '',
                'Notes': f'Error: {str(e)}',
                'Original CLIP Category': 'ERROR',
                'Original CLIP Confidence': 'Low',
                'Original CLIP Description': f'Error during classification: {str(e)}',
                'Classification_Correct': ''
            })
    
    return results

def save_updated_results(existing_df, new_results, selection_log):
    """Save updated results preserving existing user annotations."""
    
    # Create data_files directory if it doesn't exist
    data_dir = project_root / "data_files"
    data_dir.mkdir(exist_ok=True)
    
    # Combine existing data with new results
    new_df = pd.DataFrame(new_results)
    combined_df = pd.concat([existing_df, new_df], ignore_index=True)
    
    # Save updated CSV
    output_file = data_dir / "additional_images_for_evaluation.csv"
    combined_df.to_csv(output_file, index=False)
    print(f"   Saved updated evaluation table to: {output_file}")
    
    # Update selection report
    report_file = data_dir / "additional_images_selection_report.json"
    
    # Load existing report if it exists
    if report_file.exists():
        with open(report_file, 'r') as f:
            report = json.load(f)
    else:
        report = {
            'domain_distribution': {},
            'category_predictions': {},
            'confidence_distribution': {'High': 0, 'Medium': 0, 'Low': 0},
            'selection_log': []
        }
    
    # Update report with new data
    report['timestamp'] = datetime.now().isoformat()
    report['total_images_selected'] = len(combined_df)
    report['selection_strategy'] = 'Stratified sampling across vehicle function domains (updated)'
    
    # Add new selection log entries
    report['selection_log'].extend(selection_log)
    
    # Recalculate distributions from combined data
    report['domain_distribution'] = {}
    for entry in report['selection_log']:
        domain = entry['domain']
        report['domain_distribution'][domain] = report['domain_distribution'].get(domain, 0) + 1
    
    # Calculate category and confidence distributions from all data
    report['category_predictions'] = {}
    report['confidence_distribution'] = {'High': 0, 'Medium': 0, 'Low': 0}
    
    for _, row in combined_df.iterrows():
        category = row['Original CLIP Category']
        confidence = row['Original CLIP Confidence']
        
        report['category_predictions'][category] = report['category_predictions'].get(category, 0) + 1
        if confidence in report['confidence_distribution']:
            report['confidence_distribution'][confidence] += 1
    
    # Save updated report
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"   Updated selection report: {report_file}")
    
    return output_file, report_file

def main():
    """Main execution function."""
    print("Adding 10 More Images to Evaluation Set")
    print("=" * 40)
    
    # Set random seed for reproducibility
    random.seed(42)
    
    # Load existing evaluation set with user annotations
    print("1. Loading existing evaluation set...")
    existing_df, existing_eval_images = load_existing_evaluation_set()
    
    # Load ground truth images to avoid duplicates
    print("2. Loading ground truth images...")
    gt_images = load_ground_truth_images()
    print(f"   Found {len(gt_images)} ground truth images")
    
    # Combine all images to exclude
    excluded_images = existing_eval_images.union(gt_images)
    print(f"   Total images to exclude: {len(excluded_images)}")
    
    # Find all available images
    print("3. Finding all available images...")
    all_images = find_all_images()
    print(f"   Found {len(all_images)} total images")
    
    # Categorize by domain
    print("4. Categorizing images by domain...")
    domains = categorize_by_domain(all_images)
    
    # Print domain statistics
    print("   Available images per domain (excluding existing):")
    for domain, images in domains.items():
        available = len([img for img in images if img not in excluded_images])
        print(f"     {domain}: {available} available images")
    
    # Select 10 additional images
    print("5. Selecting 10 additional diverse images...")
    selected_images, selection_log = select_additional_images(domains, excluded_images, 10)
    print(f"   Selected {len(selected_images)} new images")
    
    # Run CLIP classification on new images only
    print("6. Running CLIP classification on new images...")
    new_results = run_clip_on_new_images(selected_images)
    
    # Save updated results
    print("7. Saving updated results...")
    output_file, report_file = save_updated_results(existing_df, new_results, selection_log)
    
    print("\nCompleted successfully!")
    print(f"Updated evaluation table: {output_file}")
    print(f"Updated selection report: {report_file}")
    print(f"Total images in evaluation set: {len(existing_df) + len(new_results)}")
    print("\nNext steps:")
    print("1. Review the 10 new images added to the CSV file")
    print("2. Add ground truth categories for the new images")
    print("3. Mark classification accuracy for the new images")
    print("4. All your existing annotations have been preserved")

if __name__ == "__main__":
    main()
