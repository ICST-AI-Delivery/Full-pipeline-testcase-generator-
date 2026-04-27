#!/usr/bin/env python3
"""
Path Correction Utility for CSV Files
Fixes image paths in CSV files to work with the enhanced path resolution system.
"""

import os
import csv
import argparse
import pandas as pd
from pathlib import Path


def normalize_path_separators(path_str):
    """Convert path separators to the OS-appropriate format."""
    if not isinstance(path_str, str):
        return path_str
    return path_str.replace('/', os.sep).replace('\\', os.sep)


def find_image_file(image_path, search_dirs):
    """
    Try to find an image file in various search directories.
    Returns the corrected path if found, None otherwise.
    """
    if not isinstance(image_path, str) or not image_path:
        return None
    
    # If absolute path and exists, return as-is
    if os.path.isabs(image_path) and os.path.exists(image_path):
        return image_path
    
    # Normalize path separators
    normalized_path = normalize_path_separators(image_path)
    
    # Try each search directory
    for search_dir in search_dirs:
        candidate = os.path.join(search_dir, normalized_path)
        if os.path.exists(candidate):
            # Return relative path from current working directory
            try:
                return os.path.relpath(candidate, os.getcwd())
            except ValueError:
                # If relpath fails (different drives on Windows), return absolute
                return os.path.abspath(candidate)
    
    return None


def fix_csv_paths(input_csv, output_csv=None, dry_run=False):
    """
    Fix image paths in a CSV file.
    
    Args:
        input_csv (str): Path to input CSV file
        output_csv (str): Path to output CSV file (optional, defaults to input_csv)
        dry_run (bool): If True, only report what would be changed without modifying files
    """
    if output_csv is None:
        output_csv = input_csv
    
    # Define search directories (in order of preference)
    current_dir = os.getcwd()
    search_dirs = [
        current_dir,  # Current working directory
        os.path.dirname(current_dir),  # Parent directory (useful when running from scripts/)
        os.path.join(current_dir, "Pre-FineTuneLearning Model"),  # Direct subdirectory
        os.path.join(os.path.dirname(current_dir), "Pre-FineTuneLearning Model"),  # Parent's subdirectory
    ]
    
    print(f"Reading CSV: {input_csv}")
    print(f"Search directories:")
    for i, search_dir in enumerate(search_dirs, 1):
        print(f"  {i}. {search_dir}")
    
    try:
        # Read the CSV file
        df = pd.read_csv(input_csv)
        print(f"Found {len(df)} rows")
        
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
        
        # Track changes
        fixed_count = 0
        not_found_count = 0
        already_correct_count = 0
        
        # Process each row
        for idx, row in df.iterrows():
            original_path = row[image_path_column]
            
            if not isinstance(original_path, str) or not original_path:
                continue
            
            # Check if current path already works
            if os.path.exists(original_path):
                already_correct_count += 1
                continue
            
            # Try to find the correct path
            corrected_path = find_image_file(original_path, search_dirs)
            
            if corrected_path:
                if dry_run:
                    print(f"Row {idx + 1}: Would fix '{original_path}' -> '{corrected_path}'")
                else:
                    df.at[idx, image_path_column] = corrected_path
                    print(f"Row {idx + 1}: Fixed '{original_path}' -> '{corrected_path}'")
                fixed_count += 1
            else:
                print(f"Row {idx + 1}: Could not find '{original_path}'")
                not_found_count += 1
        
        # Print summary
        print(f"\nSummary:")
        print(f"  Already correct: {already_correct_count}")
        print(f"  Fixed: {fixed_count}")
        print(f"  Not found: {not_found_count}")
        print(f"  Total: {len(df)}")
        
        # Save the corrected CSV (unless dry run)
        if not dry_run and fixed_count > 0:
            print(f"\nSaving corrected CSV to: {output_csv}")
            df.to_csv(output_csv, index=False)
            print("File saved successfully!")
        elif dry_run:
            print(f"\nDry run completed. Use --fix to apply changes.")
        elif fixed_count == 0:
            print(f"\nNo changes needed.")
        
    except Exception as e:
        print(f"Error processing CSV file: {e}")
        return False
    
    return True


def main():
    parser = argparse.ArgumentParser(description="Fix image paths in CSV files")
    parser.add_argument("input_csv", help="Path to input CSV file")
    parser.add_argument("output_csv", nargs="?", help="Path to output CSV file (optional)")
    parser.add_argument("--dry-run", action="store_true", 
                        help="Show what would be changed without modifying files")
    parser.add_argument("--fix", action="store_true",
                        help="Apply the fixes (opposite of --dry-run)")
    
    args = parser.parse_args()
    
    # Default to dry run unless --fix is specified
    dry_run = not args.fix if not args.dry_run else args.dry_run
    
    print("=" * 60)
    print("CSV Path Correction Utility")
    print("=" * 60)
    
    if dry_run:
        print("DRY RUN MODE - No files will be modified")
        print("Use --fix to apply changes")
        print("-" * 40)
    
    success = fix_csv_paths(args.input_csv, args.output_csv, dry_run=dry_run)
    
    if success:
        print("\nPath correction completed successfully!")
    else:
        print("\nPath correction failed!")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
