#!/usr/bin/env python3
"""
Cross-Domain Feature Discovery Test Script
Tests the system's ability to find relationships between features across different SRS domains
"""

import os
import sys
import time
from pathlib import Path
from typing import Dict, List, Tuple

# Add the srs_discovery module to the path
sys.path.append(str(Path(__file__).parent))

from srs_discovery.parser import SRSParser
from srs_discovery.indexer import ExactMatchIndexer
from srs_discovery.semantic_engine import SemanticSearchEngine
from srs_discovery.graph_engine import RelationshipGraphEngine
from srs_discovery.utils import logger, Feature

def discover_all_domains(srs_export_path: Path) -> Dict[str, List[Path]]:
    """Discover all domains and their feature folders"""
    
    print("🔍 Discovering SRS domains and features...")
    
    domains = {}
    
    # Look for SRS domain folders
    for item in srs_export_path.iterdir():
        if item.is_dir() and item.name.startswith("SRS_"):
            domain_name = item.name
            feature_folders = []
            
            # Get all feature folders in this domain
            for feature_folder in item.iterdir():
                if feature_folder.is_dir() and not feature_folder.name.startswith('.'):
                    feature_folders.append(feature_folder)
            
            if feature_folders:
                domains[domain_name] = feature_folders
                print(f"   📁 {domain_name}: {len(feature_folders)} features")
    
    return domains

def select_target_feature(domains: Dict[str, List[Path]]) -> Tuple[str, Path, str]:
    """Select a target feature for cross-domain relationship discovery"""
    
    print("\n🎯 Selecting target feature for analysis...")
    
    # Priority list of interesting features to test with
    priority_features = [
        ("SRS_Audio", "FAD-0_Ferrari_Audio_Director_Introduction"),
        ("SRS_Audio", "Volume"),
        ("SRS_Connectivity", "PHN-1_System_BT"),
        ("SRS_Audio", "AUD-7_CAN_Control_Signals"),
        ("SRS_Connectivity", "PHN-3_Add_Device")
    ]
    
    # Try to find a priority feature first
    for domain_name, feature_name in priority_features:
        if domain_name in domains:
            for feature_folder in domains[domain_name]:
                if feature_name in feature_folder.name:
                    print(f"✅ Selected target feature: {feature_folder.name}")
                    print(f"   📂 Domain: {domain_name}")
                    print(f"   📍 Path: {feature_folder}")
                    return feature_folder.name, feature_folder, domain_name
    
    # If no priority feature found, pick the first available feature
    for domain_name, feature_folders in domains.items():
        if feature_folders:
            target_folder = feature_folders[0]
            print(f"✅ Selected fallback feature: {target_folder.name}")
            print(f"   📂 Domain: {domain_name}")
            print(f"   📍 Path: {target_folder}")
            return target_folder.name, target_folder, domain_name
    
    return None, None, None

def parse_all_features_across_domains(parser: SRSParser, domains: Dict[str, List[Path]]) -> Dict[str, Feature]:
    """Parse all individual feature folders across all domains"""
    
    print("\n🔄 Parsing features across all domains...")
    
    all_features = {}
    domain_stats = {}
    
    for domain_name, feature_folders in domains.items():
        print(f"\n📁 Processing domain: {domain_name}")
        domain_features = 0
        
        for feature_folder in feature_folders:
            try:
                # Parse this individual feature folder
                features = parser.parse_srs_folder(str(feature_folder))
                
                if features:
                    # Add domain information to feature IDs to avoid conflicts
                    for feature_id, feature_data in features.items():
                        # Create unique cross-domain feature ID
                        cross_domain_id = f"{domain_name}::{feature_id}"
                        
                        # Add domain metadata to the feature
                        feature_data.domain = domain_name
                        feature_data.source_folder = feature_folder.name
                        
                        all_features[cross_domain_id] = feature_data
                        domain_features += 1
                
            except Exception as e:
                print(f"   ⚠️  Error parsing {feature_folder.name}: {e}")
                continue
        
        domain_stats[domain_name] = domain_features
        print(f"   ✅ Parsed {domain_features} features from {domain_name}")
    
    # Summary
    total_features = len(all_features)
    print(f"\n📊 Cross-domain parsing summary:")
    print(f"   🎯 Total features parsed: {total_features}")
    for domain, count in domain_stats.items():
        print(f"   📁 {domain}: {count} features")
    
    return all_features

def find_cross_domain_relationships(target_feature_id: str, target_domain: str, 
                                  all_features: Dict[str, Feature], 
                                  indexer: ExactMatchIndexer) -> Dict[str, List]:
    """Find relationships between target feature and features from other domains"""
    
    print(f"\n🔍 Finding cross-domain relationships for: {target_feature_id}")
    
    # Find all relationships
    relationships = indexer.find_exact_matches(target_feature_id)
    
    # Group relationships by domain
    domain_relationships = {}
    
    for rel in relationships:
        # Extract domain from the related feature ID
        if "::" in rel.related_feature_id:
            related_domain = rel.related_feature_id.split("::")[0]
            related_feature = rel.related_feature_id.split("::")[1]
        else:
            related_domain = "Unknown"
            related_feature = rel.related_feature_id
        
        # Skip relationships within the same domain for cross-domain analysis
        if related_domain == target_domain:
            continue
        
        if related_domain not in domain_relationships:
            domain_relationships[related_domain] = []
        
        domain_relationships[related_domain].append({
            'feature_id': related_feature,
            'full_id': rel.related_feature_id,
            'score': rel.score,
            'confidence': rel.confidence,
            'relationship_type': rel.relationship_type,
            'evidence': rel.evidence
        })
    
    return domain_relationships

def test_cross_domain_discovery():
    """Main test function for cross-domain feature relationship discovery"""
    
    print("=" * 80)
    print("🌐 Smart SRS Cross-Domain Feature Discovery Test")
    print("=" * 80)
    
    # Step 1: Find SRS Export folder
    srs_export_path = Path("../SRS Export")
    if not srs_export_path.exists():
        srs_export_path = Path("SRS Export")
    
    if not srs_export_path.exists():
        print("❌ ERROR: SRS Export folder not found!")
        return False
    
    print(f"✅ Found SRS Export folder: {srs_export_path.absolute()}")
    
    # Step 2: Discover all domains and features
    print("\n" + "="*60)
    print("STEP 1: Domain and Feature Discovery")
    print("="*60)
    
    domains = discover_all_domains(srs_export_path)
    
    if not domains:
        print("❌ No SRS domains found!")
        return False
    
    total_features = sum(len(folders) for folders in domains.values())
    print(f"\n✅ Discovered {len(domains)} domains with {total_features} total features")
    
    # Step 3: Select target feature
    print("\n" + "="*60)
    print("STEP 2: Target Feature Selection")
    print("="*60)
    
    target_name, target_folder, target_domain = select_target_feature(domains)
    
    if not target_folder:
        print("❌ Could not select a target feature!")
        return False
    
    # Step 4: Parse all features across domains
    print("\n" + "="*60)
    print("STEP 3: Cross-Domain Feature Parsing")
    print("="*60)
    
    parser = SRSParser(str(srs_export_path))
    all_features = parse_all_features_across_domains(parser, domains)
    
    if not all_features:
        print("❌ No features could be parsed!")
        return False
    
    # Step 5: Build cross-domain indices
    print("\n" + "="*60)
    print("STEP 4: Cross-Domain Indexing")
    print("="*60)
    
    print("🔄 Building cross-domain indices...")
    indexer = ExactMatchIndexer()
    indexer.build_indices(all_features)
    
    stats = indexer.get_statistics()
    print(f"✅ Built indices for {stats['indexed_features']} features across all domains")
    print(f"   📊 Total CAN signals: {stats['can_signals']}")
    print(f"   📊 Total expert domains: {stats['expert_domains']}")
    print(f"   📊 Total telltale codes: {stats.get('telltale_codes', 0)}")
    
    # Step 6: Find cross-domain relationships
    print("\n" + "="*60)
    print("STEP 5: Cross-Domain Relationship Discovery")
    print("="*60)
    
    # Find the target feature in the parsed features
    target_feature_id = None
    print(f"🔍 Looking for target feature matching: {target_name}")
    print(f"   In domain: {target_domain}")
    
    # Debug: Show some feature IDs from the target domain
    target_domain_features = [fid for fid in all_features.keys() if fid.startswith(f"{target_domain}::")]
    print(f"   Found {len(target_domain_features)} features in {target_domain}")
    if target_domain_features:
        print(f"   Sample features: {target_domain_features[:5]}")
    
    # Try different matching strategies
    for feature_id in all_features.keys():
        if feature_id.startswith(f"{target_domain}::"):
            # Extract the actual feature name from the ID
            feature_name = feature_id.split("::")[-1]
            
            # Try exact match first
            if target_name == feature_name:
                target_feature_id = feature_id
                print(f"✅ Found exact match: {target_feature_id}")
                break
            
            # Try partial match (target_name in feature_name)
            if target_name in feature_name:
                target_feature_id = feature_id
                print(f"✅ Found partial match: {target_feature_id}")
                break
            
            # Try reverse partial match (feature_name in target_name)
            if feature_name in target_name:
                target_feature_id = feature_id
                print(f"✅ Found reverse match: {target_feature_id}")
                break
    
    if not target_feature_id:
        print(f"❌ Target feature not found in parsed features!")
        print(f"   Tried to match: '{target_name}'")
        print(f"   Available features in {target_domain}:")
        for fid in target_domain_features[:10]:  # Show first 10
            feature_name = fid.split("::")[-1]
            print(f"     - {feature_name}")
        return False
    
    print(f"🎯 Analyzing relationships for: {target_feature_id}")
    
    domain_relationships = find_cross_domain_relationships(
        target_feature_id, target_domain, all_features, indexer
    )
    
    # Display results
    print(f"\n� Cross-domain relationship analysis results:")
    print(f"🎯 Target: {target_name} (from {target_domain})")
    
    if not domain_relationships:
        print("   ℹ️  No cross-domain relationships found")
        print("   💡 This feature might be domain-specific or isolated")
    else:
        total_relationships = sum(len(rels) for rels in domain_relationships.values())
        print(f"   ✅ Found relationships with {len(domain_relationships)} other domains")
        print(f"   🔗 Total cross-domain relationships: {total_relationships}")
        
        # Show relationships by domain
        for domain, relationships in domain_relationships.items():
            print(f"\n   🌐 Relationships with {domain}:")
            
            # Sort by confidence/score
            sorted_rels = sorted(relationships, key=lambda x: abs(x['score']), reverse=True)
            
            for i, rel in enumerate(sorted_rels[:5], 1):  # Show top 5 per domain
                score_type = "Input dependency" if rel['score'] < 0 else "Output importance"
                print(f"      {i}. {rel['feature_id']}")
                print(f"         Score: {rel['score']:+d} ({score_type})")
                print(f"         Confidence: {rel['confidence']:.3f}")
                print(f"         Evidence: {rel['evidence'][0] if rel['evidence'] else 'N/A'}")
    
    # Step 7: Test semantic search if available
    print("\n" + "="*60)
    print("STEP 6: Cross-Domain Semantic Analysis (Optional)")
    print("="*60)
    
    try:
        semantic_engine = SemanticSearchEngine()
        semantic_stats = semantic_engine.get_statistics()
        
        if semantic_stats['dependencies_available']:
            print("✅ AI dependencies available - running semantic analysis")
            
            print("🔄 Building semantic embeddings for cross-domain analysis...")
            start_time = time.time()
            semantic_engine.build_embeddings(all_features)
            build_time = time.time() - start_time
            
            print(f"✅ Built embeddings in {build_time:.2f} seconds")
            
            print(f"\n🧠 Finding semantic relationships across domains...")
            semantic_relationships = semantic_engine.find_semantic_matches(target_feature_id, max_results=10)
            
            # Group semantic relationships by domain
            semantic_by_domain = {}
            for rel in semantic_relationships:
                if "::" in rel.related_feature_id:
                    related_domain = rel.related_feature_id.split("::")[0]
                    if related_domain != target_domain:  # Cross-domain only
                        if related_domain not in semantic_by_domain:
                            semantic_by_domain[related_domain] = []
                        semantic_by_domain[related_domain].append(rel)
            
            if semantic_by_domain:
                print(f"✅ Found semantic relationships with {len(semantic_by_domain)} domains")
                for domain, rels in semantic_by_domain.items():
                    print(f"\n   🧠 Semantic matches in {domain}:")
                    for i, rel in enumerate(rels[:3], 1):  # Top 3 per domain
                        feature_name = rel.related_feature_id.split("::")[-1]
                        print(f"      {i}. {feature_name}")
                        print(f"         Similarity: {rel.confidence:.3f}")
                        print(f"         Evidence: {rel.evidence[0] if rel.evidence else 'Semantic similarity'}")
            else:
                print("   ℹ️  No cross-domain semantic relationships found")
        else:
            print("⚠️  AI dependencies not available")
            print("   Install with: pip install sentence-transformers faiss-cpu")
    
    except Exception as e:
        print(f"⚠️  Semantic analysis failed: {e}")
    
    # Final Summary
    print("\n" + "="*80)
    print("📊 CROSS-DOMAIN DISCOVERY SUMMARY")
    print("="*80)
    
    print(f"🎯 Target Feature: {target_name}")
    print(f"📂 Source Domain: {target_domain}")
    print(f"🌐 Total Domains Analyzed: {len(domains)}")
    print(f"📊 Total Features Parsed: {len(all_features)}")
    
    if domain_relationships:
        cross_domain_count = len(domain_relationships)
        total_relationships = sum(len(rels) for rels in domain_relationships.values())
        print(f"🔗 Cross-Domain Connections: {cross_domain_count} domains, {total_relationships} relationships")
        
        print(f"\n🌐 Connected Domains:")
        for domain in domain_relationships.keys():
            rel_count = len(domain_relationships[domain])
            print(f"   • {domain}: {rel_count} relationships")
    else:
        print(f"🔗 Cross-Domain Connections: None found")
        print(f"   💡 This feature appears to be domain-specific")
    
    print(f"\n✅ Cross-domain discovery test completed successfully!")
    return True

if __name__ == "__main__":
    print("🚀 Starting Cross-Domain SRS Feature Discovery Test...")
    
    try:
        success = test_cross_domain_discovery()
        
        if success:
            print("\n🎉 Cross-domain discovery test completed successfully!")
        else:
            print("\n❌ Cross-domain discovery test failed!")
            
    except KeyboardInterrupt:
        print("\n⏹️  Test interrupted by user")
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
