# Picture-Centric Process Flow Diagrams Analysis - Enhanced Transitions

**Category:** PROCESS_FLOW_DIAGRAMS  
**Template Version:** 4.0.0  
**Created:** 2026-02-26  
**Last Updated:** 2026-02-26  
**Author:** Picture Analyze Agent Development Team  
**Template Type:** Picture-Centric Analysis Template with Enhanced Transition Focus  
**Status:** Production Ready  
**Compatibility:** Application v4.0.0+

## VERSION HISTORY
| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 4.0.0 | 2026-02-26 | Enhanced transition analysis, zoom capabilities, detailed incoming/outgoing flow tracking | Development Team |
| 3.0.0 | 2026-02-25 | Converted to Picture-Centric approach, TXT output format | Development Team |
| 2.0 | 2026-02-23 | Enhanced JSON-based version with detailed condition extraction | Picture Analyze Agent |
| 1.0 | 2026-02-23 | Initial JSON-based version | Picture Analyze Agent |

## TEMPLATE INFORMATION
- **Purpose**: Picture-centric process flow diagram analysis with enhanced transition focus and zoom capabilities
- **Use Case**: Automotive state machines, process flows, and behavioral diagrams
- **Processing Time**: 5-8 minutes per image
- **Output Format**: Structured TXT with embedded tables and CSV-ready data
- **Key Enhancement**: Detailed incoming/outgoing transition analysis with zoom-in text extraction

## CORE PRINCIPLE
**PICTURE-FIRST ANALYSIS WITH TRANSITION FOCUS**: Focus on visual flow elements with special attention to transition paths, arrow directions, and connection patterns. Use zoom analysis for complex regions.

## EXECUTION METHODOLOGY

### 1. Multi-Pass Analysis Approach
**PASS 1: Overall Flow Structure**
- Identify all state bubbles/ovals and their positions
- Map all arrows and their general directions
- Identify decision diamonds and delay processes
- Mark complex regions requiring zoom analysis

**PASS 2: Zoom Analysis for Complex Regions**
- Focus on areas with dense text or multiple overlapping arrows
- Extract detailed condition text from transition labels
- Analyze connection points where multiple transitions converge
- Examine state internal text with enhanced clarity

**PASS 3: Transition Path Tracing**
- Trace each arrow from source to destination
- Document exact visual path (straight, curved, multi-segment)
- Catalog all text along transition paths
- Map bidirectional flows and parallel paths

### 2. Enhanced Transition Analysis Structure
```
=== PROCESS FLOW DIAGRAM ANALYSIS REPORT ===
├─ Image Overview & Enhancement Details
├─ ZOOM ANALYSIS REGIONS (new section)
├─ STATE MACHINE STRUCTURE (enhanced with transition focus)
├─ DETAILED TRANSITION MAPPING (new comprehensive section)
├─ STATE DEFINITIONS (with incoming/outgoing details)
├─ TRANSITION ANALYSIS (enhanced with path tracing)
├─ TRANSITION INTERSECTION ANALYSIS (new section)
├─ Decision Points & Delay Processes
├─ Complete State Machine Logic
├─ CSV Format Ready Data
├─ Automotive Context Integration
└─ Validation Checklist
```

## REQUIRED OUTPUT STRUCTURE

### Section 1: Image Overview with Zoom Regions
```
=== PROCESS FLOW DIAGRAM ANALYSIS REPORT ===

IMAGE: [filename]
├─ Content: Process flow diagram showing [describe main flow purpose]
├─ Flow Type: State Machine / Process Flow / Decision Tree / Behavioral Model
├─ Original Dimensions: [width]x[height] pixels
├─ Enhancement Applied: [OCR optimization, arrow detection, text clarity enhancement]
├─ Quality Assessment: [state visibility, arrow clarity, condition text readability]
├─ Analysis Confidence: [High/Medium/Low] - [reasoning]

=== ZOOM ANALYSIS REGIONS ===

COMPLEX REGIONS IDENTIFIED:
├─ Region 1: [coordinates or description]
│  ├─ Content Type: Dense transition text / Multiple arrow convergence / Complex state internal text
│  ├─ Zoom Focus: [specific area requiring detailed analysis]
│  ├─ Text Extraction Quality: [assessment after zoom analysis]
│  └─ Key Elements Extracted: [list of critical elements found in zoom]
├─ Region 2: [coordinates or description]
│  ├─ Content Type: [type]
│  ├─ Zoom Focus: [area]
│  ├─ Text Extraction Quality: [assessment]
│  └─ Key Elements Extracted: [elements]

ZOOM ANALYSIS RESULTS:
├─ Total Regions Analyzed: [number]
├─ Text Clarity Improvement: [percentage or qualitative assessment]
├─ Additional Details Discovered: [list any new information found through zoom]
├─ Transition Labels Enhanced: [number of transitions with improved text extraction]
```

### Section 2: Enhanced State Machine Structure
```
=== STATE MACHINE STRUCTURE ===

OVERALL FLOW ARCHITECTURE:
├─ Total States: [number] (STATUS nodes only)
├─ Total Transitions: [number] (arrows between states including bidirectional)
├─ Decision Points: [number] (diamond shapes)
├─ Delay Processes: [number] (timing elements)
├─ Flow Complexity: [Simple/Medium/Complex] - [reasoning]
├─ Transition Density: [Low/Medium/High] - [transitions per state ratio]
├─ Bidirectional Connections: [number] (states with arrows in both directions)

STATE INVENTORY WITH TRANSITION DETAILS:
├─ STATUS 0: Position: [top/center/bottom/left/right]
│  ├─ Visual Description: [shape, size, color, border style]
│  ├─ Internal Text: "[exact text from bubble, preserving line breaks]"
│  ├─ Incoming Transitions: [number] 
│  │  ├─ From STATUS [X]: [arrow description, condition summary]
│  │  ├─ From STATUS [Y]: [arrow description, condition summary]
│  │  └─ From Decision [Z]: [arrow description, condition summary]
│  ├─ Outgoing Transitions: [number]
│  │  ├─ To STATUS [A]: [arrow description, condition summary]
│  │  ├─ To STATUS [B]: [arrow description, condition summary]
│  │  └─ To Decision [C]: [arrow description, condition summary]
│  ├─ Connection Complexity: [Simple/Medium/Complex]
│  └─ Transition Intersection Point: [Yes/No - if multiple arrows converge here]

TRANSITION FLOW PATTERNS:
├─ Simple Transitions: [number] (single condition, straight arrow)
├─ Complex Transitions: [number] (multiple conditions with AND/OR logic)
├─ OR Logic Transitions: [number] (alternative paths with OR conditions)
├─ Bidirectional Flows: [number] (arrows in both directions between state pairs)
├─ Conditional Delays: [number] (transitions with RearDelay timing)
├─ Multi-Segment Arrows: [number] (arrows with curves or multiple segments)
├─ Parallel Transition Paths: [number] (multiple arrows between same states)

FLOW PATTERNS IDENTIFIED:
├─ Entry Points: [states with no incoming transitions]
├─ Exit Points: [states with no outgoing transitions or return to entry]
├─ Loop Structures: [circular flow patterns with specific state sequences]
├─ Parallel Branches: [states that can transition to multiple destinations]
├─ Decision Trees: [branching decision structures with TRUE/FALSE paths]
├─ Convergence Points: [states where multiple transition paths merge]
```

### Section 3: Detailed Transition Mapping (NEW ENHANCED SECTION)
```
=== DETAILED TRANSITION MAPPING ===

### TRANSITION PATH VISUALIZATION

**COMPLETE TRANSITION INVENTORY:**

**TRANSITION 1: STATUS 0 → [Destination]**
├─ Source State: STATUS 0 (position: [location])
├─ Destination: [STATUS X / Decision Diamond / Delay Process]
├─ Arrow Visual Path:
│  ├─ Starting Point: [exact position on source state boundary]
│  ├─ Path Description: [straight line / curved path / multi-segment]
│  ├─ Path Segments: [if multi-segment, describe each segment]
│  ├─ Ending Point: [exact position on destination boundary]
│  └─ Arrow Style: [solid/dashed/bold, head style, color if visible]
├─ Condition Label Position: [above/below/alongside arrow]
├─ Condition Text Extraction:
│  ├─ Zoom Analysis Applied: [Yes/No]
│  ├─ Text Clarity: [Excellent/Good/Fair/Poor]
│  ├─ Complete Condition Text:
│  │  ├─ Line 1: "[exact text preserving capitalization and symbols]"
│  │  ├─ Line 2: "[if multi-line condition]"
│  │  └─ Line N: "[all condition lines]"
│  └─ Text Enhancement Notes: [any improvements from zoom analysis]
├─ Logic Structure Analysis:
│  ├─ Condition Type: [Simple/Complex/OR Logic/AND Logic]
│  ├─ Boolean Operators: [AND, OR, NOT locations]
│  ├─ Comparison Operators: [==, ≤, >, <, !=, etc.]
│  ├─ Variable References: [all signal names mentioned]
│  └─ Constant Values: [all literal values, quoted strings]
├─ Timing Elements:
│  ├─ Delay Specification: "[RearDelay = X sec or null]"
│  ├─ Timing Conditions: [any time-based conditions]
│  └─ Speed Dependencies: [any velocity-related conditions]
├─ Automotive Context:
│  ├─ CAN Signals Referenced: [all automotive signals]
│  ├─ System States: [gear positions, button states, etc.]
│  └─ Safety Conditions: [any safety-related logic]

**TRANSITION 2: [Continue for all transitions...]**

### TRANSITION INTERSECTION ANALYSIS

**CONVERGENCE POINTS:**
├─ Intersection 1: [State/Decision where multiple arrows converge]
│  ├─ Incoming Arrows: [number and sources]
│  ├─ Arrow Overlap: [description of how arrows approach the intersection]
│  ├─ Condition Conflicts: [any conflicting conditions that need resolution]
│  ├─ Priority Logic: [if multiple conditions can be true simultaneously]
│  └─ Visual Clarity: [how well the intersection is drawn]

**BIDIRECTIONAL FLOW ANALYSIS:**
├─ Bidirectional Pair 1: STATUS X ↔ STATUS Y
│  ├─ Forward Transition: [condition for X→Y]
│  ├─ Reverse Transition: [condition for Y→X]
│  ├─ Mutual Exclusion: [are conditions mutually exclusive?]
│  ├─ Oscillation Risk: [potential for rapid switching]
│  └─ Automotive Logic: [why bidirectional flow exists]

### TRANSITION FREQUENCY MATRIX

**State Connection Matrix:**
| From\To | STATUS_0 | STATUS_1 | STATUS_2 | STATUS_3 | STATUS_4 | Decision_1 | Delay_1 |
|---------|----------|----------|----------|----------|----------|------------|---------|
| STATUS_0 | - | 1 | 0 | 0 | 0 | 1 | 0 |
| STATUS_1 | 1 | - | 1 | 0 | 1 | 0 | 0 |
| STATUS_2 | 0 | 1 | - | 1 | 0 | 0 | 0 |
| STATUS_3 | 0 | 0 | 1 | - | 0 | 0 | 0 |
| STATUS_4 | 0 | 1 | 0 | 0 | - | 0 | 0 |

**Transition Complexity Distribution:**
| Complexity_Level | Count | Percentage | Examples |
|------------------|-------|------------|----------|
| Simple (1 condition) | [X] | [Y%] | [list examples] |
| Medium (2-3 conditions) | [X] | [Y%] | [list examples] |
| Complex (4+ conditions or OR logic) | [X] | [Y%] | [list examples] |
```

### Section 4: Enhanced State Definitions
```
=== STATE DEFINITIONS ===

### COMPLETE STATE CATALOG WITH TRANSITION DETAILS

**STATUS 0:**
├─ Name: "STATUS 0"
├─ Position: [visual position in diagram with coordinates if possible]
├─ Description: "[complete text from state bubble, exactly as written]"
├─ System Function: [inferred automotive function]
├─ Active Conditions: [any conditions that must be true in this state]
├─ Sensor States: [any sensor readings mentioned in state description]
├─ Output Actions: [any outputs or actions performed in this state]
├─ INCOMING TRANSITION DETAILS:
│  ├─ Total Incoming: [number]
│  ├─ Transition 1: From [SOURCE] via "[condition summary]"
│  │  ├─ Full Condition: "[complete condition text]"
│  │  ├─ Trigger Type: [event/continuous/timed]
│  │  └─ Automotive Context: [what causes this transition]
│  ├─ Transition 2: From [SOURCE] via "[condition summary]"
│  └─ Incoming Priority: [if multiple transitions possible, which takes precedence]
├─ OUTGOING TRANSITION DETAILS:
│  ├─ Total Outgoing: [number]
│  ├─ Transition 1: To [DESTINATION] via "[condition summary]"
│  │  ├─ Full Condition: "[complete condition text]"
│  │  ├─ Trigger Type: [event/continuous/timed]
│  │  └─ Automotive Context: [what causes this transition]
│  ├─ Transition 2: To [DESTINATION] via "[condition summary]"
│  └─ Outgoing Logic: [mutually exclusive/parallel/conditional]
├─ State Connectivity Analysis:
│  ├─ Connection Degree: [total incoming + outgoing]
│  ├─ Hub Classification: [Entry/Process/Decision/Exit/Hub]
│  ├─ Critical Path: [Yes/No - is this state on critical system path]
│  └─ Isolation Risk: [can this state become unreachable]

### ENHANCED STATE RELATIONSHIP MATRIX

**Detailed State Connectivity:**
| State | Incoming_From | Incoming_Conditions | Outgoing_To | Outgoing_Conditions | Total_Connections | Hub_Type |
|-------|---------------|-------------------|-------------|-------------------|-------------------|----------|
| STATUS 0 | [sources] | [condition summaries] | [destinations] | [condition summaries] | [number] | [type] |
| STATUS 1 | [sources] | [condition summaries] | [destinations] | [condition summaries] | [number] | [type] |

**State Transition Dependencies:**
| State_Name | Prerequisites | Enables_Transitions_To | Blocks_Transitions_To | Timing_Constraints |
|------------|---------------|----------------------|---------------------|-------------------|
| STATUS 0 | [what must be true to enter] | [states reachable from here] | [states blocked from here] | [timing limits] |
| STATUS 1 | [prerequisites] | [enables] | [blocks] | [timing] |
```

### Section 5: Enhanced Transition Analysis
```
=== TRANSITION ANALYSIS ===

### COMPLETE TRANSITION CATALOG WITH PATH DETAILS

**TRANSITION 1: STATUS 0 → [Destination]**
├─ Arrow Direction: [↑↓←→ or descriptive with angle if curved]
├─ Visual Path Analysis:
│  ├─ Path Type: [straight/curved/multi-segment/L-shaped/S-curved]
│  ├─ Path Length: [short/medium/long relative to diagram]
│  ├─ Curvature Details: [if curved, describe arc direction and degree]
│  ├─ Intersection Points: [any points where arrow crosses other elements]
│  └─ Visual Clarity: [how clearly the arrow path can be traced]
├─ Condition Type: [Simple/Complex/OR Logic/AND Logic]
├─ Complete Condition Text:
│  ├─ Zoom Analysis Applied: [Yes/No - was zoom needed for text extraction]
│  ├─ Text Position: [above/below/alongside/embedded in arrow]
│  ├─ Line 1: "[exact text from arrow, preserving capitalization]"
│  ├─ Line 2: "[exact text if multi-line]"
│  ├─ Line N: "[all condition lines]"
│  └─ Text Enhancement: [improvements from zoom analysis]
├─ Logic Structure:
│  ├─ AND Conditions: [list all AND terms]
│  ├─ OR Alternatives: [list all OR branches]
│  ├─ Comparison Operators: [==, ≤, >, <, !=, etc.]
│  ├─ Boolean Values: [True/False/'Pressed'/etc.]
│  └─ State Transitions: [from 'X' to 'Y' notation]
├─ Timing Elements:
│  ├─ Delay Specification: "[RearDelay = X sec or null]"
│  ├─ Timing Conditions: [any time-based conditions]
│  └─ Speed Dependencies: [velocity-related conditions]
├─ CAN Signals Referenced: [any automotive signals mentioned]
├─ Automotive Context: [system behavior this transition represents]

**TRANSITION 2: [Continue for all transitions...]**

### COMPLEX CONDITION ANALYSIS

**Multi-Line Condition Example (with Zoom Enhancement):**
```
Original Arrow Text (before zoom):
"[partially visible text]"
"OR"
"[unclear condition]"

After Zoom Analysis:
"NPS_FrontButtonSts == 'Pressed'"
"Stop_GoEnable == 'False' from 'True'"
"OR"
"Stop_GoEnable == 'True' AND VehicleSpeed goes below 10km/h"
"OR"
"VehicleSpeed ≤ 10 km/h AND Stop_GoEnable == 'True' from 'False'"

Parsed Logic Structure:
Alternative 1 (AND Logic):
  - NPS_FrontButtonSts == 'Pressed'
  - Stop_GoEnable == 'False' from 'True'
Alternative 2 (AND Logic):
  - Stop_GoEnable == 'True' 
  - VehicleSpeed goes below 10km/h
Alternative 3 (AND Logic):
  - VehicleSpeed ≤ 10 km/h
  - Stop_GoEnable == 'True' from 'False'
```

### TRANSITION PATH TRACING RESULTS

**Path Tracing Summary:**
| Transition | Path_Complexity | Zoom_Required | Text_Quality | Logic_Complexity | CAN_Signals_Count |
|------------|-----------------|---------------|--------------|------------------|-------------------|
| 0→1 | Simple | No | Excellent | Simple | 1 |
| 1→4 | Complex | Yes | Good | Complex_OR | 3 |
| 4→1 | Simple | No | Good | Simple | 1 |
| 1→2 | Simple | No | Excellent | Simple | 1 |
| 2→1 | Simple | No | Excellent | Simple | 1 |
| 2→3 | Simple | No | Good | Simple | 1 |
| 3→2 | Simple | No | Good | Simple | 1 |

**Zoom Analysis Impact:**
├─ Transitions Enhanced by Zoom: [number]
├─ Text Clarity Improvements: [list specific improvements]
├─ Previously Missed Conditions: [any conditions discovered through zoom]
├─ Logic Structure Corrections: [any corrections made after zoom analysis]
```

### Section 6: Transition Intersection Analysis (NEW SECTION)
```
=== TRANSITION INTERSECTION ANALYSIS ===

### CONVERGENCE POINT ANALYSIS

**INTERSECTION 1: [State/Decision where multiple arrows converge]**
├─ Location: [position in diagram]
├─ Incoming Arrows: [number] from [list sources]
├─ Arrow Approach Analysis:
│  ├─ Arrow 1: From [SOURCE] - [approach angle/direction]
│  ├─ Arrow 2: From [SOURCE] - [approach angle/direction]
│  └─ Arrow N: From [SOURCE] - [approach angle/direction]
├─ Visual Intersection Quality:
│  ├─ Clarity: [Excellent/Good/Fair/Poor]
│  ├─ Overlap Issues: [any arrows that overlap or cross confusingly]
│  ├─ Label Conflicts: [any condition labels that interfere with each other]
│  └─ Zoom Analysis Applied: [Yes/No]
├─ Condition Logic Analysis:
│  ├─ Simultaneous Conditions: [can multiple conditions be true at once]
│  ├─ Priority Resolution: [how conflicts are resolved]
│  ├─ Mutual Exclusion: [are conditions mutually exclusive]
│  └─ Race Conditions: [potential for timing-dependent behavior]
├─ Automotive System Impact:
│  ├─ System Behavior: [what happens when multiple transitions are possible]
│  ├─ Safety Implications: [any safety-critical aspects]
│  └─ Performance Impact: [effect on system response time]

### BIDIRECTIONAL FLOW ANALYSIS

**BIDIRECTIONAL PAIR 1: STATUS X ↔ STATUS Y**
├─ Forward Transition (X→Y):
│  ├─ Condition: "[complete condition text]"
│  ├─ Trigger Type: [event/continuous/timed]
│  ├─ CAN Signals: [signals involved]
│  └─ Automotive Context: [system behavior]
├─ Reverse Transition (Y→X):
│  ├─ Condition: "[complete condition text]"
│  ├─ Trigger Type: [event/continuous/timed]
│  ├─ CAN Signals: [signals involved]
│  └─ Automotive Context: [system behavior]
├─ Relationship Analysis:
│  ├─ Mutual Exclusion: [Yes/No - are conditions mutually exclusive]
│  ├─ Oscillation Risk: [Low/Medium/High - potential for rapid switching]
│  ├─ Hysteresis: [any built-in delay or threshold differences]
│  └─ Stability Analysis: [system stability implications]
├─ Visual Path Analysis:
│  ├─ Arrow Separation: [how well separated are the bidirectional arrows]
│  ├─ Path Clarity: [can both directions be clearly traced]
│  └─ Label Positioning: [how condition labels are positioned to avoid confusion]

### PARALLEL TRANSITION ANALYSIS

**PARALLEL PATHS: [if multiple arrows exist between same states]**
├─ Path 1: [condition and context]
├─ Path 2: [condition and context]
├─ Relationship: [alternative conditions / parallel processing / error paths]
├─ Priority: [which path takes precedence if both conditions are true]
└─ Automotive Logic: [why multiple paths exist between these states]
```

### Section 7: Decision Points & Delay Processes (Enhanced)
```
=== DECISION POINTS & DELAY PROCESSES ===

### DECISION DIAMONDS (Enhanced Analysis)

**DECISION 1:**
├─ Name: "[exact text from diamond]"
├─ Position: [location in flow with coordinates if possible]
├─ Visual Analysis:
│  ├─ Shape Quality: [clear diamond/distorted/other shape]
│  ├─ Size: [relative to other elements]
│  ├─ Text Clarity: [readability of internal text]
│  └─ Zoom Analysis Applied: [Yes/No]
├─ Input Analysis:
│  ├─ Input From: [source state or transition]
│  ├─ Input Condition: "[condition that leads to this decision]"
│  ├─ Input Arrow Path: [description of incoming arrow]
│  └─ Input Timing: [any timing constraints on reaching decision]
├─ Output Analysis:
│  ├─ TRUE Path: [where TRUE arrow leads]
│  │  ├─ TRUE Condition: "[what TRUE represents]"
│  │  ├─ TRUE Arrow Path: [visual description]
│  │  └─ TRUE Destination: [target state/process]
│  ├─ FALSE Path: [where FALSE arrow leads]
│  │  ├─ FALSE Condition: "[what FALSE represents]"
│  │  ├─ FALSE Arrow Path: [visual description]
│  │  └─ FALSE Destination: [target state/process]
│  └─ Path Clarity: [how clearly TRUE/FALSE paths are marked]
├─ Decision Logic: "[exact condition being evaluated]"
├─ Automotive Context: [what system decision this represents]
├─ Timing Implications: [any timing effects of the decision]
└─ Safety Considerations: [any safety-critical aspects]

### DELAY PROCESSES (Enhanced Analysis)

**DELAY 1:**
├─ Name: "[exact text from delay box, e.g., 'RearDelay = 1 sec']"
├─ Position: [location in flow with coordinates if possible]
├─ Visual Analysis:
│  ├─ Shape: [rectangle/oval/other shape used for delay]
│  ├─ Size: [relative to other elements]
│  ├─ Text Clarity: [readability of delay specification]
│  └─ Zoom Analysis Applied: [Yes/No]
├─ Input Analysis:
│  ├─ Input From: [source state]
│  ├─ Input Condition: "[condition that triggers delay]"
│  ├─ Input Arrow Path: [description of incoming arrow]
│  └─ Input Timing: [when delay process is triggered]
├─ Output Analysis:
│  ├─ Output To: [destination state]
│  ├─ Output Condition: "[condition for exiting delay]"
│  ├─ Output Arrow Path: [description of outgoing arrow]
│  └─ Output Timing: [when delay process completes]
├─ Delay Specification:
│  ├─ Delay Value: [exact delay time]
│  ├─ Units: [seconds/milliseconds/etc.]
│  ├─ Delay Type: [fixed/variable/conditional]
│  └─ Precision: [how precisely the delay is specified]
├─ Bidirectional Analysis:
│  ├─ Bidirectional: [Yes/No - can flow both ways]
│  ├─ Reverse Path: [if bidirectional, describe reverse flow]
│  └─ Reverse Timing: [timing for reverse direction]
├─ Trigger Conditions: [what triggers the delay]
├─ Automotive Purpose: [why this delay exists in the system]
├─ System Impact: [effect on overall system timing]
└─ Safety Implications: [any safety-related aspects of the delay]

### ENHANCED TIMING ANALYSIS

**System Timing Requirements:**
| Element | Delay_Value | Units | Trigger_Condition | Completion_Condition | Purpose | Safety_Critical |
|---------|-------------|-------|-------------------|---------------------|---------|-----------------|
| RearDelay | 0 | sec | Stop_GoEnable=TRUE | VehicleSpeed≤10km/h | Immediate activation | No |
| RearDelay | 1 | sec | Reverse gear transitions | Gear position stable | Debounce switching | Yes |

**Critical Timing Paths (Enhanced):**
├─ Path 1: STATUS 0 → Decision → RearDelay(0s) → STATUS 1
│  ├─ Total Time: ~0 seconds (immediate)
│  ├─ Bottlenecks: Speed condition check
│  ├─ Variability: Depends on vehicle speed
│  └─ Safety Impact: None
├─ Path 2: STATUS 2 ↔ STATUS 3 via RearDelay(1s)
│  ├─ Total Time: 1 second (fixed)
│  ├─ Bottlenecks: Delay process
│  ├─ Variability: Fixed timing
│  └─ Safety Impact: Prevents rapid sensor switching
├─ Maximum Response Time: 1 second (worst case via RearDelay)
├─ Minimum Response Time: <0.1 seconds (direct transitions)
├─ Average Response Time: [calculated based on typical usage patterns]
└─ Timing Constraints: [any hard real-time requirements]
```

### Section 8: Complete State Machine Logic (Enhanced)
```
=== COMPLETE STATE MACHINE LOGIC ===

### ENHANCED BEHAVIORAL MODEL SUMMARY

**System Operation Overview:**
The process flow implements [describe overall system behavior] with [number] operational states, [number] decision points, and [number] delay processes. The system responds to [list key inputs] including CAN signals [list signals] and produces [list key outputs] with timing constraints ranging from [min time] to [max time]. Enhanced transition analysis reveals [key insights from detailed analysis].

**State Machine Rules (Enhanced):**
1. Entry Conditions: [how system enters initial state with specific conditions]
2. Normal Operation: [typical state transitions with transition frequencies]
3. Error Handling: [how system handles error conditions and recovery paths]
4. Exit Conditions: [how system exits or shuts down with safety considerations]
5. Safety Interlocks: [any safety-related state restrictions with timing requirements]
6. Transition Priorities: [how conflicting transitions are resolved]
7. Timing Constraints: [all timing requirements and their enforcement]

### ENHANCED TRANSITION TABLE

**Complete State Transition Matrix (with Enhanced Details):**
| Current_State | Input_Condition_1 | Logic | Input_Condition_2 | Logic | Input_Condition_N | Next_State | Delay | Action | Priority | Safety |
|---------------|-------------------|-------|-------------------|-------|-------------------|------------|-------|--------|----------|--------|
| STATUS 0 | Key_On | - | - | - | - | Stop_GoEnable | 0 sec | System Activation | High | Critical |
| Stop_GoEnable | Stop_GoEnable=TRUE | - | - | - | - | RearDelay(0s) | 0 sec | Delay Path | Medium | Normal |
| Stop_GoEnable | Stop_GoEnable=FALSE | - | - | - | - | STATUS 1 | 0 sec | Direct Path | Medium | Normal |
| RearDelay(0s) | VehicleSpeed≤10km/h | - | - | - | - | STATUS 1 | 0 sec | Speed Check | High | Critical |

### ENHANCED AUTOMOTIVE SYSTEM INTEGRATION

**CAN Signal Dependencies (Enhanced):**
| Signal_Name | Signal_Type | Possible_Values | Update_Rate | Used_In_States | Used_In_Transitions | Transition_Impact | Safety_Level |
|-------------|-------------|-----------------|-------------|----------------|-------------------|-------------------|--------------|
| Stop_GoEnable | Boolean | True/False | 100ms | [states] | [transitions] | Critical | High |
| VehicleSpeed | Numeric | 0-300 km/h | 50ms | [states] | [transitions] | Critical | High |
| NPS_FrontButtonSts | Enumerated | Pressed/Released | Event | [states] | [transitions] | Trigger | Medium |
| Key_On | Boolean | True/False | Event | [states] | [transitions] | Trigger | High |
| Gear_Position | Enumerated | P/R/N/D | 100ms | [states] | [transitions] | Condition | High |

**System Requirements Traceability (Enhanced):**
| Requirement_ID | Description | Implementing_States | Implementing_Transitions | Verification_Method | Safety_Classification |
|---------------|-------------|-------------------|------------------------|-------------------|---------------------|
| REQ-001 | [requirement] | [states] | [transitions] | [method] | [classification] |
| REQ-002 | [requirement] | [states] | [transitions] | [method] | [classification] |
| REQ-003 | [requirement] | [states] | [transitions] | [method] | [classification] |

**Transition Dependency Graph:**
├─ Critical Path: STATUS 0 → STATUS 1 → STATUS 2 → STATUS 3
├─ Alternative Paths: [list alternative paths]
├─ Error Recovery Paths: [list error recovery paths]
├─ Safety-Critical Transitions: [list safety-critical transitions]
└─ Performance-Critical Transitions: [list performance-critical transitions]
```

### Section 9: CSV Format Ready Data (Enhanced)
```
=== CSV FORMAT READY DATA ===

STATES.csv:
State_Name,Position,Description,System_Function,Incoming_Count,Outgoing_Count,Hub_Type,Critical_Path
STATUS 0,top-left,"[exact internal text]",Initial State,0,2,Entry,Yes
STATUS 1,center,"[exact internal text]",Active State,2,1,Process,Yes
STATUS 2,bottom-right,"[exact internal text]",Final State,1,0,Exit,Yes

TRANSITIONS.csv:
From_State,To_State,Direction,Condition_Text,Logic_Type,Delay_Sec,CAN_Signals,Path_Type,Zoom_Required
STATUS 0,STATUS 1,rightward,"Key_On AND Stop_GoEnable=FALSE",AND,0,"Key_On,Stop_GoEnable",straight,No
STATUS 1,STATUS 0,leftward,"Button='Pressed' OR Speed≤10km/h",OR,1,"NPS_FrontButtonSts,VehicleSpeed",curved,Yes

DECISION_POINTS.csv:
Decision_Name,Position,Input_From,True_Path,False_Path,Decision_Logic,Safety_Critical
Speed Check,center-top,STATUS 1,STATUS 2,STATUS 0,"VehicleSpeed > 50km/h",Yes

DELAY_PROCESSES.csv:
Delay_Name,Position,Input_From,Output_To,Delay_Value,Units,Bidirectional,Purpose
RearDelay,bottom-center,STATUS 1,STATUS 0,1,sec,No,Debounce
FrontDelay,top-center,STATUS 0,STATUS 1,0.5,sec,Yes,Stabilization

ZOOM_REGIONS.csv:
Region_ID,Position,Content_Type,Elements_Enhanced,Text_Quality_Before,Text_Quality_After
Region1,top-right,Dense transition text,"Transition 1→2,Transition 2→3",Poor,Good
Region2,bottom-left,Multiple arrow convergence,"Transition 3→1,Transition 4→1",Fair,Excellent

TRANSITION_INTERSECTIONS.csv:
Intersection_ID,Position,Incoming_Arrows,Outgoing_Arrows,Conflict_Resolution,Safety_Critical
Intersection1,center-left,3,1,Priority-based,Yes
Intersection2,bottom-right,2,2,Mutually exclusive,No
```

### Section 10: Validation Checklist (NEW SECTION)
```
=== VALIDATION CHECKLIST ===

### TRANSITION ANALYSIS COMPLETENESS

**Transition Validation:**
- [ ] All states have been identified and documented
- [ ] All transitions between states have been traced and documented
- [ ] All transition conditions have been extracted with exact text
- [ ] All transition paths have been visually traced and described
- [ ] All complex regions have been analyzed with zoom enhancement
- [ ] All bidirectional flows have been identified and analyzed
- [ ] All transition intersections have been analyzed for conflicts
- [ ] All decision points have TRUE/FALSE paths documented
- [ ] All delay processes have timing specifications documented
- [ ] All CAN signals referenced in transitions have been cataloged

**Zoom Analysis Validation:**
- [ ] Complex regions requiring zoom have been identified
- [ ] Zoom analysis has been applied to all complex regions
- [ ] Text extraction quality has been improved through zoom
- [ ] Previously unclear condition text has been clarified
- [ ] Transition path details have been enhanced through zoom
- [ ] Intersection points have been clarified through zoom
- [ ] State internal text has been verified through zoom where needed

**Automotive Context Validation:**
- [ ] All CAN signals have been identified and documented
- [ ] All timing requirements have been extracted and analyzed
- [ ] All safety-critical transitions have been identified
- [ ] All system requirements have been traced to states/transitions
- [ ] All error handling paths have been documented
- [ ] All performance-critical paths have been identified
- [ ] All state machine rules have been documented
```

## CRITICAL ANALYSIS REQUIREMENTS

### Text Extraction Precision:
- **EXACT TEXT PRESERVATION**: Capture all condition text exactly as written, including spacing, capitalization, and symbols
- **MULTI-LINE CONDITIONS**: Many arrows contain multiple lines of condition text that must ALL be captured
- **COMPARISON OPERATORS**: Include all operators (==, ≤, >, <, !=) exactly as shown
- **QUOTED STRINGS**: Preserve exact quotation marks and string values

### Arrow Direction Analysis:
- **CAREFUL EXAMINATION**: Examine arrow starting points, paths, and ending points
- **PATH TRACING**: Trace each arrow from source to destination, noting any curves or segments
- **INTERSECTION ANALYSIS**: Pay special attention to points where multiple arrows converge
- **BIDIRECTIONAL FLOWS**: Identify and analyze cases where arrows flow in both directions between states

### Zoom Analysis Requirements:
- **REGION IDENTIFICATION**: Identify regions with dense text or overlapping arrows that require zoom
- **TEXT ENHANCEMENT**: Use zoom to improve text extraction quality for complex conditions
- **INTERSECTION CLARITY**: Use zoom to clarify arrow paths at intersection points
- **CONDITION VERIFICATION**: Use zoom to verify multi-line conditions and complex logic

### Transition Mapping Focus:
- **COMPLETE PATH TRACING**: Document the exact visual path of each transition arrow
- **INCOMING TRANSITION DETAILS**: For each state, document all incoming transitions with sources
- **OUTGOING TRANSITION DETAILS**: For each state, document all outgoing transitions with destinations
- **INTERSECTION ANALYSIS**: Analyze points where multiple transitions converge for conflicts
- **BIDIRECTIONAL ANALYSIS**: Analyze state pairs with transitions in both directions

### Automotive System Integration:
- **CAN SIGNAL MAPPING**: Map all CAN signals to the transitions that reference them
- **TIMING REQUIREMENTS**: Document all timing constraints and delay specifications
- **SAFETY ANALYSIS**: Identify safety-critical transitions and states
- **REQUIREMENT TRACEABILITY**: Map system requirements to implementing states and transitions
