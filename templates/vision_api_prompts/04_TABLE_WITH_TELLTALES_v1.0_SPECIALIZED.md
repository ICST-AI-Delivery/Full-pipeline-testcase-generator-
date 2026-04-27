# Table with Telltales Analysis - Specialized v1.0

**Category:** TABLE_WITH_TELLTALES  
**Template Version:** 1.0.0  
**Created:** 2026-02-26  
**Last Updated:** 2026-02-26  
**Author:** Picture Analyze Agent Development Team  
**Template Type:** Hybrid Table-Telltale Specialized Analysis Template  
**Status:** Production Ready  
**Compatibility:** Application v4.0.0+

## VERSION HISTORY
| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-02-26 | Initial specialized version for table-telltale hybrid analysis | Development Team |

## TEMPLATE INFORMATION
- **Purpose**: Specialized analysis for tables containing automotive telltale icons and symbols
- **Use Case**: Configuration tables with embedded warning icons, status tables with pictograms, diagnostic tables with symbols
- **Processing Time**: 15-20 minutes per image
- **Output Format**: Structured TXT with dual table-telltale analysis and CSV-ready data

## CORE PRINCIPLE
**HYBRID TABLE-TELLTALE ANALYSIS**: Combine structured table analysis with automotive symbol recognition. Optimize for both tabular data extraction AND telltale icon identification within table cells.

## EXECUTION METHODOLOGY

### 1. Hybrid Content Identification
- Identify table structure (rows, columns, headers)
- Detect telltale icons and symbols within table cells
- Catalog automotive pictograms and warning symbols
- Assess table-telltale integration complexity

### 2. Dual Processing Pipeline
```
=== TABLE WITH TELLTALES ANALYSIS REPORT ===
├─ Hybrid Content Overview & Enhancement Details
├─ TABLE STRUCTURE ANALYSIS (rows, columns, headers)
├─ TELLTALE SYMBOL IDENTIFICATION (automotive icons within cells)
├─ CELL-BY-CELL HYBRID ANALYSIS (text + symbols per cell)
├─ AUTOMOTIVE SYMBOL CATALOG (telltale meanings and standards)
├─ TABLE-TELLTALE RELATIONSHIP MAPPING (symbol context within table)
├─ HYBRID VALIDATION TABLES (combined verification)
├─ CSV Format Ready Data (with symbol encoding)
├─ Automotive Standards Compliance
└─ Validation Checklist
```

### 3. Hybrid-Specific Processing Features
**For Table-Telltale Images:**
- **Dual Recognition**: Simultaneous table structure and symbol detection
- **Cell Analysis**: Individual cell processing for text AND symbols
- **Symbol Cataloging**: Automotive telltale identification and classification
- **Context Mapping**: Symbol meaning within table context
- **Standards Compliance**: ISO and automotive symbol standard verification
- **Encoding Strategy**: Symbol representation in tabular data

## REQUIRED OUTPUT STRUCTURE

### Section 1: Hybrid Content Overview
```
=== TABLE WITH TELLTALES ANALYSIS REPORT ===

IMAGE: [filename]
├─ Content: Table containing [describe table structure] with embedded telltale symbols
├─ Hybrid Type: Configuration Table / Status Table / Diagnostic Table / Warning Matrix
├─ Original Dimensions: [width]x[height] pixels
├─ Enhancement Applied: [table structure enhancement + symbol sharpening]
├─ Table Detection Quality: [row/column clarity, border detection]
├─ Symbol Detection Quality: [telltale clarity, symbol recognition accuracy]
├─ Hybrid Analysis Confidence: [High/Medium/Low] - [reasoning for both table and symbols]
├─ Symbol Count: [total number of telltale symbols detected]
├─ Table Dimensions: [rows] x [columns]
```

### Section 2: Table Structure Analysis
```
=== TABLE STRUCTURE ANALYSIS ===

TABLE CHARACTERISTICS:
├─ Table Domain: [Engine Control/Safety Systems/Diagnostic/Configuration]
├─ Table Type: [Configuration Matrix/Status Table/Warning Table/Diagnostic Grid]
├─ Dimensions: [number of rows] x [number of columns]
├─ Header Structure: [column headers, row headers, title]
├─ Cell Types: [text cells, symbol cells, mixed cells, empty cells]
├─ Border Style: [solid lines, dashed lines, no borders]

TABLE ORGANIZATION:
├─ HEADER ANALYSIS: [table headers and structure]
│  ├─ Column Headers: [list of column header text]
│  ├─ Row Headers: [list of row header text]
│  ├─ Table Title: [main table title or caption]
│  └─ Sub-headers: [any secondary header information]
├─ ROW STRUCTURE: [row organization and content]
│  ├─ Data Rows: [number of data-containing rows]
│  ├─ Header Rows: [number of header rows]
│  ├─ Separator Rows: [divider or spacing rows]
│  └─ Total Rows: [complete row count]
├─ COLUMN STRUCTURE: [column organization and content]
│  ├─ Data Columns: [number of data-containing columns]
│  ├─ Header Columns: [number of header columns]
│  ├─ Symbol Columns: [columns containing primarily symbols]
│  └─ Total Columns: [complete column count]

CELL CONTENT ANALYSIS:
├─ Text-Only Cells: [cells containing only text]
├─ Symbol-Only Cells: [cells containing only telltale symbols]
├─ Mixed Cells: [cells containing both text and symbols]
├─ Empty Cells: [blank or empty cells]
├─ Complex Cells: [cells with multiple symbols or complex content]
```

### Section 3: Telltale Symbol Identification (PRIMARY FOCUS)
```
=== TELLTALE SYMBOL IDENTIFICATION ===

AUTOMOTIVE SYMBOL CATEGORIES:
├─ ENGINE SYMBOLS: [engine-related warning and status icons]
│  ├─ Engine Warning: [check engine, engine malfunction symbols]
│  ├─ Oil Pressure: [oil pressure warning symbols]
│  ├─ Coolant Temperature: [temperature warning symbols]
│  └─ Engine Speed: [RPM and engine speed indicators]
├─ SAFETY SYMBOLS: [safety system telltales]
│  ├─ Airbag Symbols: [airbag warning and status icons]
│  ├─ Seatbelt Symbols: [seatbelt warning indicators]
│  ├─ ABS Symbols: [anti-lock brake system indicators]
│  └─ ESC Symbols: [electronic stability control icons]
├─ LIGHTING SYMBOLS: [vehicle lighting telltales]
│  ├─ Headlight Symbols: [headlight status and warning icons]
│  ├─ Turn Signal: [turn indicator symbols]
│  ├─ Hazard Lights: [hazard warning symbols]
│  └─ Brake Lights: [brake light status indicators]
├─ POWER SYMBOLS: [electrical and power system icons]
│  ├─ Battery Symbols: [battery status and warning icons]
│  ├─ Charging Symbols: [charging system indicators]
│  ├─ Power Management: [power system status icons]
│  └─ Hybrid/Electric: [hybrid and electric vehicle symbols]

SYMBOL DETECTION RESULTS:
├─ Total Symbols Detected: [count of all telltale symbols found]
├─ Unique Symbol Types: [count of different symbol types]
├─ Symbol Recognition Confidence: [average confidence across all symbols]
├─ Unidentified Symbols: [count of symbols not recognized]
├─ Symbol Quality Assessment: [clarity and recognizability of symbols]

### DETAILED SYMBOL CATALOG

**Identified Telltale Symbols:**
| Symbol ID | Symbol Type | Description | Location (Row,Col) | Confidence | ISO Standard | Meaning |
|-----------|-------------|-------------|-------------------|------------|--------------|---------|
| SYM_001 | Engine Warning | Check engine light | (2,3) | 95% | ISO 2575 | Engine malfunction |
| SYM_002 | Oil Pressure | Oil can symbol | (2,4) | 92% | ISO 2575 | Low oil pressure |
| SYM_003 | Temperature | Thermometer | (3,3) | 88% | ISO 2575 | High coolant temp |
| SYM_004 | Battery | Battery symbol | (3,4) | 90% | ISO 2575 | Charging system |
| SYM_005 | ABS | ABS text circle | (4,3) | 85% | ISO 2575 | ABS malfunction |

### SYMBOL CLASSIFICATION ANALYSIS

**Symbol Categories by Function:**
| Function Category | Symbol Count | Primary Colors | Typical Locations | Criticality Level |
|-------------------|--------------|----------------|-------------------|-------------------|
| Engine Systems | 8 | Red, Yellow | Rows 2-5, Cols 3-4 | High |
| Safety Systems | 6 | Red, Yellow | Rows 6-8, Cols 2-5 | Critical |
| Lighting Systems | 4 | Green, Blue | Rows 9-10, Cols 3-4 | Medium |
| Power Systems | 3 | Red, Yellow | Rows 11-12, Cols 3-4 | High |
| Information | 5 | Blue, White | Various | Low |
```

### Section 4: Cell-by-Cell Hybrid Analysis
```
=== CELL-BY-CELL HYBRID ANALYSIS ===

COMPREHENSIVE CELL MAPPING:
├─ Cell Analysis Method: [systematic row-by-row, column-by-column analysis]
├─ Content Classification: [text, symbol, mixed, empty for each cell]
├─ Symbol-Text Relationships: [how symbols relate to adjacent text]
├─ Context Integration: [symbol meaning within table context]

### DETAILED CELL CONTENT MATRIX

**Row-by-Row Cell Analysis:**

**Row 1 (Headers):**
| Column | Content Type | Text Content | Symbol Content | Combined Meaning |
|--------|--------------|--------------|----------------|------------------|
| Col 1 | Text | "System" | None | Column header |
| Col 2 | Text | "Status" | None | Column header |
| Col 3 | Text | "Warning" | None | Column header |
| Col 4 | Text | "Action" | None | Column header |

**Row 2 (Engine Systems):**
| Column | Content Type | Text Content | Symbol Content | Combined Meaning |
|--------|--------------|--------------|----------------|------------------|
| Col 1 | Text | "Engine Control" | None | System identifier |
| Col 2 | Mixed | "Active" | Green circle | System operational |
| Col 3 | Symbol | None | Check engine (SYM_001) | Engine warning active |
| Col 4 | Text | "Check ECU" | None | Required action |

**Row 3 (Oil System):**
| Column | Content Type | Text Content | Symbol Content | Combined Meaning |
|--------|--------------|--------------|----------------|------------------|
| Col 1 | Text | "Oil Pressure" | None | System identifier |
| Col 2 | Mixed | "Low" | Yellow triangle | Warning condition |
| Col 3 | Symbol | None | Oil can (SYM_002) | Oil pressure warning |
| Col 4 | Text | "Check oil level" | None | Required action |

### SYMBOL-TEXT CORRELATION ANALYSIS

**Symbol Context Mapping:**
| Symbol | Adjacent Text | Row Context | Column Context | Inferred Relationship |
|--------|---------------|-------------|----------------|----------------------|
| SYM_001 | "Engine Control" | Engine systems | Warning column | Engine system warning |
| SYM_002 | "Oil Pressure" | Oil system | Warning column | Oil pressure alert |
| SYM_003 | "Coolant Temp" | Cooling system | Warning column | Temperature warning |
| SYM_004 | "Battery" | Power system | Status column | Battery status indicator |
| SYM_005 | "ABS" | Brake system | Warning column | ABS system alert |

### MIXED CELL ANALYSIS

**Cells with Both Text and Symbols:**
| Cell Location | Text Component | Symbol Component | Relationship Type | Combined Meaning |
|---------------|----------------|------------------|-------------------|------------------|
| (2,2) | "Active" | Green circle | Status indicator | System is active/operational |
| (3,2) | "Low" | Yellow triangle | Warning level | Low level warning condition |
| (4,2) | "Fault" | Red X | Error indicator | System fault detected |
| (5,2) | "OK" | Green checkmark | Status confirmation | System operating normally |
```

### Section 5: Automotive Symbol Catalog
```
=== AUTOMOTIVE SYMBOL CATALOG ===

### ISO 2575 STANDARD COMPLIANCE

**Standard Symbol Verification:**
| Symbol ID | ISO 2575 Code | Standard Description | Detected Symbol | Compliance | Variations |
|-----------|---------------|---------------------|-----------------|------------|------------|
| SYM_001 | ISO 2575-F01 | Engine malfunction | Check engine | Full | Standard |
| SYM_002 | ISO 2575-F02 | Oil pressure | Oil can | Full | Standard |
| SYM_003 | ISO 2575-F03 | Coolant temperature | Thermometer | Partial | Modified |
| SYM_004 | ISO 2575-F04 | Battery charging | Battery | Full | Standard |
| SYM_005 | ISO 2575-F05 | ABS malfunction | ABS circle | Full | Standard |

### SYMBOL MEANING REFERENCE

**Comprehensive Symbol Dictionary:**
| Symbol Type | Visual Description | Standard Meaning | Context in Table | Severity Level | Driver Action |
|-------------|-------------------|------------------|------------------|----------------|---------------|
| Check Engine | Engine outline with exclamation | Engine system malfunction | Engine control row | High | Service required |
| Oil Pressure | Oil can with drop | Low oil pressure warning | Oil system row | Critical | Stop engine |
| Temperature | Thermometer in water | High coolant temperature | Cooling system row | Critical | Stop engine |
| Battery | Battery outline | Charging system problem | Power system row | Medium | Check charging |
| ABS | "ABS" in circle | Anti-lock brake malfunction | Brake system row | High | Service brakes |
| Airbag | Person with circle | Airbag system fault | Safety system row | Critical | Service immediately |
| Seatbelt | Person with belt | Seatbelt not fastened | Safety system row | Medium | Fasten seatbelt |
| Turn Signal | Arrow outline | Turn signal active | Lighting system row | Low | Normal operation |

### SYMBOL COLOR CODING ANALYSIS

**Color-Coded Warning Levels:**
| Color | Meaning | Symbol Count | Severity | Driver Response | Examples |
|-------|---------|--------------|----------|-----------------|----------|
| Red | Critical Warning | 8 | Critical | Immediate action | Engine, Oil, Temperature |
| Yellow/Amber | Caution | 12 | High | Service soon | Check engine, ABS |
| Green | Normal Operation | 6 | Low | No action | Turn signals, lights |
| Blue | Information | 4 | Low | Awareness | High beams, info |
| White | Status | 3 | Low | Normal | General status |

### AUTOMOTIVE SYSTEM MAPPING

**Symbol-to-System Classification:**
| Automotive System | Symbol Count | Critical Symbols | Warning Symbols | Info Symbols | System Priority |
|-------------------|--------------|------------------|-----------------|--------------|-----------------|
| Engine Management | 8 | 3 | 4 | 1 | Critical |
| Safety Systems | 6 | 4 | 2 | 0 | Critical |
| Brake Systems | 4 | 2 | 2 | 0 | Critical |
| Lighting Systems | 5 | 0 | 2 | 3 | Medium |
| Power Systems | 3 | 1 | 2 | 0 | High |
| Comfort Systems | 2 | 0 | 1 | 1 | Low |
```

### Section 6: Table-Telltale Relationship Mapping
```
=== TABLE-TELLTALE RELATIONSHIP MAPPING ===

### CONTEXTUAL SYMBOL ANALYSIS

**Symbol Meaning in Table Context:**
| Symbol | Base Meaning | Table Context | Row Header | Column Header | Contextual Meaning |
|--------|--------------|---------------|------------|---------------|-------------------|
| SYM_001 | Engine fault | Diagnostic table | Engine Control | Warning | Engine control system fault |
| SYM_002 | Oil pressure
