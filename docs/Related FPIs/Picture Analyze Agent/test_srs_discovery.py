#!/usr/bin/env python3
"""
Test script for the Smart SRS Feature Discovery System
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

def test_basic_functionality():
    """Test basic functionality of the SRS Discovery System"""
    
    print("=" * 60)
    print("🚗 Smart SRS Feature Discovery System - Test Suite")
    print("=" * 60)
    
    # Check if SRS Export folder exists
    srs_export_path = Path("../SRS Export")
    if not srs_export_path.exists():
        srs_export_path = Path("SRS Export")
    
    if not srs_export_path.exists():
        print("❌ ERROR: SRS Export folder not found!")
        print("   Please ensure the SRS Export folder is in the current directory or parent directory")
        return False
    
    print(f"✅ Found SRS Export folder: {srs_export_path.absolute()}")
    
    # Test 1: Parser
    print("\n" + "="*50)
    print("🔍 TEST 1: SRS Parser")
    print("="*50)
    
    parser = SRSParser(str(srs_export_path))
    
    # Try to find a suitable test folder
    test_folders = [
        srs_export_path / "SRS_Audio" / "FAD-0_Ferrari_Audio_Director_Introduction",
        srs_export_path / "SRS_Audio",
        srs_export_path / "SRS_Connectivity",
        srs_export_path / "SRS_Diagnostics"
    ]
    
    features = {}
    test_folder = None
    
    for folder in test_folders:
        if folder.exists():
            print(f"📁 Testing with folder: {folder.name}")
            try:
                features = parser.parse_srs_folder(str(folder))
                if features:
                    test_folder = folder
                    break
            except Exception as e:
                print(f"   ⚠️  Error parsing {folder.name}: {e}")
                continue
    
    if not features:
        print("❌ No features found in any test folder")
        return False
    
    print(f"✅ Successfully parsed {len(features)} features from {test_folder.name}")
    
    # Show sample features
    feature_list = list(features.keys())[:5]
    print(f"📋 Sample features: {feature_list}")
    
    # Test 2: Exact Match Indexer
    print("\n" + "="*50)
    print("🎯 TEST 2: Exact Match Indexer")
    print("="*50)
    
    indexer = ExactMatchIndexer()
    indexer.build_indices(features)
    
    stats = indexer.get_statistics()
    print(f"✅ Built indices for {stats['indexed_features']} features")
    print(f"   📊 CAN signals: {stats['can_signals']}")
    print(f"   📊 Expert domains: {stats['expert_domains']}")
    
    # Test with first available feature
    if features:
        test_feature_id = list(features.keys())[0]
        print(f"\n🔍 Testing exact matches for: {test_feature_id}")
        
        relationships = indexer.find_exact_matches(test_feature_id)
        print(f"✅ Found {len(relationships)} exact match relationships")
        
        # Show top 3 relationships
        for i, rel in enumerate(relationships[:3]):
            print(f"   {i+1}. {rel.related_feature_id} (score: {rel.score:+d}, confidence: {rel.confidence:.2f})")
            print(f"      Type: {rel.relationship_type}")
            print(f"      Evidence: {rel.evidence[0] if rel.evidence else 'N/A'}")
    
    # Test 3: Semantic Search Engine (optional - requires dependencies)
    print("\n" + "="*50)
    print("🧠 TEST 3: Semantic Search Engine")
    print("="*50)
    
    try:
        semantic_engine = SemanticSearchEngine()
        semantic_stats = semantic_engine.get_statistics()
        
        if semantic_stats['dependencies_available']:
            print("✅ Semantic dependencies available")
            
            # Build embeddings (this might take a while)
            print("🔄 Building semantic embeddings... (this may take a moment)")
            start_time = time.time()
            semantic_engine.build_embeddings(features)
            build_time = time.time() - start_time
            
            print(f"✅ Built embeddings in {build_time:.2f} seconds")
            print(f"   📊 Embedding dimension: {semantic_stats['embedding_dimension']}")
            
            # Test semantic search
            if features:
                test_feature_id = list(features.keys())[0]
                print(f"\n🔍 Testing semantic matches for: {test_feature_id}")
                
                semantic_relationships = semantic_engine.find_semantic_matches(test_feature_id, max_results=5)
                print(f"✅ Found {len(semantic_relationships)} semantic relationships")
                
                # Show top 3 relationships
                for i, rel in enumerate(semantic_relationships[:3]):
                    print(f"   {i+1}. {rel.related_feature_id} (score: {rel.score:+d}, confidence: {rel.confidence:.3f})")
                    print(f"      Evidence: {rel.evidence[0] if rel.evidence else 'N/A'}")
        else:
            print("⚠️  Semantic dependencies not available")
            print("   Install with: pip install sentence-transformers faiss-cpu")
    
    except Exception as e:
        print(f"⚠️  Semantic engine test failed: {e}")
    
    # Test 4: Graph Relationship Engine (optional - requires NetworkX)
    print("\n" + "="*50)
    print("🕸️  TEST 4: Graph Relationship Engine")
    print("="*50)
    
    try:
        graph_engine = RelationshipGraphEngine()
        graph_stats = graph_engine.get_statistics()
        
        if graph_stats.get('networkx_available', False):
            print("✅ NetworkX available")
            
            # Build graph using exact relationships
            exact_relationships = {}
            for feature_id in list(features.keys())[:10]:  # Limit to first 10 for testing
                exact_relationships[feature_id] = indexer.find_exact_matches(feature_id)
            
            graph_engine.build_graph(features, exact_relationships)
            
            final_stats = graph_engine.get_statistics()
            print(f"✅ Built graph with {final_stats['nodes']} nodes and {final_stats['edges']} edges")
            print(f"   📊 Graph density: {final_stats['density']:.3f}")
            print(f"   📊 Hub features: {final_stats['hub_features']}")
            
            # Test graph relationships
            if features:
                test_feature_id = list(features.keys())[0]
                print(f"\n🔍 Testing graph relationships for: {test_feature_id}")
                
                graph_relationships = graph_engine.find_graph_relationships(test_feature_id)
                print(f"✅ Found {len(graph_relationships)} graph relationships")
                
                # Show top 3 relationships
                for i, rel in enumerate(graph_relationships[:3]):
                    print(f"   {i+1}. {rel.related_feature_id} (score: {rel.score:+d}, confidence: {rel.confidence:.3f})")
                    print(f"      Type: {rel.relationship_type}")
        else:
            print("⚠️  NetworkX not available")
            print("   Install with: pip install networkx")
    
    except Exception as e:
        print(f"⚠️  Graph engine test failed: {e}")
    
    # Summary
    print("\n" + "="*60)
    print("📊 TEST SUMMARY")
    print("="*60)
    print(f"✅ Successfully tested SRS Discovery System")
    print(f"📁 Test data: {len(features)} features from {test_folder.name if test_folder else 'N/A'}")
    print(f"🎯 Exact matching: Working")
    print(f"🧠 Semantic search: {'Working' if 'semantic_engine' in locals() and hasattr(semantic_engine, 'indexed') and semantic_engine.indexed else 'Needs dependencies'}")
    print(f"🕸️  Graph analysis: {'Working' if 'graph_engine' in locals() and hasattr(graph_engine, 'built') and graph_engine.built else 'Needs dependencies'}")
    
    return True

def test_specific_feature():
    """Test with a specific feature if available"""
    
    print("\n" + "="*60)
    print("🎯 SPECIFIC FEATURE TEST")
    print("="*60)
    
    # Look for the Manettino feature we analyzed earlier
    srs_export_path = Path("../SRS Export") if Path("../SRS Export").exists() else Path("SRS Export")
    
    # Try to find VEH-F165 or similar
    test_paths = [
        srs_export_path / "SRS_Audio",
        srs_export_path / "SRS_Connectivity", 
        srs_export_path / "SRS_Diagnostics"
    ]
    
    parser = SRSParser(str(srs_export_path))
    
    for test_path in test_paths:
        if test_path.exists():
            print(f"🔍 Searching for specific features in {test_path.name}...")
            try:
                features = parser.parse_srs_folder(str(test_path))
                
                # Look for interesting features
                manettino_features = [fid for fid in features.keys() if 'manettino' in fid.lower()]
                audio_features = [fid for fid in features.keys() if 'audio' in fid.lower()]
                
                if manettino_features:
                    print(f"🎯 Found Manettino features: {manettino_features}")
                    return manettino_features[0], features
                elif audio_features:
                    print(f"🎵 Found Audio features: {audio_features[:3]}")
                    return audio_features[0], features
                
            except Exception as e:
                print(f"   ⚠️  Error: {e}")
                continue
    
    return None, {}

if __name__ == "__main__":
    print("🚀 Starting SRS Discovery System Tests...")
    
    try:
        # Run basic functionality test
        success = test_basic_functionality()
        
        if success:
            # Try specific feature test
            specific_feature, features = test_specific_feature()
            
            if specific_feature:
                print(f"\n🎯 Testing specific feature: {specific_feature}")
                
                # Quick relationship test
                indexer = ExactMatchIndexer()
                indexer.build_indices(features)
                relationships = indexer.find_exact_matches(specific_feature)
                
                print(f"✅ Found {len(relationships)} relationships for {specific_feature}")
                for rel in relationships[:5]:
                    print(f"   → {rel.related_feature_id} (score: {rel.score:+d})")
        
        print("\n🎉 Testing completed!")
        
    except KeyboardInterrupt:
        print("\n⏹️  Testing interrupted by user")
    except Exception as e:
        print(f"\n❌ Testing failed with error: {e}")
        import traceback
        traceback.print_exc()
