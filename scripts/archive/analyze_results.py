#!/usr/bin/env python3
"""
Analysis script for classification results
"""

import pandas as pd
import numpy as np

def analyze_classification_results(csv_file):
    """Analyze the classification results from CSV file"""
    
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    print("=" * 60)
    print("CLASSIFICATION RESULTS ANALYSIS")
    print("=" * 60)
    
    # Basic statistics
    print(f"\nTotal images processed: {len(df)}")
    
    # Agreement analysis
    matches = df['Match'].value_counts()
    agreement_count = matches.get('Yes', 0)
    agreement_percentage = (agreement_count / len(df)) * 100
    print(f"Agreement between classifiers: {agreement_count} ({agreement_percentage:.1f}%)")
    
    # CLIP category distribution
    print("\n" + "=" * 40)
    print("CLIP CATEGORY DISTRIBUTION")
    print("=" * 40)
    clip_categories = df['CLIP Category'].value_counts()
    for category, count in clip_categories.items():
        percentage = (count / len(df)) * 100
        print(f"{category}: {count} ({percentage:.1f}%)")
    
    # CV category distribution
    print("\n" + "=" * 40)
    print("CV CATEGORY DISTRIBUTION")
    print("=" * 40)
    cv_categories = df['CV Category'].value_counts()
    for category, count in cv_categories.items():
        percentage = (count / len(df)) * 100
        print(f"{category}: {count} ({percentage:.1f}%)")
    
    # Confidence level analysis
    print("\n" + "=" * 40)
    print("CONFIDENCE LEVEL DISTRIBUTION")
    print("=" * 40)
    
    clip_confidence = df['CLIP Confidence'].value_counts()
    cv_confidence = df['CV Confidence'].value_counts()
    
    print("CLIP Confidence Levels:")
    for level in ['High', 'Medium', 'Low']:
        count = clip_confidence.get(level, 0)
        percentage = (count / len(df)) * 100
        print(f"  {level}: {count} ({percentage:.1f}%)")
    
    print("\nCV Confidence Levels:")
    for level in ['High', 'Medium', 'Low']:
        count = cv_confidence.get(level, 0)
        percentage = (count / len(df)) * 100
        print(f"  {level}: {count} ({percentage:.1f}%)")
    
    # Agreement by confidence level
    print("\n" + "=" * 40)
    print("AGREEMENT BY CONFIDENCE LEVEL")
    print("=" * 40)
    
    high_conf_both = df[(df['CLIP Confidence'] == 'High') & (df['CV Confidence'] == 'High')]
    if len(high_conf_both) > 0:
        high_conf_agreement = sum(high_conf_both['Match'] == 'Yes')
        print(f"High confidence (both): {high_conf_agreement}/{len(high_conf_both)} ({high_conf_agreement/len(high_conf_both)*100:.1f}%)")
    
    # Processing time analysis
    print("\n" + "=" * 40)
    print("PROCESSING TIME ANALYSIS")
    print("=" * 40)
    
    # Convert processing time to float (remove 's' suffix)
    processing_times = df['Processing Time'].str.replace('s', '').astype(float)
    print(f"Average processing time: {processing_times.mean():.2f}s")
    print(f"Min processing time: {processing_times.min():.2f}s")
    print(f"Max processing time: {processing_times.max():.2f}s")
    
    # Disagreement analysis
    print("\n" + "=" * 40)
    print("DISAGREEMENT ANALYSIS")
    print("=" * 40)
    
    disagreements = df[df['Match'] == 'No']
    if len(disagreements) > 0:
        print(f"Total disagreements: {len(disagreements)}")
        print("\nDisagreement cases:")
        for idx, row in disagreements.iterrows():
            print(f"  {row['Filename']}: CLIP={row['CLIP Category']} vs CV={row['CV Category']}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    analyze_classification_results('final_classification_results.csv')
