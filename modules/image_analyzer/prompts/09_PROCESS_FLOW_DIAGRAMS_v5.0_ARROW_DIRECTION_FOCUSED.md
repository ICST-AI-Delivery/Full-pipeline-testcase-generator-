# PROCESS FLOW DIAGRAMS - v5.0 ARROW DIRECTION FOCUSED ANALYSIS

## SPECIALIZED ARROW DIRECTION DETECTION PROMPT

### PRIMARY OBJECTIVE
Perform precise arrow direction analysis with systematic transition counting and bidirectional flow detection for automotive process flow diagrams.

### ARROW ANALYSIS METHODOLOGY

#### PHASE 1: ARROW INVENTORY AND DIRECTION MAPPING
1. **Systematic Arrow Scanning**
   - Scan the entire diagram systematically (left-to-right, top-to-bottom)
   - Identify EVERY arrow in the diagram regardless of size or complexity
   - Mark each arrow with a unique identifier (A1, A2, A3, etc.)

2. **Arrow Head Detection**
   - Focus specifically on arrowhead shapes (triangular points)
   - Determine the precise direction each arrowhead points
   - Distinguish between single arrowheads and double arrowheads (bidirectional)
   - Note arrowhead size and clarity

3. **Arrow Shaft Analysis**
   - Trace each arrow line from start point to end point
   - Identify straight arrows vs. curved arrows
   - Map connection points where arrows touch state bubbles/decision diamonds
   - Detect any arrow intersections or overlaps

#### PHASE 2: CONNECTION POINT MAPPING
1. **Source Point Identification**
   - For each arrow, identify the exact source element (state, decision, process)
   - Determine the specific edge/boundary where the arrow originates
   - Note if multiple arrows originate from the same element

2. **Destination Point Identification**
   - For each arrow, identify the exact destination element
   - Determine the specific edge/boundary where the arrow terminates
   - Note if multiple arrows terminate at the same element

3. **Bidirectional Flow Detection**
   - Identify arrows that have arrowheads at both ends
   - Distinguish between true bidirectional arrows and separate unidirectional arrows between the same elements
   - Map bidirectional pairs carefully

#### PHASE 3: TRANSITION COUNTING VALIDATION
1. **Per-State Analysis**
   - For each state bubble, count incoming arrows by examining arrowheads pointing INTO the state
   - For each state bubble, count outgoing arrows by examining arrows originating FROM the state
   - Create a matrix: State → [Incoming Count, Outgoing Count]

2. **Decision Point Analysis**
   - For decision diamonds, count incoming arrows (typically 1)
   - For decision diamonds, count outgoing arrows (typically 2: TRUE/FALSE paths)
   - Verify decision logic paths

3. **Process Box Analysis**
   - For process boxes (like RearDelay), count incoming and outgoing arrows
   - Verify process flow continuity

### DETAILED ARROW ANALYSIS TEMPLATE

For each arrow identified, provide:

**ARROW [ID]: [Source] → [Destination]**
├─ Arrow Head Direction: [Direction description]
├─ Arrow Head Shape: [Clear/Unclear, Size, Triangular/Other]
├─ Arrow Shaft Type: [Straight/Curved, Length estimate]
├─ Source Connection Point: [Specific edge of source element]
├─ Destination Connection Point: [Specific edge of destination element]
├─ Bidirectional Status: [Yes/No, if yes describe both directions]
├─ Condition Label: [Text associated with arrow]
├─ Condition Label Position: [Above/Below/Beside arrow]
└─ Visual Clarity: [Excellent/Good/Poor]

### STATE TRANSITION MATRIX TEMPLATE

**STATE TRANSITION VERIFICATION MATRIX:**

| State/Element | Incoming Arrows | Outgoing Arrows | Arrow IDs In | Arrow IDs Out | Bidirectional Pairs |
|---------------|-----------------|-----------------|--------------|---------------|-------------------|
| STATUS 0      | [Count]         | [Count]         | [List]       | [List]        | [List]            |
| STATUS 1      | [Count]         | [Count]         | [List]       | [List]        | [List]            |
| STATUS 2      | [Count]         | [Count]         | [List]       | [List]        | [List]            |
| STATUS 3      | [Count]         | [Count]         | [List]       | [List]        | [List]            |
| STATUS 4      | [Count]         | [Count]         | [List]       | [List]        | [List]            |
| Decision      | [Count]         | [Count]         | [List]       | [List]        | [List]            |
| Process       | [Count]         | [Count]         | [List]       | [List]        | [List]            |

### ARROW DIRECTION VALIDATION RULES

1. **Conservation Rule**: Total outgoing arrows must equal total incoming arrows (excluding entry/exit points)
2. **Bidirectional Verification**: Each bidirectional arrow must be counted as both incoming and outgoing
3. **Decision Logic**: Decision diamonds should have 1 incoming and 2 outgoing (TRUE/FALSE)
4. **Process Flow**: Process boxes should have 1 incoming and 1 outgoing typically
5. **State Consistency**: Each state should have at least 1 incoming and 1 outgoing (except entry/exit states)

### ZOOM ANALYSIS FOR COMPLEX ARROW REGIONS

**ZOOM REGION IDENTIFICATION:**
- Identify areas with multiple arrow convergence
- Focus on areas with curved arrows or complex routing
- Examine areas where arrows cross or overlap
- Analyze regions with small or unclear arrowheads

**ZOOM ANALYSIS PROCEDURE:**
1. Isolate the complex region visually
2. Trace each arrow individually within the region
3. Verify arrowhead directions at higher detail
4. Confirm connection points precisely
5. Validate condition labels and positioning

### ERROR DETECTION AND CORRECTION

**COMMON ARROW ANALYSIS ERRORS:**
1. Miscounting bidirectional arrows (counting as 1 instead of 2)
2. Missing small or faint arrows
3. Confusing arrow direction due to curved paths
4. Misidentifying connection points on state boundaries
5. Overlooking arrows that cross behind other elements

**VALIDATION CHECKS:**
1. Verify that each outgoing arrow has a corresponding incoming arrow somewhere
2. Check that bidirectional pairs are properly identified
3. Confirm that decision diamonds have correct TRUE/FALSE paths
4. Validate that all states have logical entry/exit paths
5. Ensure arrow counts match the visual evidence

### IMPLEMENTATION INSTRUCTIONS

1. **First Pass**: Identify and number all arrows systematically
2. **Second Pass**: Determine direction and connection points for each arrow
3. **Third Pass**: Count transitions per state and validate matrix
4. **Fourth Pass**: Apply zoom analysis to complex regions
5. **Fifth Pass**: Cross-validate all counts and directions

This methodology ensures accurate arrow direction detection and precise transition counting for automotive process flow diagrams.
