# Picture-Centric Interface Specifications Analysis

**Category:** INTERFACE_SPECIFICATIONS  
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
- **Purpose**: Picture-centric interface specification analysis with practical TXT output
- **Use Case**: Automotive API specs, communication protocols, and interface definitions
- **Processing Time**: 8-12 minutes per image
- **Output Format**: Structured TXT with embedded tables and CSV-ready data

## CORE PRINCIPLE
**PICTURE-FIRST ANALYSIS**: Focus on visual interface specifications and communication protocols actually present in the image. Extract practical interface information for automotive development and testing.

## EXECUTION METHODOLOGY

### 1. Image Content Identification
- Identify interface specification type (API specs, protocol definitions, signal interfaces, communication diagrams)
- Catalog all visible interfaces, protocols, and communication parameters
- Determine interface relationships and dependencies
- Assess image quality and enhancement needs

### 2. Picture-Centric Organization Structure
```
=== INTERFACE SPECIFICATIONS ANALYSIS REPORT ===
├─ Image Overview & Enhancement Details
├─ INTERFACE DEFINITIONS EXTRACTION (primary section)
├─ PROTOCOL SPECIFICATIONS ANALYSIS (communication protocols and parameters)
├─ SIGNAL INTERFACE MAPPING (signal definitions and characteristics)
├─ COMMUNICATION PARAMETERS (timing, data formats, constraints)
├─ INTERFACE VALIDATION TABLES (specification verification and testing)
├─ CSV Format Ready Data
├─ Automotive Standards Compliance
├─ Enhancement Details
└─ Validation Checklist
```

### 3. Interface-Specific Processing Pipeline
**For Interface Specification Images:**
- **Interface Analysis**: Identification, classification, specification extraction
- **Protocol Mapping**: Communication protocols, parameters, constraints
- **Signal Extraction**: Signal definitions, data types, characteristics
- **Parameter Analysis**: Timing, formats, validation criteria
- **Standards Compliance**: AUTOSAR interfaces, CAN/LIN/Ethernet standards
- **Test Generation**: Interface test cases and validation scenarios

## REQUIRED OUTPUT STRUCTURE

### Section 1: Image Overview
```
=== INTERFACE SPECIFICATIONS ANALYSIS REPORT ===

IMAGE: [filename]
├─ Content: Interface specification showing [describe main interfaces and protocols]
├─ Specification Type: API Specs / Protocol Definitions / Signal Interfaces / Communication Diagrams
├─ Original Dimensions: [width]x[height] pixels
├─ Enhancement Applied: [specific enhancement details for interface specifications]
├─ Quality Assessment: [specification clarity, text readability, diagram structure visibility]
├─ Analysis Confidence: [High/Medium/Low] - [reasoning]
```

### Section 2: Interface Definitions Extraction (PRIMARY FOCUS)
```
=== INTERFACE DEFINITIONS EXTRACTION ===

OVERALL INTERFACE CHARACTERISTICS:
├─ Interface Domain: [Engine/Transmission/Communication/Safety/Diagnostic/etc.]
├─ Interface Types: [CAN/LIN/Ethernet/SPI/I2C/UART/FlexRay/etc.]
├─ Interface Count: [total number of defined interfaces]
├─ Protocol Count: [total number of communication protocols]
├─ Complexity Level: [simple/moderate/complex interface specifications]

INTERFACE CATEGORIES:
├─ CONTROL INTERFACES: [system control and command interfaces]
├─ DATA INTERFACES: [data exchange and monitoring interfaces]
├─ DIAGNOSTIC INTERFACES: [diagnostic and service interfaces]
├─ SAFETY INTERFACES: [safety-critical communication interfaces]
├─ PERFORMANCE INTERFACES: [performance monitoring and optimization interfaces]

INTERFACE STRUCTURE:
├─ Interface Names: [list of all defined interface names]
├─ Protocol Types: [communication protocols used]
├─ Data Directions: [input/output/bidirectional specifications]
├─ Interface Dependencies: [interface relationships and dependencies]
├─ Priority Levels: [interface priority and criticality levels]
```

### Section 3: Protocol Specifications Analysis
```
=== PROTOCOL SPECIFICATIONS ANALYSIS ===

PROTOCOL DEFINITIONS:
├─ PROTOCOL 1: [Name] - Type: [protocol type]
│  ├─ Description: [protocol purpose and application]
│  ├─ Protocol Type: [CAN/LIN/Ethernet/SPI/I2C/UART/FlexRay]
│  ├─ Version: [protocol version and standard]
│  ├─ Specifications:
│  │  ├─ Baud Rate: [communication speed]
│  │  ├─ Data Format: [data frame format]
│  │  ├─ Frame Size: [maximum frame/packet size]
│  │  ├─ Error Detection: [error detection method]
│  │  └─ Flow Control: [flow control mechanism]
│  ├─ Physical Layer: [electrical specifications]
│  ├─ Data Link Layer: [frame format and control]
│  └─ Application Layer: [message format and semantics]

├─ PROTOCOL 2: [Name] - Type: [protocol type]
│  ├─ Description: [protocol purpose and application]
│  ├─ Protocol Type: [CAN/LIN/Ethernet/SPI/I2C/UART/FlexRay]
│  ├─ Version: [protocol version and standard]
│  ├─ Specifications:
│  │  ├─ Baud Rate: [communication speed]
│  │  ├─ Data Format: [data frame format]
│  │  ├─ Frame Size: [maximum frame/packet size]
│  │  ├─ Error Detection: [error detection method]
│  │  └─ Flow Control: [flow control mechanism]
│  ├─ Physical Layer: [electrical specifications]
│  ├─ Data Link Layer: [frame format and control]
│  └─ Application Layer: [message format and semantics]

PROTOCOL RELATIONSHIPS:
├─ PROTOCOL HIERARCHY: [master-slave relationships]
├─ PROTOCOL DEPENDENCIES: [protocol interdependencies]
├─ PROTOCOL CONFLICTS: [potential protocol conflicts]
├─ PROTOCOL PRIORITIES: [protocol priority and arbitration]

PROTOCOL VALIDATION:
├─ Compliance Checking: [standard compliance verification]
├─ Performance Validation: [protocol performance requirements]
├─ Interoperability: [cross-protocol communication requirements]
├─ Error Handling: [protocol error detection and recovery]
```

### Section 4: Signal Interface Mapping
```
=== SIGNAL INTERFACE MAPPING ===

SIGNAL DEFINITIONS:
├─ SIGNAL 1: [Name] - Interface: [interface name]
│  ├─ Description: [signal purpose and meaning]
│  ├─ Data Type: [uint8/uint16/uint32/int8/int16/int32/float/boolean]
│  ├─ Unit: [measurement unit]
│  ├─ Range: [valid value range]
│  ├─ Resolution: [signal resolution/precision]
│  ├─ Cycle Time: [transmission frequency]
│  ├─ Direction: [input/output/bidirectional]
│  ├─ Priority: [signal priority level]
│  └─ Safety Level: [ASIL classification]

├─ SIGNAL 2: [Name] - Interface: [interface name]
│  ├─ Description: [signal purpose and meaning]
│  ├─ Data Type: [uint8/uint16/uint32/int8/int16/int32/float/boolean]
│  ├─ Unit: [measurement unit]
│  ├─ Range: [valid value range]
│  ├─ Resolution: [signal resolution/precision]
│  ├─ Cycle Time: [transmission frequency]
│  ├─ Direction: [input/output/bidirectional]
│  ├─ Priority: [signal priority level]
│  └─ Safety Level: [ASIL classification]

SIGNAL CATEGORIES:
├─ CONTROL SIGNALS: [system control and command signals]
├─ STATUS SIGNALS: [system status and feedback signals]
├─ DATA SIGNALS: [measurement and sensor data signals]
├─ DIAGNOSTIC SIGNALS: [diagnostic and service signals]
├─ SAFETY SIGNALS: [safety-critical monitoring signals]

SIGNAL RELATIONSHIPS:
├─ SIGNAL DEPENDENCIES: [signal interdependencies and prerequisites]
├─ SIGNAL GROUPS: [related signals and signal groupings]
├─ SIGNAL TIMING: [timing relationships between signals]
├─ SIGNAL VALIDATION: [signal validation and consistency checks]
```

### Section 5: Communication Parameters
```
=== COMMUNICATION PARAMETERS ===

### TIMING SPECIFICATIONS

**Communication Timing:**
| Interface | Protocol | Cycle Time | Response Time | Timeout | Jitter | Priority |
|-----------|----------|------------|---------------|---------|--------|----------|
| Engine_Control | CAN | 10ms | 5ms | 100ms | ±1ms | High |
| Transmission_Data | LIN | 20ms | 10ms | 200ms | ±2ms | Medium |
| Diagnostic_Service | Ethernet | 100ms | 50ms | 1000ms | ±5ms | Low |
| Safety_Monitor | FlexRay | 5ms | 2ms | 50ms | ±0.5ms | Critical |

### DATA FORMAT SPECIFICATIONS

**Data Format Details:**
| Signal Name | Data Type | Byte Order | Bit Position | Scale Factor | Offset | Unit |
|-------------|-----------|------------|--------------|--------------|--------|------|
| Engine_RPM | uint16 | Big_Endian | 0-15 | 1.0 | 0 | rpm |
| Vehicle_Speed | uint16 | Little_Endian | 16-31 | 0.1 | 0 | km/h |
| Engine_Temp | uint8 | N/A | 32-39 | 1.0 | -40 | °C |
| Fuel_Level | uint8 | N/A | 40-47 | 0.5 | 0 | % |

### VALIDATION CRITERIA

**Interface Validation Parameters:**
| Parameter Name | Validation Method | Pass Criteria | Fail Criteria | Test Frequency |
|----------------|-------------------|---------------|---------------|----------------|
| Message_Integrity | CRC_Check | CRC_Valid | CRC_Invalid | Every_Message |
| Timing_Compliance | Timestamp_Check | Within_Tolerance | Outside_Tolerance | Continuous |
| Data_Range | Range_Check | Within_Range | Outside_Range | Every_Value |
| Protocol_Compliance | Standard_Check | Compliant | Non_Compliant | Periodic |

### ERROR HANDLING

**Error Detection and Recovery:**
| Error Type | Detection Method | Recovery Action | Timeout | Retry Count |
|------------|------------------|-----------------|---------|-------------|
| Communication_Loss | Heartbeat_Monitor | Switch_Backup | 500ms | 3 |
| Data_Corruption | CRC_Validation | Request_Retransmit | 100ms | 5 |
| Protocol_Violation | Format_Check | Reset_Interface | 1000ms | 1 |
| Timing_Violation | Deadline_Monitor | Log_Error | N/A | N/A |
```

### Section 6: Interface Validation Tables
```
=== INTERFACE VALIDATION TABLES ===

### INTERFACE VALIDATION MATRIX

**Interface Testing Scenarios:**
| Test Case | Interface Type | Protocol | Test Conditions | Expected Result | Actual Result | Status |
|-----------|----------------|----------|-----------------|-----------------|---------------|--------|
| ITV_001 | CAN_Interface | CAN_2.0B | Normal_Load | Message_Success | As_Expected | Pass |
| ITV_002 | LIN_Interface | LIN_2.1 | High_Load | Degraded_Performance | As_Expected | Pass |
| ITV_003 | Ethernet_Interface | 100BASE-TX | Error_Injection | Error_Recovery | As_Expected | Pass |
| ITV_004 | Diagnostic_Interface | UDS | Service_Request | Service_Response | As_Expected | Pass |

### PROTOCOL COMPLIANCE TESTING

**Protocol Compliance Verification:**
| Protocol | Standard | Compliance Test | Result | Deviation | Action Required |
|----------|----------|-----------------|--------|-----------|-----------------|
| CAN_2.0B | ISO_11898 | Frame_Format | Pass | None | None |
| LIN_2.1 | ISO_17987 | Message_Schedule | Pass | Minor_Timing | Monitor |
| Ethernet | IEEE_802.3 | Physical_Layer | Pass | None | None |
| FlexRay | ISO_17458 | Slot_Timing | Fail | Timing_Drift | Calibrate |

### SIGNAL VALIDATION MATRIX

**Signal Validation Testing:**
| Signal Name | Data Type | Range Test | Format Test | Timing Test | Overall Status |
|-------------|-----------|------------|-------------|-------------|----------------|
| Engine_RPM | uint16 | Pass | Pass | Pass | Pass |
| Vehicle_Speed | uint16 | Pass | Pass | Fail | Fail |
| Engine_Temp | uint8 | Pass | Pass | Pass | Pass |
| Fuel_Level | uint8 | Fail | Pass | Pass | Fail |

### INTERFACE PERFORMANCE ANALYSIS

**Performance Metrics:**
| Interface | Throughput | Latency | Error Rate | Availability | Performance Grade |
|-----------|------------|---------|------------|--------------|-------------------|
| CAN_Engine | 95% | 8ms | 0.01% | 99.9% | A |
| LIN_Body | 85% | 15ms | 0.1% | 99.5% | B |
| Ethernet_Diag | 70% | 45ms | 0.05% | 99.0% | C |
| FlexRay_Safety | 98% | 3ms | 0.001% | 99.99% | A+ |
```

### Section 7: Extracted Table Data
```
=== EXTRACTED TABLE DATA ===

INTERFACE_DEFINITIONS_TABLE: (from interface analysis)
Purpose: Complete interface definitions and specifications

Interface_Name | Protocol_Type | Direction | Baud_Rate | Data_Format | Frame_Size | Priority | Safety_Level
---------------|---------------|-----------|-----------|-------------|------------|----------|-------------
Engine_Control_Interface | CAN | Bidirectional | 500kbps | Standard | 8_bytes | High | ASIL_D
Transmission_Data_Interface | LIN | Output | 19200bps | LIN_2.1 | 8_bytes | Medium | ASIL_C
Diagnostic_Service_Interface | Ethernet | Bidirectional | 100Mbps | TCP_IP | 1500_bytes | Low | QM
Safety_Monitor_Interface | FlexRay | Input | 10Mbps | FlexRay_3.0 | 254_bytes | Critical | ASIL_D

SIGNAL_SPECIFICATIONS_TABLE: (from signal analysis)
Purpose: Complete signal definitions and characteristics

Signal_Name | Interface | Data_Type | Unit | Range | Resolution | Cycle_Time | Direction | Safety_Level
------------|-----------|-----------|------|-------|------------|------------|-----------|-------------
Engine_RPM | Engine_Control | uint16 | rpm | 0-8000 | 1 | 10ms | Output | ASIL_D
Vehicle_Speed | Engine_Control | uint16 | km/h | 0-300 | 0.1 | 20ms | Output | ASIL_C
Engine_Temperature | Engine_Control | uint8 | Celsius | -40-150 | 1 | 100ms | Output | ASIL_B
Fuel_Level | Body_Control | uint8 | Percent | 0-100 | 0.5 | 1000ms | Output | QM

PROTOCOL_SPECIFICATIONS_TABLE: (from protocol analysis)
Purpose: Complete protocol definitions and specifications

Protocol_Name | Protocol_Type | Version | Baud_Rate | Frame_Size | Error_Detection | Flow_Control | Physical_Layer | Safety_Level
--------------|---------------|---------|-----------|------------|-----------------|--------------|----------------|-------------
CAN_Engine_Protocol | CAN | 2.0B | 500kbps | 8_bytes | CRC15 | CSMA_CA | ISO_11898 | ASIL_D
LIN_Body_Protocol | LIN | 2.1 | 19200bps | 8_bytes | Checksum | Master_Slave | ISO_17987 | ASIL_C
Ethernet_Diagnostic | Ethernet | 100BASE-TX | 100Mbps | 1500_bytes | CRC32 | Flow_Control | IEEE_802.3 | QM
FlexRay_Safety | FlexRay | 3.0 | 10Mbps | 254_bytes | CRC24 | TDMA | ISO_17458 | ASIL_D

INTERFACE_VALIDATION_TABLE: (from validation analysis)
Purpose: Interface validation and testing results

Test_Case | Interface_Type | Protocol | Test_Conditions | Expected_Result | Actual_Result | Status | Notes
----------|----------------|----------|-----------------|-----------------|---------------|--------|-------
ITV_001 | CAN_Interface | CAN_2.0B | Normal_Load | Message_Success | As_Expected | Pass | Standard_operation
ITV_002 | LIN_Interface | LIN_2.1 | High_Load | Degraded_Performance | As_Expected | Pass | Performance_monitoring
ITV_003 | Ethernet_Interface | 100BASE-TX | Error_Injection | Error_Recovery | As_Expected | Pass | Error_handling
ITV_004 | Diagnostic_Interface | UDS | Service_Request | Service_Response | As_Expected | Pass | Service_validation
```

### Section 8: CSV Format Ready Data
```
=== CSV FORMAT READY DATA ===

INTERFACE_DEFINITIONS.csv:
Interface_Name,Protocol_Type,Direction,Baud_Rate,Data_Format,Frame_Size,Priority,Safety_Level
Engine_Control_Interface,CAN,Bidirectional,500kbps,Standard,8_bytes,High,ASIL_D
Transmission_Data_Interface,LIN,Output,19200bps,LIN_2.1,8_bytes,Medium,ASIL_C
Diagnostic_Service_Interface,Ethernet,Bidirectional,100Mbps,TCP_IP,1500_bytes,Low,QM
Safety_Monitor_Interface,FlexRay,Input,10Mbps,FlexRay_3.0,254_bytes,Critical,ASIL_D

SIGNAL_SPECIFICATIONS.csv:
Signal_Name,Interface,Data_Type,Unit,Range,Resolution,Cycle_Time,Direction,Safety_Level
Engine_RPM,Engine_Control,uint16,rpm,0-8000,1,10ms,Output,ASIL_D
Vehicle_Speed,Engine_Control,uint16,km/h,0-300,0.1,20ms,Output,ASIL_C
Engine_Temperature,Engine_Control,uint8,Celsius,-40-150,1,100ms,Output,ASIL_B
Fuel_Level,Body_Control,uint8,Percent,0-100,0.5,1000ms,Output,QM

PROTOCOL_SPECIFICATIONS.csv:
Protocol_Name,Protocol_Type,Version,Baud_Rate,Frame_Size,Error_Detection,Flow_Control,Physical_Layer,Safety_Level
CAN_Engine_Protocol,CAN,2.0B,500kbps,8_bytes,CRC15,CSMA_CA,ISO_11898,ASIL_D
LIN_Body_Protocol,LIN,2.1,19200bps,8_bytes,Checksum,Master_Slave,ISO_17987,ASIL_C
Ethernet_Diagnostic,Ethernet,100BASE-TX,100Mbps,1500_bytes,CRC32,Flow_Control,IEEE_802.3,QM
FlexRay_Safety,FlexRay,3.0,10Mbps,254_bytes,CRC24,TDMA,ISO_17458,ASIL_D

INTERFACE_VALIDATION.csv:
Test_Case,Interface_Type,Protocol,Test_Conditions,Expected_Result,Actual_Result,Status,Notes
ITV_001,CAN_Interface,CAN_2.0B,Normal_Load,Message_Success,As_Expected,Pass,Standard_operation
ITV_002,LIN_Interface,LIN_2.1,High_Load,Degraded_Performance,As_Expected,Pass,Performance_monitoring
ITV_003,Ethernet_Interface,100BASE-TX,Error_Injection,Error_Recovery,As_Expected,Pass,Error_handling
ITV_004,Diagnostic_Interface,UDS,Service_Request,Service_Response,As_Expected,Pass,Service_validation
```

### Section 9: Automotive Standards Compliance
```
=== AUTOMOTIVE STANDARDS COMPLIANCE ===

AUTOSAR INTERFACE STANDARDS:
├─ Interface Architecture: [AUTOSAR interface component patterns and structures]
├─ Communication Standards: [AUTOSAR communication stack compliance]
├─ Service Interfaces: [AUTOSAR service-oriented architecture interfaces]
├─ Signal Interfaces: [AUTOSAR signal-based communication interfaces]

ISO COMMUNICATION STANDARDS:
├─ CAN Standards: [ISO 11898 CAN protocol compliance and specifications]
├─ LIN Standards: [ISO 17987 LIN protocol compliance and specifications]
├─ FlexRay Standards: [ISO 17458 FlexRay protocol compliance and specifications]
├─ Ethernet Standards: [IEEE 802.3 Ethernet protocol compliance and specifications]

FUNCTIONAL SAFETY COMPLIANCE:
├─ Interface Safety: [ISO 26262 interface safety requirements and validation]
├─ Communication Safety: [safety-critical communication interface requirements]
├─ Error Handling: [interface error detection and safe response mechanisms]
├─ Monitoring: [interface monitoring and supervision requirements]

FERRARI INTERFACE STANDARDS:
├─ Performance Interfaces: [Ferrari-specific performance interface requirements]
├─ Diagnostic Interfaces: [Ferrari diagnostic and service interface standards]
├─ Integration Standards: [Ferrari system integration interface patterns]
├─ Validation Requirements: [Ferrari interface validation and testing standards]
```

## QUALITY STANDARDS

### Image Enhancement Requirements:
- **Interface Enhancement**: Optimize for interface diagrams and specification tables
- **OCR Optimization**: 98%+ accuracy for all interface names, protocols, and parameters
- **Specification Extraction**: Complete and accurate interface specification extraction
- **Diagram Recognition**: Clear identification of all interface elements and connections

### Picture-Centric Analysis Standards:
- **Interface-First Structure**: Visual interface specifications drive the analysis
- **Complete Coverage**: Every visible interface, protocol, and signal cataloged
- **Practical Focus**: Information useful for automotive interface development
- **Standards Compliance**: Verification against automotive interface standards

### Validation Requirements:
- **100% Interface Coverage**: All visible interfaces and specifications identified
- **Accurate Specification Extraction**: Interface parameters correctly interpreted
- **Standards Mapping**: Proper AUTOSAR and ISO interface standard references
- **CSV Conversion**: All tabular data properly formatted for analysis tools

## EXECUTION CHECKLIST

### Pre-Processing:
- [ ] Identify interface specification type and communication domain
- [ ] Assess image quality and enhancement needs for interface analysis
- [ ] Determine specification extraction approach and complexity
- [ ] Prepare for interface, protocol, and signal analysis

### Interface Analysis:
- [ ] Catalog all interfaces with complete specifications
- [ ] Document all protocols with parameters and constraints
- [ ] Extract all signals with data types and characteristics
- [ ] Analyze interface relationships and dependencies

### Specification Analysis:
- [ ] Create complete interface specification tables
- [ ] Document communication parameters and timing requirements
- [ ] Map interface validation and testing scenarios
- [ ] Generate interface test cases and validation criteria

### Output Generation:
- [ ] Structure report with interface definitions as primary section
- [ ] Format all data for CSV conversion and analysis tools
- [ ] Document automotive standards compliance
- [ ] Provide complete validation checklist

## SUCCESS CRITERIA

### Processing Quality:
- **Interface Identification**: 100% of visible interfaces cataloged with complete specifications
- **Specification Accuracy**: 98%+ accuracy in interface specification extraction
- **Standards Compliance**: Proper mapping to automotive interface standards
- **Data Extraction**: All tabular data ready for CSV/Excel import and analysis

### Picture-Centric Focus:
- **Visual Priority**: Interface specifications and protocols are primary focus
- **Practical Output**: Information directly usable for automotive interface development
- **Technical Depth**: Complete analysis of interface characteristics and validation
- **Implementation Ready**: All data suitable for automotive system interface implementation

### Enhancement Details:
- **Applied Enhancements**: Interface diagram optimization, specification text clarity
- **Quality Metrics**: Interface recognition accuracy, specification extraction precision
- **Validation Results**: Complete coverage verification, standards compliance check

### Analysis Summary:
- **Key Findings**: Critical interfaces, protocol requirements, validation needs
- **Development Implications**: System interface requirements, communication considerations
- **Recommended Actions**: Interface optimizations, protocol clarifications, validation improvements
