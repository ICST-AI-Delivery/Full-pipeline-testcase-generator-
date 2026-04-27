# CONSOLIDATED FEATURE ANALYSIS PROMPT v1.0

## PURPOSE
This prompt generates a consolidated summary file that captures the most important visual content from all individual image analyses for a specific automotive feature. The output serves as a single reference point containing explicit content from each image.

## INSTRUCTIONS

You are provided with multiple individual image analysis files for a specific automotive feature (e.g., VEH-F165_Manettino, VEH-F247_External_Lights_Management, etc.). Your task is to create a consolidated summary that explicitly captures the visual content of each image.

### CRITICAL REQUIREMENTS:

1. **EXPLICIT CONTENT CAPTURE**: Extract and document exactly what is visible in each image
   - All text elements must be quoted exactly as they appear
   - All colors must be described with specific names/RGB values where possible
   - All shapes, layouts, and spatial relationships must be explicitly described
   - All technical values (hex codes, signal names, parameters) must be captured verbatim

2. **STANDARDIZED STRUCTURE**: Follow the format below for consistency

3. **PRESERVE TECHNICAL PRECISION**: Maintain all technical specifications without interpretation

## OUTPUT FORMAT

```
=== [FEATURE_NAME] - ALL IMAGES INFORMATION CONSOLIDATED ===

=== IMAGE [NUMBER] - [DESCRIPTIVE_TITLE] ===
Content: [Brief description of what the image shows]
Visual Elements:
- [Explicit description of visual element 1]
- [Explicit description of visual element 2]
- [Continue for all visible elements]
- [Include exact text: "Text shown: 'EXACT_TEXT_HERE'"]
- [Include exact colors: "Color: Red/Green/Blue - RGB approximately (R, G, B)"]
- [Include exact shapes: "Shape: Rectangular/Circular/etc."]
- [Include exact dimensions where visible: "Size: Approximately XxY pixels"]
- [Include exact technical values: "Signal: SignalName", "Value: 0xHEX"]

[Repeat for each image]

=== CONSOLIDATED VISUAL DATA SUMMARY ===

COLORS IDENTIFIED:
- [Color 1]: [Where used and context]
- [Color 2]: [Where used and context]
- [Continue for all colors found]

TEXT ELEMENTS EXTRACTED:
- [Category 1]: "[Exact text 1]", "[Exact text 2]", "[Exact text 3]"
- [Category 2]: "[Exact text 4]", "[Exact text 5]"
- [Continue organizing by logical categories]

SHAPES AND LAYOUTS:
- [Element type]: [Explicit description of shape and layout]
- [Element type]: [Explicit description of shape and layout]
- [Continue for all major visual elements]

TECHNICAL SPECIFICATIONS:
- [Technical aspect 1]: [Exact values and specifications]
- [Technical aspect 2]: [Exact values and specifications]
- [Continue for all technical elements found]

TABLES EXTRACTED:
- **IMAGE [NUMBER] - [TABLE_NAME]**:
  | Column 1 | Column 2 | Column 3 |
  |----------|----------|----------|
  | Data 1   | Data 2   | Data 3   |
  | Data 4   | Data 5   | Data 6   |
  
  [Table description and context]

- **IMAGE [NUMBER] - [TABLE_NAME]**:
  [Repeat for each table found]

CROSS-TABLE RELATIONSHIPS:
- [Relationship 1]: [Description of how tables relate across images]
- [Relationship 2]: [Description of data consistency patterns]
- [Continue for all identified relationships]

DIMENSIONS AND QUALITY:
- [Size specifications where available]
- [Quality observations]
- [Consistency notes]
- [Readability assessments]
```

## SPECIFIC EXTRACTION GUIDELINES:

### TEXT EXTRACTION:
- Quote all text exactly: "SPORT", "ESC OFF", "Position_1", etc.
- Include punctuation and formatting as shown
- Note text colors and backgrounds
- Capture hex values precisely: "0x1", "0x2A", etc.

### COLOR ANALYSIS:
- Use specific color names: "Red", "Orange", "Yellow/Amber", "Green", "Blue", "White", "Black"
- Provide RGB approximations where possible: "RGB approximately (255, 191, 0)"
- Note color contexts: "Red (safety critical)", "Orange (performance indicators)"

### SHAPE AND LAYOUT:
- Describe exact shapes: "Circular red knob", "Rectangular telltale with rounded corners"
- Note spatial arrangements: "5 positions arranged in arc formation", "Circular arrangement of 6 telltales"
- Include relative positioning: "Center position", "Upper left corner"

### TECHNICAL VALUES:
- Preserve exact signal names: "SuspensionSetupSts", "ABS", "TMC", "REG"
- Maintain hex formatting: "0x1", "0x2", "0x3"
- Include parameter mappings: "Position_1 (0x1) → /S (Soft)"

### TABLE EXTRACTION (CRITICAL FOR AUTOMOTIVE SPECIFICATIONS):
- **COMPLETE TABLE STRUCTURE**: Extract every table with full row/column structure preserved
- **MARKDOWN TABLE FORMAT**: Present tables in structured markdown format:
  ```
  | Column 1 | Column 2 | Column 3 |
  |----------|----------|----------|
  | Row 1 Data | Row 1 Data | Row 1 Data |
  | Row 2 Data | Row 2 Data | Row 2 Data |
  ```
- **HEADER PRESERVATION**: Maintain all table headers and sub-headers exactly as shown
- **CELL-BY-CELL ACCURACY**: Every table cell must be captured exactly, including empty cells
- **TABLE RELATIONSHIPS**: Document relationships between multiple tables in the same image
- **CROSS-TABLE REFERENCES**: Identify references between tables across different images

### DIMENSIONS:
- Note approximate sizes where visible: "Approximately 120x50 pixels"
- Include relative scale information
- Comment on visibility and clarity

## QUALITY STANDARDS:

1. **COMPLETENESS**: Every visible element must be documented
2. **ACCURACY**: All text and values must be exactly as shown
3. **CONSISTENCY**: Use the same format for similar elements across images
4. **TECHNICAL PRECISION**: Maintain automotive engineering accuracy
5. **EXPLICIT DETAIL**: Avoid vague descriptions - be specific about what is visible

## EXAMPLE USAGE:

**Input**: Individual analysis files for VEH-F247_External_Lights_Management (images 119, 120, 121)
**Output**: Consolidated file capturing explicit content from all three images with cross-image analysis

## VALIDATION CHECKLIST:

Before finalizing the consolidated analysis, verify:
- [ ] All image numbers are included
- [ ] All visible text is quoted exactly
- [ ] All colors are specifically named
- [ ] All technical values are preserved verbatim
- [ ] **ALL TABLES ARE COMPLETELY EXTRACTED** with every cell captured
- [ ] **TABLE HEADERS AND STRUCTURE** are preserved exactly as shown
- [ ] **CROSS-TABLE RELATIONSHIPS** are identified and documented
- [ ] **MARKDOWN TABLE FORMAT** is used for all tabular data
- [ ] Consolidated summaries group related information logically
- [ ] Format follows the standardized structure
- [ ] No interpretation or assumption - only explicit visual content

This prompt ensures that consolidated feature analyses maintain the same high standard of explicit content capture demonstrated in successful examples like the VEH-F165_Manettino c.txt file.
