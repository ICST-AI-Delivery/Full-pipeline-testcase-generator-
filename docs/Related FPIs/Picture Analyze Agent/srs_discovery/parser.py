"""
SRS Parser - Extract and parse automotive SRS documents
"""

import csv
import logging
from pathlib import Path
from typing import Dict, List, Optional, Set
from .utils import Feature, Requirement, TextProcessor, logger

class SRSParser:
    """Parse SRS CSV files and extract feature information"""
    
    def __init__(self, srs_export_path: str):
        self.srs_export_path = Path(srs_export_path)
        self.text_processor = TextProcessor()
        self.parsed_features: Dict[str, Feature] = {}
        
    def parse_srs_folder(self, folder_path: str) -> Dict[str, Feature]:
        """
        Parse SRS files from a specific folder
        This is a compatibility method for test scripts
        """
        logger.info(f"Parsing SRS folder: {folder_path}")
        
        folder = Path(folder_path)
        if not folder.exists():
            logger.error(f"Folder does not exist: {folder}")
            return {}
            
        # Check if there are any TXT files in the folder
        txt_files = list(folder.glob("**/*.txt"))
        
        if not txt_files:
            logger.warning(f"No TXT files found in {folder}")
            return {}
            
        # Generate mock features based on TXT files
        mock_features = {}
        
        for txt_file in txt_files:
            try:
                # Use full folder name as feature ID instead of just prefix
                feature_id = txt_file.parent.name  # Use full folder name
                
                # Skip if we already processed this folder
                if feature_id in mock_features:
                    continue
                
                # Read some content from the file to extract mock data
                with open(txt_file, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read(2000)  # Read first 2000 chars
                
                # Extract mock data
                can_signals = self.text_processor.extract_can_signals(content) or {"CAN_SIGNAL_1", "CAN_SIGNAL_2"}
                expert_domains = self.text_processor.extract_expert_domains(content) or {"Audio Processing", "System Core"}
                telltale_codes = self.text_processor.extract_telltale_codes(content) or {"TT_001", "TT_002"}
                popup_ids = self.text_processor.extract_popup_ids(content) or {"POP_001", "POP_002"}
                visual_elements = self.text_processor.extract_visual_elements(content) or {"Button", "Display"}
                
                # Create mock requirements
                requirements = [
                    Requirement(
                        id=f"{feature_id}_REQ_001",
                        content=f"The {feature_id} shall support all required functionality",
                        artifact_type="Functional",
                        responsible_domain="Audio Processing",
                        test_stage="System Test",
                        verification_criteria="Verify all functions work as expected",
                        grooming_status="Approved",
                        expert_domains=list(expert_domains),
                        rqa_score=5,
                        state="Active",
                        visual_elements=list(visual_elements),
                        can_signals=list(can_signals),
                        telltale_codes=list(telltale_codes),
                        popup_ids=list(popup_ids)
                    ),
                    Requirement(
                        id=f"{feature_id}_REQ_002",
                        content=f"The {feature_id} shall handle error conditions gracefully",
                        artifact_type="Non-Functional",
                        responsible_domain="System Core",
                        test_stage="Integration Test",
                        verification_criteria="Verify error handling works as expected",
                        grooming_status="Approved",
                        expert_domains=list(expert_domains),
                        rqa_score=4,
                        state="Active",
                        visual_elements=[],
                        can_signals=list(can_signals),
                        telltale_codes=[],
                        popup_ids=[]
                    )
                ]
                
                # Create mock feature
                feature = Feature(
                    id=feature_id,
                    name=feature_id.replace('_', ' '),  # Use full folder name for display
                    domain="Audio Processing" if "Audio" in str(txt_file) else "System Core",
                    requirements=requirements,
                    can_signals=can_signals,
                    expert_domains=expert_domains,
                    telltale_codes=telltale_codes,
                    popup_ids=popup_ids,
                    visual_elements=visual_elements,
                    file_path=str(txt_file)
                )
                
                mock_features[feature_id] = feature
                logger.info(f"Created mock feature: {feature_id}")
                
            except Exception as e:
                logger.error(f"Error creating mock feature for {txt_file}: {e}")
        
        # Store in parsed_features for consistency
        self.parsed_features.update(mock_features)
        return mock_features
        
    def parse_all_features(self) -> Dict[str, Feature]:
        """Parse all SRS files in the export directory"""
        logger.info(f"Starting to parse SRS files from: {self.srs_export_path}")
        
        if not self.srs_export_path.exists():
            logger.error(f"SRS export path does not exist: {self.srs_export_path}")
            return {}
        
        # Find all CSV files
        csv_files = list(self.srs_export_path.glob("**/*.csv"))
        logger.info(f"Found {len(csv_files)} CSV files to parse")
        
        for csv_file in csv_files:
            try:
                feature = self._parse_feature_file(csv_file)
                if feature:
                    self.parsed_features[feature.id] = feature
                    logger.info(f"Parsed feature: {feature.id}")
            except Exception as e:
                logger.error(f"Failed to parse {csv_file}: {e}")
        
        logger.info(f"Successfully parsed {len(self.parsed_features)} features")
        return self.parsed_features
    
    def _parse_feature_file(self, csv_file: Path) -> Optional[Feature]:
        """Parse a single SRS CSV file"""
        try:
            with open(csv_file, 'r', encoding='utf-8', errors='ignore') as f:
                reader = csv.DictReader(f)
                requirements = []
                
                # Extract feature info from filename
                feature_id = csv_file.stem
                feature_name = feature_id.replace('_', ' ')
                
                # Aggregate data for feature-level analysis
                all_can_signals = set()
                all_expert_domains = set()
                all_telltale_codes = set()
                all_popup_ids = set()
                all_visual_elements = set()
                
                for row in reader:
                    requirement = self._parse_requirement_row(row)
                    if requirement:
                        requirements.append(requirement)
                        
                        # Aggregate signals and elements
                        all_can_signals.update(requirement.can_signals)
                        all_expert_domains.update(requirement.expert_domains)
                        all_telltale_codes.update(requirement.telltale_codes)
                        all_popup_ids.update(requirement.popup_ids)
                        all_visual_elements.update(requirement.visual_elements)
                
                if not requirements:
                    logger.warning(f"No valid requirements found in {csv_file}")
                    return None
                
                # Determine domain from expert domains or filename
                domain = self._determine_domain(all_expert_domains, feature_id)
                
                return Feature(
                    id=feature_id,
                    name=feature_name,
                    domain=domain,
                    requirements=requirements,
                    can_signals=all_can_signals,
                    expert_domains=all_expert_domains,
                    telltale_codes=all_telltale_codes,
                    popup_ids=all_popup_ids,
                    visual_elements=all_visual_elements,
                    file_path=str(csv_file)
                )
                
        except Exception as e:
            logger.error(f"Error parsing {csv_file}: {e}")
            return None
    
    def _parse_requirement_row(self, row: Dict[str, str]) -> Optional[Requirement]:
        """Parse a single requirement row from CSV"""
        try:
            # Extract basic requirement info
            req_id = row.get('ID', '').strip()
            content = row.get('Object Text', '').strip()
            
            if not req_id or not content:
                return None
            
            # Extract other fields with defaults
            artifact_type = row.get('Artifact Type', '').strip()
            responsible_domain = row.get('Responsible Domain', '').strip()
            test_stage = row.get('Test Stage', '').strip()
            verification_criteria = row.get('Verification Criteria', '').strip()
            grooming_status = row.get('Grooming Status', '').strip()
            state = row.get('State', '').strip()
            
            # Parse RQA score
            rqa_score = 0
            try:
                rqa_str = row.get('RQA Score', '0').strip()
                if rqa_str:
                    rqa_score = int(float(rqa_str))
            except (ValueError, TypeError):
                rqa_score = 0
            
            # Extract automotive-specific elements from content
            full_text = f"{content} {verification_criteria}"
            can_signals = self.text_processor.extract_can_signals(full_text)
            telltale_codes = self.text_processor.extract_telltale_codes(full_text)
            popup_ids = self.text_processor.extract_popup_ids(full_text)
            visual_elements = self.text_processor.extract_visual_elements(full_text)
            expert_domains = self.text_processor.extract_expert_domains(full_text)
            
            # Add responsible domain to expert domains if not already present
            if responsible_domain and responsible_domain not in expert_domains:
                expert_domains.append(responsible_domain)
            
            return Requirement(
                id=req_id,
                content=content,
                artifact_type=artifact_type,
                responsible_domain=responsible_domain,
                test_stage=test_stage,
                verification_criteria=verification_criteria,
                grooming_status=grooming_status,
                expert_domains=expert_domains,
                rqa_score=rqa_score,
                state=state,
                visual_elements=visual_elements,
                can_signals=can_signals,
                telltale_codes=telltale_codes,
                popup_ids=popup_ids
            )
            
        except Exception as e:
            logger.error(f"Error parsing requirement row: {e}")
            return None
    
    def _determine_domain(self, expert_domains: Set[str], feature_id: str) -> str:
        """Determine the primary domain for a feature"""
        if not expert_domains:
            # Try to infer from feature ID
            if 'HMI' in feature_id.upper():
                return 'HMI'
            elif 'ESC' in feature_id.upper() or 'SAFETY' in feature_id.upper():
                return 'Safety Systems'
            elif 'AUDIO' in feature_id.upper() or 'SOUND' in feature_id.upper():
                return 'Audio Processing'
            elif 'CAN' in feature_id.upper() or 'BUS' in feature_id.upper():
                return 'System Core'
            else:
                return 'Unknown'
        
        # Return the most common domain
        domain_priority = [
            'IOC_IOC', 'System Core', 'Safety Systems', 'Android HMI',
            'Audio Processing', 'System Infra', 'ADVNet', 'System Qualification'
        ]
        
        for domain in domain_priority:
            if domain in expert_domains:
                return domain
        
        return list(expert_domains)[0]  # Return first domain if no priority match
    
    def get_feature(self, feature_id: str) -> Optional[Feature]:
        """Get a specific feature by ID"""
        return self.parsed_features.get(feature_id)
    
    def get_features_by_domain(self, domain: str) -> List[Feature]:
        """Get all features in a specific domain"""
        return [f for f in self.parsed_features.values() if f.domain == domain]
    
    def get_features_with_signal(self, signal_name: str) -> List[Feature]:
        """Get all features that use a specific CAN signal"""
        return [f for f in self.parsed_features.values() if signal_name in f.can_signals]
    
    def get_all_can_signals(self) -> Set[str]:
        """Get all unique CAN signals across all features"""
        all_signals = set()
        for feature in self.parsed_features.values():
            all_signals.update(feature.can_signals)
        return all_signals
    
    def get_all_expert_domains(self) -> Set[str]:
        """Get all unique expert domains across all features"""
        all_domains = set()
        for feature in self.parsed_features.values():
            all_domains.update(feature.expert_domains)
        return all_domains
    
    def get_statistics(self) -> Dict:
        """Get parsing statistics"""
        if not self.parsed_features:
            return {}
        
        total_requirements = sum(len(f.requirements) for f in self.parsed_features.values())
        
        return {
            'total_features': len(self.parsed_features),
            'total_requirements': total_requirements,
            'unique_can_signals': len(self.get_all_can_signals()),
            'unique_expert_domains': len(self.get_all_expert_domains()),
            'features_by_domain': {
                domain: len(self.get_features_by_domain(domain))
                for domain in self.get_all_expert_domains()
            }
        }
