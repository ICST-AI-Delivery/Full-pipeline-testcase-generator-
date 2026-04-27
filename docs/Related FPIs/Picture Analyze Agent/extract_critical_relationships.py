import json
import argparse

class CriticalRelationshipExtractor:
    def __init__(self, matrix_path):
        with open(matrix_path, 'r') as f:
            self.matrix = json.load(f)
    
    def extract_critical_relationships(self, target_feature):
        critical_relationships = {
            'input_dependencies': [],
            'output_dependencies': []
        }
        
        # Extract input dependencies (-3 relationships)
        for feature, relationships in self.matrix.items():
            if relationships.get(target_feature) == -3:
                critical_relationships['input_dependencies'].append(feature)
        
        # Extract output dependencies (+3 relationships)
        if self.matrix.get(target_feature):
            for related_feature, score in self.matrix[target_feature].items():
                if score == 3:
                    critical_relationships['output_dependencies'].append(related_feature)
        
        return critical_relationships

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract critical relationships for a target feature')
    parser.add_argument('--matrix_path', type=str, required=True, help='Path to the relationship matrix JSON file')
    parser.add_argument('--target_feature', type=str, required=True, help='Target feature to extract relationships for')
    
    args = parser.parse_args()
    
    extractor = CriticalRelationshipExtractor(args.matrix_path)
    critical_relationships = extractor.extract_critical_relationships(args.target_feature)
    
    print(json.dumps(critical_relationships, indent=2))
