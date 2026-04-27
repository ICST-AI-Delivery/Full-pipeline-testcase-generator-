"""
Extended Simple CLIP Pipeline - Process any CSV with image paths using existing code
Extended to search in SRS_HMI Software directory as well

Uses the same structure as clip_ground_truth_evaluation_results_simplified_descriptions.csv

Supports CLIP model ensembling (e.g., ViT-B/32, ViT-L/14, ViT-L/14@336px, ViT-H/14 if available).
"""

import os
import csv
import html
import argparse
import pandas as pd
from datetime import datetime
from pathlib import Path
from clip_classifier import CLIPImageClassifier


def auto_generate_csv(feature_name):
    """Automatically generate CSV file for a feature by scanning its directory"""
    print(f"📁 Auto-generating CSV for feature: {feature_name}")
    
    # Define possible directory paths to search - EXTENDED VERSION
    base_paths = [
        f"Pre-FineTuneLearning Model/SRS FPI export/SRS_Instrument Cluster/{feature_name}",
        f"Pre-FineTuneLearning Model/SRS FPI export/SRS_HMI Software/{feature_name}",  # Added HMI Software
        f"Pre-FineTuneLearning Model/SRS FPI export/SRS_Diagnostics/{feature_name}",  # Added Diagnostics
        f"Pre-FineTuneLearning Model/SRS FPI export/SRS_System Architecture/{feature_name}",  # Added System Architecture
        f"Pre-FineTuneLearning Model/SRS FPI export/{feature_name}",
        f"images/{feature_name}",
        feature_name  # Direct path
    ]
    
    # Find the correct directory
    feature_dir = None
    for base_path in base_paths:
        if Path(base_path).exists():
            feature_dir = Path(base_path)
            print(f"✅ Found feature directory: {feature_dir}")
            break
    
    if not feature_dir:
        print(f"❌ Error: Could not find directory for feature '{feature_name}'")
        print(f"   Searched paths:")
        for path in base_paths:
            print(f"   - {path}")
        return False
    
    print(f"🔍 Scanning directory: {feature_dir}")
    
    # Find all image files
    image_extensions = ['*.png', '*.jpg', '*.jpeg', '*.PNG', '*.JPG', '*.JPEG']
    image_files = []
    
    for ext in image_extensions:
        image_files.extend(feature_dir.glob(ext))
    
    if not image_files:
        print(f"❌ Error: No image files found in {feature_dir}")
        return False
    
    # Sort files naturally (image1, image2, image10, etc.)
    image_files.sort(key=lambda x: x.name)
    
    print(f"✅ Found {len(image_files)} images")
    
    # Create CSV data
    csv_data = []
    for img_file in image_files:
        csv_data.append({
            'Image Path': str(img_file),
            'Image Name': img_file.name,
            'Ground Truth Category': '',  # Empty for CLIP to fill
            'Notes': feature_name.replace('_', ' ').replace('-', ' ')
        })
    
    # Create DataFrame and save CSV
    df = pd.DataFrame(csv_data)
    csv_output_path = Path("data_files") / f"{feature_name}.csv"
    
    # Create data_files directory if it doesn't exist
    csv_output_path.parent.mkdir(exist_ok=True)
    
    try:
        df.to_csv(csv_output_path, index=False)
        print(f"📝 Generated CSV: {csv_output_path}")
        print(f"   Contains {len(csv_data)} image entries")
        return True
    except Exception as e:
        print(f"❌ Error saving CSV file: {e}")
        return False

def normalize_category(name: str) -> str:
    """
    Normalize category strings for robust comparison against classifier outputs.
    - Unescape HTML entities (& -> &)
    - Lowercase and strip
    - Map common aliases to canonical labels
    - Return uppercase for final comparison
    """
    if not isinstance(name, str):
        return ""

    s = html.unescape(name).strip().lower()

    # Common alias fixes
    alias_map = {
        "table + telltales": "table with telltales",
        "table with tell tales": "table with telltales",
        "color && gradients": "color and gradients",
        "colour and gradients": "color and gradients",
        "technical spec": "technical specifications",
        "technical specification": "technical specifications",
        "hmi display layout": "hmi display layouts",
        "config table": "configuration tables",
        "configuration table": "configuration tables",
        "wiring & signal diagrams": "wiring & signal diagrams",
        "telltale icons & indicators": "telltale icons & indicators",
        "telltale icons and indicators": "telltale icons & indicators",
        "wiring and signal diagrams": "wiring & signal diagrams",
        "multi-condition logic": "multi-condition logic",
        "state event matrix": "state event matrices",
        "flowchart diagram": "flowchart diagrams",
        "state flow diagram": "state flow diagrams",
        "timing diagram": "timing diagrams",
        "technical specifications": "technical specifications",
        "color and gradient": "color and gradients",
    }

    # If exact alias found
    if s in alias_map:
        s = alias_map[s]

    # Title mapping: convert to uppercase keys used in classifier
    return s.upper()


def resolve_image_path(base_csv_path: str, image_path: str) -> str:
    """
    Resolve an image path, trying multiple resolution strategies.
    1. If absolute path, use as-is
    2. Try relative to current working directory
    3. Try relative to CSV file directory
    4. Try with normalized path separators
    5. Try parent directory (useful when running from scripts/ subdirectory)
    """
    if not isinstance(image_path, str) or not image_path:
        return image_path

    # If absolute path, use as-is
    if os.path.isabs(image_path):
        if os.path.exists(image_path):
            return image_path

    # Strategy 1: Try relative to current working directory
    cwd_candidate = os.path.join(os.getcwd(), image_path)
    if os.path.exists(cwd_candidate):
        return cwd_candidate

    # Strategy 2: Try with normalized path separators (Windows compatibility)
    normalized_path = image_path.replace('/', os.sep).replace('\\', os.sep)
    cwd_normalized = os.path.join(os.getcwd(), normalized_path)
    if os.path.exists(cwd_normalized):
        return cwd_normalized

    # Strategy 3: Try relative to CSV file directory
    csv_dir = os.path.dirname(os.path.abspath(base_csv_path))
    csv_candidate = os.path.join(csv_dir, image_path)
    if os.path.exists(csv_candidate):
        return csv_candidate

    # Strategy 4: Try CSV dir with normalized separators
    csv_normalized = os.path.join(csv_dir, normalized_path)
    if os.path.exists(csv_normalized):
        return csv_normalized

    # Strategy 5: Try going up one level from current directory (useful for scripts/ subdirectory)
    parent_dir = os.path.dirname(os.getcwd())
    parent_candidate = os.path.join(parent_dir, image_path)
    if os.path.exists(parent_candidate):
        return parent_candidate

    # Strategy 6: Try parent dir with normalized separators
    parent_normalized = os.path.join(parent_dir, normalized_path)
    if os.path.exists(parent_normalized):
        return parent_normalized

    # Fallback: return original path for error handling
    return image_path


def normalize_path_for_comparison(path: str) -> str:
    """
    Normalize a path for comparison by converting to forward slashes and lowercasing.
    """
    if not isinstance(path, str):
        return ""
    
    # Convert backslashes to forward slashes and normalize case
    normalized = path.replace('\\', '/').lower().strip()
    
    # Remove any trailing slashes
    normalized = normalized.rstrip('/')
    
    return normalized


def load_merged_predictions(merged_table_path: str) -> dict:
    """
    Load existing predictions from the merged table.
    Returns a dictionary mapping normalized image paths to prediction data.
    """
    predictions_cache = {}
    
    if not os.path.exists(merged_table_path):
        print(f"Merged table not found at {merged_table_path}, starting fresh")
        return predictions_cache
    
    try:
        df = pd.read_csv(merged_table_path)
        print(f"Loaded {len(df)} existing predictions from {merged_table_path}")
        
        for _, row in df.iterrows():
            image_path = str(row.get('Image Path', ''))
            normalized_path = normalize_path_for_comparison(image_path)
            
            if normalized_path:
                predictions_cache[normalized_path] = {
                    'original_path': image_path,
                    'image_name': str(row.get('Image Name', '')),
                    'ground_truth': str(row.get('Ground Truth Category', '')),
                    'notes': str(row.get('Notes', 'nan')),
                    'clip_category': str(row.get('CLIP Predicted Category', '')),
                    'clip_confidence': str(row.get('CLIP Confidence', '')),
                    'clip_description': str(row.get('CLIP Description', '')),
                    'correct_incorrect': str(row.get('Correct/Incorrect', 'N/A')),
                    'timestamp': str(row.get('Timestamp', ''))
                }
        
        print(f"Cached {len(predictions_cache)} predictions for duplicate checking")
        
    except Exception as e:
        print(f"Error loading merged table: {e}")
        print("Starting with empty cache")
    
    return predictions_cache


def check_image_in_cache(image_path: str, predictions_cache: dict) -> dict:
    """
    Check if an image path exists in the predictions cache.
    Returns the cached prediction data if found, None otherwise.
    """
    normalized_path = normalize_path_for_comparison(image_path)
    return predictions_cache.get(normalized_path, None)


def append_to_merged_table(merged_table_path: str, new_predictions: list):
    """
    Append new predictions to the merged table.
    """
    if not new_predictions:
        print("No new predictions to append to merged table")
        return
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(os.path.abspath(merged_table_path)), exist_ok=True)
    
    # Check if file exists to determine if we need to write headers
    file_exists = os.path.exists(merged_table_path)
    
    try:
        with open(merged_table_path, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            
            # Write header if file doesn't exist
            if not file_exists:
                writer.writerow([
                    'Image Path',
                    'Image Name', 
                    'Ground Truth Category',
                    'Notes',
                    'CLIP Predicted Category',
                    'CLIP Confidence',
                    'CLIP Description',
                    'Correct/Incorrect',
                    'Timestamp'
                ])
                print(f"Created new merged table at {merged_table_path}")
            
            # Write new predictions
            for prediction in new_predictions:
                writer.writerow(prediction)
            
            csvfile.flush()
            os.fsync(csvfile.fileno())
            
        print(f"Appended {len(new_predictions)} new predictions to {merged_table_path}")
        
    except Exception as e:
        print(f"Error appending to merged table: {e}")


def process_csv_with_clip(input_csv,
                          output_csv=None,
                          model_names=("ViT-B/32",),
                          device="cpu",
                          model_weights=None,
                          temperature=0.07,
                          merged_table_path="data_files/merged_clip_predictions.csv",
                          force_reprocess=False,
                          update_merged=True):
    """
    Process any CSV file containing image paths and add CLIP predictions
    Output format matches clip_ground_truth_evaluation_results_simplified_descriptions.csv

    Args:
        input_csv (str): Path to input CSV file
        output_csv (str): Path to output CSV file (optional)
        model_names (tuple|list): CLIP models for ensemble
        device (str): 'cpu' or 'cuda'
        model_weights (list[float]|None): Optional weights per model
        temperature (float): Logits temperature scaling before softmax
        merged_table_path (str): Path to merged predictions table
        force_reprocess (bool): Force reprocessing even if prediction exists
        update_merged (bool): Whether to update the merged table with new predictions
    """
    # Load existing predictions cache (unless force reprocessing)
    predictions_cache = {}
    new_predictions = []
    
    if not force_reprocess:
        print(f"Loading existing predictions from: {merged_table_path}")
        predictions_cache = load_merged_predictions(merged_table_path)
    else:
        print("Force reprocessing enabled - skipping duplicate check")
    
    # Initialize CLIP classifier (ensemble) - only if we might need it
    classifier = None
    classifier_initialized = False
    
    def ensure_classifier():
        nonlocal classifier, classifier_initialized
        if not classifier_initialized:
            print("Initializing CLIP classifier...")
            classifier = CLIPImageClassifier(
                model_names=model_names,
                device=device,
                model_weights=model_weights,
                temperature=temperature
            )
            classifier_initialized = True

    # Set default output filename if not provided
    if output_csv is None:
        # For ground_truth_template_with_clip_predictions.csv, overwrite the same file
        if "ground_truth_template_with_clip_predictions" in input_csv:
            output_csv = input_csv  # Overwrite the same file
        else:
            base_name = os.path.splitext(os.path.basename(input_csv))[0]
            input_dir = os.path.dirname(os.path.abspath(input_csv))
            
            # Check if we're already in a data_files directory
            if input_dir.endswith("data_files"):
                # Use the same directory (don't create nested data_files)
                out_dir = input_dir
            else:
                # Create data_files subdirectory
                out_dir = os.path.join(input_dir, "data_files")
                os.makedirs(out_dir, exist_ok=True)
            
            output_csv = os.path.join(out_dir, f"{base_name}_with_clip_predictions.csv")

    print(f"Reading input CSV: {input_csv}")

    try:
        # Read input CSV
        df = pd.read_csv(input_csv)
        print(f"Found {len(df)} rows to process")

        # Auto-detect image path column
        image_path_column = None
        possible_columns = ['Image Path', 'image_path', 'path', 'Image_Path', 'Filename', 'filename']

        for col in possible_columns:
            if col in df.columns:
                image_path_column = col
                break

        if image_path_column is None:
            # Use first column as fallback
            image_path_column = df.columns[0]
            print(f"Warning: Could not auto-detect image path column. Using '{image_path_column}'")
        else:
            print(f"Using '{image_path_column}' as image path column")

        # Auto-detect other columns
        filename_column = None
        ground_truth_column = None
        notes_column = None

        for col in df.columns:
            col_lower = col.lower()
            if 'filename' in col_lower and filename_column is None:
                filename_column = col
            elif 'ground' in col_lower and 'truth' in col_lower and ground_truth_column is None:
                ground_truth_column = col
            elif 'note' in col_lower and notes_column is None:
                notes_column = col

        # Prepare results
        results = []

        # Process each row
        skipped_count = 0
        processed_count = 0
        
        for idx, row in df.iterrows():
            raw_image_path = row[image_path_column]
            
            # Skip empty rows (where image path is NaN or empty)
            if pd.isna(raw_image_path) or str(raw_image_path).strip() == "":
                print(f"  Skipping row {idx + 1}: Empty image path")
                continue
                
            image_path = resolve_image_path(input_csv, raw_image_path)

            # Extract filename from path if filename column not found
            if filename_column and pd.notna(row.get(filename_column, None)):
                image_name = row[filename_column]
            else:
                image_name = os.path.basename(str(raw_image_path)) if isinstance(raw_image_path, str) else "unknown"

            # Extract ground truth if available
            ground_truth_category = ""
            if ground_truth_column and pd.notna(row.get(ground_truth_column, None)):
                ground_truth_category = str(row[ground_truth_column]).strip()

            # Extract notes if available
            notes = "nan"
            if notes_column and pd.notna(row.get(notes_column, None)):
                notes = str(row[notes_column])

            print(f"Processing {idx + 1}/{len(df)}: {image_name}")

            # Check for existing prediction (unless force reprocessing)
            cached_prediction = None
            if not force_reprocess:
                cached_prediction = check_image_in_cache(str(raw_image_path), predictions_cache)
                
            if cached_prediction:
                print(f"  Found existing prediction - using cached result")
                skipped_count += 1
                
                # Use cached prediction but update ground truth if current CSV has it
                result = [
                    str(raw_image_path),
                    image_name,
                    ground_truth_category if ground_truth_category else cached_prediction['ground_truth'],
                    notes if notes != "nan" else cached_prediction['notes'],
                    cached_prediction['clip_category'],
                    cached_prediction['clip_confidence'],
                    cached_prediction['clip_description'],
                    cached_prediction['correct_incorrect'],
                    cached_prediction['timestamp']
                ]
                
                # Recalculate correct/incorrect if we have new ground truth
                if ground_truth_category and ground_truth_category != cached_prediction['ground_truth']:
                    ground_truth_normalized = normalize_category(ground_truth_category)
                    clip_category_normalized = normalize_category(cached_prediction['clip_category'])
                    if clip_category_normalized and clip_category_normalized == ground_truth_normalized:
                        result[7] = "Correct"
                    else:
                        result[7] = "Incorrect"
                
                results.append(result)
                continue

            # Check if image exists
            if not (isinstance(image_path, str) and os.path.exists(image_path)):
                print(f"  Warning: Image not found at {raw_image_path}")
                error_result = [
                    str(raw_image_path),
                    image_name,
                    ground_truth_category,
                    notes,
                    "FILE NOT FOUND",
                    "Low",
                    "Error: Image file not found",
                    "N/A",
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                ]
                results.append(error_result)
                if update_merged:
                    new_predictions.append(error_result)
                continue

            # Initialize classifier if needed
            ensure_classifier()
            processed_count += 1

            # Run CLIP classification
            try:
                clip_category, clip_confidence, clip_description = classifier.classify_image(image_path)

                # Determine if prediction is correct (if ground truth available)
                correct_incorrect = "N/A"
                if ground_truth_category:
                    # Normalize ground truth and prediction for comparison
                    ground_truth_normalized = normalize_category(ground_truth_category)
                    clip_category_normalized = normalize_category(clip_category)
                    if clip_category_normalized and clip_category_normalized == ground_truth_normalized:
                        correct_incorrect = "Correct"
                    else:
                        correct_incorrect = "Incorrect"

                # Add result (maintain original required output structure)
                result = [
                    str(raw_image_path),                  # keep the original path as in the CSV
                    image_name,
                    ground_truth_category,
                    notes,
                    clip_category,
                    clip_confidence,
                    clip_description,
                    correct_incorrect,
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                ]
                
                results.append(result)
                if update_merged:
                    new_predictions.append(result)

                print(f"  CLIP Prediction: {clip_category} ({clip_confidence})")
                if ground_truth_category:
                    print(f"  Ground Truth: {ground_truth_category}")
                    print(f"  Result: {correct_incorrect}")

            except Exception as e:
                print(f"  Error processing image: {e}")
                error_result = [
                    str(raw_image_path),
                    image_name,
                    ground_truth_category,
                    notes,
                    "ERROR",
                    "Low",
                    f"Error: {str(e)}",
                    "N/A",
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                ]
                results.append(error_result)
                if update_merged:
                    new_predictions.append(error_result)
        
        # Print processing summary
        print(f"\nProcessing Summary:")
        print(f"  Total rows: {len(df)}")
        print(f"  Used cached predictions: {skipped_count}")
        print(f"  Newly processed: {processed_count}")
        print(f"  New predictions to add to merged table: {len(new_predictions)}")

        # Save results to CSV in simplified structure format
        print(f"\nSaving results to: {output_csv}")
        print(f"Total results to write: {len(results)}")
        os.makedirs(os.path.dirname(os.path.abspath(output_csv)), exist_ok=True)
        
        try:
            with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                # Write header (same as simplified descriptions file)
                writer.writerow([
                    'Image Path',
                    'Image Name',
                    'Ground Truth Category',
                    'Notes',
                    'CLIP Predicted Category',
                    'CLIP Confidence',
                    'CLIP Description',
                    'Correct/Incorrect',
                    'Timestamp'
                ])
                
                # Write results one by one with error handling
                for i, result in enumerate(results):
                    try:
                        writer.writerow(result)
                        if i % 10 == 0 or i == len(results) - 1:
                            print(f"  Written {i + 1}/{len(results)} rows")
                    except Exception as e:
                        print(f"  Error writing row {i + 1}: {e}")
                        print(f"  Problematic row data: {result}")
                        # Try to write a sanitized version
                        try:
                            sanitized_result = [str(item).encode('utf-8', errors='ignore').decode('utf-8') for item in result]
                            writer.writerow(sanitized_result)
                            print(f"  Successfully wrote sanitized version of row {i + 1}")
                        except Exception as e2:
                            print(f"  Failed to write sanitized version: {e2}")
                
                # Explicitly flush the file
                csvfile.flush()
                os.fsync(csvfile.fileno())
                print(f"Successfully flushed all data to file")
                
        except Exception as e:
            print(f"Error opening/writing CSV file: {e}")
            return

        # Calculate and display accuracy if ground truth available
        correct_count = sum(1 for result in results if result[7] == "Correct")
        total_valid = sum(1 for result in results if result[7] in ["Correct", "Incorrect"])

        print(f"\nProcessing Results:")
        print(f"Total images processed: {len(results)}")

        if total_valid > 0:
            accuracy = (correct_count / total_valid) * 100
            print(f"Images with ground truth: {total_valid}")
            print(f"Correct predictions: {correct_count}")
            print(f"Accuracy: {accuracy:.2f}%")
        else:
            print("No ground truth data available for accuracy calculation")

        # Update merged table with new predictions
        if update_merged and new_predictions:
            print(f"\nUpdating merged table...")
            append_to_merged_table(merged_table_path, new_predictions)

        print(f"\nResults saved to: {output_csv}")
        print("Output format matches clip_ground_truth_evaluation_results_simplified_descriptions.csv")

    except Exception as e:
        print(f"Error processing CSV file: {e}")
        return


def parse_args():
    parser = argparse.ArgumentParser(description="Process CSVs with CLIP ensemble")
    parser.add_argument("input", nargs="?", help="Path to input CSV or feature name")
    parser.add_argument("output_csv", nargs="?", help="Path to output CSV (optional)")
    
    # Feature mode options
    parser.add_argument("--feature-mode", action="store_true",
                        help="Treat input as a feature name instead of CSV path")
    
    # Model configuration
    parser.add_argument("--models", type=str, default="ViT-B/32,ViT-L/14",
                        help="Comma-separated CLIP models, e.g., 'ViT-B/32,ViT-L/14'")
    parser.add_argument("--device", type=str, default="cpu", choices=["cpu", "cuda"],
                        help="Device to run inference on")
    parser.add_argument("--weights", type=str, default=None,
                        help="Comma-separated weights matching models, e.g., '0.2,0.4,0.4'")
    parser.add_argument("--temperature", type=float, default=0.07,
                        help="Temperature for logits scaling (e.g., 0.05–0.3)")
    
    # Duplicate checking and merged table options
    parser.add_argument("--merged-table", type=str, default="data_files/merged_clip_predictions.csv",
                        help="Path to merged predictions table for duplicate checking")
    parser.add_argument("--force-reprocess", action="store_true",
                        help="Force reprocessing of all images, ignoring cached predictions")
    parser.add_argument("--no-update-merged", action="store_true",
                        help="Don't update the merged table with new predictions")
    
    return parser.parse_args()


def main():
    print("=" * 60)
    print("Extended Simple CLIP Pipeline")
    print("=" * 60)

    args = parse_args()
    
    # Import sys for feature mode
    import sys

    # Determine if we're in feature mode or CSV mode
    feature_mode = args.feature_mode
    input_value = args.input
    
    # If no input provided, show usage
    if not input_value:
        print("Usage:")
        print("  Feature mode: python simple_clip_pipeline_extended.py --feature-mode Power_Management")
        print("  CSV mode:     python simple_clip_pipeline_extended.py path/to/input.csv [path/to/output.csv]")
        print("\nAvailable options:")
        print("  --feature-mode: Treat input as a feature name")
        print("  --models:       Comma-separated CLIP models (default: ViT-B/32,ViT-L/14)")
        print("  --device:       Device to run on (cpu or cuda, default: cpu)")
        print("  --force-reprocess: Force reprocessing all images")
        return
    
    # FEATURE MODE: Auto-generate CSV and run CLIP classification
    if feature_mode:
        feature_name = input_value
        print(f"🚀 Running in feature mode for: {feature_name}")
        
        # Step 1: Check if base CSV exists, if not generate it
        base_csv = f"data_files/{feature_name}.csv"
        if not Path(base_csv).exists():
            print(f"📁 Base CSV not found: {base_csv}")
            print("🔧 Auto-generating CSV from feature directory...")
            if not auto_generate_csv(feature_name):
                print(f"\n❌ Failed to generate CSV for {feature_name}")
                sys.exit(1)
        else:
            print(f"✅ Base CSV found: {base_csv}")
        
        # Step 2: Process the CSV with CLIP
        output_csv = f"data_files/{feature_name}_with_clip_predictions.csv"
        
        model_names = [m.strip() for m in args.models.split(",") if m.strip()]
        model_weights = [float(x) for x in args.weights.split(",")] if args.weights else None
        
        process_csv_with_clip(
            base_csv,
            output_csv,
            model_names=model_names,
            device=args.device,
            model_weights=[0.7, 0.3],
            temperature=args.temperature,
            merged_table_path=args.merged_table,
            force_reprocess=args.force_reprocess,
            update_merged=not args.no_update_merged
        )
        
        print(f"\n✅ Feature processing complete for {feature_name}!")
        print(f"📊 Results saved to: {output_csv}")
        print("\nNext step: Run vision analysis with:")
        print(f"python scripts/automated_vision_pipeline.py {feature_name}")
        
    # CSV MODE: Process a specific CSV file
    else:
        input_csv = input_value
        print(f"Processing CSV file: {input_csv}")
        
        model_names = [m.strip() for m in args.models.split(",") if m.strip()]
        model_weights = [float(x) for x in args.weights.split(",")] if args.weights else None

        process_csv_with_clip(
            input_csv,
            args.output_csv,
            model_names=model_names,
            device=args.device,
            model_weights=[0.7, 0.3],
            temperature=args.temperature,
            merged_table_path=args.merged_table,
            force_reprocess=args.force_reprocess,
            update_merged=not args.no_update_merged
        )
        
        print("\nPipeline completed!")


if __name__ == "__main__":
    main()
