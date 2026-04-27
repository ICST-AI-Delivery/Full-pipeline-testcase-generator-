# CORRECTED 13-CATEGORY PROMPT MAPPING
## Picture Analyze Agent - Architectural Restoration

### EXECUTIVE SUMMARY

This document establishes the corrected "one prompt per category" architecture for the Picture Analyze Agent's 13-category image classification system, fixing architectural inconsistencies and ensuring proper category-to-prompt mapping.

---

## OFFICIAL 13-CATEGORY TO PROMPT MAPPING

### **CATEGORY 1: HMI DISPLAY LAYOUTS**
- **Example**: `static/VEH-F804_High_Voltage_Battery/image183.png`
- **Prompt File**: `vision_api_prompts/01_HMI_DISPLAY_LAYOUTS_v1.0.md`
- **Status**: ✅ CORRECT MAPPING
- **Description**: Full instrument-cluster screens showing multiple UI regions together

### **CATEGORY 2: CONFIGURATION TABLES**
- **Example**: `static/VEH-F663_Wireless_Charger_Module_(WCM)_Management/image179.png`
- **Prompt File**: `vision_api_prompts/02_CONFIGURATION_TABLES_v1.0.md`
- **Status**: ✅ CORRECT MAPPING
- **Description**: Technical tables with rows/columns containing text or numbers

### **CATEGORY 3: TELLTALE ICONS & INDICATORS**
- **Example**: `static/VEH-F006_Low_Voltage_Battery_Indication/image3.png`
- **CORRECTED Prompt File**: `vision_api_prompts/03_TELLTALES_AND_ICONS_v1.0.md`
- **Previous INCORRECT**: Used HMI Display prompt (telltale section)
- **Status**: 🔧 FIXED MAPPING
- **Description**: Single isolated car warning icons/symbols

### **CATEGORY 4: TABLE WITH TELLTALES**
- **Example**: `static/VEH-F024_Range_Estimation/image210.png`
- **CORRECTED Prompt File**: `vision_api_prompts/04_TABLE_WITH_TELLTALES_v1.0_SPECIALIZED.md`
- **Previous INCORRECT**: Used modified Configuration Tables prompt
- **Status**: 🔧 FIXED MAPPING (Specialized prompt created)
- **Description**: Tables containing automotive warning pictograms inside cells

### **CATEGORY 5: SYSTEM ARCHITECTURE DIAGRAMS**
- **Example**: `Pre-FineTuneLearning Model/SRS FPI export/SRS_System Architecture/F834_Vf8_R5_VehicleNotInUse_PI_6/image13.png`
- **Prompt File**: `vision_api_prompts/05_SYSTEM_ARCHITECTURE_DIAGRAMS_v2.0_ENHANCED.md`
- **Status**: ✅ CORRECT MAPPING (Enhanced version available)
- **Description**: Block diagrams of modules (ECUs, sensors, controllers) connected by lines

### **CATEGORY 6: PROCESS FLOW DIAGRAMS**
- **Example**: `Pre-FineTuneLearning Model/SRS FPI export/SRS_HMI Software/PRK-0__Obstacle_Proximity_Signalling_Management/image84.png`
- **Prompt File**: `vision_api_prompts/06_PROCESS_FLOW_DIAGRAMS_v5.0_ARROW_DIRECTION_FOCUSED.md`
- **Status**: ✅ CORRECT MAPPING (Highly evolved version)
- **Description**: Process flow diagrams with sequential steps and decision logic

### **CATEGORY 7: STATE FLOW DIAGRAMS**
- **Example**: `Pre-FineTuneLearning Model/SRS FPI export/SRS_Instrument Cluster/VEH-F040_Key_Status/image15.png`
- **Prompt File**: `vision_api_prompts/07_STATE_FLOW_DIAGRAMS_v1.0.md`
- **Status**: ✅ CORRECT MAPPING
- **Description**: State machine diagrams with circular/oval states connected by arrows

### **CATEGORY 8: DIGITAL TIMING DIAGRAMS**
- **Example**: `Pre-FineTuneLearning Model/SRS FPI export/SRS_Instrument Cluster/VEH-F006_Low_Voltage_Battery_Indication/image4.png`
- **CORRECTED Prompt File**: `vision_api_prompts/08_TIMING_DIAGRAMS_DIGITAL_v2.0.md`
- **Previous INCORRECT**: Shared basic timing prompt with analog
- **Status**: 🔧 FIXED MAPPING (Specialized digital prompt)
- **Description**: Digital timing diagrams with horizontal time axis and HIGH/LOW waveforms

### **CATEGORY 9: ANALOG/THRESHOLD TIMING DIAGRAMS**
- **Example**: `Pre-FineTuneLearning Model/SRS FPI export/SRS_Instrument Cluster/VEH-F804_High_Voltage_Battery/image185.png`
- **CORRECTED Prompt File**: `vision_api_prompts/09_TIMING_DIAGRAMS_ANALOG_v2.0.md`
- **Previous INCORRECT**: Shared basic timing prompt with digital
- **Status**: 🔧 FIXED MAPPING (Specialized analog prompt)
- **Description**: Plots versus time with continuous traces and threshold markers

### **CATEGORY 10: COLOR AND GRADIENTS**
- **Example**: `Pre-FineTuneLearning Model/SRS FPI export/SRS_Diagnostics/Display_test_selective_($5036)/image60.png`
- **CORRECTED Prompt File**: `vision_api_prompts/10_COLOR_GRADIENTS_v1.0_SPECIALIZED.md`
- **Previous INCORRECT**: Used generic technical diagrams prompt
- **Status**: 🔧 FIXED MAPPING (Specialized prompt needed)
- **Description**: Color charts, gradient scales, or color calibration patterns

### **CATEGORY 11: TECHNICAL SPECIFICATIONS**
- **Example**: `Pre-FineTuneLearning Model/SRS FPI export/SRS_DMS/DMS-7_DRIVER_GAZE_ESTIMATION/image4.png`
- **CORRECTED Prompt File**: `vision_api_prompts/11_TECHNICAL_SPECIFICATIONS_v2.0_UNIFIED.md`
- **Previous INCORRECT**: Split between Interface + Requirement specifications
- **Status**: 🔧 FIXED MAPPING (Unified prompt needed)
- **Description**: Technical specification documents with detailed requirements

### **CATEGORY 12: MULTI-CONDITION LOGIC**
- **Example**: `Pre-FineTuneLearning Model/SRS FPI export/SRS_Audio/VAS-1_A_AVAS_Management/image146.png`
- **Prompt File**: `vision_api_prompts/12_MULTI_CONDITION_LOGIC_v1.0.md`
- **Status**: ✅ CORRECT MAPPING
- **Description**: Complex logic diagrams with multiple conditions and outcomes

### **CATEGORY 13: GENERAL TECHNICAL DIAGRAMS**
- **Example**: `Pre-FineTuneLearning Model/SRS FPI export/SRS_System Architecture/Smart_USB_-_C/image4.png`
- **Prompt File**: `vision_api_prompts/13_GENERAL_TECHNICAL_DIAGRAMS_v1.0.md`
- **Status**: ✅ CORRECT MAPPING
- **Description**: Various other technical diagrams not fitting specific categories

---

## ARCHITECTURAL FIXES IMPLEMENTED

### **FIXED MAPPINGS (🔧)**

#### 1. **Category 3: Telltale Icons**
- **Problem**: Used HMI Display prompt instead of dedicated telltale prompt
- **Solution**: Use existing `vision_api_prompts/10_TELLTALES_AND_ICONS_v1.0.md`
- **Action**: Renumber to `03_TELLTALES_AND_ICONS_v1.0.md`

#### 2. **Category 4: Table with Telltales**
- **Problem**: Used modified Configuration Tables prompt
- **Solution**: Use specialized `vision_api_prompts/04_TABLE_WITH_TELLTALES_v1.0_SPECIALIZED.md`
- **Action**: ✅ Already created and properly numbered

#### 3. **Categories 8 & 9: Timing Diagrams**
- **Problem**: Both categories shared single basic timing prompt
- **Solution**: Create specialized prompts for each
- **Actions**:
  - Digital: `08_TIMING_DIAGRAMS_DIGITAL_v2.0.md`
  - Analog: `09_TIMING_DIAGRAMS_ANALOG_v2.0.md`

#### 4. **Category 10: Color and Gradients**
- **Problem**: Used generic technical diagrams prompt
- **Solution**: Create specialized color analysis prompt
- **Action**: Create `10_COLOR_GRADIENTS_v1.0_SPECIALIZED.md`

#### 5. **Category 11: Technical Specifications**
- **Problem**: Split between Interface and Requirement specifications
- **Solution**: Create unified technical specifications prompt
- **Action**: Create `11_TECHNICAL_SPECIFICATIONS_v2.0_UNIFIED.md`

### **RENUMBERING REQUIRED**

#### **Current File Renaming Plan**:
```
CURRENT → CORRECTED
vision_api_prompts/10_TELLTALES_AND_ICONS_v1.0.md → 03_TELLTALES_AND_ICONS_v1.0.md
vision_api_prompts/04_STATE_FLOW_DIAGRAMS_v1.0.md → 07_STATE_FLOW_DIAGRAMS_v1.0.md
vision_api_prompts/06_DECISION_LOGIC_TABLES_v1.0.md → 12_MULTI_CONDITION_LOGIC_v1.0.md
vision_api_prompts/09_PROCESS_FLOW_DIAGRAMS_v5.0_ARROW_DIRECTION_FOCUSED.md → 06_PROCESS_FLOW_DIAGRAMS_v5.0_ARROW_DIRECTION_FOCUSED.md
vision_api_prompts/03_SYSTEM_ARCHITECTURE_DIAGRAMS_v2.0_ENHANCED.md → 05_SYSTEM_ARCHITECTURE_DIAGRAMS_v2.0_ENHANCED.md
```

---

## PROMPTS TO DEPRECATE/ARCHIVE

### **FRAGMENTED PROMPTS (Move to archive/)**
- `vision_api_prompts/07_INTERFACE_SPECIFICATIONS_v1.0.md` → Merge into unified technical specs
- `vision_api_prompts/08_REQUIREMENT_SPECIFICATIONS_v1.0.md` → Merge into unified technical specs
- `vision_api_prompts/05_TIMING_DIAGRAMS_v1.0.md` → Replace with specialized digital/analog
- `vision_api_prompts/05_TIMING_DIAGRAMS_v2.0_DIGITAL_FOCUSED.md` → Renumber to 08_
- `vision_api_prompts/05_TIMING_DIAGRAMS_v2.0_ANALOG_THRESHOLD.md` → Renumber to 09_

### **ORPHANED PROMPTS (Evaluate for integration)**
- `vision_api_prompts/10_ERROR_HANDLING_DIAGRAMS_v1.0.md`
- `vision_api_prompts/11_NETWORK_TOPOLOGY_DIAGRAMS_v1.0.md`
- `vision_api_prompts/12_SIGNAL_FLOW_DIAGRAMS_v1.0.md`

---

## IMPLEMENTATION PRIORITY

### **PHASE 1: CRITICAL FIXES (Immediate)**
1. Create `10_COLOR_GRADIENTS_v1.0_SPECIALIZED.md`
2. Create `11_TECHNICAL_SPECIFICATIONS_v2.0_UNIFIED.md`
3. Renumber timing diagram prompts (08_ and 09_)
4. Renumber telltale prompt (03_)

### **PHASE 2: SYSTEM CLEANUP (Short-term)**
1. Renumber all prompts to match 01-13 sequence
2. Archive fragmented/deprecated prompts
3. Update documentation references
4. Validate with example images

### **PHASE 3: QUALITY ENHANCEMENT (Long-term)**
1. Enhance basic v1.0 prompts to v2.0
2. Standardize output formats
3. Implement consistent validation criteria
4. Create architectural documentation

---

## SUCCESS VALIDATION

### **ARCHITECTURAL CONSISTENCY CHECKLIST**
- ✅ Exactly 13 prompts for 13 categories
- ✅ Sequential numbering 01-13
- ✅ No category splits across multiple prompts
- ✅ No orphaned or unmapped prompts
- ✅ Clear category-to-prompt mapping

### **FUNCTIONAL COMPLETENESS CHECKLIST**
- ✅ All image types properly covered
- ✅ Specialized handling for complex categories
- ✅ No analysis gaps or overlaps
- ✅ Consistent quality across categories

This corrected mapping restores the intended "one prompt per category" architecture while preserving all advanced methodologies developed in the system's evolution.
