#!/usr/bin/env python3
"""
Update FPI dependency matrix with DMS-7_DRIVER_GAZE_ESTIMATION relationships
Adapted from VFI-F164 matrix update script
"""

import pandas as pd
import json
from datetime import datetime
import os

def update_matrix_with_dms7():
    """Update the placeholder matrix with DMS-7 relationships"""
    
    # File paths
    matrix_file = 'fpi_dependency_matrix_placeholder_20260416_145904.csv'
    register_file = 'dms7_dependency_register.csv'
    
    # Generate timestamp for output files
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_matrix = f'dms7_updated_matrix_{timestamp}.csv'
    output_report = f'dms7_matrix_update_report_{timestamp}.json'
    
    try:
        # Load the placeholder matrix
        print("Loading placeholder matrix...")
        matrix_df = pd.read_csv(matrix_file, index_col=0)
        print(f"Matrix dimensions: {matrix_df.shape}")
        
        # Load DMS-7 dependency register
        print("Loading DMS-7 dependency register...")
        register_df = pd.read_csv(register_file)
        print(f"Total DMS-7 relationships: {len(register_df)}")
        
        # Initialize update tracking
        updates_made = 0
        skipped_relationships = 0
        missing_fpis = []
        update_details = []
        
        # Process each relationship
        print("Processing DMS-7 relationships...")
        for idx, row in register_df.iterrows():
            source_fpi = 'DMS-7_DRIVER_GAZE_ESTIMATION'
            target_fpi = row['related_fpi']
            score = row['score']
            direction = row['direction']
            confidence = row['confidence']
            
            # Check if both FPIs exist in matrix
            if source_fpi in matrix_df.index and target_fpi in matrix_df.columns:
                # Update the matrix cell
                current_value = matrix_df.loc[source_fpi, target_fpi]
                
                # Only update if current value is 0 (placeholder) or if new score is stronger
                if current_value == 0 or abs(score) > abs(current_value):
                    matrix_df.loc[source_fpi, target_fpi] = score
                    updates_made += 1
                    
                    update_details.append({
                        'source': source_fpi,
                        'target': target_fpi,
                        'old_value': current_value,
                        'new_value': score,
                        'direction': direction,
                        'confidence': confidence
                    })
                else:
                    skipped_relationships += 1
            else:
                # Track missing FPIs
                if source_fpi not in matrix_df.index:
                    missing_fpis.append(source_fpi)
                if target_fpi not in matrix_df.columns:
                    missing_fpis.append(target_fpi)
                skipped_relationships += 1
        
        # Ensure antisymmetric property for dependency relationships
        print("Ensuring antisymmetric properties...")
        antisymmetric_updates = 0
        
        for detail in update_details:
            source = detail['source']
            target = detail['target']
            score = detail['new_value']
            
            # For dependency relationships, ensure antisymmetric property
            if detail['direction'] in ['Upstream', 'Downstream']:
                if target in matrix_df.index and source in matrix_df.columns:
                    # Set reverse relationship to negative of forward relationship
                    reverse_score = -score
                    current_reverse = matrix_df.loc[target, source]
                    
                    if current_reverse == 0 or abs(reverse_score) > abs(current_reverse):
                        matrix_df.loc[target, source] = reverse_score
                        antisymmetric_updates += 1
        
        # Save updated matrix
        matrix_df.to_csv(output_matrix)
        
        # Generate update report
        report = {
            'timestamp': timestamp,
            'source_fpi': 'DMS-7_DRIVER_GAZE_ESTIMATION',
            'input_matrix': matrix_file,
            'input_register': register_file,
            'output_matrix': output_matrix,
            'total_relationships_processed': len(register_df),
            'updates_made': updates_made,
            'antisymmetric_updates': antisymmetric_updates,
            'skipped_relationships': skipped_relationships,
            'missing_fpis': list(set(missing_fpis)),
            'matrix_dimensions': {
                'rows': matrix_df.shape[0],
                'columns': matrix_df.shape[1]
            },
            'update_summary': {
                'high_confidence_updates': len([d for d in update_details if d['confidence'] == 'High']),
                'probable_updates': len([d for d in update_details if d['confidence'] == 'Probable']),
                'possible_updates': len([d for d in update_details if d['confidence'] == 'Possible'])
            }
        }
        
        # Save report
        with open(output_report, 'w') as f:
            json.dump(report, f, indent=2)
        
        # Print summary
        print(f"\n=== DMS-7 Matrix Update Complete ===")
        print(f"Updated matrix saved: {output_matrix}")
        print(f"Update report saved: {output_report}")
        print(f"Total relationships processed: {len(register_df)}")
        print(f"Matrix updates made: {updates_made}")
        print(f"Antisymmetric updates made: {antisymmetric_updates}")
        print(f"Relationships skipped: {skipped_relationships}")
        print(f"Missing FPIs: {len(set(missing_fpis))}")
        
        if len(set(missing_fpis)) > 0:
            print(f"First few missing FPIs: {list(set(missing_fpis))[:5]}")
        
        return output_matrix, output_report
        
    except Exception as e:
        print(f"Error updating matrix with DMS-7 relationships: {e}")
        return None, None

if __name__ == "__main__":
    update_matrix_with_dms7()
