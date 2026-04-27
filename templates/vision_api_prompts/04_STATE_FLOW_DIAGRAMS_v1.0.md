# Picture-Centric State Flow Diagrams Analysis

**Category:** STATE_FLOW_DIAGRAMS  
**Template Version:** 2.0.0  
**Created:** 2026-02-23  
**Last Updated:** 2026-02-26  
**Author:** Picture Analyze Agent Development Team  
**Template Type:** Picture-Centric Analysis Template  
**Status:** Production Ready  
**Compatibility:** Application v4.0.0+

## VERSION HISTORY
| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 2.0.0 | 2026-02-26 | Converted to Picture-Centric approach, TXT output format | Development Team |
| 1.0 | 2026-02-23 | Initial JSON-based version | Picture Analyze Agent |

## TEMPLATE INFORMATION
- **Purpose**: Picture-centric state flow diagram analysis with practical TXT output
- **Use Case**: Automotive state machines, behavioral logic, and system state analysis
- **Processing Time**: 6-10 minutes per image
- **Output Format**: Structured TXT with embedded tables and CSV-ready data

## CORE PRINCIPLE
**PICTURE-FIRST ANALYSIS**: Focus on visual states and transitions actually present in the image. Extract practical state machine information for automotive development and testing.

## EXECUTION METHODOLOGY

### 1. Image Content Identification
- Identify state machine type (finite state machine, hierarchical, concurrent)
- Catalog all visible states (initial, normal, error, final states)
- Determine state transitions and trigger conditions
- Assess image quality and enhancement needs

### 2. Picture-Centric Organization Structure
```
=== STATE FLOW DIAGRAM ANALYSIS REPORT ===
├─ Image Overview & Enhancement Details
├─ STATE MACHINE STRUCTURE ANALYSIS (primary section)
├─ STATE INVENTORY (initial, normal, error, final states)
├─ TRANSITION ANALYSIS (triggers, conditions, actions)
├─ BEHAVIORAL LOGIC EXTRACTION (state behaviors, timing)
├─ CSV Format Ready Data
├─ Automotive Standards Compliance
├─ Enhancement Details
└─ Validation Checklist
```

### 3. State Machine-Specific Processing Pipeline
**For State Flow Diagram Images:**
- **State Analysis**: Identification, classification, properties, behaviors
- **Transition Extraction**: Triggers, guards, actions, timing constraints
- **Logic Mapping**: Decision tables, state matrices, behavioral patterns
- **Standards Compliance**: ISO 26262, AUTOSAR state management
- **Test Generation**: State transition test cases and coverage
- **Safety Analysis**: Error states, fault handling, recovery mechanisms

## REQUIRED OUTPUT STRUCTURE

### Section 1: Image Overview
```
=== STATE FLOW DIAGRAM ANALYSIS REPORT ===

IMAGE: [filename]
├─ Content: State flow diagram showing [describe main states and transitions]
├─ State Machine Type: Finite State Machine / Hierarchical / Concurrent / Hybrid
├─ Original Dimensions: [width]x[height] pixels
├─ Enhancement Applied: [specific enhancement details for state diagrams]
├─ Quality Assessment: [clarity, state visibility, transition readability]
├─ Analysis Confidence: [High/Medium/Low] - [reasoning]
```

### Section 2: State Machine Structure Analysis (PRIMARY FOCUS)
```
=== STATE MACHINE STRUCTURE ANALYSIS ===

OVERALL STATE MACHINE:
├─ State Machine Type: [Finite/Hierarchical/Concurrent/Hybrid]
├─ System Domain: [Engine/Transmission/Brake/Door/etc.]
├─ Safety Level: [QM/ASIL_A/ASIL_B/ASIL_C/ASIL_D]
├─ State Count: [total number of identified states]
├─ Transition Count: [total number of transitions]

STATE HIERARCHY:
├─ Level 1 (Main States): [primary system states]
├─ Level 2 (Sub-States): [nested states within main states]
├─ Level 3 (Micro-States): [detailed operational states]
├─ Concurrent Regions: [parallel state execution areas]

STATE CATEGORIES:
├─ INITIAL STATES: [entry points to state machine]
├─ NORMAL OPERATION: [standard operational states]
├─ ERROR STATES: [fault and error handling states]
├─ FINAL STATES: [termination and shutdown states]
├─ COMPOSITE STATES: [states containing sub-states]
├─ CONCURRENT STATES: [parallel execution states]
```

### Section 3: State Inventory
```
=== STATE INVENTORY ===

INITIAL STATES:
├─ STATE 1: [Name] - Position: [coordinates]
│  ├─ State Type: Initial
│  ├─ Description: [state purpose and function]
│  ├─ Entry Actions: [actions performed on state entry]
│  ├─ Exit Actions: [actions performed on state exit]
│  ├─ Internal Actions: [ongoing activities within state]
│  └─ Timeout Conditions: [time-based transitions]

NORMAL OPERATION STATES:
├─ STATE 2: [Name] - Position: [coordinates]
│  ├─ State Type: Normal
│  ├─ Description: [state purpose and function]
│  ├─ Entry Actions: [initialization actions]
│  ├─ Exit Actions: [cleanup actions]
│  ├─ Internal Actions: [continuous behaviors]
│  ├─ Timeout Conditions: [timing constraints]
│  └─ Safety Mechanisms: [monitoring and protection]

ERROR STATES:
├─ STATE 3: [Name] - Position: [coordinates]
│  ├─ State Type: Error/Fault
│  ├─ Description: [error condition and handling]
│  ├─ Entry Actions: [error response actions]
│  ├─ Exit Actions: [recovery preparation]
│  ├─ Internal Actions: [error monitoring]
│  ├─ Recovery Conditions: [conditions for recovery]
│  └─ Safety Actions: [fail-safe behaviors]

FINAL STATES:
├─ STATE 4: [Name] - Position: [coordinates]
│  ├─ State Type: Final/Terminal
│  ├─ Description: [termination conditions]
│  ├─ Entry Actions: [shutdown procedures]
│  ├─ Exit Actions: [none - terminal state]
│  ├─ Internal Actions: [final cleanup]
│  └─ Safety Considerations: [safe shutdown requirements]
```

### Section 4: Transition Analysis
```
=== TRANSITION ANALYSIS ===

### STATE TRANSITIONS

**Primary Transitions:**
| Transition ID | Source State | Target State | Trigger Event | Guard Condition | Action | Timing |
|---------------|--------------|--------------|---------------|-----------------|--------|--------|
| TRANS-001 | Engine_Off | Cranking | Key_Turn_On | Battery_OK | Start_Sequence | 100ms |
| TRANS-002 | Cranking | Running | Engine_Started | RPM > 500 | Enable_Systems | 50ms |
| TRANS-003 | Running | Engine_Off | Key_Turn_Off | None | Shutdown_Sequence | 200ms |
| TRANS-004 | Any_State | Error_State | System_Fault | Fault_Detected | Error_Handler | 10ms |

### TRIGGER CONDITIONS

**Event-Based Triggers:**
| Trigger Name | Source | Type | Conditions | Priority | Safety Level |
|--------------|--------|------|------------|----------|--------------|
| Key_Turn_On | User Input | External | Key position change | High | ASIL_B |
| Engine_Started | Engine Sensor | Internal | RPM threshold | High | ASIL_D |
| System_Fault | Diagnostic | Internal | Error detection | Critical | ASIL_D |
| Timeout_Event | Timer | Internal | Time elapsed | Medium | ASIL_C |

### GUARD CONDITIONS

**Conditional Logic:**
| Guard Name | Expression | Variables | Valid Range | Safety Check |
|------------|------------|-----------|-------------|--------------|
| Battery_OK | Battery_Voltage > 12.0V | Battery_Voltage | 10.0-16.0V | Yes |
| Engine_Running | RPM > 500 AND Oil_Pressure > 1.0 | RPM, Oil_Pressure | RPM: 0-8000, Pressure: 0-5.0 | Yes |
| System_Ready | All_Diagnostics_OK | Diagnostic_Flags | Boolean array | Yes |
| Temperature_Normal | Engine_Temp < 110°C | Engine_Temperature | -40 to 150°C | Yes |

### TRANSITION ACTIONS

**Action Specifications:**
| Action Name | Description | Duration | Dependencies | Safety Impact |
|-------------|-------------|----------|--------------|---------------|
| Start_Sequence | Initialize engine systems | 500ms | Battery, Fuel, Ignition | ASIL_D |
| Enable_Systems | Activate vehicle functions | 200ms | Engine running | ASIL_C |
| Shutdown_Sequence | Safe system shutdown | 1000ms | None | ASIL_B |
| Error_Handler | Fault response and logging | 50ms | Diagnostic system | ASIL_D |
```

### Section 5: Behavioral Logic Extraction
```
=== BEHAVIORAL LOGIC EXTRACTION ===

### STATE BEHAVIORS

**State-Specific Activities:**
| State Name | Entry Behavior | Internal Behavior | Exit Behavior | Timing Constraints |
|------------|----------------|-------------------|---------------|-------------------|
| Engine_Off | Disable_Fuel_Pump | Monitor_Key_Status | Enable_Diagnostics | Entry: 10ms |
| Cranking | Engage_Starter | Monitor_Engine_Speed | Disengage_Starter | Max duration: 10s |
| Running | Enable_All_Systems | Control_Engine_Parameters | Prepare_Shutdown | Continuous |
| Error_State | Log_Error_Code | Monitor_Recovery_Conditions | Clear_Error_Flags | Recovery timeout: 30s |

### DECISION LOGIC TABLES

**State Transition Decision Matrix:**
| Current State | Trigger Event | Guard Condition | Next State | Action | Notes |
|---------------|---------------|-----------------|------------|--------|-------|
| Engine_Off | Key_On | Battery_OK | Cranking | Start_Sequence | Normal start |
| Engine_Off | Key_On | Battery_Low | Error_State | Battery_Warning | Low battery |
| Cranking | Engine_Started | RPM_Valid | Running | Enable_Systems | Successful start |
| Cranking | Timeout | Duration > 10s | Error_State | Start_Failed | Failed start |
| Running | Key_Off | None | Engine_Off | Shutdown_Sequence | Normal shutdown |
| Running | System_Fault | Fault_Critical | Error_State | Emergency_Stop | Safety shutdown |
| Error_State | Recovery_OK | All_Systems_Normal | Engine_Off | Reset_System | Recovery complete |

### TIMING ANALYSIS

**State Timing Requirements:**
| State Name | Min Duration | Max Duration | Timeout Action | Safety Timeout |
|------------|--------------|--------------|----------------|----------------|
| Cranking | 100ms | 10s | Abort_Start | 15s |
| Running | 1s | Unlimited | None | N/A |
| Error_State | 50ms | 60s | Force_Shutdown | 120s |
| Shutdown | 100ms | 5s | Force_Off | 10s |
```

### Section 6: Extracted Table Data
```
=== EXTRACTED TABLE DATA ===

STATE INVENTORY TABLE: (from state analysis)
Purpose: Complete state catalog with properties and behaviors

State_Name | State_Type | Position_X | Position_Y | Entry_Actions | Exit_Actions | Internal_Actions | Timeout_Duration
-----------|------------|------------|------------|---------------|--------------|------------------|------------------
Engine_Off | Initial | 100 | 200 | Disable_Fuel_Pump | Enable_Diagnostics | Monitor_Key_Status | None
Cranking | Normal | 300 | 200 | Engage_Starter | Disengage_Starter | Monitor_Engine_Speed | 10s
Running | Normal | 500 | 200 | Enable_All_Systems | Prepare_Shutdown | Control_Engine_Parameters | None
Error_State | Error | 300 | 400 | Log_Error_Code | Clear_Error_Flags | Monitor_Recovery_Conditions | 30s

TRANSITION SPECIFICATIONS TABLE: (from transition analysis)
Purpose: State transition details with triggers and conditions

Transition_ID | Source_State | Target_State | Trigger_Event | Guard_Condition | Transition_Action | Timing_Constraint
--------------|--------------|--------------|---------------|-----------------|-------------------|------------------
TRANS_001 | Engine_Off | Cranking | Key_Turn_On | Battery_OK | Start_Sequence | 100ms
TRANS_002 | Cranking | Running | Engine_Started | RPM > 500 | Enable_Systems | 50ms
TRANS_003 | Running | Engine_Off | Key_Turn_Off | None | Shutdown_Sequence | 200ms
TRANS_004 | Any_State | Error_State | System_Fault | Fault_Detected | Error_Handler | 10ms

BEHAVIORAL LOGIC TABLE: (from behavior analysis)
Purpose: State behaviors and decision logic mapping

State_Name | Trigger_Condition | Guard_Expression | Action_Sequence | Safety_Check | Test_Condition
-----------|-------------------|------------------|-----------------|--------------|---------------
Engine_Off | Key_Turn_On | Battery_Voltage > 12V | Start_Sequence | Battery_Monitor | Verify_Start_Conditions
Cranking | Engine_Speed_OK | RPM > 500 | Enable_Systems | RPM_Monitor | Verify_Engine_Running
Running | Key_Turn_Off | None | Shutdown_Sequence | Safe_Shutdown | Verify_Clean_Shutdown
Error_State | Recovery_Signal | All_Systems_OK | Reset_System | System_Check | Verify_Recovery_Complete
```

### Section 7: CSV Format Ready Data
```
=== CSV FORMAT READY DATA ===

STATE_INVENTORY.csv:
State_Name,State_Type,Position_X,Position_Y,Entry_Actions,Exit_Actions,Internal_Actions,Timeout_Duration
Engine_Off,Initial,100,200,Disable_Fuel_Pump,Enable_Diagnostics,Monitor_Key_Status,None
Cranking,Normal,300,200,Engage_Starter,Disengage_Starter,Monitor_Engine_Speed,10s
Running,Normal,500,200,Enable_All_Systems,Prepare_Shutdown,Control_Engine_Parameters,None
Error_State,Error,300,400,Log_Error_Code,Clear_Error_Flags,Monitor_Recovery_Conditions,30s

TRANSITION_SPECIFICATIONS.csv:
Transition_ID,Source_State,Target_State,Trigger_Event,Guard_Condition,Transition_Action,Timing_Constraint
TRANS_001,Engine_Off,Cranking,Key_Turn_On,Battery_OK,Start_Sequence,100ms
TRANS_002,Cranking,Running,Engine_Started,RPM > 500,Enable_Systems,50ms
TRANS_003,Running,Engine_Off,Key_Turn_Off,None,Shutdown_Sequence,200ms
TRANS_004,Any_State,Error_State,System_Fault,Fault_Detected,Error_Handler,10ms

BEHAVIORAL_LOGIC.csv:
State_Name,Trigger_Condition,Guard_Expression,Action_Sequence,Safety_Check,Test_Condition
Engine_Off,Key_Turn_On,Battery_Voltage > 12V,Start_Sequence,Battery_Monitor,Verify_Start_Conditions
Cranking,Engine_Speed_OK,RPM > 500,Enable_Systems,RPM_Monitor,Verify_Engine_Running
Running,Key_Turn_Off,None,Shutdown_Sequence,Safe_Shutdown,Verify_Clean_Shutdown
Error_State,Recovery_Signal,All_Systems_OK,Reset_System,System_Check,Verify_Recovery_Complete
```

### Section 8: Automotive Standards Compliance
```
=== AUTOMOTIVE STANDARDS COMPLIANCE ===

ISO 26262 FUNCTIONAL SAFETY:
├─ State Machine Safety: [safety state identification and handling]
├─ Error State Management: [fault detection and recovery mechanisms]
├─ Safety Mechanisms: [watchdog monitoring, state validation]
├─ Fail-Safe States: [safe default states for fault conditions]

AUTOSAR STATE MANAGEMENT:
├─ State Manager Compliance: [AUTOSAR state management patterns]
├─ Mode Management: [system mode transitions and coordination]
├─ Startup/Shutdown: [standardized initialization and termination]
├─ Error Recovery: [AUTOSAR error handling mechanisms]

AUTOMOTIVE BEHAVIORAL STANDARDS:
├─ State Timing: [real-time constraints and timing requirements]
├─ Deterministic Behavior: [predictable state machine execution]
├─ Resource Management: [state-based resource allocation]
├─ Diagnostic Integration: [state machine diagnostic capabilities]

FERRARI DESIGN STANDARDS:
├─ State Machine Consistency: [alignment with Ferrari behavioral guidelines]
├─ Performance States: [Ferrari-specific performance mode states]
├─ Safety Integration: [Ferrari safety state requirements]
├─ User Experience: [state transitions affecting driver interaction]
```

## QUALITY STANDARDS

### Image Enhancement Requirements:
- **State Diagram Enhancement**: Optimize for state visibility and transition clarity
- **OCR Optimization**: 95%+ accuracy for all state labels and transition conditions
- **Flow Accuracy**: Precise identification of state transitions and decision points
- **Logic Recognition**: Clear identification of guard conditions and actions

### Picture-Centric Analysis Standards:
- **State-First Structure**: Visual states and transitions drive the analysis
- **Complete Coverage**: Every visible state and transition cataloged
- **Practical Focus**: Information useful for automotive behavioral development
- **Standards Compliance**: Verification against automotive state management standards

### Validation Requirements:
- **100% State Coverage**: All visible states and transitions identified
- **Accurate Logic Mapping**: Guard conditions and actions correctly interpreted
- **Standards Mapping**: Proper ISO 26262 and AUTOSAR references
- **CSV Conversion**: All tabular data properly formatted

## EXECUTION CHECKLIST

### Pre-Processing:
- [ ] Identify state machine type and behavioral domain
- [ ] Assess image quality and enhancement needs
- [ ] Determine analysis approach based on state complexity
- [ ] Prepare for state and transition analysis

### State Analysis:
- [ ] Catalog all states with types and properties
- [ ] Identify all transitions with triggers and conditions
- [ ] Document behavioral logic and timing requirements
- [ ] Analyze safety mechanisms and error handling

### Logic Analysis:
- [ ] Extract all guard conditions and expressions
- [ ] Document state behaviors and actions
- [ ] Map decision logic and state matrices
- [ ] Generate test cases for state transitions

### Output Generation:
- [ ] Structure report with state machine analysis as primary section
- [ ] Format all data for CSV conversion
- [ ] Document automotive standards compliance
- [ ] Provide complete validation checklist

## SUCCESS CRITERIA

### Processing Quality:
- **State Identification**: 100% of visible states cataloged
- **Transition Accuracy**: 95%+ accuracy in trigger and condition identification
- **Standards Compliance**: Proper mapping to automotive behavioral standards
- **Data Extraction**: All tabular data ready for CSV/Excel import

### Picture-Centric Focus:
- **Visual Priority**: States and transitions are primary focus
- **Practical Output**: Information directly usable for behavioral development
- **Technical Depth**: Complete analysis of state machine functionality
- **Implementation Ready**: All data suitable for automotive system development

### Enhancement Details:
- **Applied Enhancements**: State visibility optimization, transition clarity improvement
- **Quality Metrics**: State recognition accuracy, logic mapping precision
- **Validation Results**: Complete coverage verification, standards compliance check

### Analysis Summary:
- **Key Findings**: State machine type, critical states, behavioral patterns
- **Development Implications**: System behavioral requirements, safety considerations
- **Recommended Actions**: State machine improvements, standards compliance updates
