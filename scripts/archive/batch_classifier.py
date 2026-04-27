"""
Batch Image Classification Tool
Reads image paths from a text file and runs comprehensive classification analysis
"""

import os
import csv
import time
from datetime import datetime
import sys
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

def read_image_list(file_path):
    """
    Read image paths from a text file, ignoring comments and empty lines
    
    Args:
        file_path (str): Path to the text file containing image paths
    
    Returns:
        list: List of image paths
    """
    image_paths = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                # Skip empty lines and comments
                if line and not line.startswith('#'):
                    image_paths.append(line)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        return []
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return []
    
    return image_paths

def verify_image_paths(image_paths):
    """
    Verify that all image paths exist and are accessible
    
    Args:
        image_paths (list): List of image paths to verify
    
    Returns:
        tuple: (valid_paths, invalid_paths)
    """
    valid_paths = []
    invalid_paths = []
    
    for path in image_paths:
        if os.path.exists(path):
            try:
                # Try to open the image to verify it's valid
                with Image.open(path) as img:
                    img.verify()
                valid_paths.append(path)
            except Exception as e:
                print(f"Warning: Image {path} exists but cannot be opened: {e}")
                invalid_paths.append(path)
        else:
            print(f"Warning: Image {path} not found")
            invalid_paths.append(path)
    
    return valid_paths, invalid_paths

def batch_classify_images(image_list_file, output_csv="complete_image_inventory.csv"):
    """
    Classify all images from a text file using both CLIP and CV classifiers
    
    Args:
        image_list_file (str): Path to text file containing image paths
        output_csv (str): Path to output CSV file
    """
    print("=" * 60)
    print("BATCH IMAGE CLASSIFICATION ANALYSIS")
    print("=" * 60)
    
    # Read image paths from file
    print(f"Reading image paths from: {image_list_file}")
    image_paths = read_image_list(image_list_file)
    
    if not image_paths:
        print("No image paths found in the file.")
        return
    
    print(f"Found {len(image_paths)} image paths")
    
    # Verify image paths
    print("Verifying image paths...")
    valid_paths, invalid_paths = verify_image_paths(image_paths)
    
    if invalid_paths:
        print(f"Warning: {len(invalid_paths)} invalid paths found:")
        for path in invalid_paths:
            print(f"  - {path}")
    
    if not valid_paths:
        print("No valid image paths found.")
        return
    
    print(f"Processing {len(valid_paths)} valid images...")
    
    # Initialize CLIP classifier if available
    clip_classifier = None
    clip_available = CLIP_AVAILABLE
    if clip_available:
        print("Initializing CLIP classifier...")
        try:
            clip_classifier = CLIPImageClassifier(device="cpu")
            print("CLIP classifier initialized successfully")
        except Exception as e:
            print(f"Error initializing CLIP classifier: {e}")
            clip_available = False
    
    # Create CSV file with headers
    with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Image Path', 'Filename', 
                       'CLIP Category', 'CLIP Confidence', 'CLIP Description',
                       'CV Category', 'CV Confidence', 'CV Description',
                       'Match', 'Processing Time', 'Timestamp'])
    
    # Process each image
    successful_classifications = 0
    total_processing_time = 0
    
    for idx, image_path in enumerate(valid_paths, 1):
        filename = os.path.basename(image_path)
        print(f"\nProcessing {idx}/{len(valid_paths)}: {filename}")
        print(f"Path: {image_path}")
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        match = "N/A"
        
        # Process with CLIP classifier
        clip_category = "N/A"
        clip_confidence = "N/A"
        clip_description = "N/A"
        clip_time = 0
        
        if clip_available and clip_classifier:
            try:
                start_time = time.time()
                clip_category, clip_confidence, clip_description = clip_classifier.classify_image(image_path)
                clip_time = time.time() - start_time
                print(f"  CLIP: {clip_category} ({clip_confidence}) - {clip_time:.2f}s")
            except Exception as e:
                print(f"  Error with CLIP classification: {e}")
                clip_category = "Error"
                clip_confidence = "Low"
                clip_description = str(e)
        
        # Process with CV classifier
        cv_category = "Unknown"
        cv_confidence = "Low"
        cv_description = "No description"
        cv_time = 0
        
        try:
            start_time = time.time()
            cv_category, cv_confidence, cv_description = cv_classify_image(image_path)
            cv_time = time.time() - start_time
            print(f"  CV:   {cv_category} ({cv_confidence}) - {cv_time:.2f}s")
        except Exception as e:
            print(f"  Error with CV classification: {e}")
            cv_category = "Error"
            cv_confidence = "Low"
            cv_description = str(e)
        
        # Determine if classifications match
        if clip_available and clip_classifier and clip_category != "Error" and cv_category != "Error":
            if clip_category == cv_category:
                match = "Yes"
            else:
                match = "No"
        
        # Calculate total processing time
        processing_time = clip_time + cv_time
        total_processing_time += processing_time
        
        # Save results
        with open(output_csv, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([image_path, filename, 
                           clip_category, clip_confidence, clip_description,
                           cv_category, cv_confidence, cv_description,
                           match, f"{processing_time:.2f}s", timestamp])
        
        successful_classifications += 1
    
    # Print summary
    print("\n" + "=" * 60)
    print("BATCH CLASSIFICATION COMPLETE")
    print("=" * 60)
    print(f"Total images processed: {successful_classifications}")
    print(f"Average processing time: {total_processing_time/successful_classifications:.2f}s per image")
    print(f"Total processing time: {total_processing_time:.2f}s")
    print(f"Results saved to: {output_csv}")
    
    if invalid_paths:
        print(f"\nNote: {len(invalid_paths)} images could not be processed")

def main():
    """
    Main function to run batch classification
    """
    import argparse
    
    parser = argparse.ArgumentParser(description='Batch image classification from text file')
    parser.add_argument('--input', type=str, default='image_list.txt', help='Input text file with image paths')
    parser.add_argument('--output', type=str, default='complete_image_inventory.csv', help='Output CSV file')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print(f"Error: Input file {args.input} not found")
        return
    
    batch_classify_images(args.input, args.output)

if __name__ == "__main__":
    main()
