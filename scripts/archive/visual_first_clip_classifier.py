"""
Visual-First CLIP Classifier for Automotive Technical Diagrams
Based on actual visual analysis of ground truth images
Focuses on visual characteristics rather than automotive terminology
"""

import os
import csv
import clip
import torch
import numpy as np
from PIL import Image
from datetime import datetime

class VisualFirstCLIPClassifier:
    def __init__(self, model_name="ViT-B/32", device="cpu"):
        """
        Initialize CLIP model with visual-first prompts based on ground truth analysis
        
        Args:
            model_name (str): CLIP model variant to use
            device (str): Device to run inference on ('cpu' or 'cuda')
        """
        self.device = device
        print(f"Loading Visual-First CLIP model: {model_name}")
        self.model, self.preprocess = clip.load(model_name, device=device)
        
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
        self.text_inputs = clip.tokenize(self.text_descriptions).to(device)
        
        print(f"Initialized Visual-First CLIP classifier with {len(self.categories)} categories")
        print("Prompts based on actual visual analysis of ground truth images")
    
    def classify_image(self, image_path):
        """
        Classify a single image using visual-first CLIP zero-shot classification
        
        Args:
            image_path (str): Path to the image file
            
        Returns:
            tuple: (category, confidence, description)
        """
        try:
            # Load and preprocess image
            image = Image.open(image_path).convert('RGB')
            image_input = self.preprocess(image).unsqueeze(0).to(self.device)
            
            # Perform classification
            with torch.no_grad():
                logits_per_image, logits_per_text = self.model(image_input, self.text_inputs)
                probs = logits_per_image.softmax(dim=-1).cpu().numpy()[0]
            
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
            description = f"Visual-First CLIP: {self.text_descriptions[best_idx][:80]}... (score: {confidence_score:.3f})"
            
            return category, confidence, description
            
        except Exception as e:
            print(f"Error processing {image_path}: {e}")
            return "Unknown", "Low", f"Error: {str(e)}"
    
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
            image_input = self.preprocess(image).unsqueeze(0).to(self.device)
            
            with torch.no_grad():
                logits_per_image, logits_per_text = self.model(image_input, self.text_inputs)
                probs = logits_per_image.softmax(dim=-1).cpu().numpy()[0]
            
            return dict(zip(self.category_names, probs))
            
        except Exception as e:
            print(f"Error processing {image_path}: {e}")
            return {}

def update_csv_with_visual_first_clip(csv_path, output_path=None):
    """
    Update existing CSV with Visual-First CLIP classifications
    """
    if output_path is None:
        output_path = csv_path.replace('.csv', '_visual_first_clip.csv')
    
    # Initialize classifier
    classifier = VisualFirstCLIPClassifier(device="cpu")
    
    # Read existing CSV
    rows = []
    with open(csv_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        
        # Add new columns to header
        new_header = header + ['Visual-First CLIP Category', 'Visual-First CLIP Confidence', 'Visual-First CLIP Description']
        rows.append(new_header)
        
        # Process each row
        for row_idx, row in enumerate(reader, 1):
            image_path = row[0]  # First column is Image Path
            print(f"Processing {row_idx}: {image_path}")
            
            # Run Visual-First CLIP classification
            category, confidence, description = classifier.classify_image(image_path)
            
            # Add Visual-First CLIP results to row
            new_row = row + [category, confidence, description]
            rows.append(new_row)
    
    # Write updated CSV
    with open(output_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    
    print(f"Visual-First CLIP results saved to: {output_path}")

if __name__ == "__main__":
    # Test with ground truth template
    csv_path = "data_files/ground_truth_template.csv"
    if os.path.exists(csv_path):
        update_csv_with_visual_first_clip(csv_path)
    else:
        print(f"CSV file not found: {csv_path}")
