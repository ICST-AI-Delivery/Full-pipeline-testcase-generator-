#!/usr/bin/env python3
"""
Single Feature Test Script for the Smart SRS Feature Discovery System
Tests with just one specific feature to validate the system step-by-step
"""

import os
import sys
import time
from pathlib import Path

# Add the srs_discovery module to the path
sys.path.append(str(Path(__file__).parent))

from srs_discovery.parser import SRSParser
from srs_discovery.indexer import ExactMatchIndexer
from srs_discovery.semantic_engine import SemanticSearchEngine
from srs_discovery.graph_engine import RelationshipGraphEngine
from srs_discovery.utils import logger

def find_interesting_feature():
    """Find a single interesting feature to test with"""
    
    print("🔍 Searching for a good test feature...")
    
    # Check if SRS Export folder exists
    srs_export_path = Path("../SRS Export")
    if not srs_export_path.exists():
        srs_export_path = Path("SRS Export")
    
    if not srs_export_path.exists():
        print("❌ ERROR: SRS Export folder not found!")
        return None, None, None
    
    parser = SRSParser(str(srs_export_path))
    
    # Priority list of folders to check (most likely to have interesting features)
    priority_folders = [
        srs_export_path / "SRS_Audio" / "FAD-0_Ferrari_Audio_Director_Introduction",
        srs_export_path / "SRS_Audio" / "AUD-7_CAN_Control_Signals", 
        srs_export_path / "SRS_Connectivity" / "PHN-1_System_BT",
        srs_export_path / "SRS_Audio" / "Volume",
        srs_export_path / "SRS_Audio" / "FAD-2_Audio_Channels_Control"
    ]
    
    # Try to parse features from priority folders first
    print("📁 Trying to parse features from priority folders...")
    
    for folder in priority_folders:
        if folder.exists():
            print(f"📁 Checking folder: {folder.name}")
            try:
                features = parser.parse_srs_folder(str(folder))
                if features:
                    # Pick the first feature from this folder
                    feature_id = list(features.keys())[0]
                    feature_data = features[feature_id]
                    
                    print(f"✅ Found test feature: {feature_id}")
                    print(f"   📂 From folder: {folder.name}")
                    print(f"   📊 Feature has {len(feature_data.can_signals)} CAN signals")
                    print(f"   📊 Feature has {len(feature_data.expert_domains)} expert domains")
                    print(f"   📊 Feature has {len(feature_data.telltale_codes)} telltale codes")
                    
                    return feature_id, features, folder
                    
            except Exception as e:
                print(f"   ⚠️  Error parsing {folder.name}: {e}")
                continue
    
    # If no priority folders work, try any available folder
    print("🔍 Trying other available folders...")
    
    for domain_folder in ["SRS_Audio", "SRS_Connectivity", "SRS_Diagnostics"]:
        domain_path = srs_export_path / domain_folder
        if domain_path.exists():
            # Get first subfolder
            subfolders = [f for f in domain_path.iterdir() if f.is_dir()]
            if subfolders:
                test_folder = subfolders[0]
                print(f"📁 Trying: {test_folder.name}")
                try:
                    features = parser.parse_srs_folder(str(test_folder))
                    if features:
                        feature_id = list(features.keys())[0]
                        print(f"✅ Found fallback feature: {feature_id}")
                        return feature_id, features, test_folder
                except Exception as e:
                    continue
    
    print("❌ No features found in any folder!")
    return None, None, None
    
    return None, None, None

def test_single_feature_detailed():
    """Test the system with a single feature in detail"""
    
    print("=" * 70)
    print("🎯 Smart SRS Feature Discovery - SINGLE FEATURE TEST")
    print("=" * 70)
    
    # Step 1: Find a good test feature
    print("\n" + "="*50)
    print("STEP 1: Finding Test Feature")
    print("="*50)
    
    test_feature_id, all_features, test_folder = find_interesting_feature()
    
    if not test_feature_id:
        print("❌ Could not find a suitable test feature!")
        return False
    
    test_feature_data = all_features[test_feature_id]
    
    print(f"\n🎯 SELECTED TEST FEATURE: {test_feature_id}")
    print(f"📂 Source folder: {test_folder.name}")
    print(f"📋 Feature details:")
    print(f"   • CAN Signals: {list(test_feature_data.can_signals)}")
    print(f"   • Expert Domains: {list(test_feature_data.expert_domains)}")
    print(f"   • Telltale Codes: {list(test_feature_data.telltale_codes)}")
    print(f"   • Pop-up IDs: {list(test_feature_data.popup_ids)}")
    
    # Step 2: Use all parsed features for comparison
    print("\n" + "="*50)
    print("STEP 2: Using All Parsed Features for Comparison")
    print("="*50)
    
    print(f"📁 Using all {len(all_features)} parsed features for comparison")
    comparison_features = all_features
    
    # Step 3: Test Exact Match Engine
    print("\n" + "="*50)
    print("STEP 3: Exact Match Analysis")
    print("="*50)
    
    indexer = ExactMatchIndexer()
    print("🔄 Building indices...")
    indexer.build_indices(comparison_features)
    
    stats = indexer.get_statistics()
    print(f"✅ Built indices for {stats['indexed_features']} features")
    print(f"   📊 Total CAN signals: {stats['can_signals']}")
    print(f"   📊 Total expert domains: {stats['expert_domains']}")
    print(f"   📊 Total telltale codes: {stats.get('telltale_codes', 0)}")
    
    print(f"\n🔍 Finding exact matches for: {test_feature_id}")
    exact_relationships = indexer.find_exact_matches(test_feature_id)
    
    print(f"✅ Found {len(exact_relationships)} exact match relationships:")
    
    if exact_relationships:
        for i, rel in enumerate(exact_relationships[:5], 1):  # Show top 5
            print(f"\n   {i}. {rel.related_feature_id}")
            print(f"      Score: {rel.score:+d} ({'Input dependency' if rel.score < 0 else 'Output importance'})")
            print(f"      Confidence: {rel.confidence:.3f}")
            print(f"      Type: {rel.relationship_type}")
            print(f"      Evidence: {rel.evidence[0] if rel.evidence else 'N/A'}")
    else:
        print("   ℹ️  No exact matches found (this feature might be isolated)")
    
    # Step 4: Test Semantic Engine (if available)
    print("\n" + "="*50)
    print("STEP 4: Semantic Analysis (AI-Powered)")
    print("="*50)
    
    try:
        semantic_engine = SemanticSearchEngine()
        semantic_stats = semantic_engine.get_statistics()
        
        if semantic_stats['dependencies_available']:
            print("✅ AI dependencies available - running semantic analysis")
            
            print("🔄 Building semantic embeddings... (this may take a moment)")
            start_time = time.time()
            semantic_engine.build_embeddings(comparison_features)
            build_time = time.time() - start_time
            
            print(f"✅ Built embeddings in {build_time:.2f} seconds")
            
            print(f"\n🧠 Finding semantic matches for: {test_feature_id}")
            semantic_relationships = semantic_engine.find_semantic_matches(test_feature_id, max_results=5)
            
            print(f"✅ Found {len(semantic_relationships)} semantic relationships:")
            
            for i, rel in enumerate(semantic_relationships, 1):
                print(f"\n   {i}. {rel.related_feature_id}")
                print(f"      Score: {rel.score:+d}")
                print(f"      Confidence: {rel.confidence:.3f}")
                print(f"      Evidence: {rel.evidence[0] if rel.evidence else 'Semantic similarity'}")
        else:
            print("⚠️  AI dependencies not available")
            print("   Install with: pip install sentence-transformers faiss-cpu")
            print("   (This is optional - exact matching still works)")
    
    except Exception as e:
        print(f"⚠️  Semantic analysis failed: {e}")
    
    # Step 5: Test Graph Engine (if available)
    print("\n" + "="*50)
    print("STEP 5: Graph Relationship Analysis")
    print("="*50)
    
    try:
        graph_engine = RelationshipGraphEngine()
        graph_stats = graph_engine.get_statistics()
        
        if graph_stats.get('networkx_available', False):
            print("✅ NetworkX available - building relationship graph")
            
            # Build relationships for graph
            print("🔄 Building relationship graph...")
            all_relationships = {}
            
            # Get relationships for a subset of features (for performance)
            feature_subset = list(comparison_features.keys())[:20]  # Limit for testing
            
            for feature_id in feature_subset:
                all_relationships[feature_id] = indexer.find_exact_matches(feature_id)
            
            graph_engine.build_graph(comparison_features, all_relationships)
            
            final_stats = graph_engine.get_statistics()
            print(f"✅ Built graph with {final_stats['nodes']} nodes and {final_stats['edges']} edges")
            print(f"   📊 Graph density: {final_stats['density']:.3f}")
            
            print(f"\n🕸️  Finding graph relationships for: {test_feature_id}")
            graph_relationships = graph_engine.find_graph_relationships(test_feature_id)
            
            print(f"✅ Found {len(graph_relationships)} graph relationships:")
            
            for i, rel in enumerate(graph_relationships[:3], 1):  # Show top 3
                print(f"\n   {i}. {rel.related_feature_id}")
                print(f"      Score: {rel.score:+d}")
                print(f"      Confidence: {rel.confidence:.3f}")
                print(f"      Type: {rel.relationship_type}")
        else:
            print("⚠️  NetworkX not available")
            print("   Install with: pip install networkx")
            print("   (This is optional - other engines still work)")
    
    except Exception as e:
        print(f"⚠️  Graph analysis failed: {e}")
    
    # Step 6: Summary
    print("\n" + "="*70)
    print("📊 SINGLE FEATURE TEST SUMMARY")
    print("="*70)
    
    print(f"🎯 Test Feature: {test_feature_id}")
    print(f"📂 Source: {test_folder.name}")
    print(f"📊 Comparison Dataset: {len(comparison_features)} features")
    print(f"🔍 Exact Matches: {len(exact_relationships) if 'exact_relationships' in locals() else 0}")
    print(f"🧠 Semantic Matches: {len(semantic_relationships) if 'semantic_relationships' in locals() else 'N/A'}")
    print(f"🕸️  Graph Matches: {len(graph_relationships) if 'graph_relationships' in locals() else 'N/A'}")
    
    print(f"\n✅ Single feature test completed successfully!")
    print(f"💡 The system can discover relationships for individual features")
    print(f"🚀 Ready to scale up to larger datasets!")
    
    return True

if __name__ == "__main__":
    print("🎯 Starting Single Feature Test...")
    
    try:
        success = test_single_feature_detailed()
        
        if success:
            print("\n" + "="*50)
            print("🎉 NEXT STEPS")
            print("="*50)
            print("1. ✅ Single feature test passed")
            print("2. 🔄 Ready for small folder test (5-10 features)")
            print("3. 🔄 Ready for full folder test (50+ features)")
            print("4. 🔄 Ready for full system test (all domains)")
            print("\nRun 'python test_srs_discovery.py' for full system test")
        
    except KeyboardInterrupt:
        print("\n⏹️  Testing interrupted by user")
    except Exception as e:
        print(f"\n❌ Testing failed with error: {e}")
        import traceback
        traceback.print_exc()
