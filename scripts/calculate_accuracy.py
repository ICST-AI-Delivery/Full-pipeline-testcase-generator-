"""
Calculate Accuracy Metrics from Updated CLIP Evaluation Results
"""

import pandas as pd

def calculate_accuracy_metrics(csv_path):
    """Calculate and display accuracy metrics"""
    print("Loading evaluation results...")
    df = pd.read_csv(csv_path)
    
    # Filter rows with ground truth
    df_with_gt = df[df['Ground_Truth_Category'].notna() & (df['Ground_Truth_Category'].str.strip() != "")]
    
    if len(df_with_gt) == 0:
        print("No ground truth labels found!")
        return
    
    # Count correct and wrong predictions
    correct_count = len(df_with_gt[df_with_gt['Classification_Correct'] == 'CORRECT'])
    wrong_count = len(df_with_gt[df_with_gt['Classification_Correct'] == 'WRONG'])
    total_with_gt = len(df_with_gt)
    
    accuracy = (correct_count / total_with_gt) * 100 if total_with_gt > 0 else 0
    
    print(f"\n=== UPDATED CLIP CLASSIFIER ACCURACY RESULTS ===")
    print(f"Total images with ground truth: {total_with_gt}")
    print(f"Correct predictions: {correct_count}")
    print(f"Wrong predictions: {wrong_count}")
    print(f"Overall Accuracy: {accuracy:.2f}%")
    
    # Category breakdown
    print(f"\n=== CATEGORY BREAKDOWN ===")
    category_stats = {}
    
    for _, row in df_with_gt.iterrows():
        gt_cat = row['Ground_Truth_Category'].strip()
        is_correct = row['Classification_Correct'] == 'CORRECT'
        
        if gt_cat not in category_stats:
            category_stats[gt_cat] = {'correct': 0, 'total': 0}
        
        category_stats[gt_cat]['total'] += 1
        if is_correct:
            category_stats[gt_cat]['correct'] += 1
    
    for category, stats in sorted(category_stats.items()):
        cat_accuracy = (stats['correct'] / stats['total']) * 100 if stats['total'] > 0 else 0
        print(f"{category}: {stats['correct']}/{stats['total']} ({cat_accuracy:.1f}%)")
    
    # Show predictions breakdown
    print(f"\n=== PREDICTION BREAKDOWN ===")
    prediction_counts = df['Updated_CLIP_Category'].value_counts()
    for category, count in prediction_counts.items():
        print(f"{category}: {count} images")
    
    # Show confidence distribution
    print(f"\n=== CONFIDENCE DISTRIBUTION ===")
    confidence_counts = df['Updated_CLIP_Confidence'].value_counts()
    for confidence, count in confidence_counts.items():
        print(f"{confidence}: {count} images")
    
    return accuracy, category_stats

if __name__ == "__main__":
    csv_path = "data_files/updated_clip_evaluation_results.csv"
    calculate_accuracy_metrics(csv_path)
