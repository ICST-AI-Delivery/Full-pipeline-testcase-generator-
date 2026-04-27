# Picture-Centric Telltales & Icons Analysis

**Category:** TELLTALES_AND_ICONS  
**Template Version:** 1.0.0  
**Created:** 2026-02-26  
**Last Updated:** 2026-02-26  
**Author:** Picture Analyze Agent Development Team  
**Template Type:** Picture-Centric Analysis Template  
**Status:** Production Ready  
**Compatibility:** Application v4.0.0+

## VERSION HISTORY
| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-02-26 | Initial telltales & icons specific template | Development Team |

## TEMPLATE INFORMATION
- **Purpose**: Picture-centric telltale and icon analysis with automotive standards compliance
- **Use Case**: Individual telltale symbols, warning lights, dashboard icons, and indicator analysis
- **Processing Time**: 3-5 minutes per image
- **Output Format**: Structured TXT with embedded tables and CSV-ready data

## CORE PRINCIPLE
**ICON-FIRST ANALYSIS**: Focus on individual telltale symbols and icons actually visible in the image. Extract precise automotive compliance information with ISO 2575 mapping.

## EXECUTION METHODOLOGY

### 1. Icon Content Identification
- Identify all visible telltale symbols and icons
- Catalog color states and visual characteristics
- Determine symbol types (warning, indicator, status)
- Assess image quality for precise color and shape analysis

### 2. Picture-Centric Organization Structure
```
=== TELLTALES & ICONS ANALYSIS REPORT ===
├─ Image Overview & Enhancement Details
├─ ICON INVENTORY (primary section)
├─ ISO 2575 COMPLIANCE MAPPING
├─ COLOR STATE ANALYSIS
├─ PRIORITY CLASSIFICATION
├─ AUTOMOTIVE FUNCTION MAPPING
├─ CSV Format Ready Data
├─ Standards Compliance Verification
├─ Enhancement Details
└─ Validation Checklist
```

### 3. Telltale-Specific Processing Pipeline
**For Telltale & Icon Images:**
- **Symbol Recognition**: Individual icon identification and classification
- **Color Analysis**: Precise color state detection (Red/Yellow/Green/Blue/White)
- **State Detection**: ON/OFF/BLINKING pattern analysis
- **Standards Mapping**: ISO 2575 automotive symbol compliance
- **Priority Assessment**: Critical/High/Medium/Low classification
- **Function Mapping**: Automotive system and warning function identification

## REQUIRED OUTPUT STRUCTURE

### Section 1: Image Overview
```
=== TELLTALES & ICONS ANALYSIS REPORT ===

IMAGE: [filename]
├─ Content: Telltale symbols and icons showing [describe main elements]
├─ Icon Count: [total number of visible icons/telltales]
├─ Original Dimensions: [width]x[height] pixels
├─ Enhancement Applied: [specific enhancement for icon visibility and color accuracy]
├─ Quality Assessment: [clarity, color accuracy, symbol readability]
├─ Analysis Confidence: [High/Medium/Low] - [reasoning]
```

### Section 2: Icon Inventory (PRIMARY FOCUS)
```
=== ICON INVENTORY ===

TELLTALE SYMBOLS:
├─ ICON 1: [Name/Description] - Position: [X,Y coordinates]
│  ├─ ISO 2575 Code: [official code if applicable]
│  ├─ Symbol Type: [Warning/Indicator/Status/Information]
│  ├─ Current State: [ON/OFF/BLINKING/DIMMED]
│  ├─ Color: [Red/Yellow/Green/Blue/White/Orange] - [RGB values if detectable]
│  ├─ Shape Description: [detailed visual description]
│  ├─ Size: [estimated dimensions in pixels]
│  ├─ Priority Level: [Critical/High/Medium/Low]
│  ├─ Automotive Function: [engine warning, oil pressure, battery, etc.]
│  ├─ Associated System: [engine, electrical, braking, etc.]
│  └─ Compliance Notes: [ISO 2575 compliance status]

WARNING LIGHTS:
├─ WARNING 1: [Name] - Position: [X,Y coordinates]
│  ├─ Warning Type: [Engine/Oil/Battery/Brake/etc.]
│  ├─ Current State: [Active/Inactive/Test Mode]
│  ├─ Color: [Red/Yellow] - [exact color description]
│  ├─ Urgency Level: [Immediate Stop/Service Soon/Monitor]
│  ├─ Driver Action Required: [Stop immediately/Service required/Monitor]
│  ├─ System Impact: [Safety critical/Performance/Comfort]
│  └─ Standard Reference: [ISO 2575 section]

INDICATOR LIGHTS:
├─ INDICATOR 1: [Name] - Position: [X,Y coordinates]
│  ├─ Indicator Type: [Turn Signal/High Beam/etc.]
│  ├─ Current State: [Active/Inactive/Blinking]
│  ├─ Color: [Green/Blue/White] - [exact color]
│  ├─ Function: [operational status indication]
│  ├─ Normal Operation: [expected behavior]
│  └─ Standard Compliance: [regulatory requirement]

STATUS ICONS:
├─ STATUS 1: [Name] - Position: [X,Y coordinates]
│  ├─ Status Type: [System/Mode/Configuration]
│  ├─ Current Display: [Active/Inactive/Selected]
│  ├─ Color: [any color] - [description]
│  ├─ Information Provided: [system state/mode/setting]
│  ├─ User Interaction: [informational only/user selectable]
│  └─ Context: [when this status appears]
```

### Section 3: ISO 2575 Compliance Mapping
```
=== ISO 2575 COMPLIANCE MAPPING ===

STANDARD SYMBOLS IDENTIFIED:
├─ Engine Temperature Warning (ISO 2575-2.1-01)
│  ├─ Symbol Present: [Yes/No]
│  ├─ Color Compliance: [Red - Compliant/Non-compliant]
│  ├─ Shape Accuracy: [Matches standard/Variations noted]
│  ├─ Position: [Dashboard location]
│  └─ Function: Engine overheating warning

├─ Oil Pressure Warning (ISO 2575-2.1-02)
│  ├─ Symbol Present: [Yes/No]
│  ├─ Color Compliance: [Red - Compliant/Non-compliant]
│  ├─ Shape Accuracy: [Oil can symbol accuracy]
│  ├─ Position: [Dashboard location]
│  └─ Function: Low oil pressure warning

├─ Battery/Charging Warning (ISO 2575-2.1-03)
│  ├─ Symbol Present: [Yes/No]
│  ├─ Color Compliance: [Red - Compliant/Non-compliant]
│  ├─ Shape Accuracy: [Battery symbol with +/- terminals]
│  ├─ Position: [Dashboard location]
│  └─ Function: Charging system malfunction

NON-STANDARD SYMBOLS:
├─ CUSTOM SYMBOL 1: [Description]
│  ├─ Manufacturer Specific: [Brand/Model specific symbol]
│  ├─ Function: [Inferred purpose]
│  ├─ Color Logic: [Color meaning in context]
│  └─ Standards Gap: [What standard symbol should be used]

COMPLIANCE ASSESSMENT:
├─ Total Symbols: [count]
├─ ISO 2575 Compliant: [count and percentage]
├─ Non-Standard: [count and percentage]
├─ Color Compliance: [percentage of correct colors]
└─ Overall Compliance Score: [percentage]
```

### Section 4: Color State Analysis
```
=== COLOR STATE ANALYSIS ===

COLOR CLASSIFICATION:
├─ RED SYMBOLS: [count] - Critical warnings requiring immediate attention
│  ├─ Active Red: [list of active red symbols]
│  ├─ Inactive Red: [list of inactive red symbols visible]
│  └─ Color Accuracy: [RGB values if detectable]

├─ YELLOW/AMBER SYMBOLS: [count] - Caution warnings requiring attention
│  ├─ Active Yellow: [list of active yellow symbols]
│  ├─ Inactive Yellow: [list of inactive yellow symbols visible]
│  └─ Color Accuracy: [RGB values if detectable]

├─ GREEN SYMBOLS: [count] - System active/normal operation indicators
│  ├─ Active Green: [list of active green symbols]
│  ├─ Function: [what systems are indicated as active]
│  └─ Color Accuracy: [RGB values if detectable]

├─ BLUE SYMBOLS: [count] - High beam and other blue indicators
│  ├─ Active Blue: [list of active blue symbols]
│  ├─ Function: [typically high beam headlights]
│  └─ Color Accuracy: [RGB values if detectable]

├─ WHITE SYMBOLS: [count] - Information and status indicators
│  ├─ Active White: [list of active white symbols]
│  ├─ Function: [informational displays]
│  └─ Color Accuracy: [RGB values if detectable]

BLINKING PATTERN ANALYSIS:
├─ BLINKING SYMBOLS: [count]
│  ├─ Fast Blink: [symbols with rapid blinking - typically critical]
│  ├─ Slow Blink: [symbols with slow blinking - typically caution]
│  ├─ Pattern Description: [detailed blinking pattern if detectable]
│  └─ Urgency Indication: [what the blinking pattern indicates]

COLOR COMPLIANCE CHECK:
├─ Correct Red Usage: [critical warnings only]
├─ Correct Yellow Usage: [caution warnings only]
├─ Correct Green Usage: [system active indicators only]
├─ Correct Blue Usage: [high beam and specific functions only]
└─ Color Standard Violations: [any incorrect color usage]
```

### Section 5: Priority Classification
```
=== PRIORITY CLASSIFICATION ===

CRITICAL PRIORITY (Red - Stop Immediately):
├─ Engine Temperature: [status and description]
├─ Oil Pressure: [status and description]
├─ Brake System: [status and description]
├─ Battery/Charging: [status and description]
└─ Safety Systems: [airbag, seatbelt, etc.]

HIGH PRIORITY (Red/Yellow - Service Soon):
├─ Check Engine: [status and description]
├─ ABS Warning: [status and description]
├─ Power Steering: [status and description]
├─ Transmission: [status and description]
└─ Emission System: [status and description]

MEDIUM PRIORITY (Yellow - Monitor):
├─ Fuel Level: [status and description]
├─ Tire Pressure: [status and description]
├─ Service Reminder: [status and description]
├─ Minor System Warnings: [status and description]
└─ Maintenance Indicators: [status and description]

LOW PRIORITY (Green/Blue/White - Informational):
├─ Turn Signals: [status and description]
├─ High Beam: [status and description]
├─ System Active: [cruise control, etc.]
├─ Mode Indicators: [eco mode, sport mode, etc.]
└─ Information Display: [time, temperature, etc.]

PRIORITY MATRIX:
| Symbol Name | Color | Priority | Action Required | Time Frame |
|-------------|-------|----------|-----------------|------------|
| [Name] | [Color] | [Level] | [Action] | [Immediate/Soon/Monitor] |
```

### Section 6: Automotive Function Mapping
```
=== AUTOMOTIVE FUNCTION MAPPING ===

ENGINE SYSTEM INDICATORS:
├─ Engine Temperature: [symbol status and meaning]
├─ Oil Pressure: [symbol status and meaning]
├─ Check Engine: [symbol status and meaning]
├─ Engine Oil Level: [symbol status and meaning]
└─ Coolant Level: [symbol status and meaning]

ELECTRICAL SYSTEM INDICATORS:
├─ Battery/Charging: [symbol status and meaning]
├─ Alternator: [symbol status and meaning]
├─ Electrical Fault: [symbol status and meaning]
└─ Low Voltage: [symbol status and meaning]

BRAKING SYSTEM INDICATORS:
├─ Brake System Warning: [symbol status and meaning]
├─ ABS Warning: [symbol status and meaning]
├─ Brake Pad Wear: [symbol status and meaning]
├─ Parking Brake: [symbol status and meaning]
└─ Electronic Stability: [symbol status and meaning]

LIGHTING SYSTEM INDICATORS:
├─ Headlight Failure: [symbol status and meaning]
├─ Turn Signal: [symbol status and meaning]
├─ High Beam: [symbol status and meaning]
├─ Fog Light: [symbol status and meaning]
└─ Daytime Running Lights: [symbol status and meaning]

SAFETY SYSTEM INDICATORS:
├─ Airbag Warning: [symbol status and meaning]
├─ Seatbelt Warning: [symbol status and meaning]
├─ Door Ajar: [symbol status and meaning]
├─ Security System: [symbol status and meaning]
└─ Immobilizer: [symbol status and meaning]

COMFORT/CONVENIENCE INDICATORS:
├─ Air Conditioning: [symbol status and meaning]
├─ Heated Seats: [symbol status and meaning]
├─ Cruise Control: [symbol status and meaning]
├─ Navigation: [symbol status and meaning]
└─ Phone/Bluetooth: [symbol status and meaning]

FUNCTION MAPPING TABLE:
| System Category | Symbol Count | Active Symbols | Warning Symbols | Status Symbols |
|-----------------|--------------|----------------|-----------------|----------------|
| Engine | [count] | [list] | [list] | [list] |
| Electrical | [count] | [list] | [list] | [list] |
| Braking | [count] | [list] | [list] | [list] |
| Lighting | [count] | [list] | [list] | [list] |
| Safety | [count] | [list] | [list] | [list] |
| Comfort | [count] | [list] | [list] | [list] |
```

### Section 7: CSV Format Ready Data
```
=== CSV FORMAT READY DATA ===

TELLTALE_INVENTORY.csv:
Symbol_Name,ISO_2575_Code,Position_X,Position_Y,Color,State,Priority,Function,System_Category,Compliance_Status
Engine_Temp,2.1-01,150,200,Red,OFF,Critical,Engine_Temperature_Warning,Engine,Compliant
Oil_Pressure,2.1-02,200,200,Red,OFF,Critical,Oil_Pressure_Warning,Engine,Compliant
Battery,2.1-03,250,200,Red,OFF,Critical,Charging_System_Warning,Electrical,Compliant

COLOR_STATE_ANALYSIS.csv:
Color,Symbol_Count,Active_Count,Inactive_Count,Compliance_Status,Standard_Usage
Red,5,0,5,Compliant,Critical_Warnings_Only
Yellow,3,1,2,Compliant,Caution_Warnings_Only
Green,2,2,0,Compliant,System_Active_Indicators
Blue,1,0,1,Compliant,High_Beam_Indicator
White,4,2,2,Compliant,Information_Display

PRIORITY_CLASSIFICATION.csv:
Priority_Level,Symbol_Count,Active_Symbols,Color_Distribution,Action_Required
Critical,8,0,"Red: 8, Yellow: 0",Stop_Immediately_If_Active
High,5,1,"Red: 2, Yellow: 3",Service_Soon
Medium,4,2,"Yellow: 4",Monitor_Condition
Low,6,3,"Green: 2, Blue: 1, White: 3",Informational_Only

AUTOMOTIVE_FUNCTION.csv:
System_Category,Total_Symbols,Warning_Symbols,Status_Symbols,Active_Warnings,System_Health
Engine,6,4,2,0,Normal
Electrical,3,2,1,0,Normal
Braking,4,3,1,0,Normal
Lighting,5,1,4,0,Normal
Safety,3,3,0,0,Normal
Comfort,2,0,2,0,Normal
```

### Section 8: Standards Compliance Verification
```
=== STANDARDS COMPLIANCE VERIFICATION ===

ISO 2575 AUTOMOTIVE SYMBOLS COMPLIANCE:
├─ Symbol Recognition: [percentage of symbols matching ISO 2575 standards]
├─ Color Compliance: [percentage of symbols using correct colors]
├─ Shape Accuracy: [percentage of symbols with correct shapes]
├─ Position Standards: [compliance with dashboard positioning guidelines]
└─ Overall ISO 2575 Score: [percentage compliance]

REGULATORY COMPLIANCE:
├─ FMVSS (Federal Motor Vehicle Safety Standards): [compliance status]
├─ ECE Regulations: [European compliance status]
├─ SAE Standards: [Society of Automotive Engineers compliance]
├─ Regional Requirements: [specific regional compliance notes]
└─ Manufacturer Standards: [brand-specific compliance]

ACCESSIBILITY COMPLIANCE:
├─ Color Blind Accessibility: [symbols distinguishable without color]
├─ Size Requirements: [minimum size standards met]
├─ Contrast Requirements: [adequate contrast for visibility]
├─ Universal Design: [symbols universally recognizable]
└─ Aging Population: [visibility for older drivers]

COMPLIANCE GAPS:
├─ Non-Standard Symbols: [list of symbols not matching standards]
├─ Color Violations: [incorrect color usage]
├─ Shape Deviations: [symbols with non-standard shapes]
├─ Missing Required Symbols: [required symbols not present]
└─ Recommendations: [suggested improvements for compliance]
```

### Section 9: Enhancement Details
```
=== ENHANCEMENT DETAILS ===

IMAGE PROCESSING APPLIED:
├─ Color Enhancement: [specific color correction applied]
├─ Contrast Adjustment: [contrast improvements for symbol visibility]
├─ Noise Reduction: [filtering applied to improve clarity]
├─ Sharpening: [edge enhancement for symbol definition]
└─ Brightness Optimization: [brightness adjustments made]

TELLTALE-SPECIFIC ENHANCEMENTS:
├─ Symbol Edge Detection: [edge enhancement for symbol boundaries]
├─ Color Separation: [color channel optimization]
├─ Background Suppression: [background noise reduction]
├─ Icon Isolation: [individual symbol enhancement]
└─ State Detection: [enhancement for ON/OFF state recognition]

QUALITY IMPROVEMENTS:
├─ Original Quality: [assessment of original image quality]
├─ Enhanced Quality: [quality after enhancement]
├─ Color Accuracy: [improvement in color representation]
├─ Symbol Clarity: [improvement in symbol definition]
└─ Analysis Confidence: [confidence level after enhancement]

PROCESSING LIMITATIONS:
├─ Resolution Constraints: [limitations due to image resolution]
├─ Color Depth: [limitations in color analysis]
├─ Lighting Conditions: [impact of original lighting]
├─ Image Artifacts: [any artifacts affecting analysis]
└─ Enhancement Artifacts: [any artifacts introduced by processing]
```

### Section 10: Validation Checklist
```
=== VALIDATION CHECKLIST ===

SYMBOL IDENTIFICATION:
- [ ] All visible symbols identified and cataloged
- [ ] Symbol positions accurately recorded
- [ ] Symbol states (ON/OFF/BLINKING) correctly determined
- [ ] Symbol colors accurately identified
- [ ] Symbol sizes estimated

ISO 2575 COMPLIANCE:
- [ ] Standard symbols mapped to ISO 2575 codes
- [ ] Color compliance verified against standards
- [ ] Shape accuracy assessed against standard symbols
- [ ] Non-standard symbols identified and documented
- [ ] Compliance percentage calculated

PRIORITY CLASSIFICATION:
- [ ] Critical priority symbols identified (Red)
- [ ] High priority symbols identified (Red/Yellow)
- [ ] Medium priority symbols identified (Yellow)
- [ ] Low priority symbols identified (Green/Blue/White)
- [ ] Priority matrix completed

AUTOMOTIVE FUNCTION MAPPING:
- [ ] Engine system symbols mapped
- [ ] Electrical system symbols mapped
- [ ] Braking system symbols mapped
- [ ] Lighting system symbols mapped
- [ ] Safety system symbols mapped
- [ ] Comfort system symbols mapped

DATA EXTRACTION:
- [ ] CSV format data prepared
- [ ] All tables properly formatted
- [ ] Data consistency verified
- [ ] Export readiness confirmed

QUALITY ASSURANCE:
- [ ] Image enhancement documented
- [ ] Analysis confidence assessed
- [ ] Limitations documented
- [ ] Recommendations provided
- [ ] Standards compliance verified
```

## QUALITY STANDARDS

### Image Enhancement Requirements:
- **Color Accuracy**: Precise color identification for telltale state analysis
- **Symbol Clarity**: Enhanced edge definition for accurate symbol recognition
- **Contrast Optimization**: Improved visibility of low-contrast symbols
- **Background Suppression**: Reduced background noise for better symbol isolation

### Picture-Centric Analysis Standards:
- **Symbol-First Structure**: Individual symbols drive the analysis
- **Complete Coverage**: Every visible symbol cataloged and analyzed
- **Standards Focus**: ISO 2575 compliance verification for all symbols
- **Practical Output**: Information directly usable for automotive development

### Validation Requirements:
- **100% Symbol Coverage**: All visible telltales and icons identified
- **Accurate State Reading**: Current symbol states correctly interpreted
- **Standards Mapping**: Proper ISO 2575 and automotive standard references
- **CSV Conversion**: All tabular data properly formatted for export

## EXECUTION CHECKLIST

### Pre-Processing:
- [ ] Identify telltale and icon content in image
- [ ] Assess image quality for color and symbol analysis
- [ ] Determine enhancement needs for optimal symbol visibility
- [ ] Prepare for individual symbol analysis

### Symbol Analysis:
- [ ] Catalog all visible symbols with precise positioning
- [ ] Analyze color states and visual characteristics
- [ ] Map symbols to ISO 2575 standards where applicable
- [ ] Classify symbols by priority and automotive function

### Data Extraction:
- [ ] Create comprehensive symbol inventory
- [ ] Generate color state analysis
- [ ] Document priority classification
- [ ] Map automotive functions and systems

### Output Generation:
- [ ] Structure report with symbol inventory as primary section
- [ ] Format all data for CSV conversion
- [ ] Document standards compliance status
- [ ] Provide complete validation checklist

## SUCCESS CRITERIA

### Processing Quality:
- **Symbol Identification**: 100% of visible symbols cataloged
- **State Accuracy**: 95%+ accuracy in reading symbol states
- **Standards Compliance**: Proper mapping to automotive standards
- **Data Extraction**: All tabular data ready for CSV/Excel import

### Picture-Centric Focus:
- **Symbol Priority**: Individual symbols and their states are primary focus
- **Practical Output**: Information directly usable for automotive development
- **Technical Depth**: Complete analysis of telltale functionality
- **Implementation Ready**: All data suitable for system development
