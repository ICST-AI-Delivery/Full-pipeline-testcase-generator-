"""
Exact Match Indexer - Stage 1: Lightning-fast exact matching using inverted indices
"""

import logging
from collections import defaultdict
from typing import Dict, List, Set, Optional
from .utils import Feature, RelationshipScore, SIMILARITY_SCALE, RELATIONSHIP_TYPES, logger

class ExactMatchIndexer:
    """Stage 1: Exact match engine using inverted indices for instant lookups"""
    
    def __init__(self):
        # Inverted indices for different types of exact matches
        self.can_signal_index: Dict[str, Set[str]] = defaultdict(set)
        self.expert_domain_index: Dict[str, Set[str]] = defaultdict(set)
        self.telltale_code_index: Dict[str, Set[str]] = defaultdict(set)
        self.popup_id_index: Dict[str, Set[str]] = defaultdict(set)
        self.visual_element_index: Dict[str, Set[str]] = defaultdict(set)
        
        # Reverse indices for output dependency analysis
        self.signal_providers: Dict[str, Set[str]] = defaultdict(set)
        self.domain_experts: Dict[str, Set[str]] = defaultdict(set)
        
        self.features: Dict[str, Feature] = {}
        self.indexed = False
    
    def build_indices(self, features: Dict[str, Feature]) -> None:
        """Build inverted indices from parsed features"""
        logger.info("Building exact match indices...")
        
        self.features = features
        self._clear_indices()
        
        for feature_id, feature in features.items():
            # Index CAN signals (both input and output)
            for signal in feature.can_signals:
                self.can_signal_index[signal].add(feature_id)
                # Assume feature can both consume and provide signals
                self.signal_providers[signal].add(feature_id)
            
            # Index expert domains
            for domain in feature.expert_domains:
                self.expert_domain_index[domain].add(feature_id)
                self.domain_experts[domain].add(feature_id)
            
            # Index telltale codes
            for code in feature.telltale_codes:
                self.telltale_code_index[code].add(feature_id)
            
            # Index pop-up IDs
            for popup_id in feature.popup_ids:
                self.popup_id_index[popup_id].add(feature_id)
            
            # Index visual elements
            for element in feature.visual_elements:
                self.visual_element_index[element].add(feature_id)
        
        self.indexed = True
        logger.info(f"Built indices for {len(features)} features")
        logger.info(f"Indexed {len(self.can_signal_index)} CAN signals")
        logger.info(f"Indexed {len(self.expert_domain_index)} expert domains")
    
    def find_exact_matches(self, target_feature_id: str) -> List[RelationshipScore]:
        """Find exact matches for a target feature using inverted indices"""
        if not self.indexed:
            logger.error("Indices not built. Call build_indices() first.")
            return []
        
        if target_feature_id not in self.features:
            logger.error(f"Feature {target_feature_id} not found")
            return []
        
        target_feature = self.features[target_feature_id]
        relationships = []
        
        # Track features we've already scored to avoid duplicates
        scored_features = set()
        
        # 1. CAN Signal Dependencies (Critical -3/+3)
        relationships.extend(self._find_signal_relationships(target_feature, scored_features))
        
        # 2. Expert Domain Overlaps (High -2)
        relationships.extend(self._find_domain_relationships(target_feature, scored_features))
        
        # 3. Telltale Code Matches (Moderate -1/+1)
        relationships.extend(self._find_telltale_relationships(target_feature, scored_features))
        
        # 4. Pop-up ID Matches (Moderate -1/+1)
        relationships.extend(self._find_popup_relationships(target_feature, scored_features))
        
        # 5. Visual Element Matches (Moderate -1/+1)
        relationships.extend(self._find_visual_relationships(target_feature, scored_features))
        
        # Sort by absolute score (strongest relationships first)
        relationships.sort(key=lambda x: abs(x.score), reverse=True)
        
        logger.info(f"Found {len(relationships)} exact matches for {target_feature_id}")
        return relationships
    
    def _find_signal_relationships(self, target_feature: Feature, scored_features: Set[str]) -> List[RelationshipScore]:
        """Find CAN signal-based relationships"""
        relationships = []
        
        for signal in target_feature.can_signals:
            related_features = self.can_signal_index[signal]
            
            for related_id in related_features:
                if related_id == target_feature.id or related_id in scored_features:
                    continue
                
                # Determine relationship direction and score
                score, relationship_type, evidence = self._analyze_signal_relationship(
                    target_feature, self.features[related_id], signal
                )
                
                if score != 0:
                    relationships.append(RelationshipScore(
                        related_feature_id=related_id,
                        score=score,
                        relationship_type=relationship_type,
                        evidence=evidence,
                        confidence=0.95  # High confidence for exact signal matches
                    ))
                    scored_features.add(related_id)
        
        return relationships
    
    def _analyze_signal_relationship(self, target: Feature, related: Feature, signal: str) -> tuple:
        """Analyze the relationship between two features sharing a CAN signal"""
        
        # Critical signals that indicate strong dependencies
        critical_signals = [
            'ManettinoSts', 'ESCOFFLampRequest', 'SuspensionSetupSts',
            'EngineRunningStatus', 'VehicleSpeed', 'GearPosition'
        ]
        
        # Determine if this is a critical signal
        is_critical = any(crit_sig in signal for crit_sig in critical_signals)
        
        # Analyze signal flow direction based on feature names and domains
        target_is_provider = self._is_signal_provider(target, signal)
        related_is_provider = self._is_signal_provider(related, signal)
        
        if target_is_provider and not related_is_provider:
            # Target provides signal to related feature
            score = SIMILARITY_SCALE["CRITICAL_OUTPUT"] if is_critical else SIMILARITY_SCALE["HIGH_OUTPUT"]
            relationship_type = RELATIONSHIP_TYPES["DIRECT_SIGNAL"]
            evidence = [f"Provides {signal} to {related.id}"]
            
        elif related_is_provider and not target_is_provider:
            # Target depends on signal from related feature
            score = SIMILARITY_SCALE["CRITICAL_INPUT"] if is_critical else SIMILARITY_SCALE["HIGH_INPUT"]
            relationship_type = RELATIONSHIP_TYPES["DIRECT_SIGNAL"]
            evidence = [f"Depends on {signal} from {related.id}"]
            
        else:
            # Both features use the signal (shared resource)
            score = SIMILARITY_SCALE["HIGH_INPUT"] if is_critical else SIMILARITY_SCALE["MODERATE_INPUT"]
            relationship_type = RELATIONSHIP_TYPES["SHARED_RESOURCE"]
            evidence = [f"Shares {signal} with {related.id}"]
        
        return score, relationship_type, evidence
    
    def _is_signal_provider(self, feature: Feature, signal: str) -> bool:
        """Determine if a feature is likely a provider of a specific signal"""
        
        # Signal provider patterns based on naming conventions
        provider_patterns = {
            'ManettinoSts': ['Manettino', 'Switch', 'Control'],
            'ESCOFFLampRequest': ['ESC', 'Safety', 'Control'],
            'SuspensionSetupSts': ['Suspension', 'Chassis', 'Setup'],
            'EngineRunningStatus': ['Engine', 'Powertrain', 'ECU'],
            'VehicleSpeed': ['Speed', 'Vehicle', 'Dynamics'],
            'GearPosition': ['Transmission', 'Gear', 'Drivetrain']
        }
        
        # Check if feature name/domain suggests it's a provider
        feature_text = f"{feature.name} {feature.domain}".upper()
        
        for sig_pattern, provider_keywords in provider_patterns.items():
            if sig_pattern in signal:
                return any(keyword.upper() in feature_text for keyword in provider_keywords)
        
        # Default heuristic: features with "Management", "Control", "System" are often providers
        provider_keywords = ['MANAGEMENT', 'CONTROL', 'SYSTEM', 'CONTROLLER', 'ECU']
        return any(keyword in feature_text for keyword in provider_keywords)
    
    def _find_domain_relationships(self, target_feature: Feature, scored_features: Set[str]) -> List[RelationshipScore]:
        """Find expert domain-based relationships"""
        relationships = []
        
        for domain in target_feature.expert_domains:
            related_features = self.expert_domain_index[domain]
            
            for related_id in related_features:
                if related_id == target_feature.id or related_id in scored_features:
                    continue
                
                # Domain overlap indicates shared expertise and potential integration
                relationships.append(RelationshipScore(
                    related_feature_id=related_id,
                    score=SIMILARITY_SCALE["HIGH_INPUT"],  # Features benefit from shared expertise
                    relationship_type=RELATIONSHIP_TYPES["DOMAIN_EXPERTISE"],
                    evidence=[f"Shared expertise domain: {domain}"],
                    confidence=0.8
                ))
                scored_features.add(related_id)
        
        return relationships
    
    def _find_telltale_relationships(self, target_feature: Feature, scored_features: Set[str]) -> List[RelationshipScore]:
        """Find telltale code-based relationships"""
        relationships = []
        
        for code in target_feature.telltale_codes:
            related_features = self.telltale_code_index[code]
            
            for related_id in related_features:
                if related_id == target_feature.id or related_id in scored_features:
                    continue
                
                relationships.append(RelationshipScore(
                    related_feature_id=related_id,
                    score=SIMILARITY_SCALE["MODERATE_INPUT"],
                    relationship_type=RELATIONSHIP_TYPES["SHARED_RESOURCE"],
                    evidence=[f"Shared telltale code: {code}"],
                    confidence=0.7
                ))
                scored_features.add(related_id)
        
        return relationships
    
    def _find_popup_relationships(self, target_feature: Feature, scored_features: Set[str]) -> List[RelationshipScore]:
        """Find pop-up ID-based relationships"""
        relationships = []
        
        for popup_id in target_feature.popup_ids:
            related_features = self.popup_id_index[popup_id]
            
            for related_id in related_features:
                if related_id == target_feature.id or related_id in scored_features:
                    continue
                
                relationships.append(RelationshipScore(
                    related_feature_id=related_id,
                    score=SIMILARITY_SCALE["MODERATE_INPUT"],
                    relationship_type=RELATIONSHIP_TYPES["SHARED_RESOURCE"],
                    evidence=[f"Shared pop-up ID: {popup_id}"],
                    confidence=0.7
                ))
                scored_features.add(related_id)
        
        return relationships
    
    def _find_visual_relationships(self, target_feature: Feature, scored_features: Set[str]) -> List[RelationshipScore]:
        """Find visual element-based relationships"""
        relationships = []
        
        for element in target_feature.visual_elements:
            related_features = self.visual_element_index[element]
            
            for related_id in related_features:
                if related_id == target_feature.id or related_id in scored_features:
                    continue
                
                relationships.append(RelationshipScore(
                    related_feature_id=related_id,
                    score=SIMILARITY_SCALE["MODERATE_INPUT"],
                    relationship_type=RELATIONSHIP_TYPES["SHARED_RESOURCE"],
                    evidence=[f"Shared visual element: {element}"],
                    confidence=0.6
                ))
                scored_features.add(related_id)
        
        return relationships
    
    def _clear_indices(self) -> None:
        """Clear all indices"""
        self.can_signal_index.clear()
        self.expert_domain_index.clear()
        self.telltale_code_index.clear()
        self.popup_id_index.clear()
        self.visual_element_index.clear()
        self.signal_providers.clear()
        self.domain_experts.clear()
    
    def get_statistics(self) -> Dict:
        """Get indexing statistics"""
        return {
            'indexed_features': len(self.features),
            'can_signals': len(self.can_signal_index),
            'expert_domains': len(self.expert_domain_index),
            'telltale_codes': len(self.telltale_code_index),
            'popup_ids': len(self.popup_id_index),
            'visual_elements': len(self.visual_element_index),
            'is_indexed': self.indexed
        }
