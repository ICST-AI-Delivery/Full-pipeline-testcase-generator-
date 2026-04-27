"""
Create final CSV file with CLIP predictions, ground truth, and correct/incorrect labels
Similar format to comprehensive_evaluation_results.csv but for CLIP classifier
"""

import pandas as pd
import csv

def main():
    # Read the CLIP evaluation results
    input_file = "data_files/clip_ground_truth_evaluation_results_improved_descriptions.csv"
    output_file = "data_files/clip_improved_descriptions_evaluation_results.csv"
    
    print(f"Reading CLIP evaluation results from: {input_file}")
    df = pd.read_csv(input_file)
    
    # Create the final results in the requested format
    final_results = []
    
    for _, row in df.iterrows():
        result = {
            'Image Path': row['Image Path'],
            'Image Name': row['Image Name'],
            'Ground Truth Category': row['Ground Truth Category'].strip() if pd.notna(row['Ground Truth Category']) else '',
            'CLIP Predicted Category': row['CLIP Predicted Category'],
            'CLIP Confidence': row['CLIP Confidence'],
            'Correct/Incorrect': row['Correct/Incorrect'],
            'CLIP Description': row['CLIP Description'],
            'Timestamp': row['Timestamp']
        }
        final_results.append(result)
    
    # Save to CSV
    print(f"Saving final results to: {output_file}")
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Image Path', 'Image Name', 'Ground Truth Category', 'CLIP Predicted Category', 
                     'CLIP Confidence', 'Correct/Incorrect', 'CLIP Description', 'Timestamp']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(final_results)
    
    # Print summary statistics
    total_images = len(final_results)
    correct_predictions = sum(1 for r in final_results if r['Correct/Incorrect'] == 'Correct')
    accuracy = (correct_predictions / total_images) * 100 if total_images > 0 else 0
    
    print(f"\nFinal CLIP Evaluation Summary:")
    print(f"Total Images: {total_images}")
    print(f"Correct Predictions: {correct_predictions}")
    print(f"Overall Accuracy: {accuracy:.2f}%")
    
    # Count by category
    category_stats = {}
    for result in final_results:
        gt_category = result['Ground Truth Category']
        is_correct = result['Correct/Incorrect'] == 'Correct'
        
        if gt_category not in category_stats:
            category_stats[gt_category] = {'total': 0, 'correct': 0}
        
        category_stats[gt_category]['total'] += 1
        if is_correct:
            category_stats[gt_category]['correct'] += 1
    
    print(f"\nPer-Category Results:")
    for category, stats in sorted(category_stats.items()):
        if category.strip():  # Skip empty categories
            accuracy = (stats['correct'] / stats['total']) * 100 if stats['total'] > 0 else 0
            print(f"{category}: {stats['correct']}/{stats['total']} ({accuracy:.1f}%)")
    
    print(f"\nFinal CSV file created: {output_file}")

if __name__ == "__main__":
    main()
