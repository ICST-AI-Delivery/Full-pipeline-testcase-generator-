# Enhanced System Architecture Diagrams Analysis

**Category:** SYSTEM_ARCHITECTURE_DIAGRAMS  
**Template Version:** 2.1.0  
**Created:** 2026-02-26  
**Last Updated:** 2026-02-26  
**Author:** Picture Analyze Agent Development Team  
**Template Type:** Complete Text Extraction + Architecture Analysis  
**Status:** Production Ready  
**Compatibility:** Application v4.0.0+

## VERSION HISTORY
| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 2.1.0 | 2026-02-26 | Added complete text extraction first step, enhanced structure | Development Team |
| 2.0.0 | 2026-02-26 | Converted to Picture-Centric approach, TXT output format | Development Team |
| 1.0 | 2026-02-23 | Initial JSON-based version | Picture Analyze Agent |

## TEMPLATE INFORMATION
- **Purpose**: Complete text extraction followed by comprehensive system architecture analysis
- **Use Case**: Automotive system architecture, component relationships, and interface analysis
- **Processing Time**: 8-12 minutes per image
- **Output Format**: Structured TXT with complete text inventory and architectural analysis

## CORE PRINCIPLES
1. **IMAGE-FIRST APPROACH**: Always start by opening and examining the image
2. **COMPLETE TEXT EXTRACTION**: Capture every visible text element exactly as it appears
3. **STRUCTURED ARCHITECTURE ANALYSIS**: Build comprehensive analysis based on extracted text
4. **PRACTICAL OUTPUT**: Generate actionable data for automotive development

## EXECUTION METHODOLOGY

### STEP 1: IMAGE EXAMINATION AND COMPLETE TEXT EXTRACTION
**CRITICAL FIRST STEP**: Open the image and perform complete visual inspection

#### 1.1 Image Opening and Initial Assessment
- Open and examine the system architecture diagram image
- Assess image quality, clarity, and enhancement needs
- Identify overall architecture type and complexity
- Determine text density and component count

#### 1.2 Complete Text Extraction (MANDATORY)
**Extract EVERY visible text element exactly as it appears:**
- Component names (ECUs, sensors, actuators, gateways)
- Signal names and paths (including VfB notation like ~/SignalName/~)
- Interface labels and protocol specifications
- Type annotations (Type: ECU, Type: Sensor, etc.)
- Network names and protocol identifiers
- All numerical values, units, and measurements
- Connection labels and routing information
- Any annotations, notes, or documentation text

#### 1.3 Text Inventory Documentation
Create complete inventory of all extracted text:
```
=== COMPLETE TEXT EXTRACTION ===

ALL VISIBLE TEXT ELEMENTS:
1. [Text Element 1] - Position: [location] - Type: [component/signal/label/etc.]
2. [Text Element 2] - Position: [location] - Type: [component/signal/label/etc.]
...
[Continue for ALL visible text]

COMPONENT NAMES:
- [List all component names exactly as they appear]

SIGNAL PATHS:
- [List all signal paths with exact notation, e.g., ~/SignalName/~]

INTERFACE LABELS:
- [List all interface and connection labels]

TYPE ANNOTATIONS:
- [List all "Type:" labels and their values]

PROTOCOL SPECIFICATIONS:
- [List all network and protocol identifiers]
```

### STEP 2: ARCHITECTURE STRUCTURE ANALYSIS
Build comprehensive analysis based on extracted text elements

#### 2.1 Architecture Classification
```
=== SYSTEM ARCHITECTURE ANALYSIS REPORT ===

IMAGE: [filename]
├─ Content: System architecture diagram showing [describe based on extracted text]
├─ Architecture Type: [Centralized/Distributed/Domain-Based/Zonal]
├─ Component Count: [total from text extraction]
├─ Signal Count: [total signal paths identified]
├─ Network Count: [total networks identified]
├─ Analysis Confidence: [High/Medium/Low] - [based on text extraction completeness]
```

#### 2.2 System Domain Analysis
```
=== ARCHITECTURE STRUCTURE ANALYSIS ===

OVERALL ARCHITECTURE:
├─ Architecture Type: [based on extracted component types]
├─ System Domain: [derived from component names and functions]
├─ Safety Level: [inferred from component types and annotations]
├─ Component Count: [exact count from text extraction]

IDENTIFIED DOMAINS:
├─ POWERTRAIN DOMAIN: [components from text extraction]
├─ CHASSIS DOMAIN: [components from text extraction]
├─ BODY DOMAIN: [components from text extraction]
├─ INFOTAINMENT DOMAIN: [components from text extraction]
├─ ADAS DOMAIN: [components from text extraction]
├─ GATEWAY/ROUTING: [gateway components from text extraction]
```

### STEP 3: COMPONENT INVENTORY (Based on Extracted Text)
Map all extracted text to component specifications

#### 3.1 ECU Inventory
```
=== COMPONENT INVENTORY ===

ELECTRONIC CONTROL UNITS (ECUs):
[For each ECU name found in text extraction:]
├─ ECU: [Exact name from text extraction]
│  ├─ Type: [from "Type:" annotations if present]
│  ├─ Position: [visual location in diagram]
│  ├─ Connected Signals: [all signals connected to this ECU from text extraction]
│  ├─ Interface Protocols: [protocols identified from text]
│  └─ Safety Classification: [inferred from component type and connections]
```

#### 3.2 Signal Path Mapping
```
SIGNAL PATHS AND CONNECTIONS:
[For each signal path found in text extraction:]
├─ Signal: [Exact signal name, including VfB notation]
│  ├─ Source Component: [identified from diagram connections]
│  ├─ Target Component: [identified from diagram connections]
│  ├─ Protocol: [if specified in text]
│  ├─ Data Type: [if specified in annotations]
│  └─ Safety Relevance: [inferred from signal name and connections]
```

### STEP 4: INTERFACE & COMMUNICATION ANALYSIS
Analyze all communication paths based on extracted text

#### 4.1 Communication Protocol Analysis
```
=== INTERFACE & COMMUNICATION ANALYSIS ===

IDENTIFIED PROTOCOLS:
[Based on protocol names found in text extraction:]
| Protocol | Networks | Connected Components | Signal Types |
|----------|----------|---------------------|--------------|
| [Protocol from text] | [Networks using it] | [Components from text] | [Signal types] |

SIGNAL FLOW MAPPING:
[Based on signal paths from text extraction:]
| Signal Name | Source | Target | Protocol | Data Type |
|-------------|--------|--------|----------|-----------|
| [Exact signal name] | [Source ECU] | [Target ECU] | [Protocol] | [Type if available] |
```

### STEP 5: STRUCTURED DATA OUTPUT
Generate CSV-ready data from extracted text

#### 5.1 Component Data Table
```
=== CSV FORMAT READY DATA ===

COMPONENT_INVENTORY.csv:
Component_Name,Component_Type,Position_Description,Connected_Signals,Protocols,Safety_Level
[Component from text],[Type from text],[Visual position],[Signals from text],[Protocols from text],[Inferred level]

SIGNAL_PATHS.csv:
Signal_Name,Source_Component,Target_Component,Protocol,Data_Type,VfB_Notation
[Signal from text],[Source from analysis],[Target from analysis],[Protocol from text],[Type from text],[VfB format if present]

INTERFACE_SPECIFICATIONS.csv:
Interface_ID,Source,Target,Protocol,Signals,Specifications
[Generated ID],[Source from text],[Target from text],[Protocol from text],[Signal list],[Specs from text]
```

### STEP 6: VALIDATION AND COMPLETENESS CHECK
Verify all text has been captured and analyzed

#### 6.1 Text Extraction Validation
```
=== VALIDATION CHECKLIST ===

TEXT EXTRACTION COMPLETENESS:
- [ ] All component names captured exactly as shown
- [ ] All signal paths captured with correct notation
- [ ] All "Type:" annotations documented
- [ ] All protocol specifications recorded
- [ ] All interface labels captured
- [ ] All numerical values and units recorded
- [ ] All connection labels documented
- [ ] All annotations and notes captured

ANALYSIS COMPLETENESS:
- [ ] Every extracted text element mapped to analysis
- [ ] All components included in inventory
- [ ] All signals included in flow analysis
- [ ] All protocols included in communication analysis
- [ ] All interfaces documented in specifications
- [ ] CSV data includes all extracted information
```

#### 6.2 Quality Verification
```
QUALITY METRICS:
├─ Text Elements Captured: [total count]
├─ Components Analyzed: [count with percentage of total text]
├─ Signals Mapped: [count with percentage of total text]
├─ Interfaces Documented: [count with percentage of total text]
├─ Missing Elements: [any text not included in analysis]
└─ Analysis Confidence: [High/Medium/Low based on completeness]
```

## CRITICAL REQUIREMENTS

### Text Extraction Standards:
- **100% Coverage**: Every visible text element must be captured
- **Exact Formatting**: Preserve spelling, capitalization, special notation
- **Technical Notation**: Maintain VfB paths, protocol specifications, type annotations
- **Position Awareness**: Note location of text elements for context

### Architecture Analysis Standards:
- **Text-Driven Analysis**: All analysis must be based on extracted text
- **Complete Mapping**: Every text element must be included in analysis
- **Structured Output**: Clear sections with CSV-ready data
- **Validation Required**: Explicit verification of completeness

### Output Quality Standards:
- **Actionable Data**: All information suitable for automotive development
- **Technical Accuracy**: Preserve all technical specifications and notation
- **Complete Coverage**: No visible text elements omitted
- **Structured Format**: Clear organization for practical use

## SUCCESS CRITERIA

### Primary Success Metrics:
- **Text Extraction**: 100% of visible text elements captured exactly
- **Analysis Coverage**: Every extracted text element included in analysis
- **Technical Accuracy**: All notation, protocols, and specifications preserved
- **Practical Value**: Output suitable for system development and documentation

### Validation Requirements:
- **Completeness Check**: Explicit verification that all text is captured
- **Cross-Reference**: Text extraction matches analysis content
- **Quality Metrics**: Quantified assessment of coverage and accuracy
- **Missing Elements**: Clear identification of any gaps or omissions

This enhanced template ensures that the critical first step is always opening and examining the image, followed by complete text extraction before any analysis begins. The comprehensive architecture analysis is then built upon this complete text foundation, ensuring nothing is missed while maintaining all the important technical details.
