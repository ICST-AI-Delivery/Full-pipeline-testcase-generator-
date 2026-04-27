#!/usr/bin/env python3
"""
Comprehensive FPI Testcase Context Dependency Matrix Generator

This script creates a comprehensive n×n relationship matrix where n = total number of features
in the entire SRS Export, then focuses analysis on 18 specified features using the FPI testcase
context dependency methodology with antisymmetric matrix principles.
"""

import os
import json
import csv
import pandas as pd
from pathlib import Path
from typing import Dict, List, Tuple, Set
from dataclasses import dataclass
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class FPIFeature:
    """Represents an FPI feature with its metadata and content"""
    feature_id: str
    domain: str
    full_path: str
    content: Dict = None
    
@dataclass
class FPIRelationship:
    """Represents a relationship between two FPI features"""
    main_fpi: str
    related_fpi: str
    score: int
    direction: str  # "Upstream" or "Downstream"
    necessity: str  # "Critical", "High", "Low"
    context_usage: List[str]
    extracted_context: List[str]
    reasoning: str
    confidence: str
    evidence: List[str]

class ComprehensiveFPIMatrixGenerator:
    """
    Generates comprehensive FPI testcase context dependency matrices using antisymmetric principles
    """
    
    def __init__(self, srs_export_path: str = "SRS Export/SRS Export"):
        self.srs_export_path = Path(srs_export_path)
        self.features: Dict[str, FPIFeature] = {}
        self.matrix: Dict[Tuple[str, str], int] = {}
        self.relationships: List[FPIRelationship] = []
        
        # Target features for analysis
        self.target_features = [
            # SRS_Audio
            "2xA2B_Audio_Layout",
            "AUD-0_Audio_System_Introduction",
            
            # SRS_Connectivity  
            "Access_Point_Management",
            
            # SRS_Diagnostics
            "[GPIO2]_Dig_IO_#2_-_Clock_Button_2_Over_current_(0x9062,_0x19)",
            "3D_Car_Model_Color_-_Exterior_($FE78)",
            
            # SRS_DMS
            "DMS-7_DRIVER_GAZE_ESTIMATION",
            "DMS-8_NON-NOMINAL_CONDITION_DETERMINATION",
            
            # SRS_HMI Software
            "PRK-0__Obstacle_Proximity_Signalling_Command_Management",
            "AUS-6_VIP",
            
            # SRS_Instrument Cluster
            "VEH-F165_Manettino",
            "VEH-F247_External_Lights_Management",
            
            # SRS_Navigation
            "Maps",
            "License_activation",
            
            # SRS_System Architecture
            "Ceremony_Sounds",
            "Clock_Info_Management",
            
            # SRS_Tuner
            "Internet_Radio",
            "RAD-19_Radio_Text"
        ]
        
    def discover_all_features(self) -> Dict[str, List[str]]:
        """
        Discover all features across all SRS domains
        Returns: Dictionary mapping domain -> list of features
        """
        logger.info("🔍 Discovering all features in SRS Export...")
        
        domain_features = {}
        total_features = 0
        
        if not self.srs_export_path.exists():
            logger.error(f"❌ SRS Export path not found: {self.srs_export_path}")
            return domain_features
            
        # Iterate through all SRS domains
        for domain_path in self.srs_export_path.iterdir():
            if domain_path.is_dir() and (domain_path.name.startswith("SRS_") or domain_path.name.startswith("SRS ")):
                domain_name = domain_path.name
                features = []
                
                # Discover features in this domain
                for feature_path in domain_path.iterdir():
                    if feature_path.is_dir() and not feature_path.name.startswith('.'):
                        feature_id = feature_path.name
                        features.append(feature_id)
                        
                        # Create FPIFeature object
                        fpi_feature = FPIFeature(
                            feature_id=feature_id,
                            domain=domain_name,
                            full_path=str(feature_path)
                        )
                        self.features[feature_id] = fpi_feature
                        
                domain_features[domain_name] = sorted(features)
                total_features += len(features)
                logger.info(f"  📊 {domain_name}: {len(features)} features")
                
        logger.info(f"✅ Total features discovered: {total_features}")
        logger.info(f"📈 Matrix dimensions: {total_features} × {total_features}")
        
        return domain_features
        
    def load_feature_content(self, feature_id: str) -> Dict:
        """
        Load content for a specific feature from TXT files or infer from feature name
        """
        if feature_id not in self.features:
            logger.warning(f"⚠️ Feature not found: {feature_id}")
            return {}
            
        feature = self.features[feature_id]
        feature_path = Path(feature.full_path)
        content = {
            "requirements": [],
            "signals": [],
            "configurations": [],
            "metadata": {},
            "inferred_content": {}
        }
        
        try:
            # Look for TXT files in the feature directory
            txt_files = list(feature_path.glob("*.txt"))
            
            if txt_files:
                for txt_file in txt_files:
                    try:
                        with open(txt_file, 'r', encoding='utf-8') as f:
                            txt_content = f.read()
                            content["metadata"][txt_file.stem] = txt_content
                            
                            # Parse content for signals and requirements
                            if "CAN" in txt_content or "signal" in txt_content.lower():
                                content["signals"].append({"source": txt_file.name, "content": txt_content})
                            if "requirement" in txt_content.lower() or "shall" in txt_content.lower():
                                content["requirements"].append({"source": txt_file.name, "content": txt_content})
                                
                    except Exception as e:
                        logger.warning(f"⚠️ Could not read {txt_file}: {e}")
            else:
                # If no TXT files found, infer content from feature name and domain
                content["inferred_content"] = self._infer_feature_content(feature_id, feature.domain)
                    
            # Store content in feature object
            feature.content = content
            
        except Exception as e:
            logger.warning(f"⚠️ Could not load content for {feature_id}: {e}")
            
        return content
        
    def _infer_feature_content(self, feature_id: str, domain: str) -> Dict:
        """
        Infer feature content based on feature name and domain when no TXT files are available
        """
        inferred = {
            "signals": [],
            "requirements": [],
            "automotive_context": [],
            "testcase_implications": []
        }
        
        # Automotive domain-specific inference patterns
        automotive_patterns = {
            "Audio": {
                "signals": ["AudioRequest", "VolumeRequest", "MuteRequest", "AudioSts", "VolumeSts"],
                "context": ["Audio system state", "Volume control", "Mute functionality"],
                "testcase": ["Audio output verification", "Volume level testing", "Mute state validation"]
            },
            "Connectivity": {
                "signals": ["BTRequest", "WiFiRequest", "ConnectionSts", "PairingRequest"],
                "context": ["Bluetooth connectivity", "WiFi management", "Device pairing"],
                "testcase": ["Connection establishment", "Pairing process", "Signal strength validation"]
            },
            "Diagnostics": {
                "signals": ["DiagRequest", "DTCRequest", "DiagSts", "FaultSts"],
                "context": ["Diagnostic trouble codes", "System health monitoring", "Fault detection"],
                "testcase": ["DTC generation", "Fault injection", "Diagnostic response validation"]
            },
            "DMS": {
                "signals": ["DriverGazeSts", "AttentionSts", "DMSRequest", "AlertRequest"],
                "context": ["Driver monitoring", "Attention detection", "Safety alerts"],
                "testcase": ["Gaze tracking accuracy", "Attention level detection", "Alert triggering"]
            },
            "HMI": {
                "signals": ["DisplayRequest", "PopupRequest", "HMISts", "UserInputSts"],
                "context": ["Display management", "User interface", "Popup notifications"],
                "testcase": ["Display rendering", "User interaction", "Popup behavior"]
            },
            "Instrument": {
                "signals": ["SpeedSts", "RPMSts", "FuelSts", "TelltaleRequest"],
                "context": ["Instrument cluster display", "Vehicle status", "Warning indicators"],
                "testcase": ["Gauge accuracy", "Telltale activation", "Display updates"]
            },
            "Navigation": {
                "signals": ["NavRequest", "RouteRequest", "GPSSts", "MapSts"],
                "context": ["GPS navigation", "Route calculation", "Map display"],
                "testcase": ["Route guidance", "GPS accuracy", "Map rendering"]
            },
            "System": {
                "signals": ["SystemSts", "ModeSts", "ConfigRequest", "InitSts"],
                "context": ["System architecture", "Mode management", "Configuration"],
                "testcase": ["System initialization", "Mode transitions", "Configuration validation"]
            },
            "Tuner": {
                "signals": ["RadioRequest", "FrequencySts", "StationSts", "TunerRequest"],
                "context": ["Radio tuning", "Station selection", "Signal reception"],
                "testcase": ["Frequency tuning", "Station switching", "Signal quality"]
            }
        }
        
        # Extract domain key from full domain name (e.g., "SRS_Audio" -> "Audio")
        domain_key = domain.replace("SRS_", "")
        
        if domain_key in automotive_patterns:
            pattern = automotive_patterns[domain_key]
            inferred["signals"] = pattern["signals"]
            inferred["automotive_context"] = pattern["context"]
            inferred["testcase_implications"] = pattern["testcase"]
        
        # Feature-specific inference based on feature name patterns
        feature_lower = feature_id.lower()
        
        # Manettino-specific patterns
        if "manettino" in feature_lower:
            inferred["signals"].extend(["ManettinoSts", "ManettinoRequest", "ModeSts"])
            inferred["automotive_context"].extend(["Driving mode selection", "Vehicle behavior control"])
            inferred["testcase_implications"].extend(["Mode switching validation", "Behavior change verification"])
            
        # External lights patterns
        if "external" in feature_lower and "light" in feature_lower:
            inferred["signals"].extend(["ExternalLightRequest", "LightSts", "BeamRequest"])
            inferred["automotive_context"].extend(["External lighting control", "Beam management"])
            inferred["testcase_implications"].extend(["Light activation", "Beam switching", "Bulb failure detection"])
            
        # Audio layout patterns
        if "audio" in feature_lower and "layout" in feature_lower:
            inferred["signals"].extend(["AudioLayoutRequest", "SpeakerSts", "AmplifierSts"])
            inferred["automotive_context"].extend(["Audio system configuration", "Speaker management"])
            inferred["testcase_implications"].extend(["Audio routing", "Speaker balance", "Layout switching"])
            
        # Access point patterns
        if "access" in feature_lower and "point" in feature_lower:
            inferred["signals"].extend(["APRequest", "WiFiAPSts", "ClientSts"])
            inferred["automotive_context"].extend(["WiFi access point", "Client management"])
            inferred["testcase_implications"].extend(["AP activation", "Client connection", "Network security"])
            
        # Driver gaze patterns
        if "driver" in feature_lower and "gaze" in feature_lower:
            inferred["signals"].extend(["GazeDirectionSts", "EyeTrackingSts", "AttentionLevelSts"])
            inferred["automotive_context"].extend(["Eye tracking", "Attention monitoring", "Safety assessment"])
            inferred["testcase_implications"].extend(["Gaze direction accuracy", "Attention detection", "Alert generation"])
            
        # Proximity signalling patterns
        if "proximity" in feature_lower or "obstacle" in feature_lower:
            inferred["signals"].extend(["ProximitySts", "ObstacleDetectedSts", "DistanceSts"])
            inferred["automotive_context"].extend(["Obstacle detection", "Distance measurement", "Parking assistance"])
            inferred["testcase_implications"].extend(["Detection accuracy", "Distance calculation", "Warning activation"])
            
        # Maps and navigation patterns
        if "maps" in feature_lower or "navigation" in feature_lower:
            inferred["signals"].extend(["MapDataSts", "NavigationSts", "RouteSts"])
            inferred["automotive_context"].extend(["Map data management", "Route guidance", "GPS positioning"])
            inferred["testcase_implications"].extend(["Map loading", "Route calculation", "Turn-by-turn guidance"])
            
        # Radio and tuner patterns
        if "radio" in feature_lower or "tuner" in feature_lower:
            inferred["signals"].extend(["RadioSts", "FrequencySts", "StationSts"])
            inferred["automotive_context"].extend(["Radio reception", "Station management", "Audio streaming"])
            inferred["testcase_implications"].extend(["Station tuning", "Signal quality", "Audio output"])
            
        return inferred
        
    def analyze_fpi_relationship(self, main_fpi: str, related_fpi: str) -> FPIRelationship:
        """
        Analyze the testcase context dependency relationship between two FPIs
        using the FPI testcase context dependency methodology
        """
        
        # Load content for both features
        main_content = self.load_feature_content(main_fpi)
        related_content = self.load_feature_content(related_fpi)
        
        # Initialize relationship analysis
        score = 0
        direction = ""
        necessity = ""
        context_usage = []
        extracted_context = []
        reasoning = ""
        confidence = "Undetermined"
        evidence = []
        
        # Skip self-reference (diagonal elements)
        if main_fpi == related_fpi:
            return FPIRelationship(
                main_fpi=main_fpi,
                related_fpi=related_fpi,
                score=0,
                direction="None",
                necessity="None",
                context_usage=[],
                extracted_context=[],
                reasoning="Self-reference - diagonal element",
                confidence="Confirmed",
                evidence=["Antisymmetric matrix diagonal rule"]
            )
            
        # Analyze for testcase context dependencies
        upstream_score, upstream_context = self._analyze_upstream_dependency(main_fpi, related_fpi, main_content, related_content)
        downstream_score, downstream_context = self._analyze_downstream_dependency(main_fpi, related_fpi, main_content, related_content)
        
        # Determine primary relationship direction
        if abs(upstream_score) > abs(downstream_score):
            score = -abs(upstream_score)  # Negative for upstream
            direction = "Upstream"
            context_usage = upstream_context["usage"]
            extracted_context = upstream_context["context"]
            reasoning = upstream_context["reasoning"]
            evidence = upstream_context["evidence"]
        elif abs(downstream_score) > abs(upstream_score):
            score = abs(downstream_score)  # Positive for downstream
            direction = "Downstream"
            context_usage = downstream_context["usage"]
            extracted_context = downstream_context["context"]
            reasoning = downstream_context["reasoning"]
            evidence = downstream_context["evidence"]
        else:
            score = 0
            direction = "None"
            reasoning = "No significant testcase context dependency found"
            
        # Determine necessity level
        if abs(score) == 3:
            necessity = "Critical"
            confidence = "Confirmed" if evidence else "Probable"
        elif abs(score) == 2:
            necessity = "High"
            confidence = "Probable" if evidence else "Undetermined"
        elif abs(score) == 1:
            necessity = "Low"
            confidence = "Probable" if evidence else "Undetermined"
        else:
            necessity = "None"
            confidence = "Confirmed"
            
        return FPIRelationship(
            main_fpi=main_fpi,
            related_fpi=related_fpi,
            score=score,
            direction=direction,
            necessity=necessity,
            context_usage=context_usage,
            extracted_context=extracted_context,
            reasoning=reasoning,
            confidence=confidence,
            evidence=evidence
        )
        
    def _analyze_upstream_dependency(self, main_fpi: str, related_fpi: str, main_content: Dict, related_content: Dict) -> Tuple[int, Dict]:
        """
        Analyze if related_fpi provides upstream context needed for main_fpi testcase generation
        (preconditions, setup, activation, constraints)
        """
        score = 0
        context = {
            "usage": [],
            "context": [],
            "reasoning": "",
            "evidence": []
        }
        
        # Check for signal dependencies
        main_signals = self._extract_signals(main_content)
        related_signals = self._extract_signals(related_content)
        
        # Look for signals that main_fpi consumes from related_fpi
        signal_dependencies = self._find_signal_dependencies(main_signals, related_signals)
        if signal_dependencies:
            score = max(score, 2)  # High upstream dependency
            context["usage"].extend(["Precondition", "Setup"])
            context["context"].extend([f"Signal dependency: {dep}" for dep in signal_dependencies])
            context["evidence"].extend([f"CAN signal: {dep}" for dep in signal_dependencies])
            
        # Check for state/mode dependencies
        state_dependencies = self._find_state_dependencies(main_fpi, related_fpi, main_content, related_content)
        if state_dependencies:
            score = max(score, 2)  # High upstream dependency
            context["usage"].extend(["Precondition", "Activation"])
            context["context"].extend(state_dependencies)
            context["evidence"].extend([f"State dependency: {dep}" for dep in state_dependencies])
            
        # Check for configuration dependencies
        config_dependencies = self._find_configuration_dependencies(main_content, related_content)
        if config_dependencies:
            score = max(score, 1)  # Low upstream dependency
            context["usage"].append("Setup")
            context["context"].extend(config_dependencies)
            context["evidence"].extend([f"Configuration: {dep}" for dep in config_dependencies])
            
        # Determine if critical (score 3)
        if self._is_critical_upstream_dependency(main_fpi, related_fpi, main_content, related_content):
            score = 3
            context["usage"].append("TestcaseDescription")
            context["reasoning"] = f"Critical upstream dependency: {main_fpi} cannot be tested without {related_fpi} context"
        elif score > 0:
            context["reasoning"] = f"Upstream dependency: {related_fpi} provides setup/precondition context for {main_fpi}"
            
        return score, context
        
    def _analyze_downstream_dependency(self, main_fpi: str, related_fpi: str, main_content: Dict, related_content: Dict) -> Tuple[int, Dict]:
        """
        Analyze if related_fpi provides downstream context needed for main_fpi testcase verification
        (expected results, output verification, propagated effects)
        """
        score = 0
        context = {
            "usage": [],
            "context": [],
            "reasoning": "",
            "evidence": []
        }
        
        # Check for output signal dependencies
        main_outputs = self._extract_output_signals(main_content)
        related_inputs = self._extract_input_signals(related_content)
        
        # Look for signals that main_fpi outputs to related_fpi
        output_dependencies = self._find_output_dependencies(main_outputs, related_inputs)
        if output_dependencies:
            score = max(score, 2)  # High downstream dependency
            context["usage"].extend(["ExpectedResult", "Verification"])
            context["context"].extend([f"Output verification: {dep}" for dep in output_dependencies])
            context["evidence"].extend([f"Output signal: {dep}" for dep in output_dependencies])
            
        # Check for HMI/display effects
        hmi_effects = self._find_hmi_effects(main_fpi, related_fpi, main_content, related_content)
        if hmi_effects:
            score = max(score, 2)  # High downstream dependency
            context["usage"].append("Verification")
            context["context"].extend(hmi_effects)
            context["evidence"].extend([f"HMI effect: {effect}" for effect in hmi_effects])
            
        # Check for telltale/pop-up effects
        telltale_effects = self._find_telltale_effects(main_fpi, related_fpi)
        if telltale_effects:
            score = max(score, 1)  # Low downstream dependency
            context["usage"].append("Verification")
            context["context"].extend(telltale_effects)
            context["evidence"].extend([f"Telltale: {effect}" for effect in telltale_effects])
            
        # Determine if critical (score 3)
        if self._is_critical_downstream_dependency(main_fpi, related_fpi, main_content, related_content):
            score = 3
            context["usage"].extend(["ExpectedResult", "FailureCheck"])
            context["reasoning"] = f"Critical downstream dependency: {main_fpi} testcase verification requires {related_fpi} context"
        elif score > 0:
            context["reasoning"] = f"Downstream dependency: {related_fpi} provides verification context for {main_fpi}"
            
        return score, context
        
    def _extract_signals(self, content: Dict) -> List[str]:
        """Extract signal names from feature content"""
        signals = []
        for signal_data in content.get("signals", []):
            if isinstance(signal_data, dict):
                for key, value in signal_data.items():
                    if "signal" in key.lower() or "can" in key.lower():
                        if isinstance(value, str) and value.strip():
                            signals.append(value.strip())
        
        # Also check in requirements and metadata for signal references
        for req_data in content.get("requirements", []):
            if isinstance(req_data, dict):
                for key, value in req_data.items():
                    if isinstance(value, str) and ("CAN" in value or "signal" in value.lower()):
                        # Extract signal names using simple pattern matching
                        import re
                        signal_matches = re.findall(r'\b[A-Z][a-zA-Z0-9_]*Sts?\b|\b[A-Z][a-zA-Z0-9_]*Request\b|\b[A-Z][a-zA-Z0-9_]*Signal\b', value)
                        signals.extend(signal_matches)
        
        return list(set(signals))  # Remove duplicates
        
    def _extract_output_signals(self, content: Dict) -> List[str]:
        """Extract output signals that this feature provides"""
        outputs = []
        signals = self._extract_signals(content)
        
        # Look for signals that indicate outputs (Request, Command, etc.)
        for signal in signals:
            if any(keyword in signal for keyword in ["Request", "Command", "Output", "Cmd"]):
                outputs.append(signal)
                
        return outputs
        
    def _extract_input_signals(self, content: Dict) -> List[str]:
        """Extract input signals that this feature consumes"""
        inputs = []
        signals = self._extract_signals(content)
        
        # Look for signals that indicate inputs (Status, Sts, etc.)
        for signal in signals:
            if any(keyword in signal for keyword in ["Sts", "Status", "Input", "State"]):
                inputs.append(signal)
                
        return inputs
        
    def _find_signal_dependencies(self, main_signals: List[str], related_signals: List[str]) -> List[str]:
        """Find signal dependencies between features"""
        dependencies = []
        
        for main_signal in main_signals:
            for related_signal in related_signals:
                # Check for direct signal matches or related signals
                if main_signal == related_signal:
                    dependencies.append(main_signal)
                elif self._are_related_signals(main_signal, related_signal):
                    dependencies.append(f"{main_signal} <- {related_signal}")
                    
        return dependencies
        
    def _find_output_dependencies(self, main_outputs: List[str], related_inputs: List[str]) -> List[str]:
        """Find output dependencies where main feature outputs to related feature"""
        dependencies = []
        
        for output in main_outputs:
            for input_signal in related_inputs:
                if self._are_related_signals(output, input_signal):
                    dependencies.append(f"{output} -> {input_signal}")
                    
        return dependencies
        
    def _are_related_signals(self, signal1: str, signal2: str) -> bool:
        """Check if two signals are related (e.g., Request/Status pairs)"""
        # Remove common suffixes/prefixes to find base signal name
        base1 = signal1.replace("Request", "").replace("Sts", "").replace("Status", "").replace("Cmd", "")
        base2 = signal2.replace("Request", "").replace("Sts", "").replace("Status", "").replace("Cmd", "")
        
        return base1.strip() == base2.strip() and base1.strip() != ""
        
    def _find_state_dependencies(self, main_fpi: str, related_fpi: str, main_content: Dict, related_content: Dict) -> List[str]:
        """Find state or mode dependencies between features"""
        dependencies = []
        
        # Check for common automotive state patterns
        automotive_states = ["Manettino", "Key", "Engine", "Vehicle", "Mode", "State"]
        
        main_text = str(main_content).lower()
        related_text = str(related_content).lower()
        
        for state in automotive_states:
            if state.lower() in main_text and state.lower() in related_text:
                dependencies.append(f"Shared {state} state dependency")
                
        # Check for specific automotive dependencies
        if "manettino" in main_fpi.lower() or "manettino" in related_fpi.lower():
            if any(keyword in main_text or keyword in related_text for keyword in ["audio", "display", "hmi"]):
                dependencies.append("Manettino mode affects feature behavior")
                
        return dependencies
        
    def _find_configuration_dependencies(self, main_content: Dict, related_content: Dict) -> List[str]:
        """Find configuration parameter dependencies"""
        dependencies = []
        
        main_configs = [str(item) for item in main_content.get("configurations", [])]
        related_configs = [str(item) for item in related_content.get("configurations", [])]
        
        # Look for shared configuration parameters
        for main_config in main_configs:
            for related_config in related_configs:
                if len(main_config) > 10 and main_config in related_config:
                    dependencies.append(f"Shared configuration: {main_config[:50]}...")
                    
        return dependencies
        
    def _find_hmi_effects(self, main_fpi: str, related_fpi: str, main_content: Dict, related_content: Dict) -> List[str]:
        """Find HMI display effects between features"""
        effects = []
        
        # Check for HMI-related keywords
        hmi_keywords = ["display", "hmi", "screen", "cluster", "telltale", "popup", "warning"]
        
        main_text = str(main_content).lower()
        related_text = str(related_content).lower()
        
        for keyword in hmi_keywords:
            if keyword in main_text and keyword in related_text:
                effects.append(f"Shared {keyword} interaction")
                
        # Specific automotive HMI patterns
        if "cluster" in main_fpi.lower() or "cluster" in related_fpi.lower():
            if any(keyword in main_text for keyword in ["warning", "telltale", "display"]):
                effects.append("Instrument cluster display effect")
                
        return effects
        
    def _find_telltale_effects(self, main_fpi: str, related_fpi: str) -> List[str]:
        """Find telltale or pop-up effects between features"""
        effects = []
        
        # Common automotive telltale patterns
        telltale_patterns = [
            ("fuel", "warning"),
            ("battery", "warning"), 
            ("engine", "warning"),
            ("lights", "external"),
            ("manettino", "mode")
        ]
        
        main_lower = main_fpi.lower()
        related_lower = related_fpi.lower()
        
        for pattern1, pattern2 in telltale_patterns:
            if (pattern1 in main_lower and pattern2 in related_lower) or \
               (pattern2 in main_lower and pattern1 in related_lower):
                effects.append(f"Telltale interaction: {pattern1}-{pattern2}")
                
        return effects
        
    def _is_critical_upstream_dependency(self, main_fpi: str, related_fpi: str, main_content: Dict, related_content: Dict) -> bool:
        """Determine if this is a critical upstream dependency"""
        
        # Critical patterns for automotive features
        critical_patterns = [
            # Key/ignition dependencies
            ("key", "ignition"),
            # Manettino mode dependencies  
            ("manettino", "mode"),
            # Safety system dependencies
            ("safety", "system"),
            # Engine state dependencies
            ("engine", "state")
        ]
        
        main_lower = main_fpi.lower()
        related_lower = related_fpi.lower()
        
        for pattern1, pattern2 in critical_patterns:
            if (pattern1 in main_lower and pattern2 in related_lower) or \
               (pattern2 in main_lower and pattern1 in related_lower):
                return True
                
        # Check for critical signal dependencies
        main_signals = self._extract_signals(main_content)
        related_signals = self._extract_signals(related_content)
        
        critical_signals = ["ManettinoSts", "KeySts", "EngineRunning", "VehicleSpeed"]
        
        for signal in critical_signals:
            if signal in main_signals and any(related_sig for related_sig in related_signals if signal in related_sig):
                return True
                
        return False
        
    def _is_critical_downstream_dependency(self, main_fpi: str, related_fpi: str, main_content: Dict, related_content: Dict) -> bool:
        """Determine if this is a critical downstream dependency"""
        
        # Critical output verification patterns
        if "warning" in main_fpi.lower() and "display" in related_fpi.lower():
            return True
            
        if "lights" in main_fpi.lower() and "external" in related_fpi.lower():
            return True
            
        # Check for critical output signals
        main_outputs = self._extract_output_signals(main_content)
        related_inputs = self._extract_input_signals(related_content)
        
        critical_outputs = ["ESCOFFLampRequest", "WarningRequest", "TelltaleRequest"]
        
        for output in critical_outputs:
            if output in main_outputs and any(inp for inp in related_inputs if output.replace("Request", "Sts") in inp):
                return True
                
        return False
        
    def process_target_features(self) -> Dict[str, Dict]:
        """
        Process all target features using antisymmetric matrix methodology
        """
        logger.info("🎯 Processing target features with antisymmetric matrix methodology...")
        
        # Discover all features first
        domain_features = self.discover_all_features()
        all_feature_ids = list(self.features.keys())
        
        logger.info(f"📊 Total features in matrix: {len(all_feature_ids)}")
        logger.info(f"🎯 Target features to analyze: {len(self.target_features)}")
        
        results = {}
        
        # Process each target feature
        for i, target_feature in enumerate(self.target_features):
            logger.info(f"🔄 Processing {i+1}/{len(self.target_features)}: {target_feature}")
            
            if target_feature not in self.features:
                logger.warning(f"⚠️ Target feature not found: {target_feature}")
                continue
                
            feature_relationships = []
            
            # Analyze relationships with ALL other features using antisymmetric methodology
            for other_feature in all_feature_ids:
                if target_feature == other_feature:
                    continue  # Skip self-reference
                    
                # Check if we already computed this relationship in the opposite direction
                reverse_key = (other_feature, target_feature)
                if reverse_key in self.matrix:
                    # Use antisymmetric property: M[i,j] = -M[j,i]
                    score = -self.matrix[reverse_key]
                    self.matrix[(target_feature, other_feature)] = score
                    logger.debug(f"  📐 Used antisymmetric property: {target_feature} -> {other_feature} = {score}")
                else:
                    # Compute new relationship
                    relationship = self.analyze_fpi_relationship(target_feature, other_feature)
                    self.matrix[(target_feature, other_feature)] = relationship.score
                    
                    if relationship.score != 0:
                        feature_relationships.append(relationship)
                        self.relationships.append(relationship)
                        logger.debug(f"  🔗 Found relationship: {other_feature} (score: {relationship.score:+d})")
                        
            results[target_feature] = {
                "total_relationships": len(feature_relationships),
                "critical_relationships": [r for r in feature_relationships if abs(r.score) == 3],
                "high_relationships": [r for r in feature_relationships if abs(r.score) == 2],
                "low_relationships": [r for r in feature_relationships if abs(r.score) == 1],
                "relationships": feature_relationships
            }
            
            logger.info(f"  ✅ {target_feature}: {len(feature_relationships)} relationships found")
            
        return results
        
    def generate_comprehensive_matrix(self) -> pd.DataFrame:
        """
        Generate the complete n×n antisymmetric matrix
        """
        logger.info("📊 Generating comprehensive antisymmetric matrix...")
        
        all_feature_ids = sorted(self.features.keys())
        n = len(all_feature_ids)
        
        # Initialize matrix with zeros
        matrix_data = [[0 for _ in range(n)] for _ in range(n)]
        
        # Fill matrix with computed relationships
        for i, feature1 in enumerate(all_feature_ids):
            for j, feature2 in enumerate(all_feature_ids):
                if i == j:
                    matrix_data[i][j] = 0  # Diagonal elements are zero
                else:
                    key = (feature1, feature2)
                    if key in self.matrix:
                        matrix_data[i][j] = self.matrix[key]
                    else:
                        matrix_data[i][j] = 0
                        
        # Create DataFrame
        df = pd.DataFrame(matrix_data, index=all_feature_ids, columns=all_feature_ids)
        
        logger.info(f"✅ Generated {n}×{n} matrix with {len(self.matrix)} non-zero relationships")
        
        return df
        
    def validate_antisymmetric_property(self, matrix_df: pd.DataFrame) -> Dict[str, bool]:
        """
        Validate that the matrix follows antisymmetric properties
        """
        logger.info("🔍 Validating antisymmetric matrix properties...")
        
        validation_results = {
            "antisymmetric_property": True,
            "zero_diagonal": True,
            "total_relationships": 0,
            "non_zero_relationships": 0
        }
        
        n = len(matrix_df)
        
        # Check antisymmetric property: M[i,j] = -M[j,i]
        for i in range(n):
            for j in range(n):
                if i != j:
                    if matrix_df.iloc[i, j] != -matrix_df.iloc[j, i]:
                        validation_results["antisymmetric_property"] = False
                        logger.warning(f"⚠️ Antisymmetric violation: [{i},{j}]={matrix_df.iloc[i, j]} != -[{j},{i}]={matrix_df.iloc[j, i]}")
                        
        # Check zero diagonal: M[i,i] = 0
        for i in range(n):
            if matrix_df.iloc[i, i] != 0:
                validation_results["zero_diagonal"] = False
                logger.warning(f"⚠️ Diagonal violation: [{i},{i}]={matrix_df.iloc[i, i]} != 0")
                
        # Count relationships
        validation_results["total_relationships"] = int(n * n)
        validation_results["non_zero_relationships"] = int((matrix_df != 0).sum().sum())
        
        logger.info(f"✅ Matrix validation complete:")
        logger.info(f"  📐 Antisymmetric property: {'✓' if validation_results['antisymmetric_property'] else '✗'}")
        logger.info(f"  🔘 Zero diagonal: {'✓' if validation_results['zero_diagonal'] else '✗'}")
        logger.info(f"  📊 Non-zero relationships: {validation_results['non_zero_relationships']}")
        
        return validation_results
        
    def export_results(self, results: Dict, matrix_df: pd.DataFrame, output_dir: str = "fpi_matrix_results") -> None:
        """
        Export comprehensive results to multiple formats
        """
        logger.info("📤 Exporting comprehensive results...")
        
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # 1. Export comprehensive matrix
        matrix_file = output_path / f"comprehensive_fpi_matrix_{timestamp}.csv"
        matrix_df.to_csv(matrix_file)
        logger.info(f"  📊 Matrix exported: {matrix_file}")
        
        # 2. Export dependency register
        dependency_register = []
        for relationship in self.relationships:
            dependency_register.append({
                "Main_FPI": relationship.main_fpi,
                "Related_FPI": relationship.related_fpi,
                "Score": relationship.score,
                "Direction": relationship.direction,
                "Necessity": relationship.necessity,
                "Context_Usage": "; ".join(relationship.context_usage),
                "Extracted_Context_From_Related_FPI": "; ".join(relationship.extracted_context),
                "Why_It_Is_Needed_For_Testcase_Generation": relationship.reasoning,
                "Confidence": relationship.confidence,
                "Evidence": "; ".join(relationship.evidence)
            })
            
        register_file = output_path / f"dependency_register_{timestamp}.csv"
        pd.DataFrame(dependency_register).to_csv(register_file, index=False)
        logger.info(f"  📋 Dependency register exported: {register_file}")
        
        # 3. Export feature analysis summaries
        for feature_id, feature_results in results.items():
            feature_file = output_path / f"feature_analysis_{feature_id}_{timestamp}.json"
            
            # Convert relationships to serializable format
            serializable_results = {
                "feature_id": feature_id,
                "total_relationships": feature_results["total_relationships"],
                "critical_count": len(feature_results["critical_relationships"]),
                "high_count": len(feature_results["high_relationships"]),
                "low_count": len(feature_results["low_relationships"]),
                "relationships": []
            }
            
            for rel in feature_results["relationships"]:
                serializable_results["relationships"].append({
                    "related_fpi": rel.related_fpi,
                    "score": rel.score,
                    "direction": rel.direction,
                    "necessity": rel.necessity,
                    "context_usage": rel.context_usage,
                    "extracted_context": rel.extracted_context,
                    "reasoning": rel.reasoning,
                    "confidence": rel.confidence,
                    "evidence": rel.evidence
                })
                
            with open(feature_file, 'w') as f:
                json.dump(serializable_results, f, indent=2)
                
        logger.info(f"  📁 Feature analyses exported to: {output_path}")
        
        # 4. Export consolidated summary
        summary = {
            "analysis_timestamp": timestamp,
            "total_features_in_matrix": len(self.features),
            "target_features_analyzed": len(results),
            "total_relationships_found": len(self.relationships),
            "critical_relationships": len([r for r in self.relationships if abs(r.score) == 3]),
            "high_relationships": len([r for r in self.relationships if abs(r.score) == 2]),
            "low_relationships": len([r for r in self.relationships if abs(r.score) == 1]),
            "matrix_dimensions": f"{len(self.features)}×{len(self.features)}",
            "antisymmetric_validation": self.validate_antisymmetric_property(matrix_df),
            "target_features": self.target_features,
            "feature_summaries": {}
        }
        
        for feature_id, feature_results in results.items():
            summary["feature_summaries"][feature_id] = {
                "total_relationships": feature_results["total_relationships"],
                "critical_relationships": len(feature_results["critical_relationships"]),
                "high_relationships": len(feature_results["high_relationships"]),
                "low_relationships": len(feature_results["low_relationships"])
            }
            
        summary_file = output_path / f"analysis_summary_{timestamp}.json"
        with open(summary_file, 'w') as f:
            json.dump(summary, f, indent=2)
            
        logger.info(f"  📋 Analysis summary exported: {summary_file}")
        
        # 5. Export context injection guidance
        context_guidance = {
            "critical_context_injection": {
                "upstream": [],
                "downstream": []
            },
            "high_priority_context_injection": {
                "upstream": [],
                "downstream": []
            },
            "optional_context_injection": {
                "upstream": [],
                "downstream": []
            }
        }
        
        for relationship in self.relationships:
            if abs(relationship.score) == 3:
                category = "critical_context_injection"
            elif abs(relationship.score) == 2:
                category = "high_priority_context_injection"
            elif abs(relationship.score) == 1:
                category = "optional_context_injection"
            else:
                continue
                
            direction = "upstream" if relationship.score < 0 else "downstream"
            
            context_guidance[category][direction].append({
                "main_fpi": relationship.main_fpi,
                "related_fpi": relationship.related_fpi,
                "context_usage": relationship.context_usage,
                "extracted_context": relationship.extracted_context,
                "reasoning": relationship.reasoning
            })
            
        guidance_file = output_path / f"context_injection_guidance_{timestamp}.json"
        with open(guidance_file, 'w') as f:
            json.dump(context_guidance, f, indent=2)
            
        logger.info(f"  🎯 Context injection guidance exported: {guidance_file}")
        logger.info(f"✅ All results exported to: {output_path}")

def main():
    """
    Main execution function for comprehensive FPI matrix generation
    """
    print("🚀 Starting Comprehensive FPI Testcase Context Dependency Matrix Generation")
    print("=" * 80)
    
    # Initialize generator
    generator = ComprehensiveFPIMatrixGenerator()
    
    try:
        # Step 1: Process target features
        print("\n📊 PHASE 1: Processing Target Features")
        results = generator.process_target_features()
        
        if not results:
            logger.error("❌ No results generated. Check if SRS Export path exists and contains valid features.")
            return
            
        # Step 2: Generate comprehensive matrix
        print("\n📈 PHASE 2: Generating Comprehensive Matrix")
        matrix_df = generator.generate_comprehensive_matrix()
        
        # Step 3: Validate antisymmetric properties
        print("\n🔍 PHASE 3: Validating Matrix Properties")
        validation_results = generator.validate_antisymmetric_property(matrix_df)
        
        # Step 4: Export results
        print("\n📤 PHASE 4: Exporting Results")
        generator.export_results(results, matrix_df)
        
        # Step 5: Print summary
        print("\n📋 ANALYSIS SUMMARY")
        print("=" * 50)
        print(f"Total features in matrix: {len(generator.features)}")
        print(f"Target features analyzed: {len(results)}")
        print(f"Total relationships found: {len(generator.relationships)}")
        print(f"Critical relationships (±3): {len([r for r in generator.relationships if abs(r.score) == 3])}")
        print(f"High relationships (±2): {len([r for r in generator.relationships if abs(r.score) == 2])}")
        print(f"Low relationships (±1): {len([r for r in generator.relationships if abs(r.score) == 1])}")
        print(f"Matrix dimensions: {len(generator.features)}×{len(generator.features)}")
        
        print(f"\n🔍 MATRIX VALIDATION")
        print(f"Antisymmetric property: {'✅ PASS' if validation_results['antisymmetric_property'] else '❌ FAIL'}")
        print(f"Zero diagonal: {'✅ PASS' if validation_results['zero_diagonal'] else '❌ FAIL'}")
        
        print(f"\n🎯 TARGET FEATURE RESULTS")
        for feature_id, feature_results in results.items():
            print(f"  {feature_id}:")
            print(f"    Total relationships: {feature_results['total_relationships']}")
            print(f"    Critical: {len(feature_results['critical_relationships'])}")
            print(f"    High: {len(feature_results['high_relationships'])}")
            print(f"    Low: {len(feature_results['low_relationships'])}")
            
        print("\n✅ Comprehensive FPI Matrix Generation Complete!")
        print("📁 Results exported to: fpi_matrix_results/")
        
    except Exception as e:
        logger.error(f"❌ Error during matrix generation: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
