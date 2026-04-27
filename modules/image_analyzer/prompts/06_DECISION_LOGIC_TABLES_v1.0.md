# Picture-Centric Decision Logic Tables Analysis

**Category:** DECISION_LOGIC_TABLES  
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
- **Purpose**: Picture-centric decision logic table analysis with practical TXT output
- **Use Case**: Automotive decision matrices, logic rules, and conditional behavior analysis
- **Processing Time**: 6-10 minutes per image
- **Output Format**: Structured TXT with embedded tables and CSV-ready data

## CORE PRINCIPLE
**PICTURE-FIRST ANALYSIS**: Focus on visual decision logic tables and conditional relationships actually present in the image. Extract practical decision rules for automotive development and testing.

## EXECUTION METHODOLOGY

### 1. Image Content Identification
- Identify decision table type (truth table, decision matrix, logic rules, conditional statements)
- Catalog all visible conditions, actions, and decision rules
- Determine logic relationships and decision criteria
- Assess image quality and enhancement needs

### 2. Picture-Centric Organization Structure
```
=== DECISION LOGIC TABLE ANALYSIS REPORT ===
├─ Image Overview & Enhancement Details
├─ DECISION LOGIC EXTRACTION (primary section)
├─ CONDITIONS AND INPUTS ANALYSIS (input parameters and values)
├─ ACTIONS AND OUTPUTS MAPPING (output actions and responses)
├─ DECISION RULES MATRIX (complete logic combinations)
├─ LOGIC VALIDATION TABLES (rule verification and testing)
├─ CSV Format Ready Data
├─ Automotive Standards Compliance
├─ Enhancement Details
└─ Validation Checklist
```

### 3. Decision Logic-Specific Processing Pipeline
**For Decision Logic Table Images:**
- **Logic Analysis**: Identification, classification, rule extraction
- **Condition Mapping**: Input conditions, values, thresholds
- **Action Extraction**: Output actions, responses, system behaviors
- **Rule Matrix**: Complete decision combinations and logic paths
- **Standards Compliance**: AUTOSAR logic patterns, ISO 26262 safety requirements
- **Test Generation**: Logic test cases and validation scenarios

## REQUIRED OUTPUT STRUCTURE

### Section 1: Image Overview
```
=== DECISION LOGIC TABLE ANALYSIS REPORT ===

IMAGE: [filename]
├─ Content: Decision logic table showing [describe main logic rules and conditions]
├─ Logic Type: Truth Table / Decision Matrix / Logic Rules / Conditional Statements
├─ Original Dimensions: [width]x[height] pixels
├─ Enhancement Applied: [specific enhancement details for decision tables]
├─ Quality Assessment: [table clarity, text readability, logic structure visibility]
├─ Analysis Confidence: [High/Medium/Low] - [reasoning]
```

### Section 2: Decision Logic Extraction (PRIMARY FOCUS)
```
=== DECISION LOGIC EXTRACTION ===

OVERALL LOGIC CHARACTERISTICS:
├─ Logic Domain: [Engine/Transmission/Safety/Communication/etc.]
├─ Decision Type: [Binary/Multi-value/Continuous/Threshold-based]
├─ Condition Count: [total number of input conditions]
├─ Action Count: [total number of output actions]
├─ Rule Complexity: [simple/moderate/complex logic combinations]

LOGIC CATEGORIES:
├─ SAFETY LOGIC: [safety-critical decision rules]
├─ OPERATIONAL LOGIC: [normal operation decision rules]
├─ ERROR HANDLING: [fault detection and response logic]
├─ PERFORMANCE LOGIC: [optimization and performance decisions]
├─ DIAGNOSTIC LOGIC: [system diagnostic and monitoring decisions]

DECISION STRUCTURE:
├─ Input Conditions: [list of all input parameters and conditions]
├─ Output Actions: [list of all output actions and responses]
├─ Logic Operators: [AND, OR, NOT, XOR operations used]
├─ Priority Rules: [rule precedence and conflict resolution]
├─ Default Actions: [default behaviors when no conditions met]
```

### Section 3: Conditions and Inputs Analysis
```
=== CONDITIONS AND INPUTS ANALYSIS ===

INPUT CONDITIONS:
├─ CONDITION 1: [Name] - Type: [data type]
│  ├─ Description: [condition purpose and meaning]
│  ├─ Data Type: [Boolean/Integer/Float/Enum/String]
│  ├─ Possible Values: [list of all possible values]
│  ├─ Thresholds: [threshold values and ranges]
│  ├─ Units: [measurement units if applicable]
│  ├─ Source: [signal source or sensor]
│  └─ Criticality: [Low/Medium/High/Safety-Critical]

├─ CONDITION 2: [Name] - Type: [data type]
│  ├─ Description: [condition purpose and meaning]
│  ├─ Data Type: [Boolean/Integer/Float/Enum/String]
│  ├─ Possible Values: [list of all possible values]
│  ├─ Thresholds: [threshold values and ranges]
│  ├─ Units: [measurement units if applicable]
│  ├─ Source: [signal source or sensor]
│  └─ Criticality: [Low/Medium/High/Safety-Critical]

CONDITION RELATIONSHIPS:
├─ INDEPENDENT CONDITIONS: [conditions that don't affect each other]
├─ DEPENDENT CONDITIONS: [conditions with interdependencies]
├─ MUTUALLY EXCLUSIVE: [conditions that cannot occur simultaneously]
├─ PREREQUISITE CONDITIONS: [conditions required for others]

CONDITION VALIDATION:
├─ Range Checking: [valid ranges and boundary conditions]
├─ Consistency Checks: [logical consistency requirements]
├─ Timeout Handling: [behavior when conditions timeout]
├─ Error States: [handling of invalid or missing conditions]
```

### Section 4: Actions and Outputs Mapping
```
=== ACTIONS AND OUTPUTS MAPPING ===

OUTPUT ACTIONS:
├─ ACTION 1: [Name] - Type: [action type]
│  ├─ Description: [action purpose and effect]
│  ├─ Action Type: [Telltale/Audio/Message/System_Control/Communication]
│  ├─ Parameters: [action-specific parameters and settings]
│  ├─ Duration: [action duration or persistence]
│  ├─ Priority: [action priority level]
│  ├─ Safety Impact: [safety implications of the action]
│  └─ Dependencies: [other actions or conditions required]

├─ ACTION 2: [Name] - Type: [action type]
│  ├─ Description: [action purpose and effect]
│  ├─ Action Type: [Telltale/Audio/Message/System_Control/Communication]
│  ├─ Parameters: [action-specific parameters and settings]
│  ├─ Duration: [action duration or persistence]
│  ├─ Priority: [action priority level]
│  ├─ Safety Impact: [safety implications of the action]
│  └─ Dependencies: [other actions or conditions required]

ACTION CATEGORIES:
├─ IMMEDIATE ACTIONS: [actions that execute immediately]
├─ DELAYED ACTIONS: [actions with execution delays]
├─ CONDITIONAL ACTIONS: [actions dependent on other conditions]
├─ PERSISTENT ACTIONS: [actions that remain active]
├─ ONE-TIME ACTIONS: [actions that execute once]

ACTION CONFLICTS:
├─ MUTUALLY EXCLUSIVE ACTIONS: [actions that cannot occur together]
├─ PRIORITY RESOLUTION: [how conflicting actions are resolved]
├─ OVERRIDE RULES: [higher priority action override rules]
├─ SAFETY OVERRIDES: [safety-critical action precedence]
```

### Section 5: Decision Rules Matrix
```
=== DECISION RULES MATRIX ===

### COMPLETE DECISION MATRIX

**Primary Decision Rules:**
| Rule ID | Condition 1 | Condition 2 | Condition 3 | Action 1 | Action 2 | Action 3 | Priority | Safety Level |
|---------|-------------|-------------|-------------|----------|----------|----------|----------|--------------|
| RULE_001 | Engine_Temp > 110°C | Vehicle_Speed > 0 | Coolant_Low = True | Warning_Red | Reduce_Power | Log_Critical | Critical | ASIL_D |
| RULE_002 | Engine_Temp > 90°C | Vehicle_Speed > 50 | Coolant_Low = False | Warning_Yellow | Monitor_Temp | Log_Warning | High | ASIL_C |
| RULE_003 | Engine_Temp < 60°C | Engine_Running = True | Ambient_Temp < 0°C | Warm_Up_Mode | Fast_Idle | Log_Info | Medium | QM |
| RULE_004 | Brake_Pressed = True | Vehicle_Speed > 0 | ABS_Active = False | Brake_Lights | Deceleration | Log_Brake | High | ASIL_D |

### LOGIC COMBINATIONS

**Truth Table Representation:**
| Engine_Temp | Vehicle_Speed | Coolant_Level | System_State | Warning | Power_Action | Log_Level | Notes |
|-------------|---------------|---------------|--------------|---------|--------------|-----------|-------|
| Critical | Any | Low | Emergency | Red_Flash | Limp_Mode | Critical | Immediate action required |
| High | High | Normal | Caution | Yellow_Solid | Monitor | Warning | Performance monitoring |
| Normal | Any | Normal | Normal | None | Normal | Info | Standard operation |
| Low | Any | Any | Warm_Up | Blue_Solid | Fast_Idle | Info | Cold start procedure |

### DECISION PATHS

**Logic Flow Analysis:**
| Path ID | Entry Condition | Decision Sequence | Final Action | Execution Time | Critical Path |
|---------|-----------------|-------------------|--------------|----------------|---------------|
| PATH_001 | Critical_Temperature | Temp_Check → Speed_Check → Action_Select | Emergency_Mode | <100ms | Yes |
| PATH_002 | Normal_Operation | Condition_Monitor → Status_Update → Log_Event | Continue_Normal | <50ms | No |
| PATH_003 | System_Fault | Fault_Detect → Safety_Check → Failsafe_Action | Safe_State | <200ms | Yes |
| PATH_004 | Performance_Mode | Mode_Select → Parameter_Adjust → Optimize | Enhanced_Performance | <500ms | No |

### RULE VALIDATION

**Logic Verification:**
| Rule Set | Completeness | Consistency | Conflicts | Coverage | Validation Status |
|----------|--------------|-------------|-----------|----------|-------------------|
| Temperature_Rules | 100% | Verified | None | All_Ranges | Pass |
| Speed_Rules | 95% | Verified | Minor | Most_Cases | Pass |
| Safety_Rules | 100% | Verified | Resolved | All_Critical | Pass |
| Performance_Rules | 90% | Verified | None | Normal_Operation | Pass |
```

### Section 6: Logic Validation Tables
```
=== LOGIC VALIDATION TABLES ===

### DECISION VALIDATION MATRIX

**Rule Testing Scenarios:**
| Test Case | Input Conditions | Expected Actions | Actual Result | Status | Notes |
|-----------|------------------|------------------|---------------|--------|-------|
| TC_001 | Temp=Critical, Speed=High | Warning+PowerReduction | As_Expected | Pass | Safety critical |
| TC_002 | Temp=Normal, Speed=Low | No_Action | As_Expected | Pass | Normal operation |
| TC_003 | Multiple_Faults | Highest_Priority_Action | As_Expected | Pass | Priority resolution |
| TC_004 | Invalid_Input | Default_Safe_Action | As_Expected | Pass | Error handling |

### BOUNDARY CONDITION TESTING

**Edge Case Analysis:**
| Boundary Type | Test Value | Expected Behavior | Actual Behavior | Risk Level | Action Required |
|---------------|------------|-------------------|-----------------|------------|-----------------|
| Temperature_Max | 110.0°C | Trigger_Critical | Triggered | High | None |
| Temperature_Min | -40.0°C | Cold_Start_Mode | Activated | Medium | None |
| Speed_Zero | 0.0 km/h | Stationary_Logic | Applied | Low | None |
| Speed_Max | 300.0 km/h | Performance_Limit | Limited | High | Monitor |

### LOGIC CONSISTENCY CHECK

**Consistency Verification:**
| Rule Pair | Conflict Type | Resolution Method | Priority Winner | Validation Result |
|-----------|---------------|-------------------|-----------------|-------------------|
| RULE_001 vs RULE_002 | Threshold_Overlap | Higher_Priority | RULE_001 | Consistent |
| RULE_003 vs RULE_004 | Action_Conflict | Safety_Override | RULE_004 | Resolved |
| RULE_005 vs RULE_006 | Timing_Conflict | Sequential_Execution | Both | Consistent |
| RULE_007 vs RULE_008 | Resource_Conflict | Resource_Sharing | Negotiated | Acceptable |
```

### Section 7: Extracted Table Data
```
=== EXTRACTED TABLE DATA ===

DECISION_CONDITIONS_TABLE: (from conditions analysis)
Purpose: Complete input conditions and their specifications

Condition_Name | Data_Type | Possible_Values | Thresholds | Units | Source | Criticality
---------------|-----------|-----------------|------------|-------|--------|------------
Engine_Temperature | Integer | 0-150 | Low<60,Normal60-90,High90-110,Critical>110 | Celsius | Temp_Sensor | Safety_Critical
Vehicle_Speed | Integer | 0-300 | Stationary=0,Low<50,Medium50-100,High>100 | km/h | Speed_Sensor | High
Coolant_Level | Boolean | True,False | Low=False,Normal=True | Boolean | Level_Sensor | High
Brake_Status | Boolean | True,False | Released=False,Pressed=True | Boolean | Brake_Switch | Safety_Critical

DECISION_ACTIONS_TABLE: (from actions analysis)
Purpose: Complete output actions and their specifications

Action_Name | Action_Type | Parameters | Duration | Priority | Safety_Impact | Dependencies
------------|-------------|------------|----------|----------|---------------|-------------
Warning_Red | Telltale | Color=Red,Flash=True | Continuous | Critical | ASIL_D | Power_Available
Warning_Yellow | Telltale | Color=Yellow,Flash=False | Continuous | High | ASIL_C | Power_Available
Reduce_Power | System_Control | Reduction=50% | Until_Resolved | Critical | ASIL_D | Engine_Control
Log_Critical | Communication | Level=Critical,Store=NVRAM | Immediate | High | ASIL_B | Storage_Available

DECISION_RULES_TABLE: (from rules matrix)
Purpose: Complete decision rules and logic combinations

Rule_ID | Condition_1 | Condition_2 | Condition_3 | Action_1 | Action_2 | Priority | Safety_Level
--------|-------------|-------------|-------------|----------|----------|----------|-------------
RULE_001 | Engine_Temp>110 | Vehicle_Speed>0 | Coolant_Low=True | Warning_Red | Reduce_Power | Critical | ASIL_D
RULE_002 | Engine_Temp>90 | Vehicle_Speed>50 | Coolant_Low=False | Warning_Yellow | Monitor_Temp | High | ASIL_C
RULE_003 | Engine_Temp<60 | Engine_Running=True | Ambient_Temp<0 | Warm_Up_Mode | Fast_Idle | Medium | QM
RULE_004 | Brake_Pressed=True | Vehicle_Speed>0 | ABS_Active=False | Brake_Lights | Deceleration | High | ASIL_D

LOGIC_VALIDATION_TABLE: (from validation analysis)
Purpose: Logic validation and testing results

Test_Case | Input_Conditions | Expected_Actions | Actual_Result | Status | Notes
----------|------------------|------------------|---------------|--------|-------
TC_001 | Temp=Critical,Speed=High | Warning+PowerReduction | As_Expected | Pass | Safety_critical
TC_002 | Temp=Normal,Speed=Low | No_Action | As_Expected | Pass | Normal_operation
TC_003 | Multiple_Faults | Highest_Priority_Action | As_Expected | Pass | Priority_resolution
TC_004 | Invalid_Input | Default_Safe_Action | As_Expected | Pass | Error_handling
```

### Section 8: CSV Format Ready Data
```
=== CSV FORMAT READY DATA ===

DECISION_CONDITIONS.csv:
Condition_Name,Data_Type,Possible_Values,Thresholds,Units,Source,Criticality
Engine_Temperature,Integer,0-150,Low<60;Normal60-90;High90-110;Critical>110,Celsius,Temp_Sensor,Safety_Critical
Vehicle_Speed,Integer,0-300,Stationary=0;Low<50;Medium50-100;High>100,km/h,Speed_Sensor,High
Coolant_Level,Boolean,True;False,Low=False;Normal=True,Boolean,Level_Sensor,High
Brake_Status,Boolean,True;False,Released=False;Pressed=True,Boolean,Brake_Switch,Safety_Critical

DECISION_ACTIONS.csv:
Action_Name,Action_Type,Parameters,Duration,Priority,Safety_Impact,Dependencies
Warning_Red,Telltale,Color=Red;Flash=True,Continuous,Critical,ASIL_D,Power_Available
Warning_Yellow,Telltale,Color=Yellow;Flash=False,Continuous,High,ASIL_C,Power_Available
Reduce_Power,System_Control,Reduction=50%,Until_Resolved,Critical,ASIL_D,Engine_Control
Log_Critical,Communication,Level=Critical;Store=NVRAM,Immediate,High,ASIL_B,Storage_Available

DECISION_RULES.csv:
Rule_ID,Condition_1,Condition_2,Condition_3,Action_1,Action_2,Priority,Safety_Level
RULE_001,Engine_Temp>110,Vehicle_Speed>0,Coolant_Low=True,Warning_Red,Reduce_Power,Critical,ASIL_D
RULE_002,Engine_Temp>90,Vehicle_Speed>50,Coolant_Low=False,Warning_Yellow,Monitor_Temp,High,ASIL_C
RULE_003,Engine_Temp<60,Engine_Running=True,Ambient_Temp<0,Warm_Up_Mode,Fast_Idle,Medium,QM
RULE_004,Brake_Pressed=True,Vehicle_Speed>0,ABS_Active=False,Brake_Lights,Deceleration,High,ASIL_D

LOGIC_VALIDATION.csv:
Test_Case,Input_Conditions,Expected_Actions,Actual_Result,Status,Notes
TC_001,Temp=Critical;Speed=High,Warning+PowerReduction,As_Expected,Pass,Safety_critical
TC_002,Temp=Normal;Speed=Low,No_Action,As_Expected,Pass,Normal_operation
TC_003,Multiple_Faults,Highest_Priority_Action,As_Expected,Pass,Priority_resolution
TC_004,Invalid_Input,Default_Safe_Action,As_Expected,Pass,Error_handling
```

### Section 9: Automotive Standards Compliance
```
=== AUTOMOTIVE STANDARDS COMPLIANCE ===

ISO 26262 FUNCTIONAL SAFETY:
├─ Decision Safety: [safety-critical decision logic requirements and validation]
├─ Logic Verification: [systematic verification of all decision paths]
├─ Fault Handling: [decision logic for fault detection and safe responses]
├─ Safety Monitoring: [decision logic monitoring and supervision mechanisms]

AUTOSAR DECISION PATTERNS:
├─ Decision Components: [AUTOSAR decision logic component patterns]
├─ Logic Interfaces: [standardized decision logic interfaces]
├─ Event Handling: [event-driven decision logic patterns]
├─ State Management: [decision logic for state transitions]

AUTOMOTIVE SPICE COMPLIANCE:
├─ Logic Documentation: [decision logic documentation requirements]
├─ Verification Methods: [systematic logic verification approaches]
├─ Traceability: [decision logic traceability to requirements]
├─ Change Management: [logic change control and validation]

FERRARI DECISION STANDARDS:
├─ Performance Logic: [Ferrari-specific performance decision requirements]
├─ Driver Interface: [decision logic for driver interaction and feedback]
├─ System Integration: [Ferrari system integration decision patterns]
├─ Safety Priorities: [Ferrari safety decision logic priorities]
```

## QUALITY STANDARDS

### Image Enhancement Requirements:
- **Decision Table Enhancement**: Optimize for table structure and text clarity
- **OCR Optimization**: 98%+ accuracy for all conditions, actions, and logic rules
- **Logic Extraction**: Complete and accurate decision rule extraction
- **Table Recognition**: Clear identification of all decision table elements

### Picture-Centric Analysis Standards:
- **Logic-First Structure**: Visual decision logic and rules drive the analysis
- **Complete Coverage**: Every visible condition, action, and rule cataloged
- **Practical Focus**: Information useful for automotive decision logic development
- **Standards Compliance**: Verification against automotive decision logic standards

### Validation Requirements:
- **100% Logic Coverage**: All visible decision rules and logic paths identified
- **Accurate Rule Extraction**: Decision logic correctly interpreted and documented
- **Standards Mapping**: Proper ISO 26262 and AUTOSAR decision logic references
- **CSV Conversion**: All tabular data properly formatted for analysis tools

## EXECUTION CHECKLIST

### Pre-Processing:
- [ ] Identify decision table type and logic domain
- [ ] Assess image quality and enhancement needs for decision table analysis
- [ ] Determine logic extraction approach and rule complexity
- [ ] Prepare for condition, action, and rule analysis

### Logic Analysis:
- [ ] Catalog all conditions with data types and possible values
- [ ] Document all actions with parameters and specifications
- [ ] Extract complete decision rules and logic combinations
- [ ] Analyze logic relationships and dependencies

### Decision Analysis:
- [ ] Create complete decision matrix with all rule combinations
- [ ] Document logic validation and testing scenarios
- [ ] Map critical decision paths and safety implications
- [ ] Generate decision logic test cases and validation criteria

### Output Generation:
- [ ] Structure report with decision logic extraction as primary section
- [ ] Format all data for CSV conversion and analysis tools
- [ ] Document automotive standards compliance
- [ ] Provide complete validation checklist

## SUCCESS CRITERIA

### Processing Quality:
- **Logic Identification**: 100% of visible decision rules cataloged with complete specifications
- **Rule Accuracy**: 98%+ accuracy in decision logic extraction and interpretation
- **Standards Compliance**: Proper mapping to automotive decision logic standards
- **Data Extraction**: All tabular data ready for CSV/Excel import and analysis

### Picture-Centric Focus:
- **Visual Priority**: Decision logic tables and rules are primary focus
- **Practical Output**: Information directly usable for automotive decision logic development
- **Technical Depth**: Complete analysis of decision logic characteristics and validation
- **Implementation Ready**: All data suitable for automotive system decision logic implementation

### Enhancement Details:
- **Applied Enhancements**: Table structure optimization, text clarity enhancement
- **Quality Metrics**: Logic recognition accuracy, rule extraction precision
- **Validation Results**: Complete coverage verification, standards compliance check

### Analysis Summary:
- **Key Findings**: Critical decision rules, logic conflicts, validation requirements
- **Development Implications**: System decision logic requirements, safety considerations
- **Recommended Actions**: Logic optimizations, rule clarifications, validation improvements
