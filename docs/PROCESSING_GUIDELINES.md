# Picture Analyze Agent - Processing Guidelines

**Document Version:** 1.1.0  
**Created:** 2026-01-29  
**Last Updated:** 2026-02-10 13:42:00
**Author:** Picture Analyze Agent Development Team  
**Status:** Active Guidelines  

## Overview

This document establishes standardized guidelines for processing Ferrari SRS FPI documents using the Picture Analyze Agent, ensuring consistent application of the latest enhancements across all future analyses.

## Template Selection Guidelines

### **Detailed Template (v2.3.0)**
**Use When:**
- FPI contains 4+ images requiring comprehensive documentation
- State Event Matrices present requiring complete signal mapping
- Safety-critical systems (ADAS, telltales) requiring full traceability
- Complex multi-condition tables needing detailed analysis
- Complete engineering validation required

**Processing Time:** 10-20 minutes per FPI  
**Output:** Full technical documentation with complete validation checklists

### **Concise Template (v3.2.0)**
**Use When:**
- FPI contains 1-3 images requiring essential analysis only
- Quick validation needed without extensive documentation
- Simple configuration tables or basic icons
- Preliminary analysis before detailed processing
- Time-constrained processing scenarios

**Processing Time:** 5-10 minutes per FPI  
**Output:** Streamlined analysis with essential validation items

## State Event Matrix Processing

### **Automatic Recognition Criteria**
- **Input Signals**: 5 signals shown in top section of diagram
- **Output Signals**: 5 signals shown in bottom section of diagram  
- **Matrix Structure**: Clear input → output relationship mapping
- **Signal Values**: Binary (0/1) or enumerated values
- **State Logic**: Complete combinations covering system behavior

### **Processing Standards**
- **Extract All Combinations**: Include all 32 possible states (2^5)
- **State Descriptions**: Provide human-readable descriptions for each combination
- **Signal Definitions**: Complete definition of all input and output signals
- **Engineering Format**: Structure for direct embedded system implementation
- **Validation Ready**: Format suitable for logic verification and testing

### **Quality Requirements**
- **OCR Confidence**: Minimum 94% for matrix structure recognition
- **Signal Accuracy**: 100% accuracy in input/output signal identification  
- **State Completeness**: All possible combinations documented
- **Description Quality**: Clear, engineering-appropriate state descriptions

## Inline Table Data Standards

### **Mandatory Implementation**
- **All Tables**: Every extracted table must be included inline in TXT file
- **Complete Data**: Full table content, not summaries or samples
- **Formatted Display**: Clear column separators and row organization
- **Human Readable**: Immediate review without external file dependencies
- **CSV Compatibility**: Maintain parallel CSV-ready format references

### **Table Formatting Standards**
```
TABLE DATA X: [Table Name] (from imageX.png)
Purpose: [Clear description of table purpose]

Column_1 | Column_2 | Column_3
---------|----------|----------
Value_1  | Value_2  | Value_3
Value_A  | Value_B  | Value_C
```

### **State Matrix Formatting Standards**
```
STATE EVENT MATRIX: [Matrix Name] (from imageX.png)
Purpose: [Input/output signal mapping description]

Input_1 | Input_2 || Output_1 | Output_2 | State_Description
--------|---------||---------|---------|-----------------
   0    |   0     ||    0    |    0    | [Clear state name]
   1    |   0     ||    1    |    0    | [Clear state name]

Signal Definitions:
Input Signals: [Define each signal and values]
Output Signals: [Define each signal and values]
```

## Image Classification Guidelines

### **1. TELLTALE ICONS & INDICATORS (30% of images)**
- **Enhancement Focus**: Brightness, contrast, edge definition for dashboard visibility
- **Color Analysis**: Precise hex color specifications required
- **Symbol Recognition**: Automated identification of standard automotive symbols
- **Ferrari Compliance**: Validate against automotive telltale standards
- **Documentation**: Design analysis with color codes and dimensions

### **2. CONFIGURATION TABLES (25% of images)**
- **OCR Optimization**: Enhance for 95%+ text extraction accuracy
- **Structure Recognition**: Clear column/row boundaries and headers
- **Data Validation**: Verify extracted data against visual content
- **CSV Preparation**: Format for immediate Excel import capability
- **Parameter Extraction**: Complete capture of configuration parameters and values

### **3. HMI DISPLAY LAYOUTS (15% of images)**
- **Layout Analysis**: Document dashboard interfaces, gauge clusters, and screen designs
- **UI Element Recognition**: Identify interactive components, visual hierarchies
- **Design Documentation**: Capture wireframes, mockups, and interface specifications
- **Interaction Flow**: Map user interface navigation and element relationships
- **Visual Hierarchy**: Document information organization and presentation patterns

### **4. STATE EVENT MATRICES (10% of images)**
- **Pattern Recognition**: Identify grid-based input/output structure automatically
- **Signal Extraction**: Complete mapping of all input/output relationships
- **Logic Documentation**: All state combinations with descriptions
- **Implementation Format**: Ready for embedded system development
- **Matrix Validation**: Verify completeness of state transition mappings

### **5. MULTI-CONDITION LOGIC TABLES (8% of images)**
- **Logic Parsing**: Extract complex AND/OR conditional relationships
- **Decision Matrix**: Document multi-variable decision logic
- **Condition Extraction**: Capture all logical conditions and outcomes
- **Validation Logic**: Verify logical consistency and completeness
- **Implementation Ready**: Format for software logic implementation

### **6. SYSTEM ARCHITECTURE DIAGRAMS (5% of images)**
- **Component Analysis**: Identify system components and relationships
- **Data Flow Mapping**: Document information exchange patterns
- **System Boundaries**: Define system interfaces and boundaries
- **Architecture Documentation**: Capture high-level system design
- **Flow Analysis**: Document data pathways and information exchange

### **7. PROCESS FLOW DIAGRAMS (3% of images)**
- **Flow Analysis**: Document decision trees and process sequences
- **Sequential Logic**: Capture step-by-step process flows
- **Decision Points**: Identify and document decision criteria
- **Process Validation**: Verify flow completeness and logic
- **Implementation Format**: Ready for process automation

### **8. TECHNICAL SPECIFICATIONS (2% of images)**
- **Parameter Extraction**: Capture technical parameters and specifications
- **Measurement Documentation**: Record performance characteristics
- **Specification Validation**: Verify technical accuracy and completeness
- **Standards Compliance**: Validate against automotive standards
- **Engineering Format**: Structure for technical implementation

### **9. WIRING & SIGNAL DIAGRAMS (1% of images)**
- **Connection Mapping**: Document electrical connections and signal routing
- **Signal Identification**: Capture signal names, types, and characteristics
- **Wiring Documentation**: Complete electrical connection specifications
- **Signal Validation**: Verify signal integrity and routing accuracy
- **Implementation Ready**: Format for electrical system implementation

### **10. TIMING DIAGRAMS (1% of images)**
- **Timing Analysis**: Extract signal timing sequences and relationships
- **Waveform Documentation**: Capture signal timing characteristics
- **Protocol Analysis**: Document communication protocol timing
- **Timing Validation**: Verify timing accuracy and completeness
- **Implementation Format**: Ready for timing-critical system development

### **11. TABLE + TELLTALES (2% of images)**
- **Hybrid Processing**: Combined table structure and symbol recognition
- **Contextual Mapping**: Link tabular parameters with visual indicators
- **Symbol Integration**: Process embedded telltale symbols within tables
- **Relationship Documentation**: Capture parameter-indicator relationships
- **Validation Logic**: Verify consistency between table data and symbols

## Quality Assurance Requirements

### **Processing Validation**
- **Image Enhancement**: 100% success rate across all images
- **OCR Confidence**: Minimum 95% for tables, 94% for state matrices
- **Requirement Mapping**: 100% traceability between images and requirements
- **Data Integrity**: Complete accuracy in extracted table data
- **Format Consistency**: Adherence to standardized output structure

### **Ferrari Compliance Checks**
- **Design Standards**: All visual elements validated against automotive standards
- **Color Specifications**: Accurate hex codes for telltales and indicators
- **Safety Requirements**: ADAS and safety-critical systems meet standards
- **Technical Precision**: CAN signals, telltale codes, system behaviors accurate

### **Documentation Standards**
- **Complete Coverage**: All images with linked requirements documented
- **Clear Traceability**: Explicit image-to-requirement relationships
- **Enhancement Details**: Processing applied to each image documented
- **Validation Ready**: Human review checkpoints and quality metrics provided

## Processing Workflow Standards

### **Phase 1: Discovery**
1. **FPI Analysis**: Identify all images and classify using 11-category system
2. **Content Type Classification**: Apply automated classification rules
3. **Requirement Filtering**: Include only visual-linked requirements
4. **Template Selection**: Choose detailed vs concise based on complexity
5. **Quality Pre-Assessment**: Evaluate image clarity and processing readiness

### **Phase 2: Enhancement**
1. **Content-Specific Processing**: Apply appropriate algorithms per 11 image categories
2. **OCR Optimization**: Enhance for text extraction readiness
3. **Matrix Recognition**: Identify and prepare state event matrices
4. **Hybrid Content Processing**: Special handling for Table + Telltales combinations
5. **UI Layout Enhancement**: Optimize HMI display layouts and UI designs
6. **Architecture Diagram Processing**: Enhance system architecture and data flow diagrams
7. **Quality Validation**: Verify enhancement success before extraction

### **Phase 3: Extraction**
1. **Category-Specific Processing**: Apply extraction methods per content type
2. **Table Processing**: Extract all tabular data with inline formatting
3. **State Matrix Processing**: Complete signal mapping extraction
4. **HMI Layout Processing**: Extract UI elements, layouts, and interaction flows
5. **Architecture Processing**: Extract component relationships and data flows
6. **Hybrid Processing**: Handle Table + Telltales with combined extraction
7. **Technical Analysis**: Color codes, dimensions, compliance validation
8. **Data Validation**: Verify extracted content against original images

### **Phase 4: Documentation**
1. **Structured Output**: Generate complete analysis with inline tables
2. **Requirement Mapping**: Establish complete traceability documentation
3. **Validation Preparation**: Format for human engineering review
4. **Quality Metrics**: Document processing success and confidence levels

## Error Handling and Escalation

### **OCR Confidence Below Threshold**
- **Action**: Flag for manual review and validation
- **Documentation**: Note confidence levels and potential accuracy issues
- **Escalation**: Engineering team review for critical data

### **State Matrix Recognition Failure**
- **Action**: Process as standard diagram with enhanced documentation
- **Documentation**: Note recognition attempt and fallback processing
- **Escalation**: Technical team review for algorithm improvement

### **Ferrari Compliance Issues**
- **Action**: Document deviations and flag for compliance review
- **Documentation**: Specific compliance concerns and recommendations
- **Escalation**: Quality assurance team validation required

## Continuous Improvement

### **Feedback Integration**
- **Processing Metrics**: Track success rates and quality indicators
- **User Feedback**: Incorporate engineering team validation results
- **Template Updates**: Enhance templates based on processing learnings
- **Algorithm Refinement**: Improve enhancement and extraction techniques

### **Version Control**
- **Template Versioning**: Maintain compatibility between template versions
- **Processing Standards**: Document changes to processing approaches
- **Quality Evolution**: Track improvement in processing accuracy over time
- **Documentation Updates**: Keep guidelines current with latest capabilities

---

## Compliance Checklist

For every FPI analysis, ensure:

- [ ] Appropriate template selected based on complexity
- [ ] All images classified using 11-category system
- [ ] Content-specific algorithms applied per image category
- [ ] State Event Matrices processed with complete signal mapping
- [ ] HMI Display Layouts processed with UI element extraction
- [ ] System Architecture Diagrams processed with data flow analysis
- [ ] Table + Telltales processed with hybrid extraction methods
- [ ] All table data embedded inline in TXT file
- [ ] Ferrari compliance validated for all visual elements
- [ ] Complete requirement traceability established
- [ ] OCR confidence levels meet minimum thresholds
- [ ] Processing documentation complete and accurate
- [ ] Validation checkpoints prepared for human review
- [ ] Quality metrics documented for continuous improvement

---

**Document Status:** Active Guidelines  
**Next Review:** 2026-04-10
**Approval:** Picture Analyze Agent Development Team
