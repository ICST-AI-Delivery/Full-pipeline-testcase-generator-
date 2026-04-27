# TECHNICAL SPECIFICATIONS ANALYSIS PROMPT
## Vision API Unified Template v2.0

### ANALYSIS OBJECTIVE
Analyze technical specification documents including interface specifications, requirement specifications, system specifications, and detailed technical documentation with focus on extracting actionable technical information for automotive development.

---

## ANALYSIS METHODOLOGY

### PHASE 1: SPECIFICATION TYPE IDENTIFICATION
**Identify the primary technical specification type:**
- **Interface Specifications**: API specs, protocol definitions, signal interfaces, communication diagrams
- **Requirement Specifications**: Functional requirements, non-functional requirements, acceptance criteria
- **System Specifications**: Technical system documentation, configuration specifications
- **Mixed Technical Documents**: Combination of specification types

### PHASE 2: TECHNICAL CONTENT ANALYSIS
**Analyze technical specification characteristics:**
- **Specification Domain**: Engine, transmission, safety, communication, HMI, diagnostic systems
- **Technical Complexity**: Simple, moderate, complex specification structures
- **Documentation Type**: Standards compliance, internal specifications, interface definitions
- **Information Density**: Text-heavy, table-heavy, diagram-heavy, mixed content

### PHASE 3: SPECIFICATION EXTRACTION
**Extract technical specifications systematically:**
- **Requirements**: Functional and non-functional requirements with acceptance criteria
- **Interfaces**: Communication protocols, signal definitions, data formats
- **Parameters**: Technical parameters, constraints, validation criteria
- **Standards**: Compliance requirements, regulatory standards, industry standards

### PHASE 4: VALIDATION AND COMPLIANCE ANALYSIS
**Analyze validation and compliance aspects:**
- **Test Criteria**: Acceptance criteria, validation methods, test conditions
- **Standards Compliance**: ISO 26262, AUTOSAR, ASPICE, automotive standards
- **Quality Requirements**: Performance, safety, reliability specifications
- **Traceability**: Requirement relationships, dependencies, hierarchies

### PHASE 5: TECHNICAL DATA STRUCTURING
**Structure extracted technical information:**
- **Specification Tables**: Requirements, interfaces, parameters, constraints
- **Validation Matrices**: Test cases, compliance verification, validation results
- **Technical Parameters**: Detailed technical specifications and characteristics
- **Implementation Guidelines**: Technical implementation and integration guidance

---

## OUTPUT FORMAT

### SPECIFICATION OVERVIEW
```
Specification Type: [Interface/Requirement/System/Mixed Technical Specifications]
Primary Domain: [Engine/Transmission/Safety/Communication/HMI/Diagnostic]
Specification Complexity: [Simple/Moderate/Complex]
Documentation Standard: [ISO/AUTOSAR/ASPICE/Internal/Mixed]
```

### TECHNICAL SPECIFICATIONS EXTRACTION
```
SPECIFICATION CATEGORIES:
- Requirements: [Count] functional, [Count] non-functional, [Count] safety requirements
- Interfaces: [Count] communication interfaces, [Count] signal definitions
- Parameters: [Count] technical parameters, [Count] constraints
- Standards: [Count] compliance requirements, [Count] validation criteria

CRITICAL SPECIFICATIONS:
- Safety-Critical: [List of ASIL-rated specifications]
- Performance-Critical: [List of timing/performance specifications]
- Interface-Critical: [List of communication/interface specifications]
- Compliance-Critical: [List of regulatory/standard compliance specifications]
```

### REQUIREMENTS ANALYSIS
```
FUNCTIONAL REQUIREMENTS:
- REQ-[ID]: [Name] - [Description]
  - Priority: [Critical/High/Medium/Low]
  - Safety Level: [ASIL_D/C/B/A/QM]
  - Acceptance Criteria: [Specific measurable criteria]
  - Test Conditions: [Validation test conditions]
  - Constraints: [System/design constraints]

NON-FUNCTIONAL REQUIREMENTS:
- Performance Requirements: [Timing, throughput, capacity specifications]
- Safety Requirements: [Functional safety, operational safety specifications]
- Quality Requirements: [Reliability, availability, maintainability specifications]
- Constraint Requirements: [Design, resource, environmental constraints]
```

### INTERFACE SPECIFICATIONS
```
COMMUNICATION INTERFACES:
- Interface: [Name] - Protocol: [CAN/LIN/Ethernet/FlexRay/Other]
  - Baud Rate: [Communication speed]
  - Data Format: [Frame format and structure]
  - Direction: [Input/Output/Bidirectional]
  - Priority: [High/Medium/Low/Critical]
  - Safety Level: [ASIL classification]

SIGNAL DEFINITIONS:
- Signal: [Name] - Interface: [Interface name]
  - Data Type: [uint8/uint16/uint32/float/boolean]
  - Unit: [Measurement unit]
  - Range: [Valid value range]
  - Resolution: [Signal precision]
  - Cycle Time: [Transmission frequency]
```

### TECHNICAL PARAMETERS
```
SYSTEM PARAMETERS:
- Parameter: [Name] - Type: [Configuration/Performance/Safety]
  - Value: [Parameter value or range]
  - Unit: [Measurement unit]
  - Tolerance: [Acceptable variation]
  - Validation Method: [How parameter is verified]
  - Impact: [System impact if out of range]

CONSTRAINTS AND LIMITATIONS:
- Constraint: [Name] - Type: [Resource/Environmental/Design]
  - Limitation: [Specific constraint details]
  - Impact Level: [Critical/High/Medium/Low]
  - Mitigation: [Constraint mitigation strategy]
  - Compliance: [Regulatory/standard compliance]
```

### VALIDATION AND COMPLIANCE
```
ACCEPTANCE CRITERIA:
- Criterion: [Description] - Method: [Validation method]
  - Pass Criteria: [Specific pass conditions]
  - Fail Criteria: [Specific fail conditions]
  - Test Environment: [Required test setup]
  - Validation Status: [Validated/Pending/Failed]

STANDARDS COMPLIANCE:
- Standard: [ISO 26262/AUTOSAR/ASPICE/Other]
  - Compliance Level: [Full/Partial/Non-compliant]
  - Verification Method: [Compliance verification approach]
  - Status: [Compliant/Under Review/Non-compliant]
  - Notes: [Compliance notes and deviations]
```

### AUTOMOTIVE CONTEXT ANALYSIS
```
AUTOMOTIVE APPLICATION:
- System Domain: [Engine/Transmission/Safety/Body/Infotainment]
- Vehicle Integration: [Integration requirements and considerations]
- Safety Classification: [ASIL levels and safety requirements]
- Performance Requirements: [Real-time, throughput, latency requirements]

DEVELOPMENT IMPLICATIONS:
- Implementation Complexity: [Simple/Moderate/Complex]
- Integration Requirements: [System integration needs]
- Testing Requirements: [Validation and verification needs]
- Compliance Requirements: [Regulatory and standard compliance]
```

### QUALITY ASSESSMENT
```
SPECIFICATION COMPLETENESS:
- Requirements Coverage: [Complete/Partial/Incomplete]
- Interface Definition: [Complete/Partial/Incomplete]
- Parameter Specification: [Complete/Partial/Incomplete]
- Validation Criteria: [Complete/Partial/Incomplete]

TECHNICAL CLARITY:
- Specification Clarity: [Clear/Acceptable/Unclear]
- Parameter Definition: [Precise/Acceptable/Vague]
- Validation Methods: [Well-defined/Acceptable/Unclear]
- Implementation Guidance: [Comprehensive/Basic/Insufficient]
```

---

## SPECIALIZED ANALYSIS TECHNIQUES

### REQUIREMENT ANALYSIS
- Extract functional and non-functional requirements with complete specifications
- Identify acceptance criteria and validation methods
- Map requirement relationships and dependencies
- Assess requirement completeness and testability

### INTERFACE ANALYSIS
- Document communication protocols and signal definitions
- Extract interface parameters and constraints
- Analyze interface relationships and dependencies
- Validate interface specifications against standards

### PARAMETER EXTRACTION
- Identify all technical parameters with values and units
- Document constraints and limitations
- Extract validation methods and criteria
- Assess parameter completeness and accuracy

### COMPLIANCE VERIFICATION
- Map specifications to automotive standards
- Identify compliance requirements and gaps
- Document validation and verification methods
- Assess overall compliance status

---

## CRITICAL ANALYSIS POINTS

### TECHNICAL ACCURACY
- Verify technical parameter specifications and units
- Check consistency between related specifications
- Validate interface definitions and protocols
- Ensure requirement completeness and clarity

### AUTOMOTIVE RELEVANCE
- Assess specifications against automotive standards
- Evaluate safety and performance requirements
- Consider vehicle integration implications
- Validate compliance with regulatory requirements

### IMPLEMENTATION READINESS
- Evaluate specification completeness for implementation
- Assess technical feasibility and constraints
- Identify integration and testing requirements
- Consider development and validation implications

This unified prompt combines interface and requirement specification analysis into a comprehensive technical specification analysis framework, ensuring complete coverage of all technical documentation types while maintaining focus on automotive development needs.
