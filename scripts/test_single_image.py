#!/usr/bin/env python3
"""
Test single image processing to isolate the issue
"""

import base64
import sys
from pathlib import Path
from litellm import completion

# Add utils to path for environment management
sys.path.append(str(Path(__file__).parent.parent))
from utils.env_manager import env_manager

# HARMAN API configuration
HARMAN_API_KEY = env_manager.get_config_value('HARMAN_API_KEY')
if not HARMAN_API_KEY:
    print("❌ Error: HARMAN_API_KEY not found in environment")
    print("Please add HARMAN_API_KEY=your_api_key_here to your .env file")
    sys.exit(1)

def encode_image(image_path):
    """Encode image to base64"""
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except Exception as e:
        print(f"Error encoding image: {e}")
        return None

def load_prompt():
    """Load the TELLTALE prompt"""
    prompt_path = Path("modules/image_analyzer/prompts/02_CONFIGURATION_TABLES_v1.0.md")
    if prompt_path.exists():
        with open(prompt_path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        return "Please analyze this image and describe what you see in detail."

def test_image_analysis(image_path):
    """Test analysis of a single image"""
    print(f"Testing image: {image_path}")
    
    # Check if image exists
    if not Path(image_path).exists():
        print(f"❌ Image not found: {image_path}")
        return
    
    # Encode image
    print("📷 Encoding image...")
    image_data = encode_image(image_path)
    if not image_data:
        print("❌ Failed to encode image")
        return
    
    print(f"✅ Image encoded successfully ({len(image_data)} chars)")
    
    # Load prompt
    print("📝 Loading prompt...")
    prompt_text = load_prompt()
    print(f"✅ Prompt loaded ({len(prompt_text)} chars)")
    print(f"📄 Prompt preview: {prompt_text[:100]}...")
    
    # Make API call
    print("🌐 Making API call...")
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
                            "url": f"data:image/png;base64,{image_data}"
                        }
                    },
                    {
                        "type": "text",
                        "text": prompt_text
                    }
                ]
            }],
            api_key=HARMAN_API_KEY,
            base_url="https://brllm.harman.com"
        )
        
        analysis = response.choices[0].message.content
        print("✅ API call successful!")
        print(f"📊 Response length: {len(analysis)} chars")
        print("\n" + "="*50)
        print("ANALYSIS RESULT:")
        print("="*50)
        print(analysis[:500] + "..." if len(analysis) > 500 else analysis)
        
        # Save result
        output_file = f"test_result_{Path(image_path).name}.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"Image: {image_path}\n")
            f.write(f"Analysis Date: 2026-03-23\n")
            f.write("="*50 + "\n\n")
            f.write(analysis)
        
        print(f"\n💾 Full result saved to: {output_file}")
        
    except Exception as e:
        print(f"❌ API call failed: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python test_single_image.py <image_path>")
        print("Example: python test_single_image.py 'Pre-FineTuneLearning Model/SRS FPI export/SRS_Instrument Cluster/VEH-F165_Manettino/image200.png'")
        sys.exit(1)
    
    image_path = sys.argv[1]
    test_image_analysis(image_path)

if __name__ == "__main__":
    main()
