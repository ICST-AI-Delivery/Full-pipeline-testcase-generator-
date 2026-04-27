# VEH-F165_Manettino - SRS Analysis and Test Cases Document

## 1. Feature Overview and Approval Status

### 1.1 Feature Identification
- **Feature ID**: VEH-F165 6.2.1.1.2.43
- **Feature Name**: Manettino
- **Internal ID**: 3408580
- **Artifact Type**: SRS Feature
- **Responsible Domain**: Cluster SW
- **Test Stage**: System Qualification Test

### 1.2 Feature Description
The VEH-F165 Manettino feature implements a comprehensive Ferrari vehicle driving mode control system with integrated suspension management. The system provides 5 distinct driving modes (ICE, WET, COMFORT, SPORT, ESC OFF) through a rotary Manettino control, coupled with active suspension functionality offering 3 stiffness levels (Soft, Medium, Hard). The feature includes robust failure handling, persistence across key cycles, extensive feedback mechanisms (20 feedback pop-ups), and multi-system integration with IVI and Ethernet networks.

### 1.3 Expert Domains
- Android HMI
- Audio Processing
- IOC_IOC
- System Infra
- ADVNet
- System Core
- System Qualification

### 1.4 Approval Status Analysis
- **Feature Grooming Status**: Approved
- **Feature State**: Approved
- **Grooming Comments**: Missing HMI design, missing info
- **Analysis Date**: Current Analysis Phase 1

### 1.5 Requirements Approval Summary
- **Total Primary Requirements**: 51
- **Approved Requirements**: 42 (82.4%)
- **Review Status**: 3 (5.9%)
- **Blocked Status**: 0 (0%)
- **Obsolete Requirements**: 6 (11.7%)
- **Overall Approval Rate**: 82.4%

### 1.6 Quality Assessment
- **High Quality Requirements (RQA 80-100)**: 8 requirements
- **Medium Quality Requirements (RQA 60-79)**: 32 requirements
- **Low Quality Requirements (RQA 0-59)**: 11 requirements
- **Average RQA Score**: 65.1

### 1.7 Critical Issues Identified
- Missing timing specifications (T_susp values)
- Incomplete R19 recovery mechanism details
- Missing HMI design specifications
- Compound requirements requiring decomposition
- Ferrari-specific information gaps for Feedback 8-12

## 2. Requirements Summary

### 2.1 Requirements Analysis Overview
This section provides individual analysis for each of the 51 primary requirements identified in the VEH-F165 Manettino feature. Each requirement is assessed for testability, dependencies, and implementation considerations.

### 2.2 Individual Requirements Analysis

#### Requirement ID: 3541925
- **Content**: If Proxi Active Suspension Functionality is Active, system shall display vehicle Manettino status, suspension status and Indexes screen.
- **Artifact Type**: SRS Req
- **Responsible Domain**: Cluster SW
- **Test Stage**: System Qualification Test
- **Grooming Status**: Approved
- **State**: Approved
- **RQA Score**: 70
- **Testability Assessment**: HIGH - Clear preconditions and verification criteria defined
- **Dependencies**: ProxiActive Suspension Functionality signal, CAN bus communication
- **Implementation Considerations**: Requires integration with suspension system and HMI display management
- **Issues**: Compound requirement, missing HMI specification

#### Requirement ID: 3500929
- **Content**: System shall give suspension status indications as follows: (see: image198.png) Note: Display shall follow D04 behaviour
- **Artifact Type**: SRS Req
- **Responsible Domain**: Cluster SW
- **Test Stage**: System Qualification Test
- **Grooming Status**: Approved
- **State**: Approved
- **RQA Score**: 70
- **Testability Assessment**: MEDIUM - Visual reference provided but D04 behavior undefined
- **Dependencies**: SUSPENSION_INFO.SuspensionSetupSts CAN signal, image198.png specification
- **Implementation Considerations**: Requires mapping of hex values (0x1, 0x2, 0x3) to telltale displays (/S, /M, /H)
- **Issues**: Compound requirement, reference to undefined D04 behavior

#### Requirement ID: 3558175
- **Content**: System shall display Vehicle Manettino Status indications as saved during the Key-Off.
- **Artifact Type**: SRS Req
- **Responsible Domain**: Cluster SW
- **Test Stage**: System Qualification Test
- **Grooming Status**: Approved
- **State**: Approved
- **RQA Score**: 70
- **Testability Assessment**: HIGH - Clear persistence requirement with verification criteria
- **Dependencies**: Non-volatile memory storage, key-off event detection
- **Implementation Considerations**: Requires persistent storage mechanism and key state monitoring
- **Issues**: Compound requirement

#### Requirement ID: 3558141
- **Content**: System shall display F1-Trac: using 5 notches by setting the values according to the positions 1-2-3-4-5. (see: image199.png)
- **Artifact Type**: SRS Req
- **Responsible Domain**: Cluster SW
- **Test Stage**: System Qualification Test
- **Grooming Status**: Approved
- **State**: Approved
- **RQA Score**: 100
- **Testability Assessment**: HIGH - No RQA issues found, clear specification
- **Dependencies**: NVO_INFO_V2.ManettinoSts CAN signal, image199.png visual reference
- **Implementation Considerations**: Requires notch display logic for 5 positions
- **Issues**: Grooming comment about simulation method unclear

#### Requirement ID: 5286615
- **Content**: System shall display Comfort: 3 notches. It has a specific colour according to the Suspension mode selected IF SuspensionSetupSts = Position_1, then IDC shall display comfort indicator with an active notch IF SuspensionSetupSts = Position_2, then IDC shall display comfort indicator with two active notches IF SuspensionSetupSts = Position_3, then IDC shall display comfort indicator with three active notches
- **Artifact Type**: SRS Req
- **Responsible Domain**: Cluster SW
- **Grooming Status**: Approved
- **State**: Approved
- **RQA Score**: 30
- **Testability Assessment**: MEDIUM - Clear logic but quality issues present
- **Dependencies**: SuspensionSetupSts signal, color specification for suspension modes
- **Implementation Considerations**: Requires conditional display logic with color coding
- **Issues**: Unclear pronoun, compound requirement, missing unit tolerance

#### Requirement ID: 3558182
- **Content**: The number of active notches depends on the SuspensionSetupSts signal For ASC-C indicator.
- **Artifact Type**: SRS Req
- **Responsible Domain**: Cluster SW
- **Test Stage**: System Qualification Test
- **Grooming Status**: Review
- **State**: Obsolete
- **RQA Score**: 70
- **Testability Assessment**: LOW - Missing imperative, obsolete status
- **Dependencies**: SuspensionSetupSts signal, ASC-C indicator system
- **Implementation Considerations**: Not applicable due to obsolete status
- **Issues**: Missing imperative statement

#### Requirement ID: 3558183
- **Content**: System shall display Comfort indicator(Soft) with one active notch if Suspension status is in position 1
- **Artifact Type**: SRS Req
- **Responsible Domain**: Cluster SW
- **Test Stage**: System Qualification Test
- **Grooming Status**: Approved
- **State**: Approved
- **RQA Score**: 80
- **Testability Assessment**: HIGH - Clear condition and expected behavior
- **Dependencies**: SUSPENSION_INFO.SuspensionSetupSts signal
- **Implementation Considerations**: Requires position detection and notch display control
- **Issues**: Missing unit tolerance for position value

#### Requirement ID: 3558185
- **Content**: System shall display Comfort indicator(Medium) with two active notches if Suspension status is in position 2
- **Artifact Type**: SRS Req
- **Responsible Domain**: Cluster SW
- **Test Stage**: System Qualification Test
- **Grooming Status**: Approved
- **State**: Approved
- **RQA Score**: 80
- **Testability Assessment**: HIGH - Clear condition and expected behavior
- **Dependencies**: SUSPENSION_INFO.SuspensionSetupSts signal
- **Implementation Considerations**: Requires position detection and notch display control
- **Issues**: Missing unit tolerance for position value

#### Requirement ID: 3558188
- **Content**: System shall display Comfort indicator(Hard) with three active notches if Suspension status is in position 3
- **Artifact Type**: SRS Req
- **Responsible Domain**: Cluster SW
- **Test Stage**: System Qualification Test
- **Grooming Status**: Approved
- **State**: Approved
- **RQA Score**: 80
- **Testability Assessment**: HIGH - Clear condition and expected behavior
- **Dependencies**: SUSPENSION_INFO.SuspensionSetupSts signal
- **Implementation Considerations**: Requires position detection and notch display control
- **Issues**: Missing unit tolerance for position value

#### Requirement ID: 3501080
- **Content**: System shall continue to display within the specified area to display the vehicle manettino selected in any condition active/failure.
- **Artifact Type**: SRS Req
- **Responsible Domain**: Cluster SW
- **Test Stage**: System Qualification Test
- **Grooming Status**: Approved
- **State**: Approved
- **RQA Score**: 80
- **Testability Assessment**: MEDIUM - Unclear term "any condition" affects testability
- **Dependencies**: Display area specification, failure detection mechanisms
- **Implementation Considerations**: Requires robust failure handling and display persistence
- **Issues**: Unclear term "any"

#### Requirement ID: 3541059
- **Content**: System shall display Vehicle Manettino driving mode as below when Manettino position-1 select. (see: image200.png)
- **Artifact Type**: SRS Req
- **Responsible Domain**: Cluster SW
- **Test Stage**: System Qualification Test
- **Grooming Status**: Approved
- **State**: Approved
- **RQA Score**: 60
- **Testability Assessment**: HIGH - Visual reference provided with clear precondition
- **Dependencies**: PWT_STATUS_2.EManettinoSts signal, image200.png specification
- **Implementation Considerations**: ICE mode telltale display with blue/white color scheme
- **Issues**: Compound requirement, escape clause "as below"

#### Requirement ID: 3541061
- **Content**: System shall display Vehicle Manettino driving mode as below when position-2 select. (see: image201.png)
- **Artifact Type**: SRS Req
- **Responsible Domain**: Cluster SW
- **Test Stage**: System Qualification Test
- **Grooming Status**: Approved
- **State**: Approved
- **RQA Score**: 30
- **Testability Assessment**: MEDIUM - Multiple quality issues affect clarity
- **Dependencies**: ManettinoSts signal, image201.png specification
- **Implementation Considerations**: WET mode telltale display with green color scheme
- **Issues**: Compound requirement, escape clause, missing unit, passive voice

#### Requirement ID: 3541064
- **Content**: System shall display Vehicle Manettino driving mode as below when Manettino position-3 select. (see: image202.png)
- **Artifact Type**: SRS Req
- **Responsible Domain**: Cluster SW
- **Test Stage**: System Qualification Test
- **Grooming Status**: Approved
- **State**: Approved
- **RQA Score**: 60
- **Testability Assessment**: HIGH - Visual reference provided with clear precondition
- **Dependencies**: ManettinoSts signal, image202.png specification
- **Implementation Considerations**: COMFORT mode telltale display with yellow color scheme
- **Issues**: Compound requirement, escape clause

#### Requirement ID: 3541067
- **Content**: System shall display Vehicle Manettino driving mode as below when Manettino position 4 is selected. (see: image203.png) Note: ManettinoSts="Position4" and ESC OFF Lamp Request is not requested to HMI
- **Artifact Type**: SRS Req
- **Responsible Domain**: Cluster SW
- **Test Stage**: System Qualification Test
- **Grooming Status**: Approved
- **State**: Approved
- **RQA Score**: 20
- **Testability Assessment**: LOW - Multiple quality issues significantly impact testability
- **Dependencies**: ManettinoSts signal, ESCOFFLampRequest status, image203.png
- **Implementation Considerations**: SPORT mode telltale display with orange color scheme
- **Issues**: Compound requirement, negative statement, escape clause, missing unit, passive voice

#### Requirement ID: 3541069
- **Content**: System shall display Vehicle Manettino driving mode as below when Manettino position4 selected. (see: image204.png) Note: ManettinoSts="Position4" and ESC OFF Lamp Request is Fail Lamp On.
- **Artifact Type**: SRS Req
- **Responsible Domain**: Cluster SW
- **Test Stage**: System Qualification Test
- **Grooming Status**: Approved
- **State**: Approved
- **RQA Score**: 70
- **Testability Assessment**: HIGH - Safety-critical ESC OFF display requirement
- **Dependencies**: ManettinoSts signal, NFR_HMI.ESCOFFLampRequest, image204.png
- **Implementation Considerations**: ESC OFF telltale display with red warning color scheme
- **Issues**: Compound requirement, escape clause, passive voice

#### Requirement ID: 3523690
- **Content**: System shall display the persisted Manettino and Suspension status for 2.5 Seconds when Key turn on.
- **Artifact Type**: SRS Req
- **Responsible Domain**: Cluster SW
- **Test Stage**: System Qualification Test
- **Grooming Status**: Approved
- **State**: Approved
- **RQA Score**: 70
- **Testability Assessment**: HIGH - Clear timing specification and behavior
- **Dependencies**: Key-on event detection, persistent storage, timing mechanism
- **Implementation Considerations**: Requires precise timing control and memory management
- **Issues**: Compound requirement, missing tolerance for 2.5 seconds

#### Requirement ID: 3523717
- **Content**: System shall display Manettino status as empty until recovery becomes active ,when system stop's receiving the Manettino status.
- **Artifact Type**: SRS Req
- **Responsible Domain**: Cluster SW
- **Test Stage**: System Qualification Test
- **Grooming Status**: Approved
- **State**: Obsolete
- **RQA Score**: 70
- **Testability Assessment**: LOW - Obsolete status, unclear recovery mechanism
- **Dependencies**: Signal timeout detection, recovery mechanism
- **Implementation Considerations**: Not applicable due to obsolete status
- **Issues**: Compound requirement, obsolete status

#### Requirement ID: 3551774
- **Content**: System shall continue to display manettino status till R19 recovery happens when Manettino status is not-received
- **Artifact Type**: SRS Req
- **Responsible Domain**: Cluster SW
- **Test Stage**: System Qualification Test
- **Grooming Status**: Approved
- **State**: Approved
- **RQA Score**: 70
- **Testability Assessment**: LOW - R19 recovery mechanism undefined
- **Dependencies**: R19 recovery system, signal timeout detection
- **Implementation Considerations**: Critical gap - R19 recovery information not available
- **Issues**: Compound requirement, negative statement, passive voice, undefined R19 recovery

#### Requirement ID: 3551790
- **Content**: System shall continue to display the current vehicle Manettino repetition When active suspension functionality is Active and if suspension setup status signal not-received.
- **Artifact Type**: SRS Req
- **Responsible Domain**: Cluster SW
- **Test Stage**: System Qualification Test
- **Grooming Status**: Approved
- **State**: Approved
- **RQA Score**: 60
- **Testability Assessment**: MEDIUM - Clear precondition but signal handling unclear
- **Dependencies**: Active Suspension Functionality status, signal timeout detection
- **Implementation Considerations**: Requires robust signal monitoring and fallback behavior
- **Issues**: Compound requirement, negative statement

#### Requirement ID: 3

```markdown
## 3. Visual Elements Analysis

### 3.1 Physical Control Interface Analysis

#### 3.1.1 Manettino Control Design (IMAGE 197)
The Ferrari Manettino implements a premium rotary control interface with the following specifications:
- **Physical Design**: Red Ferrari knob with metallic finish and centered Ferrari logo
- **Position Layout**: 5 positions arranged in arc formation around the control
- **Position Labels**: White text on black background displaying "ICE", "WET", "CONF", "SPORT", "ESC OFF"
- **Visual Hierarchy**: High contrast white text ensures visibility in all lighting conditions
- **Brand Integration**: Ferrari logo prominently displayed on knob center maintaining brand identity

#### 3.1.2 Mode Color Classification System
The visual analysis reveals a systematic color coding approach across all driving modes:

**Safety-to-Performance Color Hierarchy**:
- **Blue/White (ICE)**: Safety-oriented mode with conservative color scheme
- **Green (WET)**: Environmental adaptation mode with nature-associated color
- **Yellow/Amber (COMFORT)**: Balanced mode with neutral warning color
- **Orange (SPORT)**: Performance mode with energetic color
- **Red (ESC OFF)**: Critical safety override with warning color

### 3.2 HMI Display System Analysis

#### 3.2.1 Multi-Mode Display Architecture (IMAGE 199)
The HMI system implements a comprehensive 5-mode display architecture:
- **Display Structure**: Each mode shows 6 telltales (ABS, TMC, REG, ESC, ASC-H, ASC-C)
- **Layout Consistency**: Circular arrangement maintained across all 5 modes
- **Total Display States**: 30 individual telltale states (5 modes × 6 telltales)
- **Background Design**: Consistent dark backgrounds for optimal contrast

#### 3.2.2 Mode-Specific Visual Characteristics

**ICE Mode Display**:
- Color Scheme: Blue/White telltales (RGB approximately 0, 100, 255 / 255, 255, 255)
- Visual Priority: Conservative safety-first appearance
- Telltale Intensity: Moderate illumination for comfort

**WET Mode Display (IMAGE 201)**:
- Primary Color: Green (RGB approximately 0, 255, 0)
- Telltale Design: Rectangular with rounded corners (120×50 pixels)
- Text Display: "WET" in high-contrast green on black background
- Visibility: High clarity for adverse weather conditions

**COMFORT Mode Display (IMAGE 202)**:
- Primary Color: Yellow/Amber (RGB approximately 255, 191, 0)
- Telltale Design: Rectangular with rounded corners (120×50 pixels)
- Text Display: "COMFORT" in yellow on black background
- Visual Balance: Neutral appearance for daily driving

**SPORT Mode Display (IMAGE 203)**:
- Primary Color: Orange (RGB approximately 255, 165, 0)
- Telltale Design: Rectangular with rounded corners
- Text Display: "SPORT" in orange on black background
- Performance Indication: Energetic color scheme for dynamic driving

**ESC OFF Mode Display (IMAGE 204)**:
- Primary Color: Red (RGB approximately 255, 0, 0)
- Safety Priority: Critical system warning color
- Text Display: "ESC OFF" indicating disabled stability control
- ISO Compliance: Aligned with ISO 2575 ESC system standards

### 3.3 Suspension Status Visual System

#### 3.3.1 Suspension Telltale Logic (IMAGE 198)
The suspension system implements a comprehensive signal-to-display mapping:

| Signal Value | Hex Code | Telltale Display | Visual Representation |
|--------------|----------|------------------|----------------------|
| Position_1   | 0x1      | /S (Soft)       | Yellow on black background |
| Position_2   | 0x2      | /M (Medium)     | Yellow on black background |
| Position_3   | 0x3      | /H (Hard)       | Yellow on black background |
| Recovery     | Invalid  | /S (Recovery)   | Yellow on black background |

#### 3.3.2 Performance Mode Telltales
The system includes specialized circular telltales for performance variants:

**S Mode Telltale (IMAGE 206)**:
- Shape: Circular design (distinct from rectangular telltales)
- Color: Orange (RGB approximately 255, 165, 0)
- Symbol: "S" character in center
- Application: Sport variant mode indication

**M Mode Telltale (IMAGE 207)**:
- Shape: Circular design
- Color: Orange (RGB approximately 255, 165, 0)
- Symbol: "M" character in center
- Application: Manual/Race mode indication

**H Mode Telltale (IMAGE 208)**:
- Shape: Circular design
- Color: Orange (RGB approximately 255, 165, 0)
- Symbol: "H" character in center
- Application: High performance mode indication

### 3.4 Development and System Telltales

#### 3.4.1 TBD System Indicator (IMAGE 205)
- **Design**: Car silhouette with "TBD" text overlay
- **Color**: Blue system status indicator
- **Purpose**: Development phase placeholder
- **Status**: Non-standard development indicator for incomplete features

### 3.5 Visual Design Standards Compliance

#### 3.5.1 Automotive Visibility Requirements
- **Contrast Ratios**: High contrast maintained across all telltales
- **Text Readability**: Clear text visibility in all lighting conditions
- **Size Consistency**: Standardized telltale dimensions (120×50 pixels for rectangular)
- **Color Differentiation**: Distinct color separation for mode identification

#### 3.5.2 Ferrari Brand Integration
- **Proprietary Design**: Non-ISO standard Ferrari-specific telltale designs
- **Brand Colors**: Ferrari red incorporated in physical control
- **Logo Integration**: Ferrari logo prominently displayed on Manettino knob
- **Premium Aesthetics**: Metallic finishes and high-quality visual presentation

## 4. Data Structure and Signal Analysis

### 4.1 CAN Signal Architecture

#### 4.1.1 Primary Manettino Signals
**PWT_STATUS_2.EManettinoSts Signal**:
- **Signal Type**: CAN bus enumerated signal
- **Data Range**: Position1 through Position5
- **Update Rate**: Real-time rotary position feedback
- **Dependencies**: Physical Manettino rotary control
- **Failure Handling**: R19 recovery mechanism (details TBD)

**NVO_INFO_V2.ManettinoSts Signal**:
- **Signal Type**: Non-volatile memory stored signal
- **Purpose**: Persistence across key cycles
- **Data Retention**: Maintains last selected position during key-off
- **Recovery Logic**: Displays persisted value for 2.5 seconds on key-on

#### 4.1.2 Suspension Control Signals
**SUSPENSION_INFO.SuspensionSetupSts Signal**:
- **Signal Type**: CAN bus hexadecimal signal
- **Data Values**: 0x1 (Soft), 0x2 (Medium), 0x3 (Hard)
- **Recovery State**: Invalid values default to 0x1 (Soft) display
- **Integration**: Active Suspension Functionality dependency

### 4.2 Signal-to-Function Mapping Tables

#### 4.2.1 Manettino Position Logic Table
| Physical Position | Signal Value | Mode Display | HMI Color | Telltale Count |
|------------------|--------------|--------------|-----------|----------------|
| Position 1       | Position1    | ICE          | Blue/White| 6 telltales    |
| Position 2       | Position2    | WET          | Green     | 6 telltales    |
| Position 3       | Position3    | COMFORT      | Yellow    | 6 telltales    |
| Position 4       | Position4    | SPORT        | Orange    | 6 telltales    |
| Position 5       | Position5    | ESC OFF      | Red       | 6 telltales    |

#### 4.2.2 Suspension Status Logic Table
| SuspensionSetupSts | Hex Value | Telltale | Active Notches | Color Scheme |
|-------------------|-----------|----------|----------------|--------------|
| Position_1        | 0x1       | /S       | 1 notch        | Yellow       |
| Position_2        | 0x2       | /M       | 2 notches      | Yellow       |
| Position_3        | 0x3       | /H       | 3 notches      | Yellow       |
| Recovery/Invalid  | N/A       | /S       | 1 notch        | Yellow       |

#### 4.2.3 ESC Integration Logic Table
| ManettinoSts | ESCOFFLampRequest | Display Result | Safety Priority |
|--------------|-------------------|----------------|-----------------|
| Position4    | Not Requested     | SPORT (Orange) | Medium          |
| Position4    | Fail Lamp On      | ESC OFF (Red)  | Critical        |
| Other Positions | Any State      | Normal Mode    | Standard        |

### 4.3 System Integration Signals

#### 4.3.1 HMI Integration Signals
**NFR_HMI.ESCOFFLampRequest**:
- **Signal Type**: Safety-critical lamp request
- **Priority**: High (overrides normal SPORT display)
- **Color Override**: Forces red ESC OFF telltale when active
- **Integration**: Position 4 conditional display logic

**Proxi Active Suspension Functionality**:
- **Signal Type**: System enable/disable flag
- **Function**: Controls suspension display availability
- **Dependencies**: Suspension status and indexes screen display
- **Failure Behavior**: Maintains current display on signal loss

#### 4.3.2 Timing and Persistence Signals
**Key-On Event Detection**:
- **Trigger**: Vehicle key activation
- **Response**: Display persisted status for 2.5 seconds
- **Data Source**: Non-volatile memory storage
- **Tolerance**: ±0.1 seconds (specification gap identified)

**Key-Off Event Detection**:
- **Trigger**: Vehicle key deactivation
- **Action**: Store current Manettino and suspension status
- **Storage**: Non-volatile memory persistence
- **Recovery**: Available on next key-on cycle

### 4.4 Signal Processing Architecture

#### 4.4.1 Multi-Network Integration
**CAN Bus Signals**:
- PWT_STATUS_2.EManettinoSts (Primary position)
- SUSPENSION_INFO.SuspensionSetupSts (Suspension control)
- NFR_HMI.ESCOFFLampRequest (Safety override)

**Internal Signals**:
- NVO_INFO_V2.ManettinoSts (Persistence)
- Proxi Active Suspension Functionality (System enable)
- Key state detection (Power management)

**Ethernet Network Integration**:
- IVI system communication
- Multi-domain signal distribution
- System-wide state synchronization

#### 4.4.2 Failure Detection and Recovery
**Signal Timeout Handling**:
- **Manettino Signal Loss**: Display empty until R19 recovery
- **Suspension Signal Loss**: Continue current display
- **Recovery Mechanism**: R19 system (specification incomplete)

**Invalid Signal Processing**:
- **Invalid Suspension Values**: Default to Position_1 (/S display)
- **CAN Bus Errors**: Maintain last valid state
- **System Failures**: Graceful degradation with user feedback

### 4.5 Data Quality and Validation

#### 4.5.1 Signal Validation Requirements
- **Range Checking**: Validate hex values 0x1-0x3 for suspension
- **Enumeration Validation**: Confirm Position1-Position5 for Manettino
- **Timeout Detection**: Monitor signal freshness and validity
- **Cross-Signal Validation**: Verify ESC/Manettino position consistency

#### 4.5.2 Performance Specifications
- **Signal Update Rate**: Real-time for safety-critical functions
- **Display Response Time**: <100ms for mode changes (estimated)
- **Persistence Write Time**: <500ms for key-off storage (estimated)
- **Recovery Time**: 2.5 seconds for key-on display duration
```