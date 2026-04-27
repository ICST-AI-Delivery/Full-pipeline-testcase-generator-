#!/usr/bin/env python3
"""
SRS Export Feature Inventory Counter
Counts all features across all domains in SRS Export structure
"""

import os
import json

def count_features_in_domain(domain_path):
    """Count features (directories) in a domain"""
    features = []
    if os.path.exists(domain_path):
        for item in os.listdir(domain_path):
            item_path = os.path.join(domain_path, item)
            if os.path.isdir(item_path) and not item.startswith('.'):
                features.append(item)
    return features

def main():
    # Count features across all domains
    srs_export_path = 'SRS Export'
    domains = {}
    total_features = 0

    print("=== SRS EXPORT FEATURE INVENTORY ===")
    
    # First, get all domains
    domain_list = []
    for item in os.listdir(srs_export_path):
        item_path = os.path.join(srs_export_path, item)
        if os.path.isdir(item_path) and not item.startswith('.'):
            domain_list.append(item)
    
    # Now count features in each domain
    for domain in domain_list:
        domain_path = os.path.join(srs_export_path, domain)
        features = count_features_in_domain(domain_path)
        domains[domain] = {
            'feature_count': len(features),
            'features': features
        }
        total_features += len(features)

    print(f"Total Features: {total_features}")
    print(f"Total Domains: {len(domains)}")
    print()

    for domain, info in domains.items():
        count = info['feature_count']
        print(f"{domain}: {count} features")
        if info['features']:
            sample = info['features'][:3]
            print(f"  Sample: {sample}...")
        print()

    print(f"CONFIRMED SCOPE: '2xA2B_Audio_Layout' vs {total_features} related features")
    
    # Save detailed inventory
    with open('srs_feature_inventory.json', 'w') as f:
        json.dump(domains, f, indent=2)
    
    print(f"\nDetailed inventory saved to: srs_feature_inventory.json")
    return total_features, domains

if __name__ == "__main__":
    main()
