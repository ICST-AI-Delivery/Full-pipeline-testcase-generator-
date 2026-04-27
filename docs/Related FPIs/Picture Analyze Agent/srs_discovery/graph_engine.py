"""
Graph Relationship Engine - Stage 3: Multi-hop relationship discovery using NetworkX
"""

import logging
from typing import Dict, List, Set, Optional, Tuple
from collections import defaultdict, deque
from .utils import Feature, RelationshipScore, SIMILARITY_SCALE, RELATIONSHIP_TYPES, logger

try:
    import networkx as nx
    NETWORKX_AVAILABLE = True
except ImportError:
    NETWORKX_AVAILABLE = False
    logger.warning("NetworkX not available. Graph relationship discovery will be disabled.")

class RelationshipGraphEngine:
    """Stage 3: Graph-based relationship discovery using NetworkX"""
    
    def __init__(self):
        if not NETWORKX_AVAILABLE:
            logger.error("NetworkX not available. Install with: pip install networkx")
            self.graph = None
            return
        
        self.graph = nx.DiGraph()  # Directed graph for dependency relationships
        self.features: Dict[str, Feature] = {}
        self.built = False
    
    def build_graph(self, features: Dict[str, Feature], exact_relationships: Dict[str, List[RelationshipScore]]) -> None:
        """Build relationship graph from features and exact matches"""
        if not NETWORKX_AVAILABLE:
            logger.error("NetworkX not available")
            return
        
        logger.info("Building relationship graph...")
        
        self.features = features
        self.graph.clear()
        
        # Add all features as nodes
        for feature_id, feature in features.items():
            self.graph.add_node(feature_id, feature=feature)
        
        # Add edges based on exact relationships
        for source_id, relationships in exact_relationships.items():
            for rel in relationships:
                self._add_relationship_edge(source_id, rel)
        
        # Add implicit relationships based on graph analysis
        self._discover_implicit_relationships()
        
        self.built = True
        logger.info(f"Built graph with {self.graph.number_of_nodes()} nodes and {self.graph.number_of_edges()} edges")
    
    def _add_relationship_edge(self, source_id: str, relationship: RelationshipScore) -> None:
        """Add an edge to the graph based on a relationship score"""
        target_id = relationship.related_feature_id
        
        # Determine edge direction based on score
        if relationship.score < 0:
            # Source depends on target (input dependency)
            self.graph.add_edge(target_id, source_id, 
                              weight=abs(relationship.score),
                              relationship_type=relationship.relationship_type,
                              evidence=relationship.evidence,
                              confidence=relationship.confidence)
        elif relationship.score > 0:
            # Target depends on source (output importance)
            self.graph.add_edge(source_id, target_id,
                              weight=relationship.score,
                              relationship_type=relationship.relationship_type,
                              evidence=relationship.evidence,
                              confidence=relationship.confidence)
    
    def _discover_implicit_relationships(self) -> None:
        """Discover implicit relationships through graph analysis"""
        
        # Find transitive dependencies
        self._find_transitive_dependencies()
        
        # Find common dependency patterns
        self._find_common_dependency_patterns()
        
        # Find hub features (highly connected)
        self._identify_hub_features()
    
    def _find_transitive_dependencies(self) -> None:
        """Find transitive dependencies (A->B->C implies A indirectly depends on C)"""
        
        # Find paths of length 2 (one intermediate node)
        for source in self.graph.nodes():
            for intermediate in self.graph.successors(source):
                for target in self.graph.successors(intermediate):
                    if source != target and not self.graph.has_edge(source, target):
                        # Add transitive relationship with lower weight
                        source_weight = self.graph[source][intermediate]['weight']
                        intermediate_weight = self.graph[intermediate][target]['weight']
                        
                        # Transitive weight is minimum of the path weights, reduced
                        transitive_weight = min(source_weight, intermediate_weight) * 0.5
                        
                        if transitive_weight >= 1.0:  # Only add if significant
                            self.graph.add_edge(source, target,
                                              weight=transitive_weight,
                                              relationship_type="transitive_dependency",
                                              evidence=[f"Transitive dependency via {intermediate}"],
                                              confidence=0.6)
    
    def _find_common_dependency_patterns(self) -> None:
        """Find features that share common dependencies"""
        
        # Group features by their dependencies
        dependency_groups = defaultdict(list)
        
        for node in self.graph.nodes():
            # Get all predecessors (dependencies)
            predecessors = set(self.graph.predecessors(node))
            if predecessors:
                # Create a signature based on dependencies
                dep_signature = frozenset(predecessors)
                dependency_groups[dep_signature].append(node)
        
        # Add relationships between features with similar dependency patterns
        for dep_signature, feature_group in dependency_groups.items():
            if len(feature_group) > 1:
                # Features with similar dependencies are likely related
                for i, feature1 in enumerate(feature_group):
                    for feature2 in feature_group[i+1:]:
                        if not self.graph.has_edge(feature1, feature2) and not self.graph.has_edge(feature2, feature1):
                            # Add bidirectional relationship
                            self.graph.add_edge(feature1, feature2,
                                              weight=1.0,
                                              relationship_type="common_dependency_pattern",
                                              evidence=[f"Share {len(dep_signature)} common dependencies"],
                                              confidence=0.7)
    
    def _identify_hub_features(self) -> None:
        """Identify hub features that are highly connected"""
        
        # Calculate centrality measures
        in_degree_centrality = nx.in_degree_centrality(self.graph)
        out_degree_centrality = nx.out_degree_centrality(self.graph)
        
        # Identify hubs (features with high centrality)
        hub_threshold = 0.1  # Top 10% of features
        
        for node, in_centrality in in_degree_centrality.items():
            out_centrality = out_degree_centrality[node]
            
            if in_centrality > hub_threshold or out_centrality > hub_threshold:
                # Mark as hub in node attributes
                self.graph.nodes[node]['is_hub'] = True
                self.graph.nodes[node]['in_centrality'] = in_centrality
                self.graph.nodes[node]['out_centrality'] = out_centrality
    
    def find_graph_relationships(self, target_feature_id: str, max_hops: int = 2) -> List[RelationshipScore]:
        """Find graph-based relationships for a target feature"""
        if not self.built or not NETWORKX_AVAILABLE:
            logger.error("Graph not built or NetworkX not available")
            return []
        
        if target_feature_id not in self.graph:
            logger.error(f"Feature {target_feature_id} not found in graph")
            return []
        
        relationships = []
        
        # Find direct relationships
        relationships.extend(self._find_direct_graph_relationships(target_feature_id))
        
        # Find multi-hop relationships
        if max_hops > 1:
            relationships.extend(self._find_multihop_relationships(target_feature_id, max_hops))
        
        # Find structural relationships
        relationships.extend(self._find_structural_relationships(target_feature_id))
        
        # Remove duplicates and sort by confidence
        unique_relationships = {}
        for rel in relationships:
            key = rel.related_feature_id
            if key not in unique_relationships or rel.confidence > unique_relationships[key].confidence:
                unique_relationships[key] = rel
        
        final_relationships = list(unique_relationships.values())
        final_relationships.sort(key=lambda x: x.confidence, reverse=True)
        
        logger.info(f"Found {len(final_relationships)} graph relationships for {target_feature_id}")
        return final_relationships
    
    def _find_direct_graph_relationships(self, target_feature_id: str) -> List[RelationshipScore]:
        """Find direct graph relationships (immediate neighbors)"""
        relationships = []
        
        # Input dependencies (predecessors)
        for pred in self.graph.predecessors(target_feature_id):
            edge_data = self.graph[pred][target_feature_id]
            
            score = -int(edge_data['weight'])  # Negative for input dependency
            relationships.append(RelationshipScore(
                related_feature_id=pred,
                score=score,
                relationship_type=edge_data.get('relationship_type', 'graph_dependency'),
                evidence=edge_data.get('evidence', [f"Direct dependency from {pred}"]),
                confidence=edge_data.get('confidence', 0.8)
            ))
        
        # Output importance (successors)
        for succ in self.graph.successors(target_feature_id):
            edge_data = self.graph[target_feature_id][succ]
            
            score = int(edge_data['weight'])  # Positive for output importance
            relationships.append(RelationshipScore(
                related_feature_id=succ,
                score=score,
                relationship_type=edge_data.get('relationship_type', 'graph_dependency'),
                evidence=edge_data.get('evidence', [f"Direct output to {succ}"]),
                confidence=edge_data.get('confidence', 0.8)
            ))
        
        return relationships
    
    def _find_multihop_relationships(self, target_feature_id: str, max_hops: int) -> List[RelationshipScore]:
        """Find multi-hop relationships using BFS"""
        relationships = []
        
        # BFS for input dependencies (reverse direction)
        visited = set([target_feature_id])
        queue = deque([(target_feature_id, 0, [])])
        
        while queue:
            current, hops, path = queue.popleft()
            
            if hops >= max_hops:
                continue
            
            for pred in self.graph.predecessors(current):
                if pred not in visited:
                    new_path = path + [current]
                    
                    if hops + 1 == max_hops:
                        # Found a multi-hop dependency
                        path_weight = self._calculate_path_weight(new_path + [pred])
                        if path_weight > 0.5:  # Only significant paths
                            relationships.append(RelationshipScore(
                                related_feature_id=pred,
                                score=SIMILARITY_SCALE["MODERATE_INPUT"],
                                relationship_type="multihop_dependency",
                                evidence=[f"{hops+1}-hop dependency via {' -> '.join(new_path)}"],
                                confidence=path_weight * 0.6  # Reduced confidence for multi-hop
                            ))
                    else:
                        visited.add(pred)
                        queue.append((pred, hops + 1, new_path))
        
        return relationships
    
    def _calculate_path_weight(self, path: List[str]) -> float:
        """Calculate the weight of a path through the graph"""
        if len(path) < 2:
            return 0.0
        
        weights = []
        for i in range(len(path) - 1):
            if self.graph.has_edge(path[i], path[i+1]):
                weights.append(self.graph[path[i]][path[i+1]]['weight'])
        
        if not weights:
            return 0.0
        
        # Path weight is the minimum weight in the path (weakest link)
        return min(weights)
    
    def _find_structural_relationships(self, target_feature_id: str) -> List[RelationshipScore]:
        """Find relationships based on graph structure"""
        relationships = []
        
        # Find features with similar neighborhood structure
        target_neighbors = set(self.graph.predecessors(target_feature_id)) | set(self.graph.successors(target_feature_id))
        
        for other_feature in self.graph.nodes():
            if other_feature == target_feature_id:
                continue
            
            other_neighbors = set(self.graph.predecessors(other_feature)) | set(self.graph.successors(other_feature))
            
            # Calculate Jaccard similarity of neighborhoods
            if target_neighbors or other_neighbors:
                intersection = len(target_neighbors & other_neighbors)
                union = len(target_neighbors | other_neighbors)
                jaccard_similarity = intersection / union if union > 0 else 0
                
                if jaccard_similarity > 0.3:  # Significant structural similarity
                    relationships.append(RelationshipScore(
                        related_feature_id=other_feature,
                        score=SIMILARITY_SCALE["MODERATE_INPUT"],
                        relationship_type="structural_similarity",
                        evidence=[f"Structural similarity: {jaccard_similarity:.2f}", 
                                f"Share {intersection} common neighbors"],
                        confidence=jaccard_similarity
                    ))
        
        return relationships
    
    def get_dependency_chain(self, target_feature_id: str, max_depth: int = 3) -> Dict[str, List[str]]:
        """Get the complete dependency chain for a feature"""
        if not self.built or target_feature_id not in self.graph:
            return {}
        
        dependency_chain = {
            'direct_dependencies': list(self.graph.predecessors(target_feature_id)),
            'dependent_features': list(self.graph.successors(target_feature_id)),
            'transitive_dependencies': [],
            'dependency_path': []
        }
        
        # Find transitive dependencies using DFS
        visited = set()
        
        def dfs_dependencies(node, depth, path):
            if depth >= max_depth or node in visited:
                return
            
            visited.add(node)
            
            for pred in self.graph.predecessors(node):
                if pred not in path:  # Avoid cycles
                    new_path = path + [pred]
                    dependency_chain['transitive_dependencies'].append(pred)
                    dependency_chain['dependency_path'].append(' -> '.join(new_path))
                    dfs_dependencies(pred, depth + 1, new_path)
        
        dfs_dependencies(target_feature_id, 0, [target_feature_id])
        
        # Remove duplicates
        dependency_chain['transitive_dependencies'] = list(set(dependency_chain['transitive_dependencies']))
        
        return dependency_chain
    
    def get_statistics(self) -> Dict:
        """Get graph statistics"""
        if not self.built or not NETWORKX_AVAILABLE:
            return {'error': 'Graph not built or NetworkX not available'}
        
        return {
            'nodes': self.graph.number_of_nodes(),
            'edges': self.graph.number_of_edges(),
            'density': nx.density(self.graph),
            'is_connected': nx.is_weakly_connected(self.graph),
            'number_of_components': nx.number_weakly_connected_components(self.graph),
            'average_clustering': nx.average_clustering(self.graph.to_undirected()),
            'hub_features': len([n for n, d in self.graph.nodes(data=True) if d.get('is_hub', False)]),
            'networkx_available': NETWORKX_AVAILABLE
        }
