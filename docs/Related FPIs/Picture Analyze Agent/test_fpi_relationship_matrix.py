#!/usr/bin/env python3
"""
FPI Relationship Matrix Calculator
Calculates relationship matrix for FPIs from Instrument Cluster domain
"""

import os
import sys
import json
from typing import Dict, List, Tuple, Set
from collections import defaultdict

# Add the Picture Analyze Agent directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from srs_discovery.parser import SRSParser
from srs_discovery.semantic_engine import SemanticSearchEngine
from srs_discovery.graph_engine import RelationshipGraphEngine

class FPIRelationshipMatrix:
    """Calculate relationship matrix between FPIs"""
    
    def __init__(self):
        # Initialize with dummy path since we're not actually parsing SRS files
        self.parser = SRSParser("dummy_path")
        self.semantic_engine = SemanticSearchEngine()
        self.graph_engine = RelationshipGraphEngine()
        
        # Relationship levels - Updated to correct [-3, +3] range
        self.NO_RELATIONSHIP = 0     # No relationship or same FPI
        self.WEAK_POSITIVE = 1       # Weak positive relationship
        self.MODERATE_POSITIVE = 2   # Moderate positive relationship  
        self.STRONG_POSITIVE = 3     # Strong positive relationship
        self.WEAK_NEGATIVE = -1      # Weak negative relationship (minor conflicts)
        self.MODERATE_NEGATIVE = -2  # Moderate negative relationship (conflicts)
        self.STRONG_NEGATIVE = -3    # Strong negative relationship (mutually exclusive)
        
    def extract_fpi_names(self, folder_list: List[str]) -> List[str]:
        """Extract FPI names from folder names"""
        fpi_names = []
        for folder in folder_list:
            if folder.endswith('/') and not folder.startswith('.'):
                # Remove trailing slash and extract FPI name
                fpi_name = folder.rstrip('/')
                fpi_names.append(fpi_name)
        return sorted(fpi_names)
    
    def calculate_relationship_level(self, fpi1: str, fpi2: str, fpi1_data: Dict, fpi2_data: Dict) -> int:
        """
        Calculate relationship level between two FPIs
        Returns: relationship score in range [-3, +3]
        """
        if fpi1 == fpi2:
            return self.NO_RELATIONSHIP
        
        # Check for negative relationships (conflicts/mutually exclusive features)
        if self._has_strong_conflict(fpi1, fpi2):
            return self.STRONG_NEGATIVE
        elif self._has_moderate_conflict(fpi1, fpi2):
            return self.MODERATE_NEGATIVE
        elif self._has_weak_conflict(fpi1, fpi2):
            return self.WEAK_NEGATIVE
        
        # Check for positive relationships (complementary/dependent features)
        elif self._has_strong_dependency(fpi1, fpi2):
            return self.STRONG_POSITIVE
        elif self._has_moderate_dependency(fpi1, fpi2):
            return self.MODERATE_POSITIVE
        elif self._has_weak_dependency(fpi1, fpi2):
            return self.WEAK_POSITIVE
        
        return self.NO_RELATIONSHIP
    
    def _has_strong_conflict(self, fpi1: str, fpi2: str) -> bool:
        """Check if FPIs have strong negative relationship (mutually exclusive)"""
        # Define mutually exclusive feature pairs
        strong_conflicts = {
            # Security vs Remote features
            ('VEH-F001_Immobilizer', 'VEH-F003_Remote_Engine_Start'),
            # Manual vs Automatic systems
            ('VEH-F252_Electric_Parking_Brake', 'VEH-F248_Auto_EPB_Command'),
            # Different lighting modes
            ('VEH-F042_Low_Beam_Lights', 'VEH-F047_High_Beam_Lights'),
        }
        return (fpi1, fpi2) in strong_conflicts or (fpi2, fpi1) in strong_conflicts
    
    def _has_moderate_conflict(self, fpi1: str, fpi2: str) -> bool:
        """Check if FPIs have moderate negative relationship"""
        # Features that may interfere with each other
        moderate_conflicts = {
            # Comfort vs Critical systems
            ('VEH-F005_Welcome_Lighting', 'VEH-F022_EOBD_Telltale_And_Engine_ECU_Failure'),
            # Power management conflicts
            ('VEH-F663_Wireless_Charger_Module_(WCM)_Management', 'VEH-F006_Low_Voltage_Battery_Indication'),
        }
        return (fpi1, fpi2) in moderate_conflicts or (fpi2, fpi1) in moderate_conflicts
    
    def _has_weak_conflict(self, fpi1: str, fpi2: str) -> bool:
        """Check if FPIs have weak negative relationship"""
        # Minor conflicts or resource competition
        if 'Telltale' in fpi1 and 'Light' in fpi2:
            return True
        if 'Welcome' in fpi1 and ('Warning' in fpi2 or 'Alarm' in fpi2):
            return True
        return False
    
    def _has_strong_dependency(self, fpi1: str, fpi2: str) -> bool:
        """Check if FPIs have strong positive relationship (direct dependencies)"""
        # Define strong positive relationships
        strong_dependencies = {
            # Core engine/security relationships
            ('VEH-F001_Immobilizer', 'VEH-F002_Engine_Start_Stop_Button'),
            ('VEH-F002_Engine_Start_Stop_Button', 'VEH-F004_Keyless_Go'),
            ('VEH-F004_Keyless_Go', 'VEH-F001_Immobilizer'),
            # Speed-related dependencies
            ('VEH-F020_Speedometer', 'VEH-F023_Total_Odometer'),
            ('VEH-F020_Speedometer', 'VEH-F163_Trip_Computer'),
            # Safety system dependencies
            ('VEH-F134_ESC_Lamp_Management', 'VEH-F135_Tyre_Pressure_and_Temperature_Monitoring_System'),
        }
        return (fpi1, fpi2) in strong_dependencies or (fpi2, fpi1) in strong_dependencies
    
    def _has_moderate_dependency(self, fpi1: str, fpi2: str) -> bool:
        """Check if FPIs have moderate positive relationship"""
        # Same domain features that work together
        lighting_fpis = {'VEH-F027', 'VEH-F030', 'VEH-F033', 'VEH-F042', 'VEH-F047', 'VEH-F051', 'VEH-F057', 'VEH-F247'}
        safety_fpis = {'VEH-F134', 'VEH-F135', 'VEH-F136', 'VEH-F139', 'VEH-F140', 'VEH-F145'}
        powertrain_fpis = {'VEH-F803', 'VEH-F804', 'VEH-F810', 'VEH-F869'}
        
        fpi1_code = fpi1.split('_')[0]
        fpi2_code = fpi2.split('_')[0]
        
        for domain_fpis in [lighting_fpis, safety_fpis, powertrain_fpis]:
            if fpi1_code in domain_fpis and fpi2_code in domain_fpis:
                return True
        
        # Telltale management with vehicle systems
        if 'BC001' in fpi1 and 'VEH-F' in fpi2:
            return True
        if 'BC001' in fpi2 and 'VEH-F' in fpi1:
            return True
            
        return False
    
    def _has_weak_dependency(self, fpi1: str, fpi2: str) -> bool:
        """Check if FPIs have weak positive relationship"""
        # General automotive system relationships
        if 'VEH-F' in fpi1 and 'VEH-F' in fpi2:
            try:
                # Extract numeric part safely
                fpi1_part = fpi1.split('VEH-F')[1].split('_')[0]
                fpi2_part = fpi2.split('VEH-F')[1].split('_')[0]
                
                # Remove any non-numeric characters
                fpi1_clean = ''.join(c for c in fpi1_part if c.isdigit())
                fpi2_clean = ''.join(c for c in fpi2_part if c.isdigit())
                
                if fpi1_clean and fpi2_clean:
                    fpi1_num = int(fpi1_clean)
                    fpi2_num = int(fpi2_clean)
                    # Create weak relationships for nearby feature numbers
                    if abs(fpi1_num - fpi2_num) <= 5 and abs(fpi1_num - fpi2_num) > 0:
                        return True
            except (ValueError, IndexError):
                # If parsing fails, skip this relationship
                pass
        return False
    
    def build_relationship_matrix(self, fpi_names: List[str]) -> Dict:
        """Build relationship matrix for given FPIs with proper symmetry"""
        matrix = {}
        
        # Initialize matrix with zeros
        for fpi1 in fpi_names:
            matrix[fpi1] = {}
            for fpi2 in fpi_names:
                matrix[fpi1][fpi2] = 0
        
        # Calculate relationships - process each pair once to ensure perfect symmetry
        for i, fpi1 in enumerate(fpi_names):
            for j, fpi2 in enumerate(fpi_names):
                if i < j:  # Only process upper triangle to avoid duplicates
                    # Mock FPI data - in reality would load from SRS files
                    fpi1_data = {'name': fpi1}
                    fpi2_data = {'name': fpi2}
                    
                    relationship_score = self.calculate_relationship_level(fpi1, fpi2, fpi1_data, fpi2_data)
                    
                    # Set symmetric values
                    matrix[fpi1][fpi2] = relationship_score
                    matrix[fpi2][fpi1] = relationship_score
        
        return matrix
    
    def validate_matrix_symmetry(self, matrix: Dict, fpi_names: List[str]) -> bool:
        """Validate that the matrix has proper symmetry and score range"""
        print("\nValidating matrix symmetry and score range...")
        
        symmetry_violations = 0
        range_violations = 0
        diagonal_violations = 0
        
        for i, fpi1 in enumerate(fpi_names):
            for j, fpi2 in enumerate(fpi_names):
                val1 = matrix[fpi1][fpi2]
                val2 = matrix[fpi2][fpi1]
                
                # Check score range [-3, +3]
                if val1 < -3 or val1 > 3:
                    range_violations += 1
                    if range_violations <= 3:
                        print(f"  Range violation: {fpi1} -> {fpi2} = {val1} (must be in [-3, +3])")
                
                # Check diagonal is zero
                if i == j and val1 != 0:
                    diagonal_violations += 1
                    if diagonal_violations <= 3:
                        print(f"  Diagonal violation: {fpi1} -> {fpi2} = {val1} (should be 0)")
                
                # Check perfect symmetry
                if i != j and val1 != val2:
                    symmetry_violations += 1
                    if symmetry_violations <= 3:
                        print(f"  Symmetry violation: {fpi1} -> {fpi2} = {val1}, but {fpi2} -> {fpi1} = {val2}")
        
        total_violations = symmetry_violations + range_violations + diagonal_violations
        
        if total_violations == 0:
            print("✓ Matrix validation PASSED")
            return True
        else:
            print(f"✗ Matrix validation FAILED:")
            print(f"  - {symmetry_violations} symmetry violations")
            print(f"  - {range_violations} score range violations")
            print(f"  - {diagonal_violations} diagonal violations")
            return False
    
    def print_matrix(self, matrix: Dict, fpi_names: List[str]):
        """Print relationship matrix in formatted table"""
        print("\n" + "="*120)
        print("FPI RELATIONSHIP MATRIX - INSTRUMENT CLUSTER DOMAIN")
        print("="*120)
        print("\nRelationship Levels:")
        print("  +3: Strong positive relationship (direct dependencies)")
        print("  +2: Moderate positive relationship (same domain, complementary)")
        print("  +1: Weak positive relationship (related functionality)")
        print("   0: No relationship or same FPI")
        print("  -1: Weak negative relationship (minor conflicts)")
        print("  -2: Moderate negative relationship (interference)")
        print("  -3: Strong negative relationship (mutually exclusive)")
        print("="*120)
        
        # Limit to first 10 FPIs for readability
        display_fpis = fpi_names[:10]
        
        # Print header
        print(f"\n{'FPI Name':<40}", end="")
        for fpi in display_fpis:
            short_name = fpi.split('_')[0][-4:] if len(fpi.split('_')[0]) > 4 else fpi.split('_')[0]
            print(f"{short_name:>8}", end="")
        print()
        
        # Print separator
        print("-" * (40 + 8 * len(display_fpis)))
        
        # Print matrix rows
        for fpi1 in display_fpis:
            # Truncate FPI name for display
            display_name = fpi1[:37] + "..." if len(fpi1) > 40 else fpi1
            print(f"{display_name:<40}", end="")
            
            for fpi2 in display_fpis:
                value = matrix[fpi1][fpi2]
                if value > 0:
                    print(f"{value:>8}", end="")
                elif value < 0:
                    print(f"{value:>8}", end="")
                else:
                    print(f"{value:>8}", end="")
            print()
        
        print("\n" + "="*120)
        print(f"Matrix shows relationships for first {len(display_fpis)} FPIs out of {len(fpi_names)} total FPIs")
        print("="*120)

def main():
    """Main function to run FPI relationship matrix calculation"""
    print("FPI Relationship Matrix Calculator")
    print("=" * 50)
    
    # FPI folders from Instrument Cluster domain
    cluster_fpi_folders = [
        "BC001-_Virtual_Telltale_Bulck_Check_Managment/",
        "VEH-CER00_1 Opening_Ceremony_and_Closing_Ceremony/",
        "VEH-CER001 Opening_Ceremony_and_Closing_Ceremony/",
        "VEH-F001_Immobilizer/",
        "VEH-F005_Fire_Intervention_System_(FIS)/",
        "VEH-F006_Low_Voltage_Battery_Indication/",
        "VEH-F008_6.2.1.1.1.16/",
        "VEH-F020_Speedometer/",
        "VEH-F022_EOBD_Telltale_And_Engine_ECU_Failure/",
        "VEH-F023_Total_Odometer/",
        "VEH-F024_Range_Estimation/",
        "VEH-F025_Cruise_Control_Lamp_Management/",
        "VEH-F027_Position_Lights_DRL_and_Parking_Lights_Management/",
        "VEH-F030_Plate_Light/",
        "VEH-F033_Rear_Fog_Light/",
        "VEH-F040_Key_Status/",
        "VEH-F042_Low_Beam_Lights/",
        "VEH-F047_High_Beam_Lights/",
        "VEH-F051_Turn_Indicators_and_Hazard_Lights/",
        "VEH-F057_Rear_LR_Stop_Lights_and_Third_Stop_Management/",
        "VEH-F082_6.2.1.1.1.17/",
        "VEH-F087_Alarm_System/",
        "VEH-F091_Doors_Opening/",
        "VEH-F104_Window_Control_Switches_Mangement/",
        "VEH-F126_Automatic_Defrosting/",
        "VEH-F134_ESC_Lamp_Management/",
        "VEH-F135_Tyre_Pressure_and_Temperature_Monitoring_System/",
        "VEH-F136_Brake_Wear_Status/",
        "VEH-F139_AIR_BAG_Warning_Lamp_Management/",
        "VEH-F140_Unfastened_Seat_Belts_Signalling/",
        "VEH-F141_Signalling_of_Speed_Limit_Exceeded/",
        "VEH-F145_Brake_fluid_level_low_indication/",
        "VEH-F147_Intelligent_rear_windscreen_wiper_and_rear windscreen_washer/",
        "VEH-F148_Brakes_Temperature_Extimation/",
        "VEH-F150_Speeds_Intermittence_Antipanic_Windscreen_Wiper_and_Intelligent_Washer/",
        "VEH-F162_Time_and_Date/",
        "VEH-F163_Trip_Computer/",
        "VEH-F164_Energy Manettino/",
        "VEH-F165_Manettino/",
        "VEH-F175_Visualization_of_Vehicle_Performance/",
        "VEH-F179_Obstacles_Proximity_Signalling/",
        "VEH-F192_External_Temperature_Management/",
        "VEH-F200_Gear_and_Status_Indication_by_AutomaticRobotized_Gearbox/",
        "VEH-F228_Vehicle_Access_Management/",
        "VEH-F231_Key_Indentification_Managment/",
        "VEH-F241_Electric_Power_Steering/",
        "VEH-F247_External_Lights_Management/",
        "VEH-F248_Auto_EPB_Command/",
        "VEH-F249_Lift_Movement_Management/",
        "VEH-F252_Electric_Parking_Brake/",
        "VEH-F253_Auto_Vehicle_Hold/",
        "VEH-F269_Scheduled_Service_Warning/",
        "VEH-F275_Electric_Parking_Brake_Warning_Release/",
        "VEH-F301_Trunk_Management/",
        "VEH-F395_6.2.1.1.1.26/",
        "VEH-F516_Keyless_Ignition_Management/",
        "VEH-F531_Advanced_Driver_Attention_Management/",
        "VEH-F532_Driver_Drowsiness_and_Attention_Monitoring/",
        "VEH-F533_Lane_Keeping_Warning/",
        "VEH-F534_Adaptive_Cruise_Control_Management/",
        "VEH-F535_Full_Speed_Forward_Collision_Warning_with_Mitigation_Management/",
        "VEH-F559_Blind_Spot_Monitoring/",
        "VEH-F562_Traffic_Sign_Recognition/",
        "VEH-F601_Logistic_Mode_Power_Supply/",
        "VEH-F663_Wireless_Charger_Module_(WCM)_Management/",
        "VEH-F800_Power_Lift_Gate/",
        "VEH-F803_Hybrid_System_Indications/",
        "VEH-F804_High_Voltage_Battery/",
        "VEH-F805_High_Voltage_HVAC_&_H2O_Circuit/",
        "VEH-F808_6.2.1.1.1.30/",
        "VEH-F810_E-Drive_Management/",
        "VEH-F812_Recharge_Flap_Management/",
        "VEH-F813_HVB_Recharge_Management/",
        "VEH-F821_Rear_Wheel_Steering/",
        "VEH-F834_6.2.1.1.1.32/",
        "VEH-F844_Matrix_State_Events/",
        "VEH-F845_6.2.1.1.1.34/",
        "VEH-F846_Steering_Angle_Sensor/",
        "VEH-F847_Yaw_Rate/",
        "VEH-F849_Engine_Sound_Generator/",
        "VEH-F851_Fade_Warning/",
        "VEH-F853_Acoustic_Vehicle_Alerting_System/",
        "VEH-F855_CARB-EOBD/",
        "VEH-F858_Light_Sensor_Management/",
        "VEH-F868_Heated_Steering_Wheel/",
        "VEH-F869_Mild_Hybrid_Management/",
        "VEH-F870_Active_Suspension_Control_Management/",
        "VEH-F895_SGW_Management/",
        "VEH-F913_-TelltalesSafetyCheck/",
        "VEH-F913-_TelltalesSafetyCheck/",
        "VEH-PN001_Physical_needleAnalog_needle_management_on_Binnacle_(NQS)/",
        "VEH-PRJ00_1_Phone_Projection_on_NQS/",
        "VEH-PRJ001_Phone_Projection_on_NQS/"
    ]
    
    # Initialize matrix calculator
    matrix_calc = FPIRelationshipMatrix()
    
    # Extract FPI names
    fpi_names = matrix_calc.extract_fpi_names(cluster_fpi_folders)
    print(f"\nFound {len(fpi_names)} FPIs in Instrument Cluster domain")
    
    # Build relationship matrix
    print("\nCalculating relationship matrix...")
    matrix = matrix_calc.build_relationship_matrix(fpi_names)
    
    # Validate matrix symmetry
    matrix_calc.validate_matrix_symmetry(matrix, fpi_names)
    
    # Print matrix
    matrix_calc.print_matrix(matrix, fpi_names)
    
    # Save matrix to JSON file
    output_file = "Picture Analyze Agent/fpi_relationship_matrix.json"
    with open(output_file, 'w') as f:
        json.dump(matrix, f, indent=2)
    print(f"\nMatrix saved to: {output_file}")

if __name__ == "__main__":
    main()
