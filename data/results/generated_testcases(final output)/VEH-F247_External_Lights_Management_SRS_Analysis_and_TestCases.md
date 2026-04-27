# VEH-F247_External_Lights_Management - SRS Analysis and Test Cases Document

## 1. Feature Overview and Approval Status

- **Feature ID and Name**: VEH-F247 6.2.1.1.2.19 External Lights Management
- **Brief Description**: This feature manages the external lighting system of the vehicle, including automatic high beam (AHB) functionality, telltale displays, warning notifications, and pop-up visualizations. The system handles various lighting modes (manual/automatic, day/night), provides user feedback through visual and audio alerts, and manages the display of lighting status information on the instrument cluster. The feature integrates with CAN bus signals to monitor lighting states and provides comprehensive feedback to both the driver and other vehicle systems through Ethernet communication.
- **Responsible Domain**: Cluster SW
- **Test Stage**: System Qualification Test
- **Approval Status**: APPROVED (Feature grooming status: Approved)
- **Requirements Approval**: 25/41 requirements approved (4 obsolete, 12 informational items)
- **Analysis Date**: 2024-12-19

## 2. Requirements Summary

The VEH-F247 External Lights Management feature contains 41 total items consisting of 25 functional requirements, 4 obsolete requirements, and 12 informational items. The feature manages external lighting control, automatic high beam functionality, warning displays, and user notifications through visual and audio feedback systems.

### 2.2.1 CRITICAL REQUIREMENT ANALYSIS

**Req. ID**: 3554960 - F247 Info4 Visualization Display Control
- **Testability**: Medium - Requires specific timing validation and state transition monitoring
- **Dependencies**: EXTERNAL_LIGHTS.LowBeamSts, EXTERNAL_LIGHTS.HighBeamSts, STATUS_B_CAN.KeySts, Proxi Byte_146 bit_4
- **Implementation**: Complex timing logic with 30-second timer and 7-cycle repetition, requires state machine implementation

**Req. ID**: 3554967 - F247 Info4 Visualization Stop Control
- **Testability**: High - Clear trigger condition and expected behavior
- **Dependencies**: EXTERNAL_LIGHTS.LowBeamSts, ongoing Info4 display state
- **Implementation**: Timer reset functionality and visualization interruption logic

**Req. ID**: 4705667 - Info-5 Pop-up Display with Buzzer
- **Testability**: High - Clear trigger and multiple output verification points
- **Dependencies**: EXTERNAL_LIGHTS.LowBeamSts, VEH_INDICATOR_STATUS, INDICATOR_STATUS
- **Implementation**: Multi-modal output (visual, audio, communication) with D04 visualization behavior

**Req. ID**: 4705669 - F247 Info-7 Display with Buzzer
- **Testability**: High - Single trigger condition with clear outputs
- **Dependencies**: VEHSTAT_V2.LBCmdNightInfoForDisplay, VEH_INDICATOR_STATUS, INDICATOR_STATUS
- **Implementation**: Active state monitoring with D04 visualization behavior and priority-2

**Req. ID**: 4705671 - V_Car_Moving Parameter Service
- **Testability**: Low - Missing clear action and object definition
- **Dependencies**: Diagnostic SRS requirement 3971355, V_Car_Moving parameter
- **Implementation**: Parameter adjustment service with 5km/hr default value, requires diagnostic interface

**Req. ID**: 4889708 - Pop-Up Lights Switch Display
- **Testability**: Medium - Compound requirement with multiple trigger conditions
- **Dependencies**: EXTERNAL_LIGHTS.LowBeamSts, EXTERNAL_LIGHTS.HighBeamSts, EXTERNAL_LIGHTS.ExternalLightsSts
- **Implementation**: Transition detection logic for ON/OFF state changes with relative indications

**Req. ID**: 4889714 - Rear Fog Lights Indication
- **Testability**: High - Clear trigger and expected behavior
- **Dependencies**: EXTERNAL_LIGHTS.RearFogLightSts, ignition cycle detection
- **Implementation**: State transition monitoring with relative indication display

**Req. ID**: 4889715 - Classic Virtual Telltale Management
- **Testability**: Medium - Negative statement requires careful test design
- **Dependencies**: EXTERNAL_LIGHTS.LowBeamSts, EXTERNAL_LIGHTS.HighBeamSts, t_PopUp_Lights timer
- **Implementation**: 1-second timeout logic with fallback to classic telltale visualization

**Req. ID**: 3532442 - AHB True External Light Indication
- **Testability**: Medium - Compound requirement with table-based verification
- **Dependencies**: Proxi byte 146 bit 4, EXTERNAL_LIGHTS signals, telltale codes, image119.png
- **Implementation**: Conditional display logic based on AHB proxy status with B14 wireframe area display

**Req. ID**: 5530191 - AHB True OFF External Light Indication
- **Testability**: High - Clear preconditions and table-based verification
- **Dependencies**: Proxi byte 146 bit 4, EXTERNAL_LIGHTS signals, telltale codes, image120.png
- **Implementation**: AHB OFF state handling with telltale display management

**Req. ID**: 3532455 - AHB False External Light Indication
- **Testability**: Medium - Compound requirement with table reference
- **Dependencies**: Proxi byte 146 bit 4, EXTERNAL_LIGHTS signals, telltale codes, image121.png
- **Implementation**: Non-AHB mode display logic with key-off state management

**Req. ID**: 4710638 - Telltale Display Stop on Key-Off
- **Testability**: Medium - Multiple unclear pronouns and compound conditions
- **Dependencies**: EXTERNAL_LIGHTS.HighBeamSts, EXTERNAL_LIGHTS.LowBeamSts, EXTERNAL_LIGHTS.AHBFeature, STATUS_B_CAN.KeySts
- **Implementation**: Key-off detection with telltale suppression logic

**Req. ID**: 3919993 - F247 Warning1 Performance
- **Testability**: Medium - Compound requirement with proxy condition
- **Dependencies**: Proxi byte 146 bit 4, HAPTIC1.AHBFault
- **Implementation**: Conditional warning display based on AHB proxy presence

**Req. ID**: 3532490 - AHB Failure Telltale Display
- **Testability**: Medium - Compound requirement with design reference
- **Dependencies**: HAPTIC1.AHBFault, telltale code 00230, D01 visualization, image122.png
- **Implementation**: Fault detection with Ferrari Design telltale display and D01 behavior

**Req. ID**: 3532568 - AHB Failure Buzzer
- **Testability**: High - Clear trigger and audio verification
- **Dependencies**: HAPTIC1.AHBFault, AHB feature enablement, 2B buzzer audio file
- **Implementation**: Audio feedback system with priority matrix integration

**Req. ID**: 3532569 - AHB Failure Warning Text
- **Testability**: Medium - Compound requirement with multiple outputs
- **Dependencies**: HAPTIC1.AHBFault, HMI_POP.IND ID 24701, VEH_INDICATOR_STATUS, INDICATOR_STATUS
- **Implementation**: Multi-channel warning display with D01 visualization behavior

**Req. ID**: 3919997 - F247 Warning2 Performance
- **Testability**: Medium - Compound requirement with proxy condition
- **Dependencies**: Proxi byte 146 bit 4, HAPTIC1.SensorBlinded
- **Implementation**: Sensor blinded warning with conditional proxy-based activation

**Req. ID**: 3532660 - Light Sensor Blinded Buzzer
- **Testability**: High - Clear trigger and audio verification
- **Dependencies**: HAPTIC1.SensorBlinded, 2B buzzer audio file
- **Implementation**: Audio alert system for sensor blinded condition

**Req. ID**: 3532661 - Light Sensor Blinded Warning Text
- **Testability**: Medium - Compound requirement with multiple communication channels
- **Dependencies**: HAPTIC1.SensorBlinded, HMI_POP.IND ID 24702, VEH_INDICATOR_STATUS, INDICATOR_STATUS
- **Implementation**: Warning text display with D01 behavior and priority0

**Req. ID**: 3532680 - F247 Info1 ManualDay Warning - **OBSOLETE**
- **Testability**: N/A - Requirement marked as obsolete
- **Dependencies**: N/A
- **Implementation**: N/A - No implementation required

**Req. ID**: 3532682 - F247 Info2 ManualNight Pop-up
- **Testability**: Medium - Compound requirement with visualization behavior
- **Dependencies**: EXTERNAL_LIGHTS.ExternalLightsSts, HMI_POP.IND ID 24704, D01 visualization
- **Implementation**: Manual night mode detection with pop-up display and priority2

**Req. ID**: 3532683 - Audio Buzzer for Manual Light Warning
- **Testability**: Medium - Compound requirement with speed threshold
- **Dependencies**: EXTERNAL_LIGHTS.ExternalLightsSts, NFR_SPEED.VehicleSpeedVSOSig, V_Car_Moving threshold
- **Implementation**: Speed-dependent audio alert with 2A buzzer and threshold monitoring

**Req. ID**: 3935767 - Icon Display in Wire-frame Area - **OBSOLETE**
- **Testability**: N/A - Requirement marked as obsolete
- **Dependencies**: N/A
- **Implementation**: N/A - No implementation required

**Req. ID**: 3935768 - Icon Display in Wire-frame Area - **OBSOLETE**
- **Testability**: N/A - Requirement marked as obsolete
- **Dependencies**: N/A
- **Implementation**: N/A - No implementation required

**Req. ID**: 3554944 - F247 Info-3 Pop-up Display
- **Testability**: Medium - Compound requirement with complex state logic
- **Dependencies**: Proxi byte 146 bit 4, EXTERNAL_LIGHTS.ExternalLightsSts, STATUS_B_CAN.KeySts, HMI_POP.IND ID 24705
- **Implementation**: State persistence across key cycles with 2-second delay and mode transition detection

**Req. ID**: 3715956 - PROXI ADAS Configuration Information - **INFORMATIONAL**
- **Testability**: Low - Missing actor, action, and imperative
- **Dependencies**: Proxi byte 146 bit 4
- **Implementation**: Configuration reference for AHB feature availability

**Req. ID**: 3715957 - CAN Signals Usage Information - **INFORMATIONAL**
- **Testability**: Low - Missing actor and object definition
- **Dependencies**: CAN signals, Ferrari Design specifications
- **Implementation**: Reference for CAN signal utilization in external lights management

**Req. ID**: 3935769 - CAN Signals Usage Information - **INFORMATIONAL/OBSOLETE**
- **Testability**: N/A - Obsolete informational item
- **Dependencies**: N/A
- **Implementation**: N/A - No implementation required

**Req. ID**: 4889703 - Pop-Up Lights Key Event Information - **INFORMATIONAL**
- **Testability**: Medium - Clear verification criteria provided
- **Dependencies**: STATUS_B_CAN.KeySts
- **Implementation**: Key-on/Key-off event detection for pop-up display

**Req. ID**: 3532441 - External Lights Management General - **INFORMATIONAL**
- **Testability**: N/A - Section header
- **Dependencies**: N/A
- **Implementation**: N/A - Organizational structure

**Req. ID**: 3532488 - F247 Warning 1 Section - **INFORMATIONAL**
- **Testability**: N/A - Section header
- **Dependencies**: N/A
- **Implementation**: N/A - Organizational structure

**Req. ID**: 3532658 - F247 Warning 2 Section - **INFORMATIONAL**
- **Testability**: N/A - Section header
- **Dependencies**: N/A
- **Implementation**: N/A - Organizational structure

**Req. ID**: 3532678 - F247 Info 1 Section - **INFORMATIONAL/OBSOLETE**
- **Testability**: N/A - Obsolete section header
- **Dependencies**: N/A
- **Implementation**: N/A - No implementation required

**Req. ID**: 3532681 - F247 Info 2 Section - **INFORMATIONAL**
- **Testability**: N/A - Section header
- **Dependencies**: N/A
- **Implementation**: N/A - Organizational structure

**Req. ID**: 3554943 - External Light Management Info-3 Section - **INFORMATIONAL**
- **Testability**: N/A - Section header
- **Dependencies**: N/A
- **Implementation**: N/A - Organizational structure

**Req. ID**: 3554937 - VEH-F247 External Light Management Info-4 Section - **INFORMATIONAL**
- **Testability**: N/A - Section header
- **Dependencies**: N/A
- **Implementation**: N/A - Organizational structure

**Req. ID**: 3967625 - Data Usage ETH Signal Information - **INFORMATIONAL**
- **Testability**: N/A - Data usage clarification
- **Dependencies**: Ethernet signals
- **Implementation**: N/A - Documentation reference

**Req. ID**: 3967901 - F247_Info1 Signal Information - **INFORMATIONAL/OBSOLETE**
- **Testability**: N/A - Obsolete signal reference
- **Dependencies**: N/A
- **Implementation**: N/A - No implementation required

**Req. ID**: 3967908 - F247_Info2 Signal Information - **INFORMATIONAL**
- **Testability**: N/A - Signal reference documentation
- **Dependencies**: Buzzer2A, VEH_Buzzer2A, Ethernet signals
- **Implementation**: N/A - Reference documentation

**Req. ID**: 3968186 - F247_Info3 Signal Information - **INFORMATIONAL**
- **Testability**: N/A - Signal reference documentation
- **Dependencies**: Ethernet signals
- **Implementation**: N/A - Reference documentation

### 2.2.2 Requirement Quality Assessment

**High-Risk Requirements (RQA Score < 70):**

- **Req. ID 4705671** (Score: 10): Missing actor, object, and imperative - requires complete requirement restructuring for testability
- **Req. ID 4889715** (Score: 60): Negative statement and compound requirement - needs positive verification criteria and atomic test steps
- **Req. ID 3532490** (Score: 60): Compound requirement and passive voice - requires breakdown into separate verification steps
- **Req. ID 3532442** (Score: 60): Compound requirement and passive voice - needs atomic test case decomposition

**Mitigation Strategies:**
- **Compound Requirements**: Break down into individual atomic test steps focusing on single verification points
- **Missing Units/Tolerances**: Define specific measurement criteria and acceptable ranges for timing and threshold values
- **Negative Statements**: Convert to positive verification criteria with clear pass/fail conditions
- **Unclear Terms**: Establish specific, measurable definitions for terms like "classic telltale visualization"

```markdown
## 3. Visual Elements Analysis

### 3.1 CLIP-Based Image Classification Integration

The VEH-F247 External Lights Management feature utilizes four distinct visual elements that have been systematically analyzed using consolidated visual analysis methodology:

**IMAGE 119 - AHB_CONFIGURATION_MATRIX**: Configuration table (1166x311px) displaying Automatic High Beam lighting control logic with conditional proxy settings. The image contains structured tabular data with black text (RGB: 0,0,0) on white background (RGB: 255,255,255) showing 9 rows x 7 columns of technical specifications.

**IMAGE 120 - LIGHTING_CONTROL_STATE_MATRIX**: Multi-condition logic table (1165x468px) presenting lighting control combinations for Day/Night scenarios with Auto/Manual modes. Maintains consistent visual formatting with rectangular table structure and multi-level headers.

**IMAGE 121 - HEADLIGHT_DISPLAY_CONFIGURATION**: Configuration table (1200x800px) showing headlight control matrix with Use Case definitions across Day/Night scenarios. Features 10 rows x 4 columns with nested header structure.

**IMAGE 122 - AUTO_SYSTEM_WARNING_TELLTALE**: Dashboard warning icon displaying bright yellow/amber color (RGB: 255,191,0) in circular format containing letter "A", three horizontal parallel lines, and exclamation mark "!" on black background for high contrast visibility.

### 3.2 Category-Specific Visual Analysis

**Configuration Tables (Images 119, 120, 121)**:
- **Color Scheme**: Consistent black text on white background ensuring optimal readability
- **Shape Structure**: Rectangular grid layouts with multi-level header organization
- **Text Elements**: Technical signal names (LGH005, LGH006, LGH007, LGH008, LGH009, LGH011, LGH0018, LGH022), boolean states (ON/OFF/n.a), and operational modes (Auto/Manual, Day/Night)
- **Layout Consistency**: Standardized table formatting with clear cell boundaries and hierarchical header structure

**Warning Telltale (Image 122)**:
- **Color Specification**: Bright yellow/amber (RGB: 255,191,0) meeting automotive visibility standards
- **Shape Design**: Circular icon with left-to-right arrangement: Circle with "A" → Motion lines → Warning "!"
- **Visual Context**: Clean, simplified automotive dashboard iconography for automatic system malfunction indication
- **Contrast Optimization**: Black background ensures maximum visibility in various lighting conditions

### 3.3 Human Validation Visual Context Integration

**Technical Specification Validation**:
- All extracted signal names (LGH005-LGH022) correspond to actual CAN signal identifiers used in automotive lighting systems
- Boolean logic combinations (ON/OFF states) align with standard automotive electrical system operations
- Proxy condition "byte 146, bit 4" follows established CAN bus data structure protocols
- Warning telltale design adheres to ISO automotive dashboard symbol standards

**Functional Context Verification**:
- Configuration matrices demonstrate comprehensive coverage of all possible lighting state combinations
- Day/Night and Auto/Manual mode divisions reflect real-world driving scenarios
- Use Case differentiation (Use Case 1, Use Case 4) indicates multiple operational contexts
- Warning icon elements (A + motion lines + !) clearly communicate automatic system status

### 3.4 Cross-Visual Element Relationships

**Signal Consistency Analysis**:
- LGH007, LGH008, LGH005, LGH006 appear consistently across Images 119 and 120, confirming signal standardization
- Same 8 input combinations (RearFogSts/HighBeamSts/LowBeamSts) used across all configuration tables
- Display mapping in Image 121 translates signal combinations into user-visible states
- Warning integration in Image 122 provides visual feedback for automatic system status

**State Logic Correlation**:
- Four-way logic matrix (Day/Night × Auto/Manual) creates comprehensive operational coverage
- Boolean state transitions maintain logical consistency across all visual elements
- Display output variations ("Manual LB", "Auto DRL", "Not possible") reflect actual system capabilities

## 4. Data Structure and Signal Analysis

### 4.1 CAN Signal Detailed Analysis

**Primary CAN Signals**:

| Signal Name | Source | Data Type | Function | Usage Context |
|-------------|--------|-----------|----------|---------------|
| EXTERNAL_LIGHTS.LowBeamSts | CAN Bus | Boolean | Low beam headlight status | State monitoring, telltale control |
| EXTERNAL_LIGHTS.HighBeamSts | CAN Bus | Boolean | High beam headlight status | AHB control, display management |
| EXTERNAL_LIGHTS.RearFogLightSts | CAN Bus | Boolean | Rear fog light status | Indication display, state tracking |
| EXTERNAL_LIGHTS.ExternalLightsSts | CAN Bus | Enumerated | Overall external lights status | Mode detection, pop-up triggers |
| EXTERNAL_LIGHTS.AHBFeature | CAN Bus | Boolean | AHB feature availability | Conditional functionality |
| STATUS_B_CAN.KeySts | CAN Bus | Enumerated | Ignition key status | Power management, display control |
| HAPTIC1.AHBFault | CAN Bus | Boolean | AHB system fault status | Warning generation, telltale control |
| HAPTIC1.SensorBlinded | CAN Bus | Boolean | Light sensor obstruction | Warning alerts, system degradation |
| NFR_SPEED.VehicleSpeedVSOSig | CAN Bus | Numeric | Vehicle speed signal | Threshold monitoring, conditional alerts |
| VEHSTAT_V2.LBCmdNightInfoForDisplay | CAN Bus | Boolean | Night mode command status | Display control, mode indication |

**Proxy Configuration Signal**:
- **Proxi Byte 146 Bit 4**: AHB feature presence indicator determining conditional functionality across multiple requirements

### 4.2 Systematic Logic Tables from Visual Analysis

**AHB Configuration Matrix (IMAGE 119)**:
```
Conditional Logic: IF Proxi(byte 146, bit 4) == 'Present'
Input States: RearFogSts × HighBeamSts × LowBeamSts (8 combinations)
Output Modes: Auto(Day) × Manual(Day) × Auto(Night) × Manual(Night)

Key Signal Combinations:
- All ON: (LGH007)+(LGH008)+(LGH005) for Manual modes
- Rear+Low: (LGH008)+(LGH005) for Manual scenarios  
- High+Low: (LGH007)+(LGH008) for Manual Day, (LGH009)+(LGH011) for Auto Night
- High Only: (LGH007)+(LGH022) for Auto Day, (LGH007)+(LGH006) for Manual Night
- Low Only: (LGH008) for Manual Day, (LGH022)+(LGH011) for Auto Night
- All OFF: (LGH0018)+(LGH022) for Auto Day, (LGH006) for Manual Night
```

**Lighting Control State Matrix (IMAGE 120)**:
```
Extended Configuration with Variations:
- Maintains same 8 input combinations as IMAGE 119
- Auto(Night) column shows variations: (LGH007)+(LGH011) vs (LGH009)+(LGH011)
- Simplified outputs for OFF states: (LGH022) vs (LGH0018)+(LGH022), (LGH011) vs (LGH022)+(LGH011)
```

**Headlight Display Matrix (IMAGE 121)**:
```
User-Visible Output Translation:
DAY Scenario Outputs:
- High+Low: "Manual LB + HB" / "Manual LB + Hb"
- High Only: "Not possible (only flash)"
- Low Only: "Manual LB"
- All OFF: "NO" / "Auto DRL"

NIGHT Scenario Outputs:
- High+Low: "Manual LB + HB" / "Auto LB + HB"  
- High Only: "Not possible (only flashing)" / "Only for flashing"
- Low Only: "Not possible" / "Auto LB"
- All OFF: "Manual DRL" / "NO"
```

### 4.3 Signal-to-Function Relationship Mapping

**Telltale Code Assignments**:
- **LGH005**: Rear fog light telltale
- **LGH006**: Low beam night mode telltale
- **LGH007**: High beam telltale
- **LGH008**: Low beam telltale
- **LGH009**: Auto night high beam telltale
- **LGH011**: Auto night low beam telltale
- **LGH0018**: Auto day running light telltale
- **LGH022**: Day running light telltale
- **00230**: AHB failure telltale (IMAGE 122 reference)

**Ethernet Communication Signals**:
- **VEH_INDICATOR_STATUS**: Vehicle-level indicator status broadcast
- **INDICATOR_STATUS**: Local indicator status communication
- **HMI_POP.IND**: Pop-up display message identifiers (24701, 24702, 24704, 24705)

**Audio Signal Integration**:
- **Buzzer2A**: Manual light warning audio (linked to V_Car_Moving threshold)
- **Buzzer2B**: AHB fault and sensor blinded warning audio
- **VEH_Buzzer2A**: Vehicle-level audio signal distribution

### 4.4 State Machine Logic Analysis

**AHB Feature State Dependencies**:
```
Primary Condition: Proxi(byte 146, bit 4) == 'Present'
├── TRUE: Full AHB functionality with IMAGE 119/120 logic
└── FALSE: Limited functionality with IMAGE 121 Use Case logic

Operational States:
├── Auto Day: DRL and flash-only high beam
├── Manual Day: Full manual control with telltales
├── Auto Night: Automatic low/high beam switching
└── Manual Night: Manual control with night-optimized telltales
```

**Warning State Transitions**:
```
AHB Fault Detection:
HAPTIC1.AHBFault == TRUE → Telltale(00230) + Buzzer2B + Warning Text(24701)

Sensor Blinded Detection:  
HAPTIC1.SensorBlinded == TRUE → Buzzer2B + Warning Text(24702)

Speed-Dependent Manual Warning:
EXTERNAL_LIGHTS.ExternalLightsSts + NFR_SPEED > V_Car_Moving → Buzzer2A + Pop-up(24704)
```

**Timer-Based Control Logic**:
- **Info4 Visualization**: 30-second timer with 7-cycle repetition
- **Pop-up Display Timeout**: 1-second classic telltale fallback
- **Info3 State Persistence**: 2-second delay with key cycle memory
- **Key-Off Suppression**: Immediate telltale termination on STATUS_B_CAN.KeySts transition

### 4.5 Cross-Table Signal Validation

**Signal Consistency Verification**:
- All LGH### identifiers maintain consistent usage across Images 119, 120, and 121
- Boolean state combinations (8 total) provide complete input space coverage
- Addition operators (+) indicate simultaneous telltale activation requirements
- "n.a" entries represent logically impossible or disabled state combinations

**Functional Integration Points**:
- CAN signal inputs drive configuration table lookups
- Table outputs determine telltale code activation
- Ethernet signals broadcast status to vehicle systems
- Audio signals provide multi-modal user feedback
- Proxy configuration enables/disables entire feature branches
```

```markdown
## 3. Visual Elements Analysis

### 3.1 CLIP-Based Image Classification Integration

The VEH-F247 External Lights Management feature incorporates four distinct visual elements that require individual analysis using CLIP-based image classification methodology. Each image serves a specific functional purpose within the automotive lighting control system and must be analyzed separately to preserve unique technical specifications and implementation details.

### 3.2 IMAGE 119 Analysis - AHB_CONFIGURATION_MATRIX

**Visual Classification**: Technical configuration table with conditional logic implementation
**Dimensions**: 1166x311 pixels with 9 rows x 7 columns structure
**Color Scheme**: Standard black text (RGB: 0,0,0) on white background (RGB: 255,255,255)

**Technical Content Extraction**:
- **Conditional Header**: "If proxi (byte 146, bit 4) Automatic High Beam absent/present == 'Present'"
- **Signal Identifiers**: RearFogSts, HighBeamSts, LowBeamSts as primary input parameters
- **Telltale Codes**: LGH005, LGH006, LGH007, LGH008, LGH009, LGH011, LGH0018, LGH022
- **Operational Modes**: Auto(Day), Manual(Day), Auto(Night), Manual(Night)
- **Logic Operators**: Addition symbols (+) indicating simultaneous telltale activation

**Shape and Layout Analysis**:
- Rectangular table structure with multi-level header organization
- Clear cell boundaries with hierarchical column arrangement
- Boolean state representation using ON/OFF/n.a values
- Systematic 8-combination input matrix covering all possible lighting states

**Human Validation Context**:
- Proxy byte 146 bit 4 condition aligns with automotive CAN bus protocols
- LGH signal naming follows standard automotive telltale identification
- Boolean logic combinations provide comprehensive state coverage
- "n.a" entries represent logically impossible or disabled configurations

### 3.3 IMAGE 120 Analysis - LIGHTING_CONTROL_STATE_MATRIX

**Visual Classification**: Extended multi-condition logic table with operational variations
**Dimensions**: 1165x468 pixels with enhanced vertical structure
**Color Scheme**: Consistent black text (RGB: 0,0,0) on white background (RGB: 255,255,255)

**Technical Content Extraction**:
- **Signal Structure**: Identical RearFogSts, HighBeamSts, LowBeamSts input matrix as IMAGE 119
- **Telltale Variations**: Modified Auto(Night) column showing (LGH007)+(LGH011) vs (LGH009)+(LGH011)
- **Simplified Outputs**: Streamlined OFF state handling with (LGH022) vs (LGH0018)+(LGH022)
- **Mode Categories**: Same DAY/NIGHT division with Auto/Manual subcategories

**Shape and Layout Analysis**:
- Expanded rectangular table maintaining IMAGE 119's structural consistency
- Enhanced row spacing accommodating additional technical specifications
- Preserved multi-level header hierarchy with nested column organization
- Consistent Boolean logic representation across all 8 input combinations

**Human Validation Context**:
- Signal consistency verification with IMAGE 119 confirms standardized implementation
- Telltale code variations indicate operational mode refinements
- Maintained logical state coverage ensures comprehensive system behavior
- Addition operators preserve simultaneous activation requirements

### 3.4 IMAGE 121 Analysis - HEADLIGHT_DISPLAY_CONFIGURATION

**Visual Classification**: User-facing display configuration matrix with Use Case differentiation
**Dimensions**: 1200x800 pixels with 10 rows x 4 columns structure
**Color Scheme**: Standard black text on white background maintaining visual consistency

**Technical Content Extraction**:
- **Column Headers**: "Signals", "Use Case 1 Display", "Use Case 1 Virtual Telltale", "Use Case 4 Display"
- **Scenario Division**: Explicit DAY and NIGHT sections with 4 signal combinations each
- **Display States**: "Manual LB", "Manual LB + HB", "Manual LB + Hb", "Auto DRL", "Auto LB", "Auto LB + HB", "Manual DRL", "NO"
- **Impossibility Indicators**: "Not possible (only flash)", "Not possible (only flashing)", "Only for flashing"
- **Virtual Telltale**: Consistently "NO" across all entries indicating disabled virtual telltale functionality

**Shape and Layout Analysis**:
- Rectangular table with expanded column width accommodating descriptive text
- Clear DAY/NIGHT section separation with horizontal dividers
- Simplified signal combination format focusing on HighBeamSts/LowBeamSts pairs
- User-readable display terminology replacing technical signal codes

**Human Validation Context**:
- Display terminology translates technical signals into user-visible states
- Use Case differentiation indicates multiple operational contexts
- "Not possible" entries reflect real-world lighting system limitations
- Manual/Auto prefixes align with operational mode classifications

### 3.5 IMAGE 122 Analysis - AUTO_SYSTEM_WARNING_TELLTALE

**Visual Classification**: Automotive dashboard warning icon with multi-element design
**Dimensions**: Standard automotive telltale icon proportions
**Color Scheme**: Bright yellow/amber (RGB: 255,191,0) on black background for maximum contrast

**Technical Content Extraction**:
- **Primary Element**: Circular area containing letter "A" for automatic system identification
- **Motion Indicator**: Three horizontal parallel lines representing system activity
- **Warning Symbol**: Exclamation mark "!" indicating alert or malfunction status
- **Layout Sequence**: Left-to-right arrangement: Circle with "A" → Motion lines → Warning "!"

**Shape and Layout Analysis**:
- Circular primary shape providing clear focal point
- Linear motion elements creating visual flow indication
- Punctuation-based warning symbol for universal recognition
- Clean, simplified iconography optimized for dashboard visibility

**Human Validation Context**:
- Yellow/amber color meets ISO automotive warning standards
- Letter "A" clearly identifies automatic system context
- Motion lines universally indicate active system operation
- Exclamation mark provides immediate alert recognition
- Black background ensures visibility in various lighting conditions

### 3.6 Cross-Visual Element Integration Analysis

**Signal Consistency Verification**:
- LGH007, LGH008, LGH005, LGH006 maintain consistent usage across IMAGE 119 and IMAGE 120
- IMAGE 121 translates these technical signals into user-comprehensible display states
- IMAGE 122 provides visual feedback mechanism for automatic system status

**Functional Relationship Mapping**:
- IMAGE 119 establishes baseline AHB configuration logic
- IMAGE 120 provides operational variations and refinements
- IMAGE 121 delivers user-facing display translations
- IMAGE 122 supplies warning indication for system malfunctions

## 4. Data Structure and Signal Analysis

### 4.1 IMAGE 119 Data Analysis - AHB_CONFIGURATION_MATRIX

**CAN Signal Structure**:
| Input Signal | Data Type | Function | State Values |
|--------------|-----------|----------|--------------|
| RearFogSts | Boolean | Rear fog light status | ON/OFF |
| HighBeamSts | Boolean | High beam headlight status | ON/OFF |
| LowBeamSts | Boolean | Low beam headlight status | ON/OFF |

**Telltale Code Mapping**:
- **LGH005**: Rear fog light telltale activation
- **LGH006**: Night mode low beam telltale
- **LGH007**: High beam telltale indicator
- **LGH008**: Standard low beam telltale
- **LGH009**: Automatic night high beam telltale
- **LGH011**: Automatic night low beam telltale
- **LGH0018**: Automatic day running light telltale
- **LGH022**: Day running light telltale

**Logic Matrix Implementation**:
```
Proxy Condition: byte 146, bit 4 == 'Present'
Input Combinations (8 total):
1. RearFog=ON, HighBeam=ON, LowBeam=ON → Manual: (LGH007)+(LGH008)+(LGH005)
2. RearFog=ON, HighBeam=ON, LowBeam=OFF → All modes: n.a
3. RearFog=ON, HighBeam=OFF, LowBeam=ON → Manual: (LGH008)+(LGH005)
4. RearFog=ON, HighBeam=OFF, LowBeam=OFF → All modes: n.a
5. RearFog=OFF, HighBeam=ON, LowBeam=ON → Manual(Day): (LGH007)+(LGH008), Auto(Night): (LGH009)+(LGH011)
6. RearFog=OFF, HighBeam=ON, LowBeam=OFF → Auto(Day): (LGH007)+(LGH022), Manual(Night): (LGH007)+(LGH006)
7. RearFog=OFF, HighBeam=OFF, LowBeam=ON → Manual(Day): (LGH008), Auto(Night): (LGH022)+(LGH011)
8. RearFog=OFF, HighBeam=OFF, LowBeam=OFF → Auto(Day): (LGH0018)+(LGH022), Manual(Night): (LGH006)
```

### 4.2 IMAGE 120 Data Analysis - LIGHTING_CONTROL_STATE_MATRIX

**Signal Consistency Verification**:
- Maintains identical input signal structure as IMAGE 119
- Preserves same 8-combination Boolean logic matrix
- Implements identical proxy condition dependency

**Operational Variations**:
| State Combination | IMAGE 119 Output | IMAGE 120 Output | Variation Type |
|-------------------|------------------|------------------|----------------|
| OFF+ON+ON Auto(Night) | (LGH009)+(LGH011) | (LGH007)+(LGH011) | Telltale code substitution |
| OFF+OFF+ON Auto(Night) | (LGH022)+(LGH011) | (LGH011) | Simplified output |
| OFF+OFF+OFF Auto(Day) | (LGH0018)+(LGH022) | (LGH022) | Reduced telltale activation |

**State Machine Logic**:
```
Enhanced Configuration Matrix:
- Maintains baseline logic from IMAGE 119
- Introduces operational refinements for specific state combinations
- Preserves critical safety states (Manual modes unchanged)
- Optimizes automatic mode telltale activation patterns
```

### 4.3 IMAGE 121 Data Analysis - HEADLIGHT_DISPLAY_CONFIGURATION

**Display Translation Matrix**:
| Signal Input | Use Case 1 Display | Use Case 4 Display | Operational Context |
|--------------|-------------------|-------------------|---------------------|
| **DAY Scenarios** |
| High=ON, Low=ON | Manual LB + HB | Manual LB + Hb | Full manual control |
| High=ON, Low=OFF | Not possible (only flash) | Not possible (only flash) | Flash-only operation |
| High=OFF, Low=ON | Manual LB | Manual LB | Standard low beam |
| High=OFF, Low=OFF | NO | Auto DRL | DRL activation difference |
| **NIGHT Scenarios** |
| High=ON, Low=ON | Manual LB + HB | Auto LB + HB | Manual vs Auto distinction |
| High=ON, Low=OFF | Not possible (only flashing) | Only for flashing | Flashing-only limitation |
| High=OFF, Low=ON | Not possible | Auto LB | Auto mode enablement |
| High=OFF, Low=OFF | Manual DRL | NO | DRL vs OFF state |

**Use Case Differentiation**:
- **Use Case 1**: Manual control emphasis with explicit user actions
- **Use Case 4**: Automatic system integration with intelligent switching
- **Virtual Telltale**: Consistently disabled ("NO") across all scenarios

**Signal-to-Display Mapping**:
```
Technical Signal → User Display Translation:
- HighBeamSts + LowBeamSts → "Manual LB + HB"/"Auto LB + HB"
- HighBeamSts only → "Not possible (only flash/flashing)"
- LowBeamSts only → "Manual LB"/"Auto LB"
- All OFF → "NO"/"Auto DRL"/"Manual DRL"
```

### 4.4 IMAGE 122 Data Analysis - AUTO_SYSTEM_WARNING_TELLTALE

**Visual Signal Specifications**:
| Element | Technical Specification | Function |
|---------|------------------------|----------|
| Color Code | RGB(255,191,0) | Automotive amber warning standard |
| Shape Primary | Circular with "A" | Automatic system identification |
| Motion Lines | Three horizontal parallels | System activity indication |
| Warning Symbol | Exclamation mark "!" | Alert/malfunction status |
| Background | Black (RGB: 0,0,0) | Maximum contrast optimization |

**Integration with CAN Signals**:
```
Telltale Activation Logic:
- Trigger Signal: HAPTIC1.AHBFault == TRUE
- Telltale Code: 00230 (referenced in requirements)
- Display Behavior: D01 visualization with Ferrari Design
- Audio Integration: Buzzer2B activation
- Communication: VEH_INDICATOR_STATUS + INDICATOR_STATUS broadcast
```

**Warning State Machine**:
```
AHB System Status → Visual Feedback:
- Normal Operation: Telltale OFF
- AHB Fault Detected: IMAGE 122 telltale ON + Audio alert
- Sensor Blinded: Alternative warning (different telltale)
- System Disabled: No telltale activation
```

### 4.5 Cross-Image Data Integration Analysis

**Signal Flow Architecture**:
```
CAN Bus Inputs → IMAGE 119/120 Logic Tables → IMAGE 121 Display Translation → IMAGE 122 Warning Feedback
```

**Comprehensive Signal Mapping**:
- **Input Layer**: RearFogSts, HighBeamSts, LowBeamSts (IMAGE 119/120)
- **Processing Layer**: LGH### telltale code generation (IMAGE 119/120)
- **Output Layer**: User display states (IMAGE 121)
- **Feedback Layer**: Warning telltale activation (IMAGE 122)

**State Consistency Validation**:
- All 8 Boolean input combinations maintain logical consistency across IMAGE 119 and IMAGE 120
- IMAGE 121 display states align with technical signal combinations from IMAGE 119/120
- IMAGE 122 warning integration provides fault feedback for automatic system failures
- Proxy condition (byte 146, bit 4) enables/disables entire feature branch consistently

**Data Structure Dependencies**:
```
Primary Dependencies:
- IMAGE 119 ↔ IMAGE 120: Signal consistency with operational variations
- IMAGE 119/120 → IMAGE 121: Technical-to-user translation mapping
- System Fault → IMAGE 122: Warning feedback activation
- Proxy Configuration → All Images: Feature enablement control
```
```