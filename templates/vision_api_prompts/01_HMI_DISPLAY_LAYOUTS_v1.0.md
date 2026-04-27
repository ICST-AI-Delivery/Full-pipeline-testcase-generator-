# Picture-Centric HMI Display Layouts Analysis

**Category:** HMI_DISPLAY_LAYOUTS  
**Template Version:** 2.3.0  
**Created:** 2026-02-25  
**Last Updated:** 2026-02-25  
**Author:** Picture Analyze Agent Development Team  
**Template Type:** Picture-Centric Analysis Template  
**Status:** Production Ready  
**Compatibility:** Application v4.0.0+

## VERSION HISTORY
| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 2.3.0 | 2026-02-25 | Converted to Picture-Centric approach, TXT output format | Development Team |
| 1.0 | 2026-02-23 | Initial JSON-based version | Picture Analyze Agent |

## TEMPLATE INFORMATION
- **Purpose**: Picture-centric HMI display layout analysis with practical TXT output
- **Use Case**: Automotive dashboard, instrument cluster, and infotainment display analysis
- **Processing Time**: 5-8 minutes per image
- **Output Format**: Structured TXT with embedded tables and CSV-ready data

## CORE PRINCIPLE
**PICTURE-FIRST ANALYSIS**: Focus on visual elements actually present in the image. Extract practical information for automotive development and testing.

## EXECUTION METHODOLOGY

### 1. Image Content Identification
- Identify display type (instrument cluster, infotainment, HUD, multi-display)
- Catalog all visible UI elements (gauges, telltales, buttons, text displays)
- Determine display regions and layout structure
- Assess image quality and enhancement needs

### 2. Picture-Centric Organization Structure
```
=== HMI DISPLAY LAYOUT ANALYSIS REPORT ===
├─ Image Overview & Enhancement Details
├─ DISPLAY STRUCTURE ANALYSIS (primary section)
├─ UI ELEMENT INVENTORY (telltales, gauges, buttons)
├─ Visual Content Extraction (tables/data from display)
├─ Telltale & Warning Light Analysis
├─ CSV Format Ready Data
├─ Automotive Standards Compliance
├─ Enhancement Details
└─ Validation Checklist
```

### 3. HMI-Specific Processing Pipeline
**For HMI Display Images:**
- **Display Analysis**: Layout regions, resolution, visual hierarchy
- **Element Extraction**: Telltales, gauges, buttons, text displays with positions
- **State Analysis**: Current display state, possible state variations
- **Standards Mapping**: ISO 2575 telltale symbols, automotive compliance
- **Decision Tables**: Display state conditions and visual outputs
- **Ferrari Compliance**: Design standards, telltale codes, color schemes

## REQUIRED OUTPUT STRUCTURE

### Section 1: Image Overview
```
=== HMI DISPLAY LAYOUT ANALYSIS REPORT ===

IMAGE: [filename]
├─ Content: HMI display layout showing [describe main elements]
├─ Display Type: Instrument Cluster / Infotainment / HUD / Multi-Display
├─ Original Dimensions: [width]x[height] pixels
├─ Enhancement Applied: [specific enhancement details for HMI displays]
├─ Quality Assessment: [clarity, readability, telltale visibility]
├─ Analysis Confidence: [High/Medium/Low] - [reasoning]
```

### Section 2: Display Structure Analysis (PRIMARY FOCUS)
```
=== DISPLAY STRUCTURE ANALYSIS ===

OVERALL LAYOUT:
├─ Display Type: [Instrument Cluster/Infotainment/HUD/Combined]
├─ Screen Resolution: [estimated resolution]
├─ Aspect Ratio: [ratio]
├─ Orientation: [Landscape/Portrait/Custom]

DISPLAY REGIONS:
├─ LEFT PANEL: [dimensions] - [purpose: gauges, telltales, etc.]
├─ CENTER AREA: [dimensions] - [purpose: main display, navigation, etc.]
├─ RIGHT PANEL: [dimensions] - [purpose: secondary info, controls, etc.]
├─ STATUS BAR: [dimensions] - [purpose: system status, time, etc.]
├─ CONTROL AREA: [dimensions] - [purpose: buttons, touch controls, etc.]

VISUAL HIERARCHY:
├─ Primary Elements: [most prominent displays - speedometer, main gauges]
├─ Secondary Elements: [supporting information - trip computer, clock]
├─ Warning Elements: [safety-critical indicators - check engine, oil pressure]
├─ Background Elements: [decorative or structural elements]
```

### Section 3: UI Element Inventory
```
=== UI ELEMENT INVENTORY ===

GAUGES & METERS:
├─ GAUGE 1: [Name] - [Type: Analog/Digital] - Position: [coordinates]
│  ├─ Current Reading: [value and units]
│  ├─ Scale Range: [min] to [max] [units]
│  ├─ Visual Style: [color, needle type, background]
│  ├─ Markings: [major ticks, labels, zones]
│  └─ State: [normal/warning/error indicators]

TELLTALES & WARNING LIGHTS:
├─ TELLTALE 1: [Name/Symbol] - Position: [coordinates]
│  ├─ ISO 2575 Code: [if applicable]
│  ├─ Current State: [ON/OFF/BLINKING]
│  ├─ Color: [Green/Yellow/Red/Blue/White]
│  ├─ Shape: [description]
│  ├─ Associated Text: [if any]
│  └─ Priority Level: [Low/Medium/High/Critical]

TEXT DISPLAYS:
├─ DISPLAY 1: [Name] - Position: [coordinates]
│  ├─ Current Text: "[exact text shown]"
│  ├─ Font Style: [size, weight, color]
│  ├─ Background: [color, style]
│  ├─ Update Frequency: [static/dynamic]
│  └─ Information Type: [speed, temperature, time, etc.]

INTERACTIVE ELEMENTS:
├─ BUTTON 1: [Name/Label] - Position: [coordinates]
│  ├─ Type: [Physical/Touch/Capacitive]
│  ├─ Visual State: [pressed/unpressed/highlighted]
│  ├─ Label Text: "[exact text]"
│  ├─ Icon: [description if present]
│  └─ Function: [inferred purpose]
```

### Section 4: Visual Content Extraction
```
=== VISUAL CONTENT EXTRACTION ===

### DISPLAY STATE ANALYSIS

**Current Display State:**
- System Mode: [Day/Night/Auto/Custom]
- Brightness Level: [estimated level]
- Color Scheme: [description]
- Active Warnings: [list any active warning states]
- User Interface Mode: [Normal/Menu/Settings/etc.]

**State Transition Indicators:**
- Mode Indicators: [any visible mode indicators]
- Menu Navigation: [visible navigation elements]
- User Input Areas: [touch zones, button areas]

### TELLTALE STATE MATRIX

**Active Telltales:**
| Telltale Name | ISO Code | Position | Color | State | Priority | Meaning |
|---------------|----------|----------|-------|-------|----------|---------|
| [Name] | [Code] | [X,Y] | [Color] | [ON/OFF/BLINK] | [Level] | [Description] |

**Inactive Telltales (Visible but OFF):**
| Telltale Name | ISO Code | Position | Expected States | Function |
|---------------|----------|----------|-----------------|----------|
| [Name] | [Code] | [X,Y] | [ON/BLINK] | [Description] |

### GAUGE READINGS EXTRACTION

**Primary Gauges:**
| Gauge Type | Current Value | Scale Range | Units | Warning Zones | Normal Range |
|------------|---------------|-------------|-------|---------------|--------------|
| Speedometer | [value] | [min-max] | [km/h or mph] | [red zones] | [normal range] |
| Tachometer | [value] | [min-max] | [RPM] | [red zones] | [normal range] |
| Fuel | [value] | [min-max] | [level/percentage] | [low zone] | [normal range] |

### DECISION TABLES FOR DISPLAY STATES

**Telltale Activation Matrix:**
| System Condition | Sensor Input | Telltale Response | Color | Blink Pattern | User Action |
|-------------------|--------------|-------------------|-------|---------------|-------------|
| Engine Normal | Temp < 90°C | Engine Temp OFF | - | - | None |
| Engine Warning | Temp 90-110°C | Engine Temp ON | Yellow | Solid | Monitor |
| Engine Critical | Temp > 110°C | Engine Temp ON | Red | Fast Blink | Stop Engine |

**Display Mode Matrix:**
| Time of Day | Light Sensor | User Setting | Display Mode | Brightness | Color Scheme |
|-------------|--------------|--------------|--------------|------------|--------------|
| Day | High | Auto | Day Mode | High | White/Black |
| Night | Low | Auto | Night Mode | Low | Red/Black |
| Manual | Any | Day | Day Mode | High | White/Black |
| Manual | Any | Night | Night Mode | Low | Red/Black |
```

### Section 5: Extracted Table Data
```
=== EXTRACTED TABLE DATA ===

TELLTALE REFERENCE TABLE: (from display analysis)
Purpose: Complete telltale inventory with automotive standards mapping

Telltale_Name | ISO_2575_Code | Position_X | Position_Y | Color | Current_State | Priority_Level | Function_Description
--------------|---------------|------------|------------|-------|---------------|----------------|--------------------
Engine_Temp   | 2.1-01        | 150        | 200        | Yellow| OFF           | Medium         | Engine temperature warning
Oil_Pressure  | 2.1-02        | 200        | 200        | Red   | OFF           | High           | Oil pressure warning
Battery       | 2.1-03        | 250        | 200        | Red   | OFF           | High           | Charging system warning

GAUGE READINGS TABLE: (from current display state)
Purpose: Current gauge values and scale information

Gauge_Type | Current_Value | Min_Scale | Max_Scale | Units | Warning_Threshold | Critical_Threshold
-----------|---------------|-----------|-----------|-------|-------------------|-------------------
Speed      | 72            | 0         | 320       | km/h  | 120               | 200
RPM        | 2500          | 0         | 8000      | RPM   | 6000              | 7500
Fuel       | 75            | 0         | 100       | %     | 15                | 5

DISPLAY REGIONS TABLE: (from layout analysis)
Purpose: Screen real estate allocation and purpose mapping

Region_Name | X_Start | Y_Start | Width | Height | Purpose | Content_Type
------------|---------|---------|-------|--------|---------|-------------
Left_Panel  | 0       | 0       | 400   | 600    | Primary_Gauges | Analog_Displays
Center_Info | 400     | 0       | 200   | 300    | Digital_Readouts | Text_Numeric
Right_Panel | 600     | 0       | 300   | 600    | Secondary_Info | Mixed_Content
Status_Bar  | 0       | 550     | 900   | 50     | System_Status | Icons_Text
```

### Section 6: CSV Format Ready Data
```
=== CSV FORMAT READY DATA ===

TELLTALE_INVENTORY.csv:
Telltale_Name,ISO_Code,Position_X,Position_Y,Color,State,Priority,Function
Engine_Temp,2.1-01,150,200,Yellow,OFF,Medium,Engine temperature warning
Oil_Pressure,2.1-02,200,200,Red,OFF,High,Oil pressure warning
Battery,2.1-03,250,200,Red,OFF,High,Charging system warning

GAUGE_READINGS.csv:
Gauge_Type,Current_Value,Min_Scale,Max_Scale,Units,Warning_Threshold,Critical_Threshold
Speed,72,0,320,km/h,120,200
RPM,2500,0,8000,RPM,6000,7500
Fuel,75,0,100,%,15,5

DISPLAY_LAYOUT.csv:
Region_Name,X_Start,Y_Start,Width,Height,Purpose,Content_Type
Left_Panel,0,0,400,600,Primary_Gauges,Analog_Displays
Center_Info,400,0,200,300,Digital_Readouts,Text_Numeric
Right_Panel,600,0,300,600,Secondary_Info,Mixed_Content
```

### Section 7: Automotive Standards Compliance
```
=== AUTOMOTIVE STANDARDS COMPLIANCE ===

ISO 2575 TELLTALE COMPLIANCE:
├─ Standard Symbols: [X/Y symbols match ISO 2575]
├─ Color Usage: [compliant/non-compliant with color standards]
├─ Priority Levels: [correct priority indication through color/position]
├─ Symbol Clarity: [readability at standard viewing distances]

ISO 15008 HMI COMPLIANCE:
├─ Text Readability: [font sizes meet minimum requirements]
├─ Color Contrast: [adequate contrast ratios for day/night viewing]
├─ Information Hierarchy: [clear primary/secondary information structure]
├─ Distraction Minimization: [appropriate information density]

ISO 26262 FUNCTIONAL SAFETY:
├─ Safety-Critical Displays: [redundancy and fail-safe states]
├─ Warning Prioritization: [critical warnings prominently displayed]
├─ System State Indication: [clear system status communication]
├─ Error State Handling: [appropriate error indication methods]

FERRARI DESIGN STANDARDS:
├─ Brand Consistency: [alignment with Ferrari HMI guidelines]
├─ Color Palette: [use of approved Ferrari colors]
├─ Typography: [approved fonts and sizing]
├─ Layout Principles: [adherence to Ferrari design language]
```

## QUALITY STANDARDS

### Image Enhancement Requirements:
- **HMI-Specific Enhancement**: Optimize for telltale visibility and gauge readability
- **OCR Optimization**: 95%+ accuracy for all text elements and numeric displays
- **Color Accuracy**: Precise color identification for telltale states
- **Contrast Enhancement**: Improve visibility of low-contrast elements

### Picture-Centric Analysis Standards:
- **Element-First Structure**: Visual elements drive the analysis
- **Complete Coverage**: Every visible UI element cataloged
- **Practical Focus**: Information useful for automotive development
- **Standards Compliance**: Verification against automotive HMI standards

### Validation Requirements:
- **100% Element Coverage**: All visible telltales, gauges, and controls identified
- **Accurate State Reading**: Current display state correctly interpreted
- **Standards Mapping**: Proper ISO 2575 and automotive standard references
- **CSV Conversion**: All tabular data properly formatted

## EXECUTION CHECKLIST

### Pre-Processing:
- [ ] Identify HMI display type and main components
- [ ] Assess image quality and enhancement needs
- [ ] Determine analysis approach based on display complexity
- [ ] Prepare for telltale and gauge analysis

### Element Analysis:
- [ ] Catalog all telltales with ISO 2575 mapping
- [ ] Extract all gauge readings and scale information
- [ ] Document all interactive elements and controls
- [ ] Analyze display regions and layout structure

### Data Extraction:
- [ ] Create comprehensive telltale inventory
- [ ] Extract current gauge values and states
- [ ] Document display mode and visual settings
- [ ] Generate decision tables for state transitions

### Output Generation:
- [ ] Structure report with display analysis as primary section
- [ ] Format all data for CSV conversion
- [ ] Document automotive standards compliance
- [ ] Provide complete validation checklist

## SUCCESS CRITERIA

### Processing Quality:
- **Element Identification**: 100% of visible UI elements cataloged
- **State Accuracy**: 95%+ accuracy in reading current display states
- **Standards Compliance**: Proper mapping to automotive standards
- **Data Extraction**: All tabular data ready for CSV/Excel import

### Picture-Centric Focus:
- **Visual Priority**: Display elements and their states are primary focus
- **Practical Output**: Information directly usable for development
- **Technical Depth**: Complete analysis of HMI functionality
- **Implementation Ready**: All data suitable for system development
