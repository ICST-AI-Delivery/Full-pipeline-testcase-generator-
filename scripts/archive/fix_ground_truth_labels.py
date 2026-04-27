"""
Fix remaining label inconsistencies in ground truth template
"""

import pandas as pd
import csv

def fix_ground_truth_labels():
    """
    Fix the remaining label inconsistencies in the ground truth template
    """
    
    # Read the current ground truth template
    df = pd.read_csv('data_files/ground_truth_template.csv')
    
    print(f"Loaded ground truth template with {len(df)} images")
    print("\nFixing label inconsistencies...")
    
    # Fix the remaining issues identified in the evaluation
    label_fixes = {
        # Remove trailing newlines and spaces
        'CONFIGURATION TABLES\n': 'CONFIGURATION TABLES',
        'CONFIGURATION TABLE': 'CONFIGURATION TABLES',  # Standardize to plural
        'TELLTALES ICONS &INDICATORS': 'TELLTALE ICONS & INDICATORS',  # Fix spacing and typo
        'PROCESS FLOW DIAGRAM': 'PROCESS FLOW DIAGRAMS',  # Standardize to plural
        'SYSTEM ARCHITECTURE DIAGRAMS': 'SYSTEM ARCHITECTURE',  # Match classifier output
    }
    
    # Apply fixes
    changes_made = 0
    for idx, row in df.iterrows():
        original_label = row['Ground_Truth_Category']
        cleaned_label = original_label.strip()  # Remove whitespace
        
        # Apply specific fixes
        if cleaned_label in label_fixes:
            new_label = label_fixes[cleaned_label]
            df.at[idx, 'Ground_Truth_Category'] = new_label
            print(f"  Fixed: '{original_label}' -> '{new_label}'")
            changes_made += 1
    
    print(f"\nMade {changes_made} label corrections")
    
    # Save the corrected template
    df.to_csv('data_files/ground_truth_template.csv', index=False)
    print("Saved corrected ground truth template")
    
    # Show the final label distribution
    print("\nFinal label distribution:")
    label_counts = df['Ground_Truth_Category'].value_counts()
    for label, count in label_counts.items():
        print(f"  {label}: {count}")
    
    return df

if __name__ == "__main__":
    fix_ground_truth_labels()
