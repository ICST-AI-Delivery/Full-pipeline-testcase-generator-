#!/usr/bin/env python3
"""
Automated Feature Analysis Generator

This script processes all images from a feature using CLIP predictions to automatically
select the appropriate vision API prompt and generate comprehensive analysis in a single file.

Usage:
    python automated_feature_analysis_generator.py --feature VEH-F844 --csv data_files/VEH-F844_Matrix_State_Event_with_clip_predictions.csv
"""

import pandas as pd
import os
from pathlib import Path
import argparse
from datetime import datetime
import json

class AutomatedAnalysisGenerator:
    def __init__(self):
        self.category_prompt_mapping = {
            "SYSTEM ARCHITECTURE DIAGRAMS": "03_SYSTEM_ARCHITECTURE_DIAGRAMS_v2.0_ENHANCED.md",
            "TIMING DIAGRAMS": "05_TIMING_DIAGRAMS_v5.0_ENHANCED_STATE_MATRIX.md",
            "CONFIGURATION TABLES": "02_CONFIGURATION_TABLES_v1.0.md",
            "TABLE WITH TELLTALES": "04_TABLE_WITH_TELLTALES_v1.0_SPECIALIZED.md",
            "STATE FLOW DIAGRAMS": "04_STATE_FLOW_DIAGRAMS_v2.1_SEQUENTIAL_MATRIX.md",
            "PROCESS FLOW DIAGRAMS": "09_PROCESS_FLOW_DIAGRAMS_v5.0_ARROW_DIRECTION_FOCUSED.md",
            "HMI DISPLAY LAYOUTS": "01_HMI_DISPLAY_LAYOUTS_v1.0.md",
            "DECISION LOGIC TABLES": "06_DECISION_LOGIC_TABLES_v1.0.md",
            "INTERFACE SPECIFICATIONS": "07_INTERFACE_SPECIFICATIONS_v1.0.md",
            "REQUIREMENT SPECIFICATIONS": "08_REQUIREMENT_SPECIFICATIONS_v1.0.md",
            "ERROR HANDLING DIAGRAMS": "10_ERROR_HANDLING_DIAGRAMS_v1.0.md",
            "TELLTALES AND ICONS": "10_TELLTALES_AND_ICONS_v1.0.md",
            "COLOR GRADIENTS": "10_COLOR_GRADIENTS_v1.0_SPECIALIZED.md",
            "NETWORK TOPOLOGY DIAGRAMS": "11_NETWORK_TOPOLOGY_DIAGRAMS_v1.0.md",
            "TECHNICAL SPECIFICATIONS": "11_TECHNICAL_SPECIFICATIONS_v2.0_UNIFIED.md",
            "SIGNAL FLOW DIAGRAMS": "12_SIGNAL_FLOW_DIAGRAMS_v1.0.md",
            "GENERAL TECHNICAL DIAGRAMS": "13_GENERAL_TECHNICAL_DIAGRAMS_v1.0.md"
        }
        
        self.vision_prompts_dir = Path("modules/image_analyzer/prompts")
        self.base_dir = Path(".")
        
    def load_csv_data(self, csv_path):
        """Load and validate CSV data with CLIP predictions"""
        try:
            df = pd.read_csv(csv_path)
            required_columns = ['Image Path', 'Image Name', 'CLIP Predicted Category', 'CLIP Confidence']
            
            missing_columns = [col for col in required_columns if col not in df.columns]
            if missing_columns:
                raise ValueError(f"Missing required columns: {missing_columns}")
                
            return df
        except Exception as e:
            print(f"Error loading CSV: {e}")
            return None
    
    def load_vision_prompt_template(self, category):
        """Load the appropriate vision API prompt template for the category"""
        if category not in self.category_prompt_mapping:
            print(f"Warning: No prompt mapping found for category '{category}'. Using general template.")
            prompt_file = "13_GENERAL_TECHNICAL_DIAGRAMS_v1.0.md"
        else:
            prompt_file = self.category_prompt_mapping[category]
        
        prompt_path = self.vision_prompts_dir / prompt_file
        
        if not prompt_path.exists():
            print(f"Warning: Prompt file {prompt_file} not found. Using fallback.")
            return self.create_fallback_prompt(category)
        
        try:
            with open(prompt_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
