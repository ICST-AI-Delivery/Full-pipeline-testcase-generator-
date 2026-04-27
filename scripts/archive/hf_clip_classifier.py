"""
Hugging Face CLIP-based Image Classifier for Automotive Technical Diagrams
Corporate-friendly alternative using transformers library
"""

import os
import csv
import torch
import numpy as np
from PIL import Image
from datetime import datetime
from transformers import CLIPProcessor, CLIPModel

class HFCLIPImageClassifier:
    def __init__(self, model_name="openai/clip-vit-base-patch32", device="cpu"):
        """
        Initialize Hugging Face CLIP model for image classification
        
        Args:
            model_name (str): Hugging Face CLIP model to use
            device (str): Device to run inference on ('cpu' or 'cuda')
        """
        self.device = device
        print(f"Loading Hugging Face CLIP model: {model_name}")
        
        # Load model and processor
        self.model = CLIPModel.from_pretrained(model_name)
        self.processor = CLIPProcessor.from_pretrained(model_name)
        self.model.to(device)
        
        # Standardized automotive diagram categories (from clip_classifier.py)
        self.categories = {
            "HMI DISPLAY LAYOUTS": (
                "A full instrument-cluster screen showing multiple UI regions together (speed/RPM/fuel/warnings). "
                "A single cohesive dashboard display, NOT a lone warning icon and NOT a blocky flowchart of boxes and arrows."
            ),
            "CONFIGURATION TABLES": (
                "A technical table with rows and columns whose cells contain only text or numbers. "
                "May include borders, headers, or colored/shaded text BUT NOT COLORED ICONS "
                "but NO pictogram shapes or dashboard symbols. No icon silhouettes in any cell."
            ),
            "MULTI-CONDITION LOGIC": (
                "A logic-gate diagram combining conditions with AND and OR gate symbols. "
                "Rectangular condition blocks feed into gate icons; outputs chain through gates. Not a module block diagram."
            ),
            "SYSTEM ARCHITECTURE DIAGRAMS": (
                "A block diagram of modules (ECUs, sensors, controllers) as rectangular boxes connected by lines or arrows. "
                "Focus on components and data or wiring connections; no logic gate symbols."
            ),
            "STATE FLOW DIAGRAMS": (
                "A state machine diagram with circular/oval states connected by arrows and labeled transitions. "
                "Emphasis on state bubbles and directional connectors. NOT a waveform with a horizontal time axis."
            ),
            "FLOWCHART DIAGRAMS": (
                "Process flow diagrams showing sequential steps and decision logic with connected shapes. "
                "Contains rectangular process boxes, diamond decisions with Yes/No branches, start/end terminators, and arrows for workflow. "
                "Must not contain a horizontal time axis with stacked HIGH/LOW waveform rows."
            ),
            "TECHNICAL SPECIFICATIONS": (
                "A document-style page dominated by paragraphs, bullet lists, or headings. "
                "May include small text-only tables, but the page is mostly text blocks. "
                "NOT a dense spreadsheet grid and NOT a table of pictogram icons; no dashboard symbol shapes."
            ),
            "WIRING & SIGNAL DIAGRAMS": "Electrical wiring schematic with wires, connectors, pins, and circuit lines.",
            "TIMING DIAGRAMS": (
                "Digital timing diagram with a horizontal time axis, stacked HIGH/LOW waveform rows, "
                "rectangular step transitions, and vertical alignment guides. Shows signal states over time, "
                "with synchronized markers and temporal relationships. Not a flowchart or wiring schematic."
            ),
            "TIMING – ANALOG / THRESHOLD": (
                "A plot versus time or parameter with axes and units. "
                "Single or few continuous traces (ramps, slopes) and threshold markers, or ON/OFF versus a non‑time variable such as speed or temperature."
            ),
            "TABLE WITH TELLTALES": (
                "A table that contains automotive warning pictograms INSIDE its cells. "
                "At least one cell shows a recognizable colored image with an icon (battery, oil lamp, ABS, seatbelt), i.e., a drawn symbol with an outline. "
                "Not just colored or shaded cells—must be a visible pictogram."
            ),
            "COLOR AND GRADIENTS": "Color chart, gradient scale, or color calibration pattern. No text or icons.",
            "TELLTALE ICONS & INDICATORS": "Single isolated car warning icon or symbol on a plain background with no other dashboard elements. Only one warning light (battery, oil, temperature, etc.)."
        }
        
        # Prepare text inputs for classification
        self.category_names = list(self.categories.keys())
        self.text_descriptions = list(self.categories.values())
        
        print(f"Initialized HF CLIP classifier with {len(self.categories)} categories")
    
    def classify_image(self, image_path):
        """
        Classify a single image using Hugging Face CLIP zero-shot classification
        
        Args:
            image_path (str): Path to the image file
            
        Returns:
            tuple: (category, confidence, description)
        """
        try:
            # Load and preprocess image
            image = Image.open(image_path).convert('RGB')
            
            # Prepare inputs
            inputs = self.processor(
                text=self.text_descriptions,
                images=image,
                return_tensors="pt",
                padding=True
            )
            
            # Move to device
            inputs = {k: v.to(self.device) for k, v in inputs.items()}
            
            # Perform classification
            with torch.no_grad():
                outputs = self.model(**inputs)
                logits_per_image = outputs.logits_per_image
                probs = logits_per_image.softmax(dim=1).cpu().numpy()[0]
            
            # Get best prediction
            best_idx = np.argmax(probs)
            category = self.category_names[best_idx]
            confidence_score = float(probs[best_idx])
            
            # Determine confidence level
            if confidence_score > 0.7:
                confidence = "High"
            elif confidence_score > 0.4:
                confidence = "Medium"
            else:
                confidence = "Low"
            
            # Create description
            description = f"HF-CLIP classification: {self.text_descriptions[best_idx]} (score: {confidence_score:.3f})"
            
            return category, confidence, description
            
        except Exception as e:
            print(f"Error processing {image_path}: {e}")
            return "Unknown", "Low", f"Error: {str(e)}"
    
    def classify_batch(self, image_directory, output_csv="hf_clip_classifications.csv"):
        """
        Process all images in a directory and save results to CSV
        
        Args:
            image_directory (str): Directory containing images
            output_csv (str): Output CSV file path
        """
        print(f"Processing images in: {image_directory}")
        
        # Create CSV file with headers
        with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Image Path', 'Filename', 'Image Type', 'Confidence', 
                           'Visual Characteristics', 'Timestamp'])
        
        # Collect all image files
        image_files = []
        for root, dirs, files in os.walk(image_directory):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                    image_path = os.path.join(root, file)
                    image_files.append((image_path, file))
        
        if not image_files:
            print(f"No image files found in {image_directory}")
            return
        
        print(f"Found {len(image_files)} images to process")
        
        # Process images
        results = []
        for idx, (image_path, filename) in enumerate(image_files, 1):
            print(f"Processing {idx}/{len(image_files)}: {filename}")
            
            category, confidence, description = self.classify_image(image_path)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            # Prepare result
            relative_path = os.path.relpath(image_path, image_directory)
            result = [relative_path, filename, category, confidence, description, timestamp]
            results.append(result)
            
            # Save in batches of 10
            if len(results) >= 10:
                with open(output_csv, mode='a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerows(results)
                results = []
        
        # Save remaining results
        if results:
            with open(output_csv, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(results)
        
        print(f"Classification complete! Results saved to: {output_csv}")
    
    def get_category_probabilities(self, image_path):
        """
        Get probabilities for all categories
        
        Args:
            image_path (str): Path to the image file
            
        Returns:
            dict: Category probabilities
        """
        try:
            image = Image.open(image_path).convert('RGB')
            
            inputs = self.processor(
                text=self.text_descriptions,
                images=image,
                return_tensors="pt",
                padding=True
            )
            
            inputs = {k: v.to(self.device) for k, v in inputs.items()}
            
            with torch.no_grad():
                outputs = self.model(**inputs)
                logits_per_image = outputs.logits_per_image
                probs = logits_per_image.softmax(dim=1).cpu().numpy()[0]
            
            return dict(zip(self.category_names, probs))
            
        except Exception as e:
            print(f"Error processing {image_path}: {e}")
            return {}

def main():
    """
    Example usage of Hugging Face CLIP classifier
    """
    # Initialize classifier
    print("Initializing Hugging Face CLIP classifier...")
    classifier = HFCLIPImageClassifier(device="cpu")  # Use "cuda" if GPU available
    
    # Example 1: Classify single image
    image_path = "F834_image13_SystemArchitecture.png"
    if os.path.exists(image_path):
        print(f"\nSingle Image Classification:")
        print(f"Image: {image_path}")
        
        category, confidence, description = classifier.classify_image(image_path)
        print(f"Category: {category}")
        print(f"Confidence: {confidence}")
        print(f"Description: {description}")
        
        # Show all probabilities
        probs = classifier.get_category_probabilities(image_path)
        print(f"\nAll Category Probabilities:")
        for cat, prob in sorted(probs.items(), key=lambda x: x[1], reverse=True):
            print(f"  {cat}: {prob:.3f}")
    else:
        print(f"Image {image_path} not found. Skipping single image test.")
    
    # Example 2: Batch processing
    static_dir = "static"
    if os.path.exists(static_dir):
        print(f"\nBatch Processing:")
        classifier.classify_batch(static_dir, "hf_clip_results.csv")
    else:
        print(f"Directory '{static_dir}' not found. Skipping batch processing.")

if __name__ == "__main__":
    main()
