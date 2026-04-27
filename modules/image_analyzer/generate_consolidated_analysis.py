#!/usr/bin/env python3
"""
Generate consolidated analysis for a feature using all individual image analyses.
This script sends the CONSOLIDATED_IMAGE_ANALYSIS prompt with all analysis files to the Vision API.
"""

import argparse
import os
import sys
from pathlib import Path
from litellm import completion

# Add utils to path for environment management
sys.path.append(str(Path(__file__).parent.parent))
from utils.env_manager import env_manager

# HARMAN API configuration
HARMAN_BASE_URL = "https://brllm.harman.com"
DEFAULT_MODEL = "openai/sonnet-4-asia"

def load_prompt_template():
    """Load the consolidated analysis prompt template"""
    prompt_path = Path("modules/image_analyzer/prompts/CONSOLIDATED_IMAGE_ANALYSIS_v1.0.md")
    if not prompt_path.exists():
        print(f"❌ Prompt template not found: {prompt_path}")
        return None
    
    with open(prompt_path, 'r', encoding='utf-8') as f:
        return f.read()

def find_feature_directory(feature_name):
    """Find the feature directory in analysis_results"""
    analysis_dir = Path("data/results")
    if not analysis_dir.exists():
        print(f"❌ Analysis results directory not found: {analysis_dir}")
        return None
    
    # Look for exact match first
    feature_dir = analysis_dir / feature_name
    if feature_dir.exists():
        return feature_dir
    
    # Look for partial matches
    matching_dirs = [d for d in analysis_dir.iterdir() if d.is_dir() and feature_name in d.name]
    
    if not matching_dirs:
        print(f"❌ No feature directory found for: {feature_name}")
        print(f"Available features:")
        for d in analysis_dir.iterdir():
            if d.is_dir():
                print(f"  - {d.name}")
        return None
    
    if len(matching_dirs) > 1:
        print(f"❌ Multiple matching directories found for '{feature_name}':")
        for d in matching_dirs:
            print(f"  - {d.name}")
        print("Please use the exact directory name.")
        return None
    
    return matching_dirs[0]

def collect_analysis_files(feature_dir):
    """Collect all individual analysis files for the feature"""
    analysis_files = []
    
    # Skip the consolidated file (c.txt) if it exists
    for file_path in feature_dir.iterdir():
        if file_path.is_file() and file_path.suffix == '.txt' and file_path.name != 'c.txt':
            analysis_files.append(file_path)
    
    if not analysis_files:
        print(f"❌ No analysis files found in: {feature_dir}")
        return []
    
    # Sort files by name for consistent ordering
    analysis_files.sort(key=lambda x: x.name)
    return analysis_files

def read_analysis_files(analysis_files):
    """Read content from all analysis files"""
    file_contents = []
    
    for file_path in analysis_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                file_contents.append(f"=== FILE: {file_path.name} ===\n{content}\n")
        except Exception as e:
            print(f"⚠️  Warning: Could not read {file_path.name}: {e}")
    
    return "\n".join(file_contents)

def generate_consolidated_analysis(feature_name, analysis_content, prompt_template, model, api_key):
    """Send request to Vision API for consolidated analysis"""
    
    # Prepare the full prompt
    full_prompt = f"""
{prompt_template}

=== FEATURE TO ANALYZE ===
Feature Name: {feature_name}

=== INDIVIDUAL ANALYSIS FILES ===
{analysis_content}

Please generate a consolidated analysis following the format specified in the prompt template above.
"""
    
    print("🌐 Making API call for consolidated analysis...")
    try:
        response = completion(
            model=model,
            max_tokens=8000,  # Increased for comprehensive consolidated analysis
            messages=[{
                "role": "user",
                "content": full_prompt
            }],
            api_key=api_key,
            base_url=HARMAN_BASE_URL
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        print(f"❌ API call failed: {e}")
        return None

def save_consolidated_analysis(feature_dir, content, output_filename):
    """Save the consolidated analysis to the feature directory"""
    output_path = feature_dir / output_filename
    
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return output_path
    except Exception as e:
        print(f"❌ Failed to save consolidated analysis: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(
        description="Generate consolidated analysis for a feature",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/generate_consolidated_analysis.py --feature VEH-F165_Manettino
  python scripts/generate_consolidated_analysis.py --feature VEH-F247_External_Lights_Management --output consolidated_summary.txt
  python scripts/generate_consolidated_analysis.py --feature DMS-7 --model openai/gpt-4-vision
        """
    )
    
    parser.add_argument(
        '--feature', 
        required=True,
        help='Feature name (directory name in analysis_results)'
    )
    
    parser.add_argument(
        '--output', 
        default='c.txt',
        help='Output filename (default: c.txt)'
    )
    
    parser.add_argument(
        '--model', 
        default=DEFAULT_MODEL,
        help=f'Model to use (default: {DEFAULT_MODEL})'
    )
    
    args = parser.parse_args()
    
    print(f"🚀 Starting consolidated analysis for feature: {args.feature}")
    
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
    
    # Step 1: Load prompt template
    print("📝 Loading prompt template...")
    prompt_template = load_prompt_template()
    if not prompt_template:
        sys.exit(1)
    print(f"✅ Prompt template loaded ({len(prompt_template)} chars)")
    
    # Step 2: Find feature directory
    print(f"📁 Looking for feature directory: {args.feature}")
    feature_dir = find_feature_directory(args.feature)
    if not feature_dir:
        sys.exit(1)
    print(f"✅ Found feature directory: {feature_dir}")
    
    # Step 3: Collect analysis files
    print("📄 Collecting individual analysis files...")
    analysis_files = collect_analysis_files(feature_dir)
    if not analysis_files:
        sys.exit(1)
    print(f"✅ Found {len(analysis_files)} analysis files:")
    for file_path in analysis_files:
        print(f"  - {file_path.name}")
    
    # Step 4: Read analysis content
    print("📖 Reading analysis file contents...")
    analysis_content = read_analysis_files(analysis_files)
    if not analysis_content:
        print("❌ No content could be read from analysis files")
        sys.exit(1)
    print(f"✅ Analysis content loaded ({len(analysis_content)} chars)")
    
    # Step 5: Generate consolidated analysis
    print(f"🤖 Generating consolidated analysis using model: {args.model}")
    consolidated_analysis = generate_consolidated_analysis(
        args.feature, 
        analysis_content, 
        prompt_template, 
        args.model, 
        api_key
    )
    
    if not consolidated_analysis:
        print("❌ Failed to generate consolidated analysis")
        sys.exit(1)
    
    print(f"✅ Consolidated analysis generated ({len(consolidated_analysis)} chars)")
    
    # Step 6: Save consolidated analysis
    print(f"💾 Saving consolidated analysis to: {args.output}")
    output_path = save_consolidated_analysis(feature_dir, consolidated_analysis, args.output)
    
    if not output_path:
        sys.exit(1)
    
    print(f"🎉 SUCCESS! Consolidated analysis saved to: {output_path}")
    print(f"📊 Analysis length: {len(consolidated_analysis)} characters")
    
    # Show preview
    print("\n" + "="*60)
    print("CONSOLIDATED ANALYSIS PREVIEW:")
    print("="*60)
    preview = consolidated_analysis[:500] + "..." if len(consolidated_analysis) > 500 else consolidated_analysis
    print(preview)
    print("="*60)

if __name__ == "__main__":
    main()
