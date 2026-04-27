# ENHANCED STATE MATRIX TIMING DIAGRAMS ANALYSIS PROMPT v5.0

## OVERVIEW
This prompt is designed for comprehensive analysis of complex timing diagrams with integrated state matrices, combining temporal signal analysis with systematic state event extraction.

## VISUAL STRUCTURE RECOGNITION

### 1. DIAGRAM SECTION IDENTIFICATION
**Multi-Section Analysis:**
- **Upper Section:** Timing signals with temporal relationships
- **Lower Section:** State matrix grid with filled/unfilled indicators
- **Separation Elements:** Horizontal lines, spacing, or visual boundaries
- **Vertical Correlation:** Time reference lines connecting both sections

**Visual Indicators to Identify:**
- Clear horizontal separation between timing and matrix sections
- Grid-based structure in lower section
- Filled circles (●) and unfilled circles (○) patterns
- Multiple rows representing different indication types
- Multiple columns representing time progression

### 2. SIGNAL CATEGORIZATION FRAMEWORK
**Input Signals (Upper Section):**
- Binary digital signals with HIGH/LOW states
- Signal names with clear ON/OFF or True/False labels
- Temporal transitions showing state changes
- Hierarchical dependencies (e.g., Key → HMI → Warning)

**Output Indicators (Lower Section):**
- Matrix rows representing different indication types
- IndicationID, IndicationSts, IndicationUserAction patterns
- State representations through circle fill patterns

## SYSTEMATIC SIGNAL ANALYSIS

### 3. INPUT PARAMETER EXTRACTION
**For Each Input Signal:**
```
| Signal Name | Type | Values | Description | Dependencies |
|-------------|------|--------|-------------|--------------|
| Signal_1    | Binary | 0/1 | Function | Prerequisites |
```

**Signal Analysis Steps:**
1. **Identify Signal Names:** Extract exact text labels
2. **Determine Value Range:** Map HIGH/LOW to binary 0/1
3. **Document Initial States:** Record starting values
4. **Identify Dependencies:** Note prerequisite relationships
5. **Calculate State Space:** Compute 2^n for n input signals

### 4. STATE MATRIX EXTRACTION METHODOLOGY

**MANDATORY REQUIREMENT: COMPLETE STATE SPACE ANALYSIS**
**🚨 CRITICAL: The state matrix MUST contain exactly 2^n rows where n is the number of input signals.**
**Document ALL possible input combinations (00000 through 11111 for 5 inputs), identifying which are valid operational states and which are invalid based on automotive dependency rules.**

**Matrix Grid Decoding:**
1. **Row Identification:**
   - Map each row to specific indication types
   - Document row labels (IndicationID, IndicationSts, etc.)
   - Note any special markings (**, *, etc.)

2. **Column Analysis:**
   - Count total time columns shown in visual diagram
   - Correlate each column to timing diagram events
   - **IMPORTANT:** Visual columns may show only key transitions, not complete state space
   - Map column positions to input state combinations

3. **Complete State Space Documentation:**
   - **Generate ALL 2^n possible input combinations systematically**
   - **Example for 5 inputs:** States 00-31 (binary 00000 through 11111)
   - **Identify valid vs. invalid states based on automotive logic**
   - **Document output patterns for each state combination**

4. **Circle Pattern Analysis:**
   - ● (Filled) = Active/True state
   - ○ (Unfilled) = Inactive/False state
   - Document exact pattern for each cell
   - **Note:** Visual matrix may show only subset of complete state space

**CRITICAL: OUTPUT COLUMN IDENTIFICATION**
**Pay special attention to identifying all output columns in the matrix:**
- **Examine Column Headers Carefully:** Don't assume generic "Output_1, Output_2, Output_3"
- **Identify Actual Output Types:** Look for specific column names like IndicationID, IndicationSts, IndicationUserAction
- **Recognize Duplicate Types:** Note when the same output type appears multiple times (e.g., two IndicationID columns, two IndicationSts columns)
- **Complete Output Extraction:** Ensure all output columns are identified and documented

**Example - VEH-F844 image65 Output Pattern:**
The actual outputs are: IndicationId, IndicationSts, IndicationId, IndicationSts, IndicationUserAction
(Note: IndicationId and IndicationSts each appear twice as separate columns)

**State Event Table Creation:**
**MANDATORY: Create complete 2^n state table, not just visible timing columns**
```
| State | Input_1 | Input_2 | Input_N | Output_1 | Output_2 | Output_N | State_Description |
|-------|---------|---------|---------|----------|----------|----------|-------------------|
| 00    | 0       | 0       | 0       | 0        | 0        | 0        | System Off        |
| 01    | 0       | 0       | 1       | 0        | 0        | 0        | Invalid State     |
| ...   | ...     | ...     | ...     | ...      | ...      | ...      | ...               |
| 31    | 1       | 1       | 1       | 1        | 1        | 1        | Full System Active|
```
**Note:** Include ALL 2^n combinations, marking invalid states based on automotive logic

## COMPREHENSIVE ANALYSIS STRUCTURE

### 5. REQUIRED ANALYSIS SECTIONS

**A. VISUAL STRUCTURE ANALYSIS**
- Diagram type identification
- Complexity level assessment
- Section separation analysis

**B. SIGNAL IDENTIFICATION**
- Complete input signal enumeration
- Output indication mapping
- Signal categorization

**C. INPUT PARAMETERS ANALYSIS**
- Tabular signal documentation
- Value range specification
- Dependency relationships

**D. INITIAL STATE ANALYSIS**
- Starting state documentation
- System initialization patterns

**E. STATE MATRIX COMPLEXITY ANALYSIS**
- Theoretical state space calculation (2^n)
- Observed vs. theoretical state comparison
- Matrix representation patterns

**F. MATRIX STATE EVENTS ANALYSIS**
- Grid structure documentation
- Row and column mapping
- Actual matrix state extraction
- Time column analysis table
- Detailed state event documentation
- Complete state-to-indication mapping

**G. AUTOMOTIVE LOGIC VALIDATION**
- Valid state dependencies
- Invalid state combinations
- Domain-specific rule checking

**H. ENHANCED ANALYSIS INSIGHTS**
- Complexity factors
- System behavior patterns
- Automotive integration aspects

### 6. STATE EVENT MATRIX OUTPUT FORMAT

**MANDATORY OUTPUT FORMAT - COMPLETE 2^n STATE SPACE:**
```
STATE EVENT MATRIX: [Matrix Name] (from imageX.png)
Purpose: [Matrix purpose - input/output signal mapping]

State | Input_1 | Input_2 | Input_N || Output_1 | Output_2 | Output_N | State_Description
------|---------|---------|---------||---------|---------|---------|-----------------
  00  |   0     |   0     |   0     ||    0    |    0    |    0    | [State Description]
  01  |   0     |   0     |   1     ||    0    |    0    |    0    | [State Description - Invalid if applicable]
  02  |   0     |   1     |   0     ||    0    |    0    |    0    | [State Description - Invalid if applicable]
  03  |   0     |   1     |   1     ||    0    |    0    |    0    | [State Description - Invalid if applicable]
  ... |  ...    |  ...    |  ...    ||   ...   |   ...   |   ...   | ...
  XX  |   1     |   1     |   1     ||    1    |    1    |    1    | [Final State Description]

Signal Definitions:
Input Signals: [Define each input signal and its values]
Output Signals: [Define each output signal and its values]

Valid States: [List valid operational states]
Invalid States: [List invalid states and reasons - e.g., violating automotive dependencies]
```

**Format Requirements:**
- **Matrix Name:** Descriptive name based on diagram content
- **Image Reference:** Include source image filename
- **Purpose Statement:** Brief description of matrix function
- **Complete State Table:** All 2^n possible input combinations
- **Clear Column Separation:** Use || to separate inputs from outputs
- **State Descriptions:** Meaningful description for each state
- **Signal Definitions:** Explicit definitions of all signals and their value meanings

## AUTOMOTIVE DOMAIN VALIDATION

### 7. DEPENDENCY RULE CHECKING
**Standard Automotive Dependencies:**
- Key_Status = 1 required for all system operations
- HMI activation depends on Key_Status = 1
- Warning conditions require both Key and HMI active
- User interface functions require warning conditions
- Escape/interaction functions require active UI elements

**Invalid State Identification:**
- Any operation without proper prerequisites
- Impossible state combinations
- Logic violations in automotive context

## METHODOLOGY EFFECTIVENESS ASSESSMENT

### 8. ANALYSIS QUALITY METRICS
**Strengths Documentation:**
- Signal identification completeness
- State matrix extraction accuracy
- Automotive domain validation
- Temporal correlation analysis

**Challenges Encountered:**
- Complexity factors that required special handling
- Multi-section analysis difficulties
- Domain knowledge requirements

**Key Improvements:**
- Enhanced capabilities over traditional approaches
- Integrated timing and matrix analysis
- Comprehensive state event documentation

## OUTPUT REQUIREMENTS

### 9. MANDATORY DELIVERABLES
1. **Complete Signal Inventory:** All inputs and outputs identified
2. **Full State Matrix:** 2^n state space with observed patterns
3. **Matrix State Events:** Detailed extraction of grid patterns
4. **State-to-Indication Mapping:** Complete correlation table
5. **Critical State Events:** Key transition documentation
6. **Automotive Validation:** Domain-specific rule checking
7. **Methodology Assessment:** Analysis effectiveness evaluation

### 10. ANALYSIS VALIDATION CHECKLIST
- [ ] All input signals identified and documented
- [ ] **State space calculated (2^n methodology) - MANDATORY COMPLETE**
- [ ] **ALL 2^n possible input combinations documented**
- [ ] **Valid vs. invalid states identified based on automotive logic**
- [ ] Matrix grid systematically decoded
- [ ] Time columns correlated to timing events (if shown)
- [ ] **Complete state-to-indication mapping for ALL 2^n states**
- [ ] Automotive dependencies validated
- [ ] Critical state events documented
- [ ] Analysis methodology assessed
- [ ] **Verification: State count equals 2^n exactly**

## EXAMPLE APPLICATION SCENARIOS

**Simple State Matrix (3 inputs):**
- Traditional timing diagrams with clear separation
- 8 possible states (2^3)
- Basic input/output relationships

**Complex State Matrix (5+ inputs):**
- Integrated timing and matrix visualization
- 32+ possible states (2^5+)
- Multiple simultaneous indications
- Hierarchical dependencies
- User interaction capabilities

This enhanced prompt ensures comprehensive analysis of both simple and complex timing diagrams with integrated state matrices, providing consistent, detailed results for automotive system documentation.
