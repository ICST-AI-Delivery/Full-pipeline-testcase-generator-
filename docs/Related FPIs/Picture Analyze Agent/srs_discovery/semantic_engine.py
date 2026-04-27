"""
Semantic Search Engine - Stage 2: Vector-based similarity matching using sentence transformers
"""

import numpy as np
import logging
from typing import Dict, List, Optional, Tuple
from .utils import Feature, RelationshipScore, SIMILARITY_SCALE, RELATIONSHIP_TYPES, logger, CacheManager

try:
    from sentence_transformers import SentenceTransformer
    import faiss
    DEPENDENCIES_AVAILABLE = True
except ImportError:
    DEPENDENCIES_AVAILABLE = False
    logger.warning("sentence-transformers or faiss not available. Semantic search will be disabled.")

class SemanticSearchEngine:
    """Stage 2: Semantic similarity matching using sentence transformers and FAISS"""
    
    def __init__(self, model_name: str = "all-MiniLM-L6-v2", cache_manager: Optional[CacheManager] = None):
        self.model_name = model_name
        self.cache_manager = cache_manager or CacheManager()
        
        if not DEPENDENCIES_AVAILABLE:
            logger.error("Required dependencies not available. Install with: pip install sentence-transformers faiss-cpu")
            self.model = None
            self.index = None
            return
        
        # Initialize sentence transformer model
        try:
            self.model = SentenceTransformer(model_name)
            logger.info(f"Loaded semantic model: {model_name}")
        except Exception as e:
            logger.error(f"Failed to load semantic model: {e}")
            self.model = None
        
        # FAISS index for fast similarity search
        self.index = None
        self.feature_embeddings: Dict[str, np.ndarray] = {}
        self.feature_texts: Dict[str, str] = {}
        self.feature_ids: List[str] = []
        self.indexed = False
    
    def build_embeddings(self, features: Dict[str, Feature]) -> None:
        """Build embeddings for all features"""
        if not self.model:
            logger.error("Semantic model not available")
            return
        
        logger.info("Building semantic embeddings...")
        
        # Check cache first
        cache_key = f"embeddings_{self.model_name}_{len(features)}"
        cached_data = self.cache_manager.load_cache(cache_key)
        
        if cached_data:
            self.feature_embeddings = cached_data['embeddings']
            self.feature_texts = cached_data['texts']
            self.feature_ids = cached_data['ids']
            logger.info("Loaded embeddings from cache")
        else:
            # Generate embeddings
            self._generate_embeddings(features)
            
            # Cache the results
            cache_data = {
                'embeddings': self.feature_embeddings,
                'texts': self.feature_texts,
                'ids': self.feature_ids
            }
            self.cache_manager.save_cache(cache_key, cache_data)
        
        # Build FAISS index
        self._build_faiss_index()
        self.indexed = True
        
        logger.info(f"Built semantic embeddings for {len(features)} features")
    
    def _generate_embeddings(self, features: Dict[str, Feature]) -> None:
        """Generate embeddings for all features"""
        texts_to_encode = []
        feature_ids = []
        
        for feature_id, feature in features.items():
            # Create comprehensive text representation
            feature_text = self._create_feature_text(feature)
            
            texts_to_encode.append(feature_text)
            feature_ids.append(feature_id)
            self.feature_texts[feature_id] = feature_text
        
        # Generate embeddings in batch for efficiency
        logger.info(f"Generating embeddings for {len(texts_to_encode)} features...")
        embeddings = self.model.encode(texts_to_encode, show_progress_bar=True)
        
        # Store embeddings
        for i, feature_id in enumerate(feature_ids):
            self.feature_embeddings[feature_id] = embeddings[i]
        
        self.feature_ids = feature_ids
    
    def _create_feature_text(self, feature: Feature) -> str:
        """Create comprehensive text representation of a feature for embedding"""
        text_parts = []
        
        # Feature name and domain
        text_parts.append(f"Feature: {feature.name}")
        text_parts.append(f"Domain: {feature.domain}")
        
        # Expert domains
        if feature.expert_domains:
            text_parts.append(f"Expert domains: {', '.join(feature.expert_domains)}")
        
        # CAN signals
        if feature.can_signals:
            text_parts.append(f"CAN signals: {', '.join(feature.can_signals)}")
        
        # Requirement content (sample to avoid too long text)
        requirement_texts = []
        for req in feature.requirements[:5]:  # Limit to first 5 requirements
            if req.content:
                # Clean and truncate requirement text
                clean_content = req.content.replace('\n', ' ').strip()
                if len(clean_content) > 200:
                    clean_content = clean_content[:200] + "..."
                requirement_texts.append(clean_content)
        
        if requirement_texts:
            text_parts.append("Requirements: " + " | ".join(requirement_texts))
        
        # Verification criteria (sample)
        verification_texts = []
        for req in feature.requirements[:3]:
            if req.verification_criteria:
                clean_criteria = req.verification_criteria.replace('\n', ' ').strip()
                if len(clean_criteria) > 100:
                    clean_criteria = clean_criteria[:100] + "..."
                verification_texts.append(clean_criteria)
        
        if verification_texts:
            text_parts.append("Verification: " + " | ".join(verification_texts))
        
        return " ".join(text_parts)
    
    def _build_faiss_index(self) -> None:
        """Build FAISS index for fast similarity search"""
        if not self.feature_embeddings:
            logger.error("No embeddings available to build index")
            return
        
        # Convert embeddings to numpy array
        embeddings_array = np.array([self.feature_embeddings[fid] for fid in self.feature_ids])
        
        # Create FAISS index
        dimension = embeddings_array.shape[1]
        self.index = faiss.IndexFlatIP(dimension)  # Inner product for cosine similarity
        
        # Normalize embeddings for cosine similarity
        faiss.normalize_L2(embeddings_array)
        
        # Add embeddings to index
        self.index.add(embeddings_array)
        
        logger.info(f"Built FAISS index with {self.index.ntotal} vectors")
    
    def find_semantic_matches(self, target_feature_id: str, max_results: int = 20) -> List[RelationshipScore]:
        """Find semantic matches for a target feature"""
        if not self.indexed or not self.model:
            logger.error("Semantic engine not properly initialized")
            return []
        
        if target_feature_id not in self.feature_embeddings:
            logger.error(f"Feature {target_feature_id} not found in embeddings")
            return []
        
        # Get target embedding
        target_embedding = self.feature_embeddings[target_feature_id].reshape(1, -1)
        faiss.normalize_L2(target_embedding)
        
        # Search for similar features
        similarities, indices = self.index.search(target_embedding, max_results + 1)  # +1 to exclude self
        
        relationships = []
        
        for i, (similarity, idx) in enumerate(zip(similarities[0], indices[0])):
            if idx == -1:  # Invalid index
                continue
            
            related_feature_id = self.feature_ids[idx]
            
            # Skip self-match
            if related_feature_id == target_feature_id:
                continue
            
            # Convert similarity to relationship score
            score, relationship_type, evidence = self._analyze_semantic_similarity(
                target_feature_id, related_feature_id, similarity
            )
            
            if score != 0:
                relationships.append(RelationshipScore(
                    related_feature_id=related_feature_id,
                    score=score,
                    relationship_type=relationship_type,
                    evidence=evidence,
                    confidence=float(similarity)
                ))
        
        # Sort by confidence (similarity score)
        relationships.sort(key=lambda x: x.confidence, reverse=True)
        
        logger.info(f"Found {len(relationships)} semantic matches for {target_feature_id}")
        return relationships
    
    def _analyze_semantic_similarity(self, target_id: str, related_id: str, similarity: float) -> Tuple[int, str, List[str]]:
        """Analyze semantic similarity and convert to relationship score"""
        
        # Similarity thresholds
        high_threshold = 0.8
        moderate_threshold = 0.6
        low_threshold = 0.4
        
        # Determine relationship strength based on similarity
        if similarity >= high_threshold:
            score = SIMILARITY_SCALE["HIGH_INPUT"]  # High semantic similarity suggests shared context
            strength = "high"
        elif similarity >= moderate_threshold:
            score = SIMILARITY_SCALE["MODERATE_INPUT"]
            strength = "moderate"
        elif similarity >= low_threshold:
            score = SIMILARITY_SCALE["MODERATE_INPUT"]
            strength = "low"
        else:
            return 0, "", []  # Too low similarity to be meaningful
        
        relationship_type = RELATIONSHIP_TYPES["SEMANTIC_SIMILARITY"]
        evidence = [
            f"Semantic similarity: {similarity:.3f} ({strength})",
            f"Similar content and context with {related_id}"
        ]
        
        # Add specific evidence based on text analysis
        target_text = self.feature_texts.get(target_id, "")
        related_text = self.feature_texts.get(related_id, "")
        
        # Look for common keywords or concepts
        common_concepts = self._find_common_concepts(target_text, related_text)
        if common_concepts:
            evidence.append(f"Common concepts: {', '.join(common_concepts[:3])}")
        
        return score, relationship_type, evidence
    
    def _find_common_concepts(self, text1: str, text2: str) -> List[str]:
        """Find common automotive concepts between two texts"""
        
        # Automotive domain keywords
        automotive_keywords = [
            'engine', 'transmission', 'brake', 'suspension', 'steering', 'safety',
            'airbag', 'seatbelt', 'abs', 'esc', 'traction', 'stability', 'cruise',
            'parking', 'lane', 'collision', 'blind', 'spot', 'camera', 'radar',
            'lidar', 'sensor', 'actuator', 'ecu', 'can', 'bus', 'signal',
            'telltale', 'warning', 'lamp', 'indicator', 'display', 'hmi',
            'infotainment', 'navigation', 'audio', 'bluetooth', 'usb', 'climate',
            'hvac', 'heating', 'cooling', 'ventilation', 'power', 'battery',
            'alternator', 'starter', 'fuel', 'injection', 'ignition', 'exhaust',
            'emission', 'catalyst', 'turbo', 'supercharger', 'hybrid', 'electric'
        ]
        
        text1_lower = text1.lower()
        text2_lower = text2.lower()
        
        common_concepts = []
        for keyword in automotive_keywords:
            if keyword in text1_lower and keyword in text2_lower:
                common_concepts.append(keyword)
        
        return common_concepts
    
    def get_feature_similarity(self, feature_id1: str, feature_id2: str) -> float:
        """Get similarity score between two specific features"""
        if not self.indexed or feature_id1 not in self.feature_embeddings or feature_id2 not in self.feature_embeddings:
            return 0.0
        
        emb1 = self.feature_embeddings[feature_id1]
        emb2 = self.feature_embeddings[feature_id2]
        
        # Normalize embeddings
        emb1_norm = emb1 / np.linalg.norm(emb1)
        emb2_norm = emb2 / np.linalg.norm(emb2)
        
        # Compute cosine similarity
        similarity = np.dot(emb1_norm, emb2_norm)
        return float(similarity)
    
    def get_statistics(self) -> Dict:
        """Get semantic engine statistics"""
        return {
            'model_name': self.model_name,
            'indexed_features': len(self.feature_embeddings),
            'embedding_dimension': len(next(iter(self.feature_embeddings.values()))) if self.feature_embeddings else 0,
            'faiss_index_size': self.index.ntotal if self.index else 0,
            'is_indexed': self.indexed,
            'dependencies_available': DEPENDENCIES_AVAILABLE
        }
