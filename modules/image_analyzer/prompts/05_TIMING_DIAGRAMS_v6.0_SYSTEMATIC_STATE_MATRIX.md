# SYSTEMATIC STATE MATRIX TIMING DIAGRAMS ANALYSIS PROMPT v6.0

## OVERVIEW
This prompt implements a systematic placeholder-based methodology for comprehensive analysis of timing diagrams with integrated state matrices. The approach ensures complete 2^n state space coverage through structured step-by-step analysis.

## METHODOLOGY: SYSTEMATIC PLACEHOLDER-BASED ANALYSIS

### CORE PRINCIPLE
**Start with a placeholder matrix containing all 2^n input combinations with unknown (X) output values. For each output signal, analyze the logic rules and systematically replace X values with determined 0/1 values.**

## STEP 1: INITIAL SETUP AND PLACEHOLDER MATRIX CREATION

### 1.1 VISUAL STRUCTURE RECOGNITION
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

### 1.2 INPUT SIGNAL IDENTIFICATION
**Extract from image and document systematically:**

| Signal Name | Type | Value Range | Description | Dependencies |
|-------------|------|-------------|-------------|--------------|
| Signal_1 | Binary | 0=[State0], 1=[State1] | [Function description] | [Prerequisites] |
| Signal_2 | Binary | 0=[State0], 1=[State1] | [Function description] | [Prerequisites] |
| Signal_3 | Binary | 0=[State0], 1=[State1] | [Function description] | [Prerequisites] |
| Signal_4 | Binary | 0=[State0], 1=[State1] | [Function description] | [Prerequisites] |
| Signal_5 | Binary | 0=[State0], 1=[State1] | [Function description] | [Prerequisites] |

**Calculate State Space:**
- **Total Input Signals:** n = [number]
- **Total States Required:** 2^n = [calculation]
- **State Range:** 00...0 through 11...1 (binary)
- **Decimal Range:** State 0 through State (2^n - 1)

### 1.3 OUTPUT SIGNAL IDENTIFICATION
**🚨 CRITICAL: COMPLETE OUTPUT COLUMN IDENTIFICATION**
**Pay special attention to identifying all output columns in the matrix:**
- **Examine Column Headers Carefully:** Don't assume generic names
- **Identify Actual Output Types:** Look for specific names like IndicationID, IndicationSts, IndicationUserAction
- **Recognize Duplicate Types:** Note when the same output type appears multiple times
- **Complete Output Extraction:** Ensure all output columns are identified

**Document all outputs systematically:**

| Output Name | Type | Value Range | Description | Activation Logic |
|-------------|------|-------------|-------------|------------------|
| Output_1 | Binary | 0=[Inactive], 1=[Active] | [Function description] | [To be determined] |
| Output_2 | Binary | 0=[Inactive], 1=[Active] | [Function description] | [To be determined] |
| Output_3 | Binary | 0=[Inactive], 1=[Active] | [Function description] | [To be determined] |
| Output_4 | Binary | 0=[Inactive], 1=[Active] | [Function description] | [To be determined] |
| Output_5 | Binary | 0=[Inactive], 1=[Active] | [Function description] | [To be determined] |

### 1.4 CREATE INITIAL PLACEHOLDER MATRIX
**PLACEHOLDER STATE MATRIX: [System Name] (from [image])**

| State | Input1 | Input2 | Input3 | Input4 | Input5 || Output1 | Output2 | Output3 | Output4 | Output5 | State_Description |
|-------|--------|--------|--------|--------|--------||---------|---------|---------|---------|---------|-------------------|
| 00    | 0      | 0      | 0      | 0      | 0      || X       | X       | X       | X       | X       | [To be determined] |
| 01    | 0      | 0      | 0      | 0      | 1      || X       | X       | X       | X       | X       | [To be determined] |
| 02    | 0      | 0      | 0      | 1      | 0      || X       | X       | X       | X       | X       | [To be determined] |
| 03    | 0      | 0      | 0      | 1      | 1      || X       | X       | X       | X       | X       | [To be determined] |
| 04    | 0      | 0      | 1      | 0      | 0      || X       | X       | X       | X       | X       | [To be determined] |
| 05    | 0      | 0      | 1      | 0      | 1      || X       | X       | X       | X       | X       | [To be determined] |
| 06    | 0      | 0      | 1      | 1      | 0      || X       | X       | X       | X       | X       | [To be determined] |
| 07    | 0      | 0      | 1      | 1      | 1      || X       | X       | X       | X       | X       | [To be determined] |
| 08    | 0      | 1      | 0      | 0      | 0      || X       | X       | X       | X       | X       | [To be determined] |
| 09    | 0      | 1      | 0      | 0      | 1      || X       | X       | X       | X       | X       | [To be determined] |
| 10    | 0      | 1      | 0      | 1      | 0      || X       | X       | X       | X       | X       | [To be determined] |
| 11    | 0      | 1      | 0      | 1      | 1      || X       | X       | X       | X       | X       | [To be determined] |
| 12    | 0      | 1      | 1      | 0      | 0      || X       | X       | X       | X       | X       | [To be determined] |
| 13    | 0      | 1      | 1      | 0      | 1      || X       | X       | X       | X       | X       | [To be determined] |
| 14    | 0      | 1      | 1      | 1      | 0      || X       | X       | X       | X       | X       | [To be determined] |
| 15    | 0      | 1      | 1      | 1      | 1      || X       | X       | X       | X       | X       | [To be determined] |
| 16    | 1      | 0      | 0      | 0      | 0      || X       | X       | X       | X       | X       | [To be determined] |
| 17    | 1      | 0      | 0      | 0      | 1      || X       | X       | X       | X       | X       | [To be determined] |
| 18    | 1      | 0      | 0      | 1      | 0      || X       | X       | X       | X       | X       | [To be determined] |
| 19    | 1      | 0      | 0      | 1      | 1      || X       | X       | X       | X       | X       | [To be determined] |
| 20    | 1      | 0      | 1      | 0      | 0      || X       | X       | X       | X       | X       | [To be determined] |
| 21    | 1      | 0      | 1      | 0      | 1      || X       | X       | X       | X       | X       | [To be determined] |
| 22    | 1      | 0      | 1      | 1      | 0      || X       | X       | X       | X       | X       | [To be determined] |
| 23    | 1      | 0      | 1      | 1      | 1      || X       | X       | X       | X       | X       | [To be determined] |
| 24    | 1      | 1      | 0      | 0      | 0      || X       | X       | X       | X       | X       | [To be determined] |
| 25    | 1      | 1      | 0      | 0      | 1      || X       | X       | X       | X       | X       | [To be determined] |
| 26    | 1      | 1      | 0      | 1      | 0      || X       | X       | X       | X       | X       | [To be determined] |
| 27    | 1      | 1      | 0      | 1      | 1      || X       | X       | X       | X       | X       | [To be determined] |
| 28    | 1      | 1      | 1      | 0      | 0      || X       | X       | X       | X       | X       | [To be determined] |
| 29    | 1      | 1      | 1      | 0      | 1      || X       | X       | X       | X       | X       | [To be determined] |
| 30    | 1      | 1      | 1      | 1      | 0      || X       | X       | X       | X       | X       | [To be determined] |
| 31    | 1      | 1      | 1      | 1      | 1      || X       | X       | X       | X       | X       | [To be determined] |

**Note:** Adjust number of inputs/outputs and states based on actual image content.

## STEP 2: SYSTEMATIC OUTPUT SIGNAL ANALYSIS

### 2.1 OUTPUT 1 ANALYSIS: [Output1 Name]

#### A. Visual Pattern Recognition
**From timing diagram/matrix grid:**
- Examine visual indicators (●/○, HIGH/LOW, filled/unfilled)
- Identify which time columns show this output as active
- Note any visual patterns or correlations
- Document exact visual evidence

**Visual Evidence for Output1:**
- Column 1: [●/○] - State [binary combination]
- Column 2: [●/○] - State [binary combination]
- Column 3: [●/○] - State [binary combination]
- [Continue for all visible columns]

#### B. Logic Rule Determination
**Analyze input conditions for Output1 = 1:**
- Review each state where visual shows Output1 active
- Identify common input parameter patterns
- Determine the Boolean logic rule
- Consider automotive dependency rules

**Derived Logic Rule for Output1:**
```
Output1 = 1 when: [Boolean expression using Input1, Input2, etc.]
Example: Output1 = 1 when (Input1=1 AND Input2=1 AND Input3=1)
```

**Logic Validation:**
- Test rule against all visual evidence
- Check for consistency across all active states
- Validate against automotive safety rules

#### C. Apply Logic to All States
**State-by-state evaluation for Output1:**
- State 00 (00000): Input conditions → Output1 = [0 or 1] because [reason]
- State 01 (00001): Input conditions → Output1 = [0 or 1] because [reason]
- State 02 (00010): Input conditions → Output1 = [0 or 1] because [reason]
- [Continue for all 2^n states...]

#### D. Replace X Values for Output1
**Update placeholder matrix with Output1 values determined above**

### 2.2 OUTPUT 2 ANALYSIS: [Output2 Name]
**Repeat the same systematic process:**
- Visual pattern recognition
- Logic rule determination
- Apply logic to all states
- Replace X values for Output2

### 2.3 OUTPUT 3 ANALYSIS: [Output3 Name]
**Repeat the same systematic process for Output3**

### 2.4 OUTPUT 4 ANALYSIS: [Output4 Name]
**Repeat the same systematic process for Output4**

### 2.5 OUTPUT 5 ANALYSIS: [Output5 Name]
**Repeat the same systematic process for Output5**

## STEP 3: FINAL MATRIX COMPILATION

### 3.1 Complete State Matrix (All X Values Replaced)
**FINAL STATE MATRIX: [System Name] (from [image])**

| State | Input1 | Input2 | Input3 | Input4 | Input5 || Output1 | Output2 | Output3 | Output4 | Output5 | State_Description |
|-------|--------|--------|--------|--------|--------||---------|---------|---------|---------|---------|-------------------|
| 00    | 0      | 0      | 0      | 0      | 0      || [0/1]   | [0/1]   | [0/1]   | [0/1]   | [0/1]   | [Final description] |
| 01    | 0      | 0      | 0      | 0      | 1      || [0/1]   | [0/1]   | [0/1]   | [0/1]   | [0/1]   | [Final description] |
| [Continue for all 2^n states with final determined values...]

### 3.2 Logic Rules Summary
**Complete Boolean Logic for All Outputs:**
- Output1 = [Boolean expression derived from analysis]
- Output2 = [Boolean expression derived from analysis]
- Output3 = [Boolean expression derived from analysis]
- Output4 = [Boolean expression derived from analysis]
- Output5 = [Boolean expression derived from analysis]

### 3.3 Signal Definitions
**Input Signals:**
- Input1: 0=[State0 description], 1=[State1 description]
- Input2: 0=[State0 description], 1=[State1 description]
- [Continue for all inputs]

**Output Signals:**
- Output1: 0=[Inactive description], 1=[Active description]
- Output2: 0=[Inactive description], 1=[Active description]
- [Continue for all outputs]

### 3.4 State Classification
**Valid States:** [List states that follow automotive logic]
**Invalid States:** [List states that violate dependencies with reasons]

## STEP 4: ANALYSIS VALIDATION

### 4.1 Cross-Reference with Visual Evidence
**Visual Validation:**
- Compare final matrix against timing diagram columns
- Verify circle patterns (●=1, ○=0) match output values
- Confirm state transitions align with visual sequence
- Check for any discrepancies

### 4.2 Logic Consistency Check
**Internal Consistency:**
- Verify Boolean expressions produce expected results
- Check for contradictions in logic rules
- Validate dependency relationships between inputs/outputs
- Ensure automotive safety rules are followed

### 4.3 Completeness Verification
**Systematic Verification Checklist:**
- [ ] All 2^n states included (no missing combinations)
- [ ] All X placeholders replaced with 0 or 1
- [ ] Logic rules consistently applied across all states
- [ ] Visual patterns from image accurately reflected
- [ ] Domain-specific rules (automotive/system logic) validated
- [ ] State descriptions updated with final determinations

## AUTOMOTIVE DOMAIN VALIDATION

### 5.1 DEPENDENCY RULE CHECKING
**Standard Automotive Dependencies:**
- Key_Status = 1 required for all system operations
- HMI activation depends on Key_Status = 1
- Warning conditions require both Key and HMI active
- User interface functions require warning conditions
- Escape/interaction functions require active UI elements

### 5.2 INVALID STATE IDENTIFICATION
**Categories of Invalid States:**
- Any operation without proper prerequisites
- Impossible state combinations
- Logic violations in automotive context
- Safety rule violations

## METHODOLOGY ADVANTAGES

### 6.1 SYSTEMATIC BENEFITS
1. **Complete Coverage:** Ensures all 2^n states are analyzed
2. **Structured Approach:** Breaks complex analysis into manageable steps
3. **Audit Trail:** Clear documentation of how each value was determined
4. **Error Prevention:** Placeholder system prevents missing states
5. **Logic Clarity:** Separate analysis of each output improves accuracy
6. **Validation Framework:** Built-in checks ensure consistency

### 6.2 QUALITY ASSURANCE
- No states accidentally omitted
- Clear reasoning for each output value
- Systematic verification process
- Visual evidence correlation
- Domain rule validation

## OUTPUT REQUIREMENTS

### 7.1 MANDATORY DELIVERABLES
1. **Complete Signal Inventory:** All inputs and outputs identified with exact names
2. **Placeholder Matrix:** Initial 2^n state space with X values
3. **Output-by-Output Analysis:** Systematic logic determination for each output
4. **Final Complete Matrix:** All X values replaced with determined 0/1 values
5. **Logic Rules Summary:** Boolean expressions for all outputs
6. **State Classification:** Valid vs. invalid states with reasoning
7. **Validation Results:** Verification against visual evidence and domain rules

### 7.2 ANALYSIS VALIDATION CHECKLIST
- [ ] All input signals identified and documented with exact names
- [ ] **State space calculated (2^n methodology) - MANDATORY COMPLETE**
- [ ] **ALL 2^n possible input combinations documented in placeholder matrix**
- [ ] **Each output analyzed systematically with logic rule determination**
- [ ] **All X placeholders replaced with determined 0/1 values**
- [ ] **Valid vs. invalid states identified based on automotive logic**
- [ ] Matrix grid systematically decoded with visual evidence
- [ ] **Complete state-to-indication mapping for ALL 2^n states**
- [ ] Automotive dependencies validated
- [ ] Logic rules tested for consistency
- [ ] **Verification: Final state count equals 2^n exactly**

## EXAMPLE APPLICATION SCENARIOS

### 8.1 SIMPLE STATE MATRIX (3 inputs)
- Traditional timing diagrams with clear separation
- 8 possible states (2^3)
- Basic input/output relationships
- Straightforward automotive dependencies

### 8.2 COMPLEX STATE MATRIX (5+ inputs)
- Integrated timing and matrix visualization
- 32+ possible states (2^5+)
- Multiple simultaneous indications
- Hierarchical dependencies
- User interaction capabilities

## IMPLEMENTATION INSTRUCTIONS

### 9.1 STEP-BY-STEP EXECUTION
1. **Start with placeholder matrix** - Create complete 2^n table with X values
2. **Analyze one output at a time** - Never skip this systematic approach
3. **Document visual evidence** - Record exact patterns from image
4. **Derive logic rules** - Determine Boolean expressions from patterns
5. **Apply systematically** - Replace X values for one output completely before moving to next
6. **Validate continuously** - Check logic consistency at each step
7. **Complete verification** - Use checklist to ensure nothing missed

### 9.2 CRITICAL SUCCESS FACTORS
- **Never skip the placeholder matrix creation**
- **Always analyze outputs one at a time**
- **Document reasoning for every logic rule**
- **Validate against visual evidence continuously**
- **Ensure complete 2^n state coverage**

This enhanced systematic prompt ensures comprehensive, accurate, and complete analysis of timing diagrams with integrated state matrices through a structured placeholder-based methodology.
