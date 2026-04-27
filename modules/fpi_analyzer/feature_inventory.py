import os
import json
from datetime import datetime

# Define the base path
base_path = 'SRS Export/SRS Export'

# Domain mapping with discovered feature counts
domains = {
    'SRS_Audio': [],
    'SRS_Connectivity': [],
    'SRS_Diagnostics': [],
    'SRS_DMS': [],
    'SRS_HMI Software': [],
    'SRS_Instrument Cluster': [],
    'SRS_Navigation': [],
    'SRS_System Architecture': [],
    'SRS_Tuner': []
}

# Collect all features from each domain
total_features = 0
for domain in domains.keys():
    domain_path = os.path.join(base_path, domain)
    if os.path.exists(domain_path):
        features = []
        for item in os.listdir(domain_path):
            if os.path.isdir(os.path.join(domain_path, item)) and not item.startswith('.'):
                feature_path = f'{base_path}/{domain}/{item}/'
                features.append(feature_path)
        domains[domain] = features
        total_features += len(features)
        print(f'{domain}: {len(features)} features')

print(f'\nTOTAL FEATURES DISCOVERED: {total_features}')

# Create comprehensive feature path list
all_features = []
for domain, features in domains.items():
    all_features.extend(features)

# Save to file
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_file = f'complete_srs_feature_paths_{timestamp}.txt'

with open(output_file, 'w', encoding='utf-8') as f:
    f.write('# Complete SRS Feature Path Inventory\n')
    f.write(f'# Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
    f.write(f'# Total Features: {total_features}\n\n')
    
    for domain, features in domains.items():
        f.write(f'## {domain} ({len(features)} features)\n')
        for feature in sorted(features):
            f.write(f'{feature}\n')
        f.write('\n')

# Also save as JSON for programmatic use
json_file = f'complete_srs_feature_inventory_{timestamp}.json'
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump({
        'timestamp': datetime.now().isoformat(),
        'total_features': total_features,
        'domains': domains,
        'all_features': all_features
    }, f, indent=2, ensure_ascii=False)

print(f'\nFiles created:')
print(f'- {output_file}')
print(f'- {json_file}')
