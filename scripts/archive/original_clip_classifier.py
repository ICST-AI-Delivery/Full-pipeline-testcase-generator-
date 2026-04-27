#!/usr/bin/env python3
"""
Original CLIP Classifier
=======================

This module provides functions for classifying images using the original CLIP model.
It's used by the evaluation scripts to classify images into predefined categories.
"""

import os
import sys
from pathlib import Path
import torch
import clip
from PIL import Image
import numpy as np

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

# Define the categories for classification
CATEGORIES = [
    "TELLTALE ICONS & INDICATORS",
    "HMI DISPLAY LAYOUTS",
    "TABLE + TELLTALES",
    "CONFIGURATION TABLES",
    "PROCESS FLOW DIAGRAMS",
    "WIRING & SIGNAL DIAGRAMS",
    "TECHNICAL SPECIFICATIONS",
    "MULTI-CONDITION LOGIC TABLES",
    "SYSTEM ARCHITECTURE",
    "STATE EVENT MATRICES",
    "TIMING DIAGRAMS"
]

def get_category_descriptions():
    """Return detailed descriptions for each category."""
    return {
        "TELLTALE ICONS & INDICATORS": "Images showing vehicle dashboard warning lights, status indicators, or symbolic icons used in automotive interfaces",
        "HMI DISPLAY LAYOUTS": "Screen layouts, UI designs, or mockups for vehicle infotainment or instrument cluster displays",
        "TABLE + TELLTALES": "Combined images showing both tabular data and vehicle indicator symbols or warning lights",
        "CONFIGURATION TABLES": "Tables showing system configuration parameters, settings options, or feature toggles",
        "PROCESS FLOW DIAGRAMS": "Flowcharts or diagrams showing sequences of operations, decision points, or process workflows",
        "WIRING & SIGNAL DIAGRAMS": "Electrical schematics, wiring diagrams, or signal flow representations between vehicle components",
        "TECHNICAL SPECIFICATIONS": "Detailed technical requirements, parameters, or specifications for vehicle systems or components",
        "MULTI-CONDITION LOGIC TABLES": "Truth tables, state transition tables, or conditional logic representations with multiple inputs/outputs",
        "SYSTEM ARCHITECTURE": "High-level diagrams showing system components, their relationships, and overall structure",
        "STATE EVENT MATRICES": "Matrices or tables showing relationships between system states and events or transitions",
        "TIMING DIAGRAMS": "Diagrams showing signal timing, sequences, or temporal relationships between events or operations"
    }

def load_clip_model():
    """Load the CLIP model."""
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, preprocess = clip.load("ViT-B/32", device=device)
    return model, preprocess, device

def classify_image(image_path):
    """
    Classify an image using CLIP.
    
    Args:
        image_path: Path to the image file
        
    Returns:
        Dictionary with classification results or None if classification fails
    """
    try:
        # Ensure the path is absolute
        if not os.path.isabs(image_path):
            image_path = os.path.join(project_root, image_path)
        
        # Check if file exists
        if not os.path.exists(image_path):
            print(f"Image file not found: {image_path}")
            return None
        
        # Load the model
        model, preprocess, device = load_clip_model()
        
        # Load and preprocess the image
        image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)
        
        # Get category descriptions
        descriptions = get_category_descriptions()
        
        # Prepare text inputs
        text_inputs = torch.cat([
            clip.tokenize(f"This is an image of {category.lower()}: {descriptions[category]}")
            for category in CATEGORIES
        ]).to(device)
        
        # Calculate features
        with torch.no_grad():
            image_features = model.encode_image(image)
            text_features = model.encode_text(text_inputs)
            
            # Normalize features
            image_features = image_features / image_features.norm(dim=-1, keepdim=True)
            text_features = text_features / text_features.norm(dim=-1, keepdim=True)
            
            # Calculate similarity scores
            similarity = (100.0 * image_features @ text_features.T).softmax(dim=-1)
            
            # Get the best match
            values, indices = similarity[0].topk(3)
            
        # Get top 3 predictions
        top_predictions = [
            {
                "category": CATEGORIES[idx.item()],
                "confidence": val.item(),
                "description": descriptions[CATEGORIES[idx.item()]]
            }
            for val, idx in zip(values, indices)
        ]
        
        # Return the best match
        return {
            "category": top_predictions[0]["category"],
            "confidence": top_predictions[0]["confidence"],
            "description": top_predictions[0]["description"],
            "top_predictions": top_predictions
        }
        
    except Exception as e:
        print(f"Error classifying image {image_path}: {e}")
        return None

if __name__ == "__main__":
    # Simple test if run directly
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
        result = classify_image(image_path)
        if result:
            print(f"Category: {result['category']}")
            print(f"Confidence: {result['confidence']:.3f}")
            print(f"Description: {result['description']}")
            print("\nTop 3 predictions:")
            for i, pred in enumerate(result['top_predictions'], 1):
                print(f"{i}. {pred['category']} ({pred['confidence']:.3f})")
        else:
            print(f"Failed to classify {image_path}")
    else:
        print("Usage: python original_clip_classifier.py <image_path>")
