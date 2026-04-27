# Picture-Centric Process Flow Diagrams Analysis

**Category:** PROCESS_FLOW_DIAGRAMS  
**Template Version:** 3.0.0  
**Created:** 2026-02-25  
**Last Updated:** 2026-02-25  
**Author:** Picture Analyze Agent Development Team  
**Template Type:** Picture-Centric Analysis Template  
**Status:** Production Ready  
**Compatibility:** Application v4.0.0+

## VERSION HISTORY
| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 3.0.0 | 2026-02-25 | Converted to Picture-Centric approach, TXT output format | Development Team |
| 2.0 | 2026-02-23 | Enhanced JSON-based version with detailed condition extraction | Picture Analyze Agent |
| 1.0 | 2026-02-23 | Initial JSON-based version | Picture Analyze Agent |

## TEMPLATE INFORMATION
- **Purpose**: Picture-centric process flow diagram analysis with practical TXT output
- **Use Case**: Automotive state machines, process flows, and behavioral diagrams
- **Processing Time**: 4-7 minutes per image
- **Output Format**: Structured TXT with embedded tables and CSV-ready data

## CORE PRINCIPLE
**PICTURE-FIRST ANALYSIS**: Focus on visual flow elements actually present in the image. Extract complete state machine logic for automotive system development.

## EXECUTION METHODOLOGY

### 1. Flow Diagram Content Identification
- Identify state bubbles/ovals (STATUS 0, STATUS 1, etc.)
- Catalog all arrows and their directions
- Extract all condition text on arrows (including multi-line conditions)
- Identify decision diamonds and delay processes

### 2. Picture-Centric Organization Structure
```
=== PROCESS FLOW DIAGRAM ANALYSIS REPORT ===
├─ Image Overview & Enhancement Details
├─ STATE MACHINE STRUCTURE (primary section)
├─ STATE DEFINITIONS (complete state descriptions)
├─ TRANSITION ANALYSIS (arrows, conditions, logic)
├─ Decision Points & Delay Processes
├─ Complete State Machine Logic
├─ CSV Format Ready Data
├─ Automotive Context Integration
└─ Validation Checklist
```

### 3. Process Flow Processing Pipeline
**For Process Flow Diagram Images:**
- **State Identification**: All STATUS nodes with complete descriptions
- **Transition Extraction**: Arrow directions, conditions, and logic operators
- **Condition Analysis**: Multi-line conditions, OR/AND logic, exact text preservation
- **Flow Logic**: Complete behavioral model with all guard conditions
- **Automotive Context**: CAN signals, system states, and timing requirements

## REQUIRED OUTPUT STRUCTURE

### Section 1: Image Overview
```
=== PROCESS FLOW DIAGRAM ANALYSIS REPORT ===

IMAGE: [filename]
├─ Content: Process flow diagram showing [describe main flow purpose]
├─ Flow Type: State Machine / Process Flow / Decision Tree / Behavioral Model
├─ Original Dimensions: [width]x[height] pixels
├─ Enhancement Applied: [OCR optimization, arrow detection, text clarity enhancement]
├─ Quality Assessment: [state visibility, arrow clarity, condition text readability]
├─ Analysis Confidence: [High/Medium/Low] - [reasoning]
```

### Section 2: State Machine Structure (PRIMARY FOCUS)
```
=== STATE MACHINE STRUCTURE ===

OVERALL FLOW ARCHITECTURE:
├─ Total States: [number] (STATUS nodes only)
├─ Total Transitions: [number] (arrows between states)
├─ Decision Points: [number] (diamond shapes)
├─ Delay Processes: [number] (timing elements)
├─ Flow Complexity: [Simple/Medium/Complex] - [reasoning]

STATE INVENTORY:
├─ STATE 0: [Position: top/center/bottom/left/right]
│  ├─ Visual Description: [shape, size, color]
│  ├─ Internal Text: "[exact text from bubble, preserving line breaks]"
│  ├─ Incoming Transitions: [number] from [list source states]
│  └─ Outgoing Transitions: [number] to [list target states]
├─ STATE 1: [Position]
│  ├─ Visual Description: [description]
│  ├─ Internal Text: "[exact text]"
│  ├─ Incoming Transitions: [details]
│  └─ Outgoing Transitions: [details]

TRANSITION OVERVIEW:
├─ Simple Transitions: [number] (single condition)
├─ Complex Transitions: [number] (multiple conditions)
├─ OR Logic Transitions: [number] (alternative paths)
├─ Bidirectional Flows: [number] (arrows in both directions)
├─ Conditional Delays: [number] (transitions with timing)

FLOW PATTERNS IDENTIFIED:
├─ Entry Points: [states with no incoming transitions]
├─ Exit Points: [states with no outgoing transitions]
├─ Loop Structures: [any circular flow patterns]
├─ Parallel Branches: [any parallel processing paths]
├─ Decision Trees: [branching decision structures]
```

### Section 3: State Definitions
```
=== STATE DEFINITIONS ===

### COMPLETE STATE CATALOG

**STATE 0:**
├─ Name: "STATUS 0"
├─ Position: [visual position in diagram]
├─ Description: "[complete text from state bubble, exactly as written]"
├─ System Function: [inferred automotive function]
├─ Active Conditions: [any conditions that must be true in this state]
├─ Sensor States: [any sensor readings mentioned in state description]
├─ Output Actions: [any outputs or actions performed in this state]

**STATE 1:**
├─ Name: "STATUS 1"
├─ Position: [visual position in diagram]
├─ Description: "[complete text from state bubble, exactly as written]"
├─ System Function: [inferred automotive function]
├─ Active Conditions: [conditions]
├─ Sensor States: [sensor readings]
├─ Output Actions: [actions]

### STATE RELATIONSHIP MATRIX

**State Connectivity:**
| State | Incoming_From | Outgoing_To | Total_Connections | State_Type |
|-------|---------------|-------------|-------------------|------------|
| STATUS 0 | [list] | [list] | [number] | Entry/Process/Exit |
| STATUS 1 | [list] | [list] | [number] | Entry/Process/Exit |

**State Descriptions Summary:**
| State_Name | Internal_Text | System_Function | Key_Parameters |
|------------|---------------|-----------------|----------------|
| STATUS 0 | "[exact text]" | [function] | [parameters] |
| STATUS 1 | "[exact text]" | [function] | [parameters] |
```

### Section 4: Transition Analysis
```
=== TRANSITION ANALYSIS ===

### COMPLETE TRANSITION CATALOG

**TRANSITION 1: STATUS 0 → STATUS 1**
├─ Arrow Direction: [↑↓←→ or descriptive]
├─ Visual Path: [describe arrow path and any curves]
├─ Condition Type: [Simple/Complex/OR Logic/AND Logic]
├─ Complete Condition Text:
│  ├─ Line 1: "[exact text from arrow, preserving capitalization]"
│  ├─ Line 2: "[exact text if multi-line]"
│  ├─ Line N: "[all condition lines]"
├─ Logic Structure:
│  ├─ AND Conditions: [list all AND terms]
│  ├─ OR Alternatives: [list all OR branches]
│  ├─ Comparison Operators: [==, ≤, >, <, !=, etc.]
│  ├─ Boolean Values: [True/False/'Pressed'/etc.]
├─ Timing Elements:
│  ├─ Delay Specification: "[RearDelay = X sec or null]"
│  ├─ Timing Conditions: [any time-based conditions]
├─ CAN Signals Referenced: [any automotive signals mentioned]

**TRANSITION 2: STATUS 1 → STATUS 0**
├─ Arrow Direction: [direction]
├─ Visual Path: [description]
├─ Condition Type: [type]
├─ Complete Condition Text: [all lines exactly as written]
├─ Logic Structure: [AND/OR analysis]
├─ Timing Elements: [delays and timing]
├─ CAN Signals Referenced: [signals]

### COMPLEX CONDITION ANALYSIS

**Multi-Line Condition Example:**
```
Original Arrow Text:
"NPS_FrontButtonSts == 'Pressed'"
"Stop_GoEnable == 'False' from 'True'"
"VehicleSpeed ≤ 10km/h"
"OR"
"Stop_GoEnable == 'True' AND VehicleSpeed goes below 10km/h"

Parsed Logic Structure:
Alternative 1 (AND Logic):
  - NPS_FrontButtonSts == 'Pressed'
  - Stop_GoEnable == 'False' from 'True'
  - VehicleSpeed ≤ 10km/h
Alternative 2 (OR Logic):
  - Stop_GoEnable == 'True' AND VehicleSpeed goes below 10km/h
```

### DECISION LOGIC TABLES

**Transition Condition Matrix:**
| From_State | To_State | Condition_1 | Logic_Op | Condition_2 | Logic_Op | Condition_N | Delay | Result |
|------------|----------|-------------|----------|-------------|----------|-------------|-------|--------|
| STATUS 0 | STATUS 1 | Key_On | AND | Stop_GoEnable=FALSE | AND | [condition] | 0 sec | Transition |
| STATUS 1 | STATUS 0 | Button='Pressed' | OR | Speed≤10km/h | - | - | 1 sec | Transition |

**Boolean Logic Summary:**
| Transition | AND_Conditions | OR_Alternatives | Complex_Logic | Timing_Dependent |
|------------|----------------|-----------------|---------------|------------------|
| 0→1 | [list] | [list] | [Yes/No] | [Yes/No] |
| 1→0 | [list] | [list] | [Yes/No] | [Yes/No] |
```

### Section 5: Decision Points & Delay Processes
```
=== DECISION POINTS & DELAY PROCESSES ===

### DECISION DIAMONDS

**DECISION 1:**
├─ Name: "[exact text from diamond]"
├─ Position: [location in flow]
├─ Input From: [source state or transition]
├─ TRUE Path: [where TRUE arrow leads]
├─ FALSE Path: [where FALSE arrow leads]
├─ Decision Logic: "[exact condition being evaluated]"
├─ Automotive Context: [what system decision this represents]

### DELAY PROCESSES

**DELAY 1:**
├─ Name: "[exact text from delay box, e.g., 'RearDelay = 1 sec']"
├─ Position: [location in flow]
├─ Input From: [source state]
├─ Output To: [destination state]
├─ Bidirectional: [Yes/No - can flow both ways]
├─ Timing Specification: [exact delay value and units]
├─ Trigger Conditions: [what triggers the delay]
├─ Automotive Purpose: [why this delay exists in the system]

### TIMING ANALYSIS

**System Timing Requirements:**
| Element | Delay_Value | Units | Trigger_Condition | Purpose |
|---------|-------------|-------|-------------------|---------|
| RearDelay | 1 | sec | [condition] | [automotive purpose] |
| FrontDelay | 0.5 | sec | [condition] | [automotive purpose] |

**Critical Timing Paths:**
- Path 1: [state sequence with total timing]
- Path 2: [state sequence with total timing]
- Maximum Response Time: [worst case timing]
- Minimum Response Time: [best case timing]
```

### Section 6: Complete State Machine Logic
```
=== COMPLETE STATE MACHINE LOGIC ===

### BEHAVIORAL MODEL SUMMARY

**System Operation Overview:**
The process flow implements [describe overall system behavior] with [number] states and [number] transitions. The system responds to [list key inputs] and produces [list key outputs] with timing constraints of [timing summary].

**State Machine Rules:**
1. Entry Conditions: [how system enters initial state]
2. Normal Operation: [typical state transitions during normal operation]
3. Error Handling: [how system handles error conditions]
4. Exit Conditions: [how system exits or shuts down]
5. Safety Interlocks: [any safety-related state restrictions]

### COMPLETE TRANSITION TABLE

**Full State Transition Matrix:**
| Current_State | Input_Condition_1 | Logic | Input_Condition_2 | Logic | Input_Condition_N | Next_State | Delay | Action |
|---------------|-------------------|-------|-------------------|-------|-------------------|------------|-------|--------|
| STATUS 0 | Key_On | AND | Stop_GoEnable=FALSE | - | - | STATUS 1 | 0 sec | [action] |
| STATUS 1 | Button='Pressed' | OR | Speed≤10km/h | - | - | STATUS 0 | 1 sec | [action] |

### AUTOMOTIVE SYSTEM INTEGRATION

**CAN Signal Dependencies:**
| Signal_Name | Signal_Type | Possible_Values | Update_Rate | Used_In_States | Used_In_Transitions |
|-------------|-------------|-----------------|-------------|----------------|-------------------|
| Stop_GoEnable | Boolean | True/False | 100ms | [states] | [transitions] |
| VehicleSpeed | Numeric | 0-300 km/h | 50ms | [states] | [transitions] |
| NPS_FrontButtonSts | Enumerated | Pressed/Released | Event | [states] | [transitions] |

**System Requirements Traceability:**
- REQ-001: [requirement] → [states/transitions that implement it]
- REQ-002: [requirement] → [states/transitions that implement it]
- REQ-003: [requirement] → [states/transitions that implement it]
```

### Section 7: CSV Format Ready Data
```
=== CSV FORMAT READY DATA ===

STATES.csv:
State_Name,Position,Description,System_Function,Incoming_Count,Outgoing_Count
STATUS 0,top-left,"[exact internal text]",Initial State,0,2
STATUS 1,center,"[exact internal text]",Active State,2,1
STATUS 2,bottom-right,"[exact internal text]",Final State,1,0

TRANSITIONS.csv:
From_State,To_State,Direction,Condition_Text,Logic_Type,Delay_Sec,CAN_Signals
STATUS 0,STATUS 1,rightward,"Key_On AND Stop_GoEnable=FALSE",AND,0,"Key_On,Stop_GoEnable"
STATUS 1,STATUS 0,leftward,"Button='Pressed' OR Speed≤10km/h",OR,1,"NPS_FrontButtonSts,VehicleSpeed"

DECISION_POINTS.csv:
Decision_Name,Position,Input_From,True_Path,False_Path,Decision_Logic
Speed Check,center-top,STATUS 1,STATUS 2,STATUS 0,"VehicleSpeed > 50km/h"

DELAY_PROCESSES.csv:
Delay_Name,Position,Input_From,Output_To,Delay_Value,Units,Bidirectional
RearDelay,bottom-center,STATUS 1,STATUS 0,1,sec,No
FrontDelay,top-center,STATUS 0,STATUS 1,0.5,sec,Yes
```

## CRITICAL ANALYSIS REQUIREMENTS

### Text Extraction Precision:
- **EXACT TEXT PRESERVATION**: Capture all condition text exactly as written, including spacing, capitalization, and symbols
- **MULTI-LINE CONDITIONS**: Many arrows contain multiple lines of condition text that must ALL be captured
- **COMPARISON OPERATORS**: Include all operators (==, ≤, >, <, !=) exactly as shown
- **QUOTED STRINGS**: Preserve exact quotation marks and string values

### Arrow Direction Analysis:
- **CAREFUL EXAMINATION**: Examine
