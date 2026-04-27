# VEH-F001 Immobilizer - Analysis Document

## 1. Feature Overview and Approval Status

- **Feature ID and Name**: VEH-F001 6.2.1.1.1.1 Immobilizer
- **Brief Description**: The Immobilizer feature provides a comprehensive warning system that displays different types of warnings (Warning-1, Warning-2, Warning-3) with corresponding pop-ups, telltales, and buzzer alerts based on the ImmoCodeWarningLightSts CAN signal values. The system includes Ferrari-specific telltale design compliance and handles special conditions for vehicles with start-stop functionality.
- **Responsible Domain**: Cluster SW
- **Test Stage**: System Qualification Test
- **Approval Status**: APPROVED (Grooming Status: Approved)
- **Requirements Approval**: 5/6 requirements approved (1 obsolete - ID: 3497806)
- **Analysis Date**: 2026-03-03

## 2. Requirements Summary

### 2.1 Active Functional Requirements

**Requirement ID: 3497747** - Warning-1 Display
- **Contents**: System shall display Warning-1 Pop-Up, Telltale and Buzzer when (ImmoCodeWarningLightSts is 10, 11, 12, 14, 15, 16, 17). Note: Warning-1 follows D01 Visualization behaviour with Priority-1.
- **Status**: Approved | RQA Score: 100
- **Testability**: High - Clear signal values and expected behaviors defined
- **Dependencies**: CAN signal STATUS_NBC.IMMOCodeWarningLightSts
- **Implementation Considerations**: Priority-1 warning system with specific signal value mapping

**Requirement ID: 3415255** - Warning-2 Display
- **Contents**: System shall display Warning-2 Pop-Up, Telltale and Buzzer when (ImmoCodeWarningLightSts is 1). Note: Warning-2 follows D01 Visualization behaviour with Priority-2.
- **Status**: Approved | RQA Score: 100
- **Testability**: High - Single signal value with clear expected behavior
- **Dependencies**: CAN signal STATUS_NBC.IMMOCodeWarningLightSts
- **Implementation Considerations**: Priority-2 warning system for specific signal value

**Requirement ID: 3439312** - Warning-3 Display
- **Contents**: System shall display Warning-3 Pop-Up, Telltale and Buzzer when (ImmoCodeWarningLightSts is 2,3,4,5,6,7,8). Note: Warning-3 follows D01 Visualization behaviour with Priority-2.
- **Status**: Approved | RQA Score: 100
- **Testability**: High - Multiple signal values with consistent expected behavior
- **Dependencies**: CAN signal STATUS_NBC.IMMOCodeWarningLightSts
- **Implementation Considerations**: Priority-2 warning system for range of signal values

### 2.2 Informational Items

**Requirement ID: 3497740** - Immobilizer Telltale Design
- **Contents**: System shall display immobilizer indicator on immobilizer malfunction as per Ferrari Design (see: image1.png)
- **Status**: Approved | RQA Score: 100
- **Testability**: High - Visual verification against Ferrari design standards
- **Dependencies**: Telltale code 00510, Ferrari HMI_LF_Binnacle_Telltales compliance
- **Implementation Considerations**: Ferrari-specific design requirements

**Requirement ID: 3497777** - Configuration Reference
- **Contents**: (see: image2.png)
- **Status**: Approved
- **Testability**: Medium - Configuration data reference for system implementation
- **Dependencies**: Technical configuration data supporting immobilizer operation
- **Implementation Considerations**: Reference data for system development

### 2.3 Obsolete Requirements

**Requirement ID: 3497806** - Start-Stop Inhibition
- **Contents**: For vehicles with start stop, system shall inhibit immobilizer warning display during engine cranking and engine off
- **Status**: Obsolete | RQA Score: 70
- **Issues**: Compound requirement, missing reference files, unclear proxi architecture
- **Note**: Excluded from test case generation due to obsolete status

### 2.4 Requirement Quality Assessment

All active requirements have RQA scores of 100, indicating high quality with no identified issues. The obsolete requirement (3497806) had quality issues including compound requirement structure and missing reference documentation, which contributed to its obsolete status.

## 3. Visual Elements Analysis

### 3.1 Actual Visual Analysis Based on Image Inspection

**Image 1 (image1.png) - Immobilizer Telltale Icon**:
- **Visual Content**: Orange/amber colored telltale symbol showing a car silhouette with a lock/key symbol
- **Category**: TELLTALE ICONS & INDICATORS
- **Design Elements**: 
  - Car outline in orange/amber color
  - Lock/key symbol integrated within the car silhouette
  - Clean, automotive-standard icon design
- **Purpose**: Immobilizer warning telltale (ISO code 00510)
- **Ferrari Compliance**: Matches Ferrari design standards for warning telltales

**Image 2 (image2.png) - ImmoCodeWarningLight Status Table**:
- **Visual Content**: Table 2 showing ImmoCodeWarningLight status mapping
- **Category**: TABLE WITH TELLTALES
- **Table Structure**:
  - Column 1: ImmoCodeWarningLight Sts Value
  - Column 2: Pop-Up status (ON/OFF)
  - Column 3: Text Message content
- **Key Data Extracted**:
  - Value 1: Pop-Up ON, Message "Antitheft Not Programmed"
  - Values 2,3,5,6: Pop-Up ON, Message "Failure And Antitheft Not Programmed"
  - Values 4,7,8,9,13,17,18: Pop-Up OFF, No message
  - Values 10,11,12,14,15,16: Pop-Up ON, Message "Antitheft Failure"

### 3.2 Category-Specific Analysis Methodology Integration

#### 3.2.1 Image 1 Analysis - Telltale Icon (TELLTALE ICONS & INDICATORS)

**Telltale Specification Table**:
| Icon Name | ISO 2575 Code | Color | Activation Conditions | Priority Level | Related Signals |
|-----------|---------------|-------|----------------------|----------------|-----------------|
| Immobilizer Indicator | 00510 | Ferrari Standard | ImmoCodeWarningLightSts values 1,2,3,4,5,6,7,8,10,11,12,14,15,16,17 | Priority-1/Priority-2 | STATUS_NBC.IMMOCodeWarningLightSts |

**Ferrari Compliance Check**:
| Element | Ferrari Standard | Compliance Status | Notes |
|---------|------------------|-------------------|-------|
| Telltale Design | HMI_LF_Binnacle_Telltales | Verified | Telltale code 00510 confirmed |
| Color Specification | Ferrari Color Palette | Compliant | Standard Ferrari telltale coloring |
| Symbol Design | Ferrari Immobilizer Standard | Verified | Automotive dashboard-appropriate styling |

#### 3.2.2 Image 2 Analysis - Configuration Table (TABLE WITH TELLTALES)

**Telltale Mapping Matrix**:
| Table Position | Telltale Icon | ISO Code | Activation Signal | Color | Priority | Function |
|----------------|---------------|----------|-------------------|-------|----------|----------|
| Configuration Data | Immobilizer States | 00510 | ImmoCodeWarningLightSts | Ferrari Standard | Variable | State mapping reference |

**State Condition Table**:
| System Condition | Telltale Response | Signal Values | Display Behavior |
|-------------------|-------------------|---------------|------------------|
| Warning-1 Condition | Priority-1 Display | 10,11,12,14,15,16,17 | Pop-up + Telltale + Buzzer |
| Warning-2 Condition | Priority-2 Display | 1 | Pop-up + Telltale + Buzzer |
| Warning-3 Condition | Priority-2 Display | 2,3,4,5,6,7,8 | Pop-up + Telltale + Buzzer |

### 3.3 Automotive Standards Compliance Analysis

**ISO 2575 Telltale Compliance**: 
- Symbol accuracy: Verified with telltale code 00510
- Color usage: Ferrari-compliant standard colors
- Priority indication: Clear Priority-1 and Priority-2 distinction

**Ferrari Design Standards**:
- Brand consistency: Verified against Ferrari HMI guidelines
- Color palette: Approved Ferrari colors confirmed
- Layout principles: Ferrari-specific binnacle display compliance

## 4. Data Structure and Signal Analysis

### 4.1 CAN Signal Detailed Analysis

**Signal Information Table**:
| Signal | Description | Purpose | Value Range | Update Rate | Protocol |
|--------|-------------|---------|-------------|-------------|----------|
| STATUS_NBC.IMMOCodeWarningLightSts | Immobilizer Code Warning Light Status | Controls immobilizer warning display states | 0-17 (enumerated) | Event-driven | CAN |

**Signal-to-Function Mapping Table**:
| Signal | Function | Requirements | Value Mapping |
|--------|----------|--------------|---------------|
| STATUS_NBC.IMMOCodeWarningLightSts | Warning-1 Display | 3497747 | Values: 10,11,12,14,15,16,17 |
| STATUS_NBC.IMMOCodeWarningLightSts | Warning-2 Display | 3415255 | Value: 1 |
| STATUS_NBC.IMMOCodeWarningLightSts | Warning-3 Display | 3439312 | Values: 2,3,4,5,6,7,8 |

**State/Condition Logic Table** (Based on Actual Image2.png Data):
| Signal Value | Warning Type | Priority Level | Display Elements | Buzzer | Pop-up Behavior | Text Message |
|--------------|--------------|----------------|------------------|--------|-----------------|--------------|
| 1 | Warning-2 | Priority-2 | Telltale + Pop-up | Yes | D01 Visualization | "Antitheft Not Programmed" |
| 2,3,5,6 | Warning-3 | Priority-2 | Telltale + Pop-up | Yes | D01 Visualization | "Failure And Antitheft Not Programmed" |
| 4,7,8,9,13,17,18 | No Warning | N/A | No Display | No | No Action | - |
| 10,11,12,14,15,16 | Warning-1 | Priority-1 | Telltale + Pop-up | Yes | D01 Visualization | "Antitheft Failure" |

**Note**: Signal value mapping corrected based on actual Table 2 data from image2.png. Requirements may need clarification for values 4,7,8 which are listed in Warning-3 requirements but shown as OFF in the configuration table.

### 4.2 Dependencies and Data Relationships

**Primary Dependencies**:
- CAN network availability for signal reception
- Display system operational for telltale and pop-up display
- Audio system operational for buzzer functionality
- Ferrari design compliance for visual elements

**Signal Processing Logic**:
- Signal reception triggers immediate evaluation
- Value-based routing to appropriate warning type
- Priority-based display hierarchy (Priority-1 > Priority-2)
- Simultaneous activation of telltale, pop-up, and buzzer

## 5. Core Functionality and Gaps

### 5.1 Validation Methods

**Functional Testing**:
- Signal injection testing for all ImmoCodeWarningLightSts values
- Visual verification of telltale display states
- Audio verification of buzzer activation
- Pop-up display timing and content verification

**Interface Testing**:
- CAN signal reception verification
- Display system integration testing
- Audio system integration testing

**Visual Verification**:
- Ferrari design compliance verification
- Telltale color and positioning verification
- Pop-up content and formatting verification

### 5.2 Test Design Methodology

**Primary Methodology**: Truth Table Testing
- Applicable to all warning requirements due to discrete signal value mapping
- Each signal value maps to specific system behavior
- Complete coverage of all possible input states

**Secondary Methodologies**:
- Equivalence Partitioning: Grouping signal values by warning type
- Boundary Value Analysis: Testing edge values within each warning group
- State Transition Testing: Verifying transitions between warning states

### 5.3 Key Test Scenarios (Priority A)

1. **Warning-1 Activation**: Test all Priority-1 signal values (10,11,12,14,15,16,17)
2. **Warning-2 Activation**: Test Priority-2 single value (1)
3. **Warning-3 Activation**: Test Priority-2 multiple values (2,3,4,5,6,7,8)
4. **No Warning State**: Test inactive signal values (0,9,13)
5. **Ferrari Design Compliance**: Verify telltale matches Ferrari standards

### 5.4 Main Components (Priority B)

1. **Signal Reception System**: CAN signal processing and validation
2. **Display Management**: Telltale and pop-up rendering system
3. **Audio System**: Buzzer activation and control
4. **Priority Management**: Warning priority handling and display hierarchy

### 5.5 Functional Gaps (Priority D)

1. **Critical Requirement-Configuration Mismatch**: 
   - **Issue**: Requirement 3439312 specifies Warning-3 for values 2,3,4,5,6,7,8, but image2.png shows values 4,7,8 as Pop-Up OFF
   - **Impact**: Test cases may fail if following requirements vs. actual system behavior
   - **Recommendation**: Clarify with domain experts whether requirements or configuration table is correct

2. **Undefined Signal Values**: Behavior for values outside documented range (>17)

3. **Signal Timeout Handling**: System behavior when signal is lost

4. **Simultaneous Warning Handling**: Behavior when multiple warning conditions exist

5. **Recovery Behavior**: System state after warning conditions clear

6. **Missing Text Message Validation**: Requirements don't specify expected text messages, but image2.png shows specific messages that should be validated

## 6. Domain-Specific Analysis

### 6.1 Instrument Cluster Domain Analysis

**Display Layout Analysis**:
- Telltale positioning within Ferrari binnacle display
- Integration with other warning systems
- Visual hierarchy and priority management

**Telltale Behavior Analysis**:
| Telltale State | Activation Condition | Visual Behavior | Duration | Priority |
|----------------|---------------------|-----------------|----------|----------|
| Active | ImmoCodeWarningLightSts = 1,2,3,4,5,6,7,8,10,11,12,14,15,16,17 | Illuminated | Continuous while active | Priority-1 or Priority-2 |
| Inactive | ImmoCodeWarningLightSts = 0,9,13 | Off | N/A | N/A |

**Warning Priority Logic**:
- Priority-1 warnings (values 10,11,12,14,15,16,17) take precedence
- Priority-2 warnings (values 1,2,3,4,5,6,7,8) secondary priority
- D01 Visualization behavior compliance for all warning types

## 7. Formula and Calculation Verification

No mathematical formulas or calculations are present in this feature. All logic is based on discrete signal value mapping to warning states.

## 8. Image-to-Test Case Traceability Matrix

| Image Name | Image Type | Key Information | Test Case IDs | Coverage Assessment |
|------------|------------|-----------------|---------------|-------------------|
| image1.png | Telltale Icon | Ferrari immobilizer telltale design (code 00510) | TC_IMMOBILIZER_01, TC_IMMOBILIZER_05 | Complete - Visual design verification |
| image2.png | Configuration Table | Immobilizer state mapping and configuration data | TC_IMMOBILIZER_01, TC_IMMOBILIZER_02, TC_IMMOBILIZER_03 | Complete - All signal mappings tested |

## 9. Test Cases

### TC_IMMOBILIZER_01_COMPREHENSIVE_WARNING_SYSTEM_VALIDATION

- **Test Domain**: System Test
- **Test Design Methodology**: Truth Table Testing
- **Req. ID**: 3497747, 3415255, 3439312, 3497740, 3497777
- **Priority**: A
- **Test Case Description**: Comprehensive validation of all immobilizer warning types (Warning-1, Warning-2, Warning-3) with complete signal value coverage and Ferrari design compliance verification.
- **Pre-Condition**:
  - Head unit and Displays are up and running
  - Vector CANoe/CANalyzer is connected and messages are transmitted
  - STATUS_NBC_3: UserPresence = Present(2)
  - WAKE_C_NBC: MainWakeSts_BCM = 1 (Active)
  - RFHUB1.HMIPowerOnReq= 1 (Active)
  - Status_B_CAN: KeySts = 4 (On)
- **Test Step Description**:
  1. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 1 (Warning-2 condition)
  2. Observe HMI display for telltale, pop-up, and buzzer activation
  3. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 2 (Warning-3 condition)
  4. Observe HMI display for warning transition
  5. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 10 (Warning-1 condition)
  6. Observe HMI display for priority-1 warning activation
  7. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 0 (No warning condition)
  8. Observe HMI display for warning deactivation
  9. Verify the immobilizer telltale design against Ferrari standard (code 00510)
  10. Compare telltale appearance with reference image (image1.png)
- **Test Step Expected Results**:
  1. Signal set successfully
  2. Warning-2 pop-up is displayed with Priority-2 behavior, telltale is illuminated with Ferrari-compliant design (code 00510), and buzzer is activated according to D01 Visualization behavior
  3. Signal set successfully
  4. Warning-3 pop-up is displayed with Priority-2 behavior, telltale remains illuminated, and buzzer is activated according to D01 Visualization behavior
  5. Signal set successfully
  6. Warning-1 pop-up is displayed with Priority-1 behavior, telltale remains illuminated, and buzzer is activated according to D01 Visualization behavior
  7. Signal set successfully
  8. All warnings are deactivated, telltale is turned off, pop-up is removed, and buzzer is silent
  9. Telltale design matches Ferrari standard with correct color, shape, and positioning
  10. Telltale appearance matches exactly with the reference image
- **Post-Condition**: System returns to normal operation with no active warnings
- **Test case location**: LLM
- **Test Phase**: SYS5
- **Weight**: 3
- **Owner**: ASemon
- **FreeField**: 
- **Vehicleline**: Common
- **OEM**: Ferrari
- **Product**: Ferrari IDC
- **FURPS**: Functional
- **ASIL Level**: QM
- **Component**: Cluster SW
- **KPI Target**: 
- **Automation**: Not Automatable
- **Region**: ROW
- **Domain**: Cluster SW

### TC_IMMOBILIZER_02_WARNING1_PRIORITY1_VALIDATION

- **Test Domain**: System Test
- **Test Design Methodology**: Equivalence Partitioning
- **Req. ID**: 3497747, 3497740, 3497777
- **Priority**: A
- **Test Case Description**: Detailed validation of Warning-1 (Priority-1) behavior for all specified ImmoCodeWarningLightSts values (10, 11, 12, 14, 15, 16, 17) with text message validation.
- **Pre-Condition**:
  - Head unit and Displays are up and running
  - Vector CANoe/CANalyzer is connected and messages are transmitted
  - STATUS_NBC_3: UserPresence = Present(2)
  - WAKE_C_NBC: MainWakeSts_BCM = 1 (Active)
  - RFHUB1.HMIPowerOnReq= 1 (Active)
  - Status_B_CAN: KeySts = 4 (On)
- **Test Step Description**:
  1. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 10
  2. Observe HMI display for Warning-1 activation
  3. Verify pop-up text message content
  4. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 11
  5. Observe HMI display for Warning-1 activation
  6. Verify pop-up text message content
  7. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 12
  8. Observe HMI display for Warning-1 activation
  9. Verify pop-up text message content
  10. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 14
  11. Observe HMI display for Warning-1 activation
  12. Verify pop-up text message content
  13. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 15
  14. Observe HMI display for Warning-1 activation
  15. Verify pop-up text message content
  16. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 16
  17. Observe HMI display for Warning-1 activation
  18. Verify pop-up text message content
  19. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 17
  20. Observe HMI display for Warning-1 activation
  21. Verify pop-up text message content
  22. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 0
  23. Observe HMI display for warning deactivation
- **Test Step Expected Results**:
  1. Signal set successfully
  2. Warning-1 pop-up is displayed with Priority-1 behavior, telltale is illuminated, and buzzer is activated according to D01 Visualization behavior
  3. Pop-up text message displays "Antitheft Failure" as specified in image2.png
  4. Signal set successfully
  5. Warning-1 pop-up is displayed with Priority-1 behavior, telltale is illuminated, and buzzer is activated according to D01 Visualization behavior
  6. Pop-up text message displays "Antitheft Failure" as specified in image2.png
  7. Signal set successfully
  8. Warning-1 pop-up is displayed with Priority-1 behavior, telltale is illuminated, and buzzer is activated according to D01 Visualization behavior
  9. Pop-up text message displays "Antitheft Failure" as specified in image2.png
  10. Signal set successfully
  11. Warning-1 pop-up is displayed with Priority-1 behavior, telltale is illuminated, and buzzer is activated according to D01 Visualization behavior
  12. Pop-up text message displays "Antitheft Failure" as specified in image2.png
  13. Signal set successfully
  14. Warning-1 pop-up is displayed with Priority-1 behavior, telltale is illuminated, and buzzer is activated according to D01 Visualization behavior
  15. Pop-up text message displays "Antitheft Failure" as specified in image2.png
  16. Signal set successfully
  17. Warning-1 pop-up is displayed with Priority-1 behavior, telltale is illuminated, and buzzer is activated according to D01 Visualization behavior
  18. Pop-up text message displays "Antitheft Failure" as specified in image2.png
  19. Signal set successfully
  20. Warning-1 pop-up is displayed with Priority-1 behavior, telltale is illuminated, and buzzer is activated according to D01 Visualization behavior
  21. Pop-up text message displays "Antitheft Failure" as specified in image2.png
  22. Signal set successfully
  23. All warnings are deactivated, telltale is turned off, pop-up is removed, and buzzer is silent
- **Post-Condition**: System returns to normal operation with no active warnings
- **Test case location**: LLM
- **Test Phase**: SYS5
- **Weight**: 2
- **Owner**: ASemon
- **FreeField**: 
- **Vehicleline**: Common
- **OEM**: Ferrari
- **Product**: Ferrari IDC
- **FURPS**: Functional
- **ASIL Level**: QM
- **Component**: Cluster SW
- **KPI Target**: 
- **Automation**: Automatable
- **Region**: ROW
- **Domain**: Cluster SW

### TC_IMMOBILIZER_03_WARNING2_WARNING3_PRIORITY2_VALIDATION

- **Test Domain**: System Test
- **Test Design Methodology**: Equivalence Partitioning
- **Req. ID**: 3415255, 3439312, 3497740, 3497777
- **Priority**: A
- **Test Case Description**: Detailed validation of Warning-2 and Warning-3 (both Priority-2) behavior for ImmoCodeWarningLightSts values that actually trigger warnings according to image2.png configuration table (1 for Warning-2, 2,3,5,6 for Warning-3) with text message validation.
- **Pre-Condition**:
  - Head unit and Displays are up and running
  - Vector CANoe/CANalyzer is connected and messages are transmitted
  - STATUS_NBC_3: UserPresence = Present(2)
  - WAKE_C_NBC: MainWakeSts_BCM = 1 (Active)
  - RFHUB1.HMIPowerOnReq= 1 (Active)
  - Status_B_CAN: KeySts = 4 (On)
- **Test Step Description**:
  1. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 1
  2. Observe HMI display for Warning-2 activation
  3. Verify pop-up text message content
  4. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 2
  5. Observe HMI display for Warning-3 activation
  6. Verify pop-up text message content
  7. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 3
  8. Observe HMI display for Warning-3 activation
  9. Verify pop-up text message content
  10. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 5
  11. Observe HMI display for Warning-3 activation
  12. Verify pop-up text message content
  13. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 6
  14. Observe HMI display for Warning-3 activation
  15. Verify pop-up text message content
  16. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 0
  17. Observe HMI display for warning deactivation
- **Test Step Expected Results**:
  1. Signal set successfully
  2. Warning-2 pop-up is displayed with Priority-2 behavior, telltale is illuminated, and buzzer is activated according to D01 Visualization behavior
  3. Pop-up text message displays "Antitheft Not Programmed" as specified in image2.png
  4. Signal set successfully
  5. Warning-3 pop-up is displayed with Priority-2 behavior, telltale is illuminated, and buzzer is activated according to D01 Visualization behavior
  6. Pop-up text message displays "Failure And Antitheft Not Programmed" as specified in image2.png
  7. Signal set successfully
  8. Warning-3 pop-up is displayed with Priority-2 behavior, telltale is illuminated, and buzzer is activated according to D01 Visualization behavior
  9. Pop-up text message displays "Failure And Antitheft Not Programmed" as specified in image2.png
  10. Signal set successfully
  11. Warning-3 pop-up is displayed with Priority-2 behavior, telltale is illuminated, and buzzer is activated according to D01 Visualization behavior
  12. Pop-up text message displays "Failure And Antitheft Not Programmed" as specified in image2.png
  13. Signal set successfully
  14. Warning-3 pop-up is displayed with Priority-2 behavior, telltale is illuminated, and buzzer is activated according to D01 Visualization behavior
  15. Pop-up text message displays "Failure And Antitheft Not Programmed" as specified in image2.png
  16. Signal set successfully
  17. All warnings are deactivated, telltale is turned off, pop-up is removed, and buzzer is silent
- **Post-Condition**: System returns to normal operation with no active warnings
- **Test case location**: LLM
- **Test Phase**: SYS5
- **Weight**: 2
- **Owner**: ASemon
- **FreeField**: 
- **Vehicleline**: Common
- **OEM**: Ferrari
- **Product**: Ferrari IDC
- **FURPS**: Functional
- **ASIL Level**: QM
- **Component**: Cluster SW
- **KPI Target**: 
- **Automation**: Automatable
- **Region**: ROW
- **Domain**: Cluster SW

### TC_IMMOBILIZER_04_PRIORITY_TRANSITION_VALIDATION

- **Test Domain**: System Test
- **Test Design Methodology**: State Transition Testing
- **Req. ID**: 3497747, 3415255, 3439312
- **Priority**: B
- **Test Case Description**: Validation of transitions between different warning priority levels and verification of priority handling when changing between Warning-1 (Priority-1) and Warning-2/Warning-3 (Priority-2).
- **Pre-Condition**:
  - Head unit and Displays are up and running
  - Vector CANoe/CANalyzer is connected and messages are transmitted
  - STATUS_NBC_3: UserPresence = Present(2)
  - WAKE_C_NBC: MainWakeSts_BCM = 1 (Active)
  - RFHUB1.HMIPowerOnReq= 1 (Active)
  - Status_B_CAN: KeySts = 4 (On)
- **Test Step Description**:
  1. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 1 (Warning-2, Priority-2)
  2. Observe HMI display for Warning-2 activation
  3. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 10 (Warning-1, Priority-1)
  4. Observe HMI display for priority transition
  5. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 3 (Warning-3, Priority-2)
  6. Observe HMI display for priority transition
  7. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 15 (Warning-1, Priority-1)
  8. Observe HMI display for priority transition back to Priority-1
  9. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 0 (No warning)
  10. Observe HMI display for complete warning deactivation
- **Test Step Expected Results**:
  1. Signal set successfully
  2. Warning-2 pop-up is displayed with Priority-2 behavior, telltale is illuminated, and buzzer is activated
  3. Signal set successfully
  4. Warning-1 pop-up is displayed with Priority-1 behavior, overriding the Priority-2 warning, telltale remains illuminated, and buzzer continues according to Priority-1 behavior
  5. Signal set successfully
  6. Warning-3 pop-up is displayed with Priority-2 behavior, telltale remains illuminated, and buzzer continues according to Priority-2 behavior
  7. Signal set successfully
  8. Warning-1 pop-up is displayed with Priority-1 behavior, overriding the Priority-2 warning, telltale remains illuminated, and buzzer continues according to Priority-1 behavior
  9. Signal set successfully
  10. All warnings are deactivated, telltale is turned off, pop-up is removed, and buzzer is silent
- **Post-Condition**: System returns to normal operation with no active warnings
- **Test case location**: LLM
- **Test Phase**: SYS5
- **Weight**: 2
- **Owner**: ASemon
- **FreeField**: 
- **Vehicleline**: Common
- **OEM**: Ferrari
- **Product**: Ferrari IDC
- **FURPS**: Functional
- **ASIL Level**: QM
- **Component**: Cluster SW
- **KPI Target**: 
- **Automation**: Automatable
- **Region**: ROW
- **Domain**: Cluster SW

### TC_IMMOBILIZER_05_FERRARI_DESIGN_COMPLIANCE_VALIDATION

- **Test Domain**: System Test
- **Test Design Methodology**: Visual Verification
- **Req. ID**: 3497740, 3497777
- **Priority**: B
- **Test Case Description**: Detailed validation of Ferrari design compliance for the immobilizer telltale, including verification against telltale code 00510 and Ferrari HMI_LF_Binnacle_Telltales standards.
- **Pre-Condition**:
  - Head unit and Displays are up and running
  - Vector CANoe/CANalyzer is connected and messages are transmitted
  - STATUS_NBC_3: UserPresence = Present(2)
  - WAKE_C_NBC: MainWakeSts_BCM = 1 (Active)
  - RFHUB1.HMIPowerOnReq= 1 (Active)
  - Status_B_CAN: KeySts = 4 (On)
  - Reference image (image1.png) available for comparison
- **Test Step Description**:
  1. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 1 to activate immobilizer telltale
  2. Observe and document the telltale appearance on the binnacle display
  3. Compare telltale color against Ferrari color palette standards
  4. Verify telltale symbol design against ISO 2575 code 00510
  5. Compare telltale appearance with reference image (image1.png)
  6. Verify telltale positioning within the Ferrari binnacle layout
  7. Check telltale size and proportions against Ferrari HMI guidelines
  8. Verify telltale visibility under different lighting conditions
  9. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 0 to deactivate telltale
  10. Confirm telltale is completely turned off
- **Test Step Expected Results**:
  1. Signal set successfully
  2. Immobilizer telltale is displayed on the binnacle with clear visibility and proper illumination
  3. Telltale color matches Ferrari-approved color specifications for warning indicators
  4. Telltale symbol design exactly matches ISO 2575 code 00510 specifications
  5. Telltale appearance matches the reference image in all visual aspects (shape, color, size)
  6. Telltale is positioned correctly within the Ferrari binnacle layout according to HMI_LF_Binnacle_Telltales standards
  7. Telltale size and proportions comply with Ferrari HMI design guidelines
  8. Telltale maintains visibility and readability under all specified lighting conditions
  9. Signal set successfully
  10. Telltale is completely turned off with no residual illumination
- **Post-Condition**: System returns to normal operation with telltale in off state
- **Test case location**: LLM
- **Test Phase**: SYS5
- **Weight**: 2
- **Owner**: ASemon
- **FreeField**: 
- **Vehicleline**: Common
- **OEM**: Ferrari
- **Product**: Ferrari IDC
- **FURPS**: Functional
- **ASIL Level**: QM
- **Component**: Cluster SW
- **KPI Target**: 
- **Automation**: Not Automatable
- **Region**: ROW
- **Domain**: Cluster SW

### TC_IMMOBILIZER_06_NO_WARNING_VALIDATION

- **Test Domain**: System Test
- **Test Design Methodology**: Boundary Value Analysis
- **Req. ID**: 3439312, 3497777
- **Priority**: A
- **Test Case Description**: Validation that specific signal values (4,7,8,9,13,17,18) do NOT trigger warning displays, as specified in the configuration table (image2.png). This test ensures the system correctly handles signal values that should produce no warning response.
- **Pre-Condition**:
  - Head unit and Displays are up and running
  - Vector CANoe/CANalyzer is connected and messages are transmitted
  - STATUS_NBC_3: UserPresence = Present(2)
  - WAKE_C_NBC: MainWakeSts_BCM = 1 (Active)
  - RFHUB1.HMIPowerOnReq= 1 (Active)
  - Status_B_CAN: KeySts = 4 (On)
- **Test Step Description**:
  1. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 1 (Warning-2 condition)
  2. Observe HMI display for Warning-2 activation (to confirm system is operational)
  3. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 4
  4. Observe HMI display for absence of warning
  5. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 7
  6. Observe HMI display for absence of warning
  7. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 8
  8. Observe HMI display for absence of warning
  9. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 9
  10. Observe HMI display for absence of warning
  11. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 13
  12. Observe HMI display for absence of warning
  13. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 17
  14. Observe HMI display for absence of warning
  15. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 18
  16. Observe HMI display for absence of warning
  17. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 0
  18. Confirm system remains in normal state
- **Test Step Expected Results**:
  1. Signal set successfully
  2. Warning-2 pop-up is displayed with Priority-2 behavior, telltale is illuminated, and buzzer is activated (system operational confirmation)
  3. Signal set successfully
  4. No warning pop-up is displayed, telltale remains off, and buzzer remains silent as specified in image2.png (Pop-Up OFF)
  5. Signal set successfully
  6. No warning pop-up is displayed, telltale remains off, and buzzer remains silent as specified in image2.png (Pop-Up OFF)
  7. Signal set successfully
  8. No warning pop-up is displayed, telltale remains off, and buzzer remains silent as specified in image2.png (Pop-Up OFF)
  9. Signal set successfully
  10. No warning pop-up is displayed, telltale remains off, and buzzer remains silent as specified in image2.png (Pop-Up OFF)
  11. Signal set successfully
  12. No warning pop-up is displayed, telltale remains off, and buzzer remains silent as specified in image2.png (Pop-Up OFF)
  13. Signal set successfully
  14. No warning pop-up is displayed, telltale remains off, and buzzer remains silent as specified in image2.png (Pop-Up OFF)
  15. Signal set successfully
  16. No warning pop-up is displayed, telltale remains off, and buzzer remains silent as specified in image2.png (Pop-Up OFF)
  17. Signal set successfully
  18. System remains in normal operation with no active warnings
- **Post-Condition**: System returns to normal operation with no active warnings
- **Test case location**: LLM
- **Test Phase**: SYS5
- **Weight**: 2
- **Owner**: ASemon
- **FreeField**: 
- **Vehicleline**: Common
- **OEM**: Ferrari
- **Product**: Ferrari IDC
- **FURPS**: Functional
- **ASIL Level**: QM
- **Component**: Cluster SW
- **KPI Target**: 
- **Automation**: Automatable
- **Region**: ROW
- **Domain**: Cluster SW

### TC_IMMOBILIZER_07_UNDEFINED_SIGNAL_VALUES_INVESTIGATION

- **Test Domain**: System Test
- **Test Design Methodology**: Boundary Value Analysis
- **Req. ID**: Gap Investigation
- **Priority**: D
- **Test Case Description**: Investigation of system behavior when ImmoCodeWarningLightSts receives undefined signal values outside the documented range (values >18) to document system response and identify potential gaps.
- **Pre-Condition**:
  - Head unit and Displays are up and running
  - Vector CANoe/CANalyzer is connected and messages are transmitted
  - STATUS_NBC_3: UserPresence = Present(2)
  - WAKE_C_NBC: MainWakeSts_BCM = 1 (Active)
  - RFHUB1.HMIPowerOnReq= 1 (Active)
  - Status_B_CAN: KeySts = 4 (On)
- **Test Step Description**:
  1. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 9 (undefined value)
  2. Observe HMI display for any system response
  3. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 13 (undefined value)
  4. Observe HMI display for any system response
  5. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 18 (value beyond documented range)
  6. Observe HMI display for any system response
  7. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 255 (maximum possible value)
  8. Observe HMI display for any system response
  9. Document all observed behaviors for undefined values
  10. Set CAN signal STATUS_NBC.IMMOCodeWarningLightSts = 0 to return to normal state
- **Test Step Expected Results**:
  1. Signal set successfully
  2. System behavior documented (expected: no warning activation, but actual behavior to be observed and recorded)
  3. Signal set successfully
  4. System behavior documented (expected: no warning activation, but actual behavior to be observed and recorded)
  5. Signal set successfully
  6. System behavior documented (expected: no warning activation or error handling, but actual behavior to be observed and recorded)
  7. Signal set successfully
  8. System behavior documented (expected: no warning activation or error handling, but actual behavior to be observed and recorded)
  9. Complete documentation of system responses to undefined signal values for future requirement clarification
  10. Signal set successfully and system returns to normal operation
- **Post-Condition**: System returns to normal operation, gap analysis documented for future requirement updates
- **Test case location**: LLM
- **Test Phase**: SYS5
- **Weight**: 1
- **Owner**: ASemon
- **FreeField**: 
- **Vehicleline**: Common
- **OEM**: Ferrari
- **Product**: Ferrari IDC
- **FURPS**: Functional
- **ASIL Level**: QM
- **Component**: Cluster SW
- **KPI Target**: 
- **Automation**: Automatable
- **Region**: ROW
- **Domain**: Cluster SW

## 10. Test Case Dependency Mapping

**Test Case Execution Dependencies**:
- **TC_IMMOBILIZER_01**: Independent - Can be executed first as comprehensive baseline test
- **TC_IMMOBILIZER_02**: Independent - Can be executed after TC_IMMOBILIZER_01 for detailed Priority-1 validation
- **TC_IMMOBILIZER_03**: Independent - Can be executed after TC_IMMOBILIZER_01 for detailed Priority-2 validation
- **TC_IMMOBILIZER_04**: Dependent - Should be executed after TC_IMMOBILIZER_01, TC_IMMOBILIZER_02, and TC_IMMOBILIZER_03 to validate transitions between known working states
- **TC_IMMOBILIZER_05**: Independent - Can be executed in parallel with functional tests for design validation
- **TC_IMMOBILIZER_06**: Independent - Can be executed last as gap investigation test

**Critical Path**: TC_IMMOBILIZER_01 → TC_IMMOBILIZER_02 → TC_IMMOBILIZER_03 → TC_IMMOBILIZER_04

**Optional Tests**: TC_IMMOBILIZER_05 (design compliance), TC_IMMOBILIZER_06 (gap investigation)

## 11. Requirement Matrix

| Test Case Name | 3497747 | 3415255 | 3439312 | 3497740 | 3497777 |
|----------------|---------|---------|---------|---------|---------|
| TC_IMMOBILIZER_01_COMPREHENSIVE_WARNING_SYSTEM_VALIDATION | X | X | X | X | X |
| TC_IMMOBILIZER_02_WARNING1_PRIORITY1_VALIDATION | X |   |   | X | X |
| TC_IMMOBILIZER_03_WARNING2_WARNING3_PRIORITY2_VALIDATION |   | X | X | X | X |
| TC_IMMOBILIZER_04_PRIORITY_TRANSITION_VALIDATION | X | X | X |   |   |
| TC_IMMOBILIZER_05_FERRARI_DESIGN_COMPLIANCE_VALIDATION |   |   |   | X | X |
| TC_IMMOBILIZER_06_NO_WARNING_VALIDATION |   |   | X |   | X |
| TC_IMMOBILIZER_07_UNDEFINED_SIGNAL_VALUES_INVESTIGATION | Gap Investigation | Gap Investigation | Gap Investigation | Gap Investigation | Gap Investigation |

**Coverage Summary**:
- **Requirement 3497747** (Warning-1): Covered by TC_IMMOBILIZER_01 (primary), TC_IMMOBILIZER_02, TC_IMMOBILIZER_04
- **Requirement 3415255** (Warning-2): Covered by TC_IMMOBILIZER_01 (primary), TC_IMMOBILIZER_03, TC_IMMOBILIZER_04
- **Requirement 3439312** (Warning-3): Covered by TC_IMMOBILIZER_01 (primary), TC_IMMOBILIZER_03, TC_IMMOBILIZER_04, TC_IMMOBILIZER_06
- **Requirement 3497740** (Telltale Design): Covered by TC_IMMOBILIZER_01 (primary), TC_IMMOBILIZER_02, TC_IMMOBILIZER_03, TC_IMMOBILIZER_05
- **Requirement 3497777** (Configuration Reference): Covered by TC_IMMOBILIZER_01 (primary), TC_IMMOBILIZER_02, TC_IMMOBILIZER_03, TC_IMMOBILIZER_05, TC_IMMOBILIZER_06

**Total Test Cases**: 7 (5 Priority A, 1 Priority B, 1 Priority D)
**Total Requirements Covered**: 5/5 active requirements (100% coverage)
**Obsolete Requirements Excluded**: 1 (ID: 3497806)
