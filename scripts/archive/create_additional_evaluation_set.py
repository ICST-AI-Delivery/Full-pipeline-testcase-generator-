#!/usr/bin/env python3
"""
Create Additional Evaluation Set for CLIP Classifier
==================================================

This script selects 24 diverse images from the available collection and runs
CLIP classification on them to create a separate evaluation table.

The goal is to:
1. Select images with maximum diversity across domains and categories
2. Run CLIP classifier to get predictions
3. Create a CSV file with the same structure as ground_truth_template_original_clip.csv
4. Add a Classification_Correct column for manual validation later
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

def load_existing_ground_truth():
    """Load existing ground truth images to avoid duplicates."""
    existing_file = project_root / "data_files" / "ground_truth_template_original_clip.csv"
    if existing_file.exists():
        df = pd.read_csv(existing_file)
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

def select_diverse_images(domains, existing_images, target_count=24):
    """Select diverse images using stratified sampling."""
    selected_images = []
    selection_log = []
    
    # Remove existing images from domains
    for domain_name, images in domains.items():
        domains[domain_name] = [img for img in images if img not in existing_images]
    
    # Calculate images per domain (aim for even distribution)
    non_empty_domains = {k: v for k, v in domains.items() if v}
    images_per_domain = max(1, target_count // len(non_empty_domains))
    
    print(f"Found {len(non_empty_domains)} non-empty domains")
    print(f"Target: {images_per_domain} images per domain")
    
    # First pass: get base allocation from each domain
    for domain_name, images in non_empty_domains.items():
        if not images:
            continue
            
        # Randomly sample from this domain
        sample_size = min(images_per_domain, len(images))
        sampled = random.sample(images, sample_size)
        
        for img in sampled:
            selected_images.append(img)
            selection_log.append({
                'image': img,
                'domain': domain_name,
                'reason': f'Stratified sampling from {domain_name}'
            })
    
    # Second pass: fill remaining slots randomly from all available
    remaining_slots = target_count - len(selected_images)
    if remaining_slots > 0:
        all_remaining = []
        for images in non_empty_domains.values():
            all_remaining.extend([img for img in images if img not in selected_images])
        
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

def run_clip_on_images(image_paths):
    """Run CLIP classifier on selected images."""
    results = []
    
    print(f"Running CLIP classification on {len(image_paths)} images...")
    
    for i, image_path in enumerate(image_paths, 1):
        print(f"Processing {i}/{len(image_paths)}: {image_path}")
        
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
                print(f"  Failed to classify {image_path}")
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
            print(f"  Error processing {image_path}: {e}")
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

def save_results(results, selection_log):
    """Save results to CSV and create selection report."""
    
    # Create data_files directory if it doesn't exist
    data_dir = project_root / "data_files"
    data_dir.mkdir(exist_ok=True)
    
    # Save main results CSV
    df = pd.DataFrame(results)
    output_file = data_dir / "additional_images_for_evaluation.csv"
    df.to_csv(output_file, index=False)
    print(f"Saved evaluation table to: {output_file}")
    
    # Create selection report
    report = {
        'timestamp': datetime.now().isoformat(),
        'total_images_selected': len(results),
        'selection_strategy': 'Stratified sampling across vehicle function domains',
        'domain_distribution': {},
        'category_predictions': {},
        'confidence_distribution': {'High': 0, 'Medium': 0, 'Low': 0},
        'selection_log': selection_log
    }
    
    # Calculate domain distribution
    for entry in selection_log:
        domain = entry['domain']
        report['domain_distribution'][domain] = report['domain_distribution'].get(domain, 0) + 1
    
    # Calculate category and confidence distributions
    for result in results:
        category = result['Original CLIP Category']
        confidence = result['Original CLIP Confidence']
        
        report['category_predictions'][category] = report['category_predictions'].get(category, 0) + 1
        if confidence in report['confidence_distribution']:
            report['confidence_distribution'][confidence] += 1
    
    # Save selection report
    report_file = data_dir / "additional_images_selection_report.json"
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"Saved selection report to: {report_file}")
    
    return output_file, report_file

def main():
    """Main execution function."""
    print("Creating Additional Evaluation Set for CLIP Classifier")
    print("=" * 55)
    
    # Set random seed for reproducibility
    random.seed(42)
    
    # Find all available images
    print("1. Finding all available images...")
    all_images = find_all_images()
    print(f"   Found {len(all_images)} total images")
    
    # Load existing ground truth to avoid duplicates
    print("2. Loading existing ground truth images...")
    existing_images = load_existing_ground_truth()
    print(f"   Found {len(existing_images)} existing ground truth images")
    
    # Categorize by domain
    print("3. Categorizing images by domain...")
    domains = categorize_by_domain(all_images)
    
    # Print domain statistics
    print("   Domain distribution:")
    for domain, images in domains.items():
        available = len([img for img in images if img not in existing_images])
        print(f"     {domain}: {available} available images")
    
    # Select diverse images
    print("4. Selecting 24 diverse images...")
    selected_images, selection_log = select_diverse_images(domains, existing_images, 24)
    print(f"   Selected {len(selected_images)} images")
    
    # Run CLIP classification
    print("5. Running CLIP classification...")
    results = run_clip_on_images(selected_images)
    
    # Save results
    print("6. Saving results...")
    output_file, report_file = save_results(results, selection_log)
    
    print("\nCompleted successfully!")
    print(f"Evaluation table: {output_file}")
    print(f"Selection report: {report_file}")
    print("\nNext steps:")
    print("1. Review the generated CSV file")
    print("2. Add ground truth categories in the 'Ground_Truth_Category' column")
    print("3. Mark classification accuracy in the 'Classification_Correct' column")

if __name__ == "__main__":
    main()
