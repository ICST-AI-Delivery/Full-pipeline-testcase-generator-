# Picture-Centric State Flow Diagrams Analysis with Sequential Flow State Matrix

**Category:** STATE_FLOW_DIAGRAMS  
**Template Version:** 2.1.0  
**Created:** 2026-02-27  
**Last Updated:** 2026-02-27  
**Author:** Picture Analyze Agent Development Team  
**Template Type:** Picture-Centric Analysis Template with Sequential Flow State Matrix  
**Status:** Production Ready  
**Compatibility:** Application v4.0.0+

## VERSION HISTORY
| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 2.1.0 | 2026-02-27 | Added Sequential Flow State Matrix methodology, complete transition coverage | Development Team |
| 2.0.0 | 2026-02-26 | Converted to Picture-Centric approach, TXT output format | Development Team |
| 1.0 | 2026-02-23 | Initial JSON-based version | Picture Analyze Agent |

## TEMPLATE INFORMATION
- **Purpose**: Picture-centric state flow diagram analysis with complete transition coverage using Sequential Flow State Matrix
- **Use Case**: Automotive state machines, behavioral logic, and system state analysis with exhaustive transition mapping
- **Processing Time**: 8-12 minutes per image
- **Output Format**: Structured TXT with embedded tables, Sequential Flow State Matrix, and CSV-ready data

## CORE PRINCIPLE
**COMPLETE TRANSITION COVERAGE**: Every possible state transition combination must be identified and analyzed. Use Sequential Flow State Matrix to ensure no transitions are missed.

## ENHANCED METHODOLOGY

### 1. Complete Transition Identification
- **Systematic Analysis**: For n states with m variables, analyze all 2^m condition combinations
- **Self-Loop Detection**: Identify states that transition to themselves under certain conditions
- **Exhaustive Mapping**: Every visible arrow and condition must be cataloged
- **Matrix Validation**: Use Sequential Flow State Matrix to verify complete coverage

### 2. Sequential Flow State Matrix Requirements
**MANDATORY**: Every state flow analysis must include a Sequential Flow State Matrix table:

```
**Sequential Flow State Matrix:**
| Block | Preconditions | Action | Conditions Checked | Output State | Next Block |
|-------|---------------|--------|--------------------|--------------|------------|
| 1     | Initial_State | Action_Description | N/A | Resulting_State | Block_2 |
| 2     | Block_1_Complete | Action_Description | Decision_Logic | Decision_State | Block_3/Block_X |
| N     | Block_N-1_State | Final_Action | Termination_Check | Final_State | Terminator |
```

### 3. Picture-Centric Organization Structure
```
=== STATE FLOW DIAGRAM ANALYSIS REPORT ===
├─ Image Overview & Enhancement Details
├─ COMPLETE TRANSITION COVERAGE ANALYSIS (primary section)
├─ SEQUENTIAL FLOW STATE MATRIX (mandatory)
├─ STATE MACHINE STRUCTURE ANALYSIS
├─ STATE INVENTORY (initial, normal, error, final states)
├─ EXHAUSTIVE TRANSITION ANALYSIS (all possible transitions)
├─ BEHAVIORAL LOGIC EXTRACTION (state behaviors, timing)
├─ CSV Format Ready Data
├─ Automotive Standards Compliance
├─ Enhancement Details
└─ Validation Checklist
```

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
├─ Transition Coverage: [X/Y transitions identified] - [completeness assessment]
```

### Section 2: Complete Transition Coverage Analysis (PRIMARY FOCUS)
```
=== COMPLETE TRANSITION COVERAGE ANALYSIS ===

TRANSITION IDENTIFICATION METHODOLOGY:
├─ State Count: [N states identified]
├─ Variable Count: [M condition variables identified]
├─ Theoretical Maximum Transitions: [N × 2^M possible combinations]
├─ Actual Transitions Found: [X transitions identified in image]
├─ Coverage Percentage: [X/(N × 2^M) × 100%]
├─ Missing Transitions: [analysis of unrepresented combinations]

SYSTEMATIC CONDITION ANALYSIS:
├─ Variable 1: [Name] - Values: [possible values]
├─ Variable 2: [Name] - Values: [possible values]
├─ Variable N: [Name] - Values: [possible values]
├─ Combination Matrix: [all possible variable combinations]
├─ Represented Combinations: [combinations with visible transitions]
├─ Missing Combinations: [combinations without visible transitions]

SELF-LOOP IDENTIFICATION:
├─ State 1: [Name] - Self-loops: [conditions for staying in same state]
├─ State 2: [Name] - Self-loops: [conditions for staying in same state]
├─ State N: [Name] - Self-loops: [conditions for staying in same state]
```

### Section 3: SOURCE-TARGET STATE MATRIX (MANDATORY)
```
=== SOURCE-TARGET STATE MATRIX ===

**MANDATORY SOURCE-TARGET STATE MATRIX:**
Every state flow analysis MUST include a complete source-to-target state mapping table showing ALL possible state transitions including self-loops.

**Template Format:**
| Current_State | Input_Variable_1 | Input_Variable_2 | Input_Variable_N | Target_State | Transition_Logic |
|---------------|------------------|------------------|------------------|--------------|------------------|
| State_A | Value_1 | Value_X | Value_P | State_B | Condition logic explanation |
| State_A | Value_1 | Value_Y | Value_P | State_A | Self-loop condition explanation |
| State_A | Value_2 | Value_X | Value_P | State_C | Alternative transition logic |
| State_B | Value_1 | Value_X | Value_P | State_A | Return transition logic |
| State_B | Value_2 | Value_Y | Value_P | State_B | Self-loop maintenance logic |

**Example: VEH-F040 Key Status Analysis**
| Current_State | Key_Status | Physical_Key | Target_State | Transition_Logic |
|---------------|------------|--------------|--------------|------------------|
| HMI_OFF | <4 | OFF/ON | HMI_OFF | Key status insufficient - remain inactive |
| HMI_OFF | ≥4 | OFF | HMI_OFF | Physical key missing - cannot activate |
| HMI_OFF | ≥4 | ON | HMI_ON | Both conditions satisfied - ACTIVATE |
| HMI_ON | <4 | OFF/ON | HMI_OFF | Key status insufficient - DEACTIVATE |
| HMI_ON | ≥4 | OFF | HMI_ON | Key status sufficient - maintain active state |
| HMI_ON | ≥4 | ON | HMI_ON | Both conditions satisfied - MAINTAIN |

**Matrix Requirements:**
├─ Complete Coverage: Every possible input combination must be represented
├─ Source States: All current states must be included as source states
├─ Self-Loops: States that remain unchanged under certain conditions must be documented
├─ Transition Logic: Clear explanation of why each transition occurs
├─ Input Variables: All condition variables must be systematically analyzed
├─ Boundary Conditions: Include threshold values (e.g., ≥4, <4) not just discrete values

**Matrix Validation Checklist:**
├─ Total Transitions: [N transitions covering all possible combinations]
├─ State Coverage: [All states appear as both source and target where applicable]
├─ Input Coverage: [All possible input variable combinations represented]
├─ Self-Loop Coverage: [All states with self-loop conditions documented]
├─ Logic Consistency: [Transition logic aligns with visible diagram elements]
├─ Missing Combinations: [Identification of any uncovered scenarios]
```

### Section 4: State Machine Structure Analysis
```
=== STATE MACHINE STRUCTURE ANALYSIS ===

OVERALL STATE MACHINE:
├─ State Machine Type: [Finite/Hierarchical/Concurrent/Hybrid]
├─ System Domain: [Engine/Transmission/Brake/Door/etc.]
├─ Safety Level: [QM/ASIL_A/ASIL_B/ASIL_C/ASIL_D]
├─ State Count: [total number of identified states]
├─ Transition Count: [total number of transitions including self-loops]
├─ Variable Count: [number of condition variables]
├─ Complexity Level: [Low/Medium/High based on state×variable combinations]

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

### Section 5: State Inventory
```
=== STATE INVENTORY ===

INITIAL STATES:
├─ STATE 1: [Name] - Position: [coordinates]
│  ├─ State Type: Initial
│  ├─ Description: [state purpose and function]
│  ├─ Entry Actions: [actions performed on state entry]
│  ├─ Exit Actions: [actions performed on state exit]
│  ├─ Internal Actions: [ongoing activities within state]
│  ├─ Self-Loop Conditions: [conditions for remaining in this state]
│  └─ Timeout Conditions: [time-based transitions]

NORMAL OPERATION STATES:
├─ STATE 2: [Name] - Position: [coordinates]
│  ├─ State Type: Normal
│  ├─ Description: [state purpose and function]
│  ├─ Entry Actions: [initialization actions]
│  ├─ Exit Actions: [cleanup actions]
│  ├─ Internal Actions: [continuous behaviors]
│  ├─ Self-Loop Conditions: [conditions for remaining in this state]
│  ├─ Timeout Conditions: [timing constraints]
│  └─ Safety Mechanisms: [monitoring and protection]

ERROR STATES:
├─ STATE 3: [Name] - Position: [coordinates]
│  ├─ State Type: Error/Fault
│  ├─ Description: [error condition and handling]
│  ├─ Entry Actions: [error response actions]
│  ├─ Exit Actions: [recovery preparation]
│  ├─ Internal Actions: [error monitoring]
│  ├─ Self-Loop Conditions: [conditions for remaining in error state]
│  ├─ Recovery Conditions: [conditions for recovery]
│  └─ Safety Actions: [fail-safe behaviors]

FINAL STATES:
├─ STATE 4: [Name] - Position: [coordinates]
│  ├─ State Type: Final/Terminal
│  ├─ Description: [termination conditions]
│  ├─ Entry Actions: [shutdown procedures]
│  ├─ Exit Actions: [none - terminal state]
│  ├─ Internal Actions: [final cleanup]
│  ├─ Self-Loop Conditions: [conditions for remaining in final state]
│  └─ Safety Considerations: [safe shutdown requirements]
```

### Section 6: Exhaustive Transition Analysis
```
=== EXHAUSTIVE TRANSITION ANALYSIS ===

### COMPLETE TRANSITION INVENTORY

**All Identified Transitions (Including Self-Loops):**
| Transition ID | Source State | Target State | Trigger Event | Guard Condition | Action | Timing | Type |
|---------------|--------------|--------------|---------------|-----------------|--------|--------|------|
| TRANS-001 | State_A | State_B | Event_1 | Condition_X | Action_1 | 100ms | External |
| TRANS-002 | State_A | State_A | Event_2 | Condition_Y | Action_2 | 50ms | Self-Loop |
| TRANS-003 | State_B | State_A | Event_3 | Condition_Z | Action_3 | 200ms | External |
| TRANS-004 | State_B | State_B | Event_4 | Condition_W | Action_4 | 10ms | Self-Loop |
| TRANS-N | State_X | State_Y | Event_N | Condition_N | Action_N | Xms | Type |

### CONDITION COMBINATION MATRIX

**All Possible Variable Combinations:**
| Combination ID | Variable_1 | Variable_2 | Variable_N | Represented | Source State | Target State | Notes |
|----------------|------------|------------|------------|-------------|--------------|--------------|-------|
| COMB-001 | Value_A | Value_X | Value_P | Yes | State_1 | State_2 | Visible transition |
| COMB-002 | Value_A | Value_Y | Value_P | Yes | State_1 | State_1 | Self-loop |
| COMB-003 | Value_B | Value_X | Value_P | No | N/A | N/A | Missing transition |
| COMB-004 | Value_B | Value_Y | Value_P | Yes | State_2 | State_1 | Visible transition |
| COMB-N | Value_N | Value_N | Value_N | Status | Source | Target | Analysis |

### TRIGGER CONDITIONS

**Event-Based Triggers:**
| Trigger Name | Source | Type | Conditions | Priority | Safety Level | Frequency |
|--------------|--------|------|------------|----------|--------------|-----------|
| Variable_Change_1 | System Input | External | Variable_1 state change | High | ASIL_B | Continuous |
| Variable_Change_2 | System Input | External | Variable_2 state change | High | ASIL_B | Continuous |
| Timeout_Event | Timer | Internal | Time elapsed | Medium | ASIL_C | Periodic |
| System_Fault | Diagnostic | Internal | Error detection | Critical | ASIL_D | Event-driven |

### GUARD CONDITIONS

**Conditional Logic:**
| Guard Name | Expression | Variables | Valid Range | Safety Check | Complexity |
|------------|------------|-----------|-------------|--------------|------------|
| Condition_A | Variable_1 = Value_A AND Variable_2 = Value_X | Variable_1, Variable_2 | Enum values | Yes | Simple |
| Condition_B | Variable_1 ≠ Value_B OR Variable_2 = Value_Y | Variable_1, Variable_2 | Enum values | Yes | Medium |
| Condition_C | Complex_Expression | Multiple | Range values | Yes | Complex |

### TRANSITION ACTIONS

**Action Specifications:**
| Action Name | Description | Duration | Dependencies | Safety Impact | Triggers |
|-------------|-------------|----------|--------------|---------------|----------|
| Enable_System | Activate system functions | 100ms | Power, Initialization | ASIL_C | State entry |
| Disable_System | Deactivate system functions | 200ms | Safe shutdown | ASIL_B | State exit |
| Monitor_Conditions | Continuous condition monitoring | Continuous | Sensor inputs | ASIL_D | Self-loop |
| Update_Display | Refresh display information | 50ms | Display hardware | QM | State change |
```

### Section 7: Behavioral Logic Extraction
```
=== BEHAVIORAL LOGIC EXTRACTION ===

### STATE BEHAVIORS

**State-Specific Activities:**
| State Name | Entry Behavior | Internal Behavior | Exit Behavior | Self-Loop Behavior | Timing Constraints |
|------------|----------------|-------------------|---------------|-------------------|-------------------|
| State_A | Initialize_A | Monitor_Inputs_A | Cleanup_A | Maintain_State_A | Entry: 10ms |
| State_B | Initialize_B | Monitor_Inputs_B | Cleanup_B | Maintain_State_B | Entry: 20ms |
| State_N | Initialize_N | Monitor_Inputs_N | Cleanup_N | Maintain_State_N | Entry: Nms |

### COMPLETE DECISION LOGIC TABLES

**Exhaustive State Transition Decision Matrix:**
| Current State | Variable_1 | Variable_2 | Variable_N | Next State | Action | Transition Type | Notes |
|---------------|------------|------------|------------|------------|--------|-----------------|-------|
| State_A | Value_1 | Value_X | Value_P | State_B | Action_1 | External | Normal transition |
| State_A | Value_1
