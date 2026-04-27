# CLIP Pipeline Usage Guide

## How to Run the Simple CLIP Pipeline

The `simple_clip_pipeline.py` script can be run in several ways:

### Method 1: Automatic Processing (Easiest)
Simply run the script without any arguments to process all available CSV files:

```bash
python scripts/simple_clip_pipeline.py
```

This will automatically:
- Find and process `ground_truth_template.csv`
- Find and process `additional_images_with_old_clip_descriptions.csv`
- Create output files with `_with_clip_predictions.csv` suffix

### Method 2: Process a Specific CSV File
To process a specific CSV file:

```bash
python scripts/simple_clip_pipeline.py "path/to/your/input.csv"
```

Example:
```bash
python scripts/simple_clip_pipeline.py "data_files/ground_truth_template.csv"
```

### Method 3: Specify Both Input and Output Files
To control both input and output filenames:

```bash
python scripts/simple_clip_pipeline.py "input.csv" "output.csv"
```

Example:
```bash
python scripts/simple_clip_pipeline.py "data_files/ground_truth_template.csv" "data_files/my_results.csv"
```

## What the Pipeline Does

1. **Loads your existing CLIP classifier** (from `clip_classifier.py`)
2. **Auto-detects CSV structure** - Finds columns for:
   - Image paths (looks for: 'Image Path', 'image_path', 'path', etc.)
   - Filenames (looks for: 'Filename', 'filename', etc.)
   - Ground truth (looks for: columns with 'ground' and 'truth')
   - Notes (looks for: columns with 'note')
3. **Processes each image** using CLIP classification
4. **Outputs standardized format** matching `clip_ground_truth_evaluation_results_simplified_descriptions.csv`

## Output Format

The pipeline always creates CSV files with these columns:
- `Image Path`
- `Image Name`
- `Ground Truth Category`
- `Notes`
- `CLIP Predicted Category`
- `CLIP Confidence`
- `CLIP Description`
- `Correct/Incorrect`
- `Timestamp`

## Requirements

Make sure you have:
- Python with required packages (pandas, torch, clip, etc.)
- The `clip_classifier.py` file in the scripts folder
- Image files accessible at the paths specified in your CSV

## Example Usage Session

```bash
# Navigate to your project directory
cd "c:\Users\Sleahu\OneDrive - HARMAN\Desktop\Picture Analyze Agent\Picture Analyze Agent"

# Run the pipeline automatically
python scripts/simple_clip_pipeline.py

# Or process a specific file
python scripts/simple_clip_pipeline.py "data_files/my_images.csv"
```

## Troubleshooting

- **"File not found" errors**: Check that image paths in your CSV are correct
- **Column detection issues**: The script will show which columns it's using
- **Memory issues**: The script uses CPU by default; change to "cuda" in the code if you have GPU
- **Permission errors**: Make sure you can write to the output directory

## Output Files Created

When you run the pipeline, it creates new CSV files with your CLIP predictions:
- `ground_truth_template_with_clip_predictions.csv`
- `additional_images_with_old_clip_descriptions_with_clip_predictions.csv`
- Or custom names if you specify them

These files maintain the exact same structure as your `clip_ground_truth_evaluation_results_simplified_descriptions.csv` for consistency.
