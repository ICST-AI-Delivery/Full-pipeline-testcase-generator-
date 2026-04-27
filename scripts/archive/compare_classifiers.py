"""
Comparison Tool for Image Classification Methods
Compares CLIP-based and CV-based classifiers on the same images
"""

import os
import csv
import time
from datetime import datetime
import sys
import argparse
from PIL import Image

# Import both classifiers
sys.path.insert(0, ".")
sys.path.insert(0, "Pre-FineTuneLearning Model")

# Try to import CLIP
try:
    import clip
    import torch
    CLIP_AVAILABLE = True
except ImportError:
    print("Warning: CLIP not available. Only CV-based classification will be used.")
    CLIP_AVAILABLE = False

# Import classifiers
if CLIP_AVAILABLE:
    from clip_classifier import CLIPImageClassifier
from classify_images import classify_image as cv_classify_image

def compare_classifiers(image_paths, output_csv="classification_comparison.csv"):
    """
    Compare CLIP and CV-based classifiers on the same images
    
    Args:
        image_paths (list): List of image paths to classify
        output_csv (str): Path to output CSV file
    """
    # Initialize CLIP classifier if available
    clip_classifier = None
    if CLIP_AVAILABLE:
        print("Initializing CLIP classifier...")
        clip_classifier = CLIPImageClassifier(device="cpu")
    
    # Create CSV file with headers
    with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Image Path', 'Filename', 
                       'CLIP Category', 'CLIP Confidence', 'CLIP Description',
                       'CV Category', 'CV Confidence', 'CV Description',
                       'Match', 'Processing Time', 'Timestamp'])
    
    print(f"Processing {len(image_paths)} images...")
    
    # Process each image
    for idx, image_path in enumerate(image_paths, 1):
        filename = os.path.basename(image_path)
        print(f"Processing {idx}/{len(image_paths)}: {filename}")
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        match = "N/A"
        
        # Process with CLIP classifier
        clip_category = "N/A"
        clip_confidence = "N/A"
        clip_description = "N/A"
        
        if CLIP_AVAILABLE and clip_classifier:
            try:
                start_time = time.time()
                clip_category, clip_confidence, clip_description = clip_classifier.classify_image(image_path)
                clip_time = time.time() - start_time
                print(f"  CLIP: {clip_category} ({clip_confidence})")
            except Exception as e:
                print(f"  Error with CLIP classification: {e}")
                clip_time = 0
        else:
            clip_time = 0
        
        # Process with CV classifier
        try:
            start_time = time.time()
            cv_category, cv_confidence, cv_description = cv_classify_image(image_path)
            cv_time = time.time() - start_time
            print(f"  CV:   {cv_category} ({cv_confidence})")
        except Exception as e:
            print(f"  Error with CV classification: {e}")
            cv_category = "Error"
            cv_confidence = "Low"
            cv_description = str(e)
            cv_time = 0
        
        # Determine if classifications match
        if CLIP_AVAILABLE and clip_classifier:
            if clip_category == cv_category:
                match = "Yes"
            else:
                match = "No"
        
        # Calculate total processing time
        processing_time = clip_time + cv_time
        
        # Save results
        with open(output_csv, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([image_path, filename, 
                           clip_category, clip_confidence, clip_description,
                           cv_category, cv_confidence, cv_description,
                           match, f"{processing_time:.2f}s", timestamp])
    
    print(f"\nComparison complete! Results saved to: {output_csv}")

def find_sample_images(directory, max_images=5, per_folder=1):
    """
    Find a representative sample of images from the directory structure
    
    Args:
        directory (str): Root directory to search
        max_images (int): Maximum number of images to return
        per_folder (int): Maximum number of images per subfolder
    
    Returns:
        list: List of image paths
    """
    image_paths = []
    
    for root, dirs, files in os.walk(directory):
        folder_images = 0
        
        # Sort files to get consistent results
        files.sort()
        
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                if folder_images < per_folder:
                    image_path = os.path.join(root, file)
                    image_paths.append(image_path)
                    folder_images += 1
                    
                    # Check if we've reached the maximum
                    if len(image_paths) >= max_images:
                        return image_paths
    
    return image_paths

def main():
    """
    Main function to run the comparison
    """
    parser = argparse.ArgumentParser(description='Compare image classification methods')
    parser.add_argument('--dir', type=str, default='static', help='Directory containing images')
    parser.add_argument('--output', type=str, default='classification_comparison.csv', help='Output CSV file')
    parser.add_argument('--max', type=int, default=10, help='Maximum number of images to process')
    parser.add_argument('--per-folder', type=int, default=1, help='Maximum images per subfolder')
    parser.add_argument('--specific', type=str, default=None, help='Specific image to classify')
    
    args = parser.parse_args()
    
    if args.specific:
        # Process a specific image
        if os.path.exists(args.specific):
            compare_classifiers([args.specific], args.output)
        else:
            print(f"Error: Image {args.specific} not found")
    else:
        # Find sample images
        print(f"Finding sample images in {args.dir}...")
        image_paths = find_sample_images(args.dir, args.max, args.per_folder)
        
        if not image_paths:
            print(f"No images found in {args.dir}")
            return
        
        print(f"Found {len(image_paths)} images")
        compare_classifiers(image_paths, args.output)

if __name__ == "__main__":
    main()
