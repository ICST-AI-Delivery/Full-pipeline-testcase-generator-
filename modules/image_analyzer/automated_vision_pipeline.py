#!/usr/bin/env python3
"""
Automated Vision Analysis Pipeline
Processes CLIP-classified images with specialized prompts using Claude API

This script assumes the CSV with CLIP predictions already exists.
Use simple_clip_pipeline.py first to generate the CSV with CLIP predictions.
"""

import os
import sys
import pandas as pd
import base64
from pathlib import Path
from litellm import completion

# Add utils to path for environment management
sys.path.append(str(Path(__file__).parent.parent))
from utils.env_manager import env_manager


# =============================================================================
# CONFIGURATION - API key loaded from environment
# =============================================================================
# API key is now loaded from environment variables via .env file

# Category to prompt file mapping
CATEGORY_PROMPTS = {
    "HMI DISPLAY LAYOUTS": "01_HMI_DISPLAY_LAYOUTS_v1.0.md",
    "CONFIGURATION TABLES": "02_CONFIGURATION_TABLES_v1.0.md",
    "SYSTEM ARCHITECTURE DIAGRAMS": "03_SYSTEM_ARCHITECTURE_DIAGRAMS_v2.0_ENHANCED.md",
    "STATE FLOW DIAGRAMS": "04_STATE_FLOW_DIAGRAMS_v2.1_SEQUENTIAL_MATRIX.md",
    "TABLE WITH TELLTALES": "04_TABLE_WITH_TELLTALES_v1.0_SPECIALIZED.md",
    "TIMING DIAGRAMS": "05_TIMING_DIAGRAMS_v6.0_SYSTEMATIC_STATE_MATRIX.md",
    "DECISION LOGIC TABLES": "06_DECISION_LOGIC_TABLES_v1.0.md",
    "INTERFACE SPECIFICATIONS": "07_INTERFACE_SPECIFICATIONS_v1.0.md",
    "REQUIREMENT SPECIFICATIONS": "08_REQUIREMENT_SPECIFICATIONS_v1.0.md",
    "PROCESS FLOW DIAGRAMS": "09_PROCESS_FLOW_DIAGRAMS_v5.0_ARROW_DIRECTION_FOCUSED.md",
    "TELLTALE ICONS & INDICATORS": "10_TELLTALES_AND_ICONS_v1.0.md",
    "ERROR HANDLING DIAGRAMS": "10_ERROR_HANDLING_DIAGRAMS_v1.0.md",
    "COLOR GRADIENTS": "10_COLOR_GRADIENTS_v1.0_SPECIALIZED.md",
    "NETWORK TOPOLOGY DIAGRAMS": "11_NETWORK_TOPOLOGY_DIAGRAMS_v1.0.md",
    "TECHNICAL SPECIFICATIONS": "11_TECHNICAL_SPECIFICATIONS_v2.0_UNIFIED.md",
    "SIGNAL FLOW DIAGRAMS": "12_SIGNAL_FLOW_DIAGRAMS_v1.0.md",
    "GENERAL TECHNICAL DIAGRAMS": "13_GENERAL_TECHNICAL_DIAGRAMS_v1.0.md"
}

def load_prompt(category):
    """Load specialized prompt for given category"""
    prompt_file = CATEGORY_PROMPTS.get(category)
    if not prompt_file:
        print(f"Warning: No prompt mapping for category '{category}', using general analysis")
        return "Please analyze this technical image in detail, focusing on all visible elements, text, symbols, and their relationships."
    
    # Fix path resolution - prompts are in modules/image_analyzer/prompts/
    prompt_path = Path("modules/image_analyzer/prompts") / prompt_file
    if not prompt_path.exists():
        print(f"Warning: Prompt file {prompt_file} not found at {prompt_path}, using general analysis")
        return "Please analyze this technical image in detail, focusing on all visible elements, text, symbols, and their relationships."
    
    try:
        with open(prompt_path, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"✅ Successfully loaded specialized prompt: {prompt_file}")
            return content
    except Exception as e:
        print(f"Error reading prompt file {prompt_file}: {e}")
        return "Please analyze this technical image in detail, focusing on all visible elements, text, symbols, and their relationships."

def encode_image(image_path):
    """Encode image to base64 for Claude API"""
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except Exception as e:
        print(f"Error encoding image {image_path}: {e}")
        return None

def analyze_image(api_key, image_path, prompt_text, image_name):
    """Send image and prompt to HARMAN API for analysis"""
    print(f"  Analyzing {image_name}...")
    
    # Encode image
    image_data = encode_image(image_path)
    if not image_data:
        return None
    
    # Determine image format
    image_format = "image/png"
    if image_path.lower().endswith(('.jpg', '.jpeg')):
        image_format = "image/jpeg"
    
    try:
        response = completion(
            model="openai/sonnet-4.6-asia",
            max_tokens=4000,
            messages=[{
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:{image_format};base64,{image_data}"
                        }
                    },
                    {
                        "type": "text",
                        "text": prompt_text
                    }
                ]
            }],
            api_key=api_key,
            base_url="https://brllm.harman.com",
            max_budget=1000.0  # Increase budget limit
        )

        # LiteLLM response format
        return response.choices[0].message.content
    except Exception as e:
        print(f"  Error analyzing {image_name}: {e}")
        return None


def save_analysis(analysis_text, feature_name, image_name, category):
    """Save analysis to organized file structure"""
    # Create output directory
    output_dir = Path("data/results") / feature_name
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Create filename with category info
    category_short = category.replace(" ", "_").replace("&", "AND")
    output_file = output_dir / f"{image_name.split('.')[0]}_{category_short}_analysis.txt"
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"Image: {image_name}\n")
            f.write(f"Category: {category}\n")
            f.write(f"Analysis Date: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 80 + "\n\n")
            f.write(analysis_text)
        print(f"  Saved: {output_file}")
        return True
    except Exception as e:
        print(f"  Error saving analysis for {image_name}: {e}")
        return False

def process_csv(csv_file, feature_name, api_key):
    """Main processing function"""
    print(f"Processing feature: {feature_name}")
    print(f"CSV file: {csv_file}")
    
    # Read CSV file
    try:
        df = pd.read_csv(csv_file)
        print(f"Found {len(df)} images to process")
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return False
    
    # Process each image
    processed = 0
    skipped = 0
    
    for index, row in df.iterrows():
        image_path = row['Image Path']
        image_name = row['Image Name']
        category = row['CLIP Predicted Category']
        
        # Skip if no category or image path
        if pd.isna(category) or pd.isna(image_path):
            print(f"  Skipping {image_name}: Missing category or path")
            skipped += 1
            continue
        
        # Check if image file exists
        if not Path(image_path).exists():
            print(f"  Skipping {image_name}: Image file not found")
            skipped += 1
            continue
        
        # Load appropriate prompt
        prompt_text = load_prompt(category)
        
        # Analyze image
        analysis = analyze_image(api_key, image_path, prompt_text, image_name)
        if analysis:
            if save_analysis(analysis, feature_name, image_name, category):
                processed += 1
            else:
                skipped += 1
        else:
            skipped += 1
    
    print(f"\nProcessing complete!")
    print(f"Successfully processed: {processed} images")
    print(f"Skipped: {skipped} images")
    print(f"Results saved to: data/results/{feature_name}/")
    
    return True

def main():
    """Command line interface for vision analysis only"""
    if len(sys.argv) < 2:
        print("Usage: python automated_vision_pipeline.py <feature_name>")
        print("Example: python automated_vision_pipeline.py VEH-F165_Manettino")
        print("\nThis will:")
        print("1. Load the CSV with CLIP predictions")
        print("2. Process images with vision analysis using specialized prompts")
        print("\nPrerequisite: Run simple_clip_pipeline.py first to generate the CSV with CLIP predictions")
        print("Command: python scripts/simple_clip_pipeline.py --feature-mode <feature_name>")
        print("\nAPI key is loaded from .env file (HARMAN_API_KEY variable)")
        sys.exit(1)
    
    feature_name = sys.argv[1]
    
    # Get API key from environment
    try:
        api_key = env_manager.get_config_value('HARMAN_API_KEY')
        if not api_key:
            print("❌ Error: HARMAN_API_KEY not found in environment")
            print("Please add HARMAN_API_KEY=your_api_key_here to your .env file")
            sys.exit(1)
    except Exception as e:
        print(f"❌ Error loading API key: {e}")
        sys.exit(1)
    
    print(f"🚀 Starting vision analysis for feature: {feature_name}")
    print("=" * 60)
    
    # Check if CLIP predictions exist
    clip_csv = f"data/processed/{feature_name}_with_clip_predictions.csv"
    if not Path(clip_csv).exists():
        print(f"❌ CLIP predictions not found: {clip_csv}")
        print("Please run simple_clip_pipeline.py first to generate CLIP predictions:")
        print(f"python modules/image_analyzer/simple_clip_pipeline.py --feature-mode {feature_name}")
        sys.exit(1)
    
    # Process images with vision analysis
    print("\n🎯 Starting vision analysis...")
    print("=" * 40)
    success = process_csv(clip_csv, feature_name, api_key)
    
    if success:
        print(f"\n🎉 Vision analysis complete for {feature_name}!")
        print("=" * 60)
        print("📊 Results summary:")
        print(f"   • CLIP CSV: {clip_csv}")
        print(f"   • Analysis results: data/results/{feature_name}/")
    else:
        print(f"\n❌ Vision analysis failed for {feature_name}")
        sys.exit(1)

if __name__ == "__main__":
    main()
