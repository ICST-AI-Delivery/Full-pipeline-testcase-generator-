# Complete Flowchart Analysis: Obstacle Proximity Signalling Management State Machine

## Visual Overview

This is a complex state machine flowchart for the **Obstacle Proximity Signalling Management** system. The diagram contains:
- **5 main states** (STATUS 0, STATUS 1, STATUS 2, STATUS 3, STATUS 4)
- **2 delay processes** (ReadDelay = 0 sec, ReadDelay = 1 sec)
- **1 decision point** (Stop_GoEnable)
- **12 distinct transitions** with specific directional arrows

## Complete State Descriptions

### STATUS 0 (System Initialization)
- **Visual Position:** Top center of diagram
- **Shape:** Small circular node
- **Content:** "STATUS 0", "System OFF", "Key OFF"
- **Purpose:** Initial system state before activation

### STATUS 1 (Primary Active State)
- **Visual Position:** Center-left, largest node
- **Shape:** Large circular node with extensive text
- **Content:** 
  - "STATUS_HMI: ReverseGearRCSSts = 'Not_Inserted'"
  - "Front Sensor = OFF"
  - "Rear Sensor = ON"
  - "ELSE Rear Sensor = OFF"
  - "Status Backlight 1"
- **Purpose:** Main operational state when not in reverse

### STATUS 2 (Reverse Preparation)
- **Visual Position:** Bottom-left
- **Shape:** Circular node
- **Content:**
  - "STATUS_HMI: ReverseGearRCSSts = 'Inserted'"
  - "Front Sensor = ON"
  - "Rear Sensor = ON"
  - "Status Backlight 2"
- **Purpose:** Preparation state when reverse gear is engaged

### STATUS 3 (Reverse Active)
- **Visual Position:** Bottom center
- **Shape:** Circular node
- **Content:**
  - "STATUS_HMI: ReverseGearRCSSts = 'Inserted'"
  - "Front Sensor = OFF"
  - "Rear Sensor = ON"
  - "Status Backlight 1"
- **Purpose:** Active reverse operation mode

### STATUS 4 (Forward Proximity Active)
- **Visual Position:** Center-right
- **Shape:** Circular node
- **Content:**
  - "STATUS_HMI: ReverseGearRCSSts = 'Not_Inserted'"
  - "Front Sensor = ON"
  - "IF ReadDelayPD THEN Rear Sensor = ON"
  - "ELSE Rear Sensor = OFF"
  - "Status Backlight 2"
- **Purpose:** Forward proximity signalling active state

## Complete Transition Analysis (All 12 Transitions with Exact Directions)

### Transition 1: System Startup
- **From:** STATUS 0
- **To:** Stop_GoEnable (Decision Diamond)
- **Arrow Direction:** Straight downward ↓
- **Trigger:** Key_On
- **Description:** Initial system activation when ignition is turned on

### Transition 2: Feature Enabled Branch
- **From:** Stop_GoEnable Decision
- **To:** ReadDelay = 0 sec
- **Arrow Direction:** Horizontal rightward →
- **Trigger:** TRUE
- **Label on Arrow:** "TRUE"
- **Description:** When proximity feature is enabled in configuration

### Transition 3: Feature Disabled Branch
- **From:** Stop_GoEnable Decision
- **To:** STATUS 1
- **Arrow Direction:** Straight downward ↓
- **Trigger:** FALSE
- **Label on Arrow:** "FALSE"
- **Description:** When proximity feature is disabled, bypass delay and go to normal operation

### Transition 4: Delay Completion to Normal Operation
- **From:** ReadDelay = 0 sec
- **To:** STATUS 1
- **Arrow Direction:** Curved leftward and downward ↙
- **Trigger:** ReadDelay = 0 sec completion
- **Label on Arrow:** "NPS_FrontButtonSts == 'Pressed'" and "Stop_GoEnable == 'False' from 'True'"
- **Description:** After initialization delay, enter normal operation state

### Transition 5: Speed Safety Return
- **From:** STATUS 1
- **To:** ReadDelay = 0 sec
- **Arrow Direction:** Curved upward and rightward ↗
- **Trigger:** VehicleSpeed > 10 km/h
- **Label on Arrow:** "VehicleSpeed > 10 km/h"
- **Description:** Safety mechanism - return to delay state when speed exceeds threshold

### Transition 6: Forward Proximity Activation (Complex Multi-Line Conditions)
- **From:** STATUS 1
- **To:** STATUS 4
- **Arrow Direction:** Horizontal rightward →
- **Complex Trigger Conditions:**
  - Line 1: "NPS_FrontButtonSts == 'Pressed'"
  - Line 2: "Stop_GoEnable == 'False' from 'True'"
  - Line 3: "NPS_FrontButtonSts == 'Pressed' AND VehicleSpeed ≤ 10km/h"
  - Line 4: "OR"
  - Line 5: "Stop_GoEnable == 'True' AND VehicleSpeed goes below 10km/h"
  - Line 6: "VehicleSpeed ≤ 10km/h AND Stop_GoEnable == 'True' from 'False'"
- **Description:** Multiple pathways to activate forward proximity signalling

### Transition 7: Enter Reverse Preparation
- **From:** STATUS 1
- **To:** STATUS 2
- **Arrow Direction:** Straight downward ↓ (left side of STATUS 1)
- **Trigger:** ReverseGearRCSSts change
- **Label on Arrow:** "ReverseGearRCSSts == 'Not_Inserted'"
- **Description:** Transition to reverse preparation state

### Transition 8: Reverse Gear Engagement with Delay
- **From:** STATUS 2
- **To:** ReadDelay = 1 sec
- **Arrow Direction:** Horizontal rightward →
- **Trigger:** ReverseGearRCSSts == 'Inserted'
- **Label on Arrow:** "ReadDelay = 1 sec"
- **Description:** When reverse gear is engaged, start 1-second safety delay

### Transition 9: Delay Interruption Return
- **From:** ReadDelay = 1 sec
- **To:** STATUS 2
- **Arrow Direction:** Straight upward ↑
- **Trigger:** ReverseGearRCSSts == 'Not_Inserted'
- **Label on Arrow:** "ReverseGearRCSSts == 'Not_Inserted'"
- **Description:** If reverse gear disengaged during delay, return to preparation

### Transition 10: Delay Completion to Reverse Active
- **From:** ReadDelay = 1 sec
- **To:** STATUS 3
- **Arrow Direction:** Straight downward ↓
- **Trigger:** Delay completion with reverse gear still engaged
- **Label on Arrow:** "ReverseGearRCSSts == 'Inserted'"
- **Description:** After 1-second delay, enter full reverse operation

### Transition 11: Exit Reverse via Gear Disengagement
- **From:** STATUS 3
- **To:** STATUS 2
- **Arrow Direction:** Straight upward ↑ (right side)
- **Trigger:** ReverseGearRCSSts == 'Not_Inserted'
- **Label on Arrow:** "ReverseGearRCSSts == 'Not_Inserted'"
- **Description:** Return to preparation when reverse gear is disengaged

### Transition 12: Manual Override Exit from Reverse
- **From:** STATUS 3
- **To:** STATUS 2
- **Arrow Direction:** Horizontal leftward ←
- **Trigger:** NPS_FrontButtonSts == 'Pressed'
- **Label on Arrow:** "NPS_FrontButtonSts == 'Pressed'"
- **Description:** Manual user override to exit reverse operation via button press

## Decision Point Analysis

### Stop_GoEnable Decision Diamond
- **Visual:** Diamond-shaped node below STATUS 0
- **Purpose:** Determines system configuration state
- **TRUE Path:** Rightward to ReadDelay = 0 sec (feature enabled)
- **FALSE Path:** Downward to STATUS 1 (feature disabled)

## Delay Process Analysis

### ReadDelay = 0 sec
- **Visual:** Rectangular process node on right side
- **Input:** From Stop_GoEnable (TRUE branch)
- **Output:** To STATUS 1 (curved arrow)
- **Bidirectional:** Receives return from STATUS 1 on speed violation
- **Purpose:** Initialization delay and speed safety buffer

### ReadDelay = 1 sec
- **Visual:** Rectangular process node between STATUS 2 and STATUS 3
- **Input:** From STATUS 2 (rightward arrow)
- **Output:** To STATUS 3 (downward arrow)
- **Bidirectional:** Can return to STATUS 2 if conditions change
- **Purpose:** Safety delay before full reverse activation

## System Logic Patterns

1. **Speed Safety Logic:** Continuous monitoring prevents operation above 10 km/h
2. **Gear-Based State Management:** Reverse gear status drives major state transitions
3. **Dual Delay System:** Different delays (0 sec and 1 sec) for different operational phases
4. **Manual Override Capability:** Front button provides user control in multiple states
5. **Sensor Configuration Management:** Each state defines specific front/rear sensor patterns
6. **Status Indication:** Different backlight configurations (1 vs 2) for different states

## Critical Safety Features

- **Speed Threshold Enforcement:** System automatically returns to safe state above 10 km/h
- **Reverse Delay Protection:** 1-second delay prevents accidental activation
- **Manual Override:** User can exit any state via front button
- **Gear Status Monitoring:** Continuous monitoring of reverse gear position
- **Sensor State Management:** Appropriate sensor activation based on operational mode

This state machine represents a sophisticated automotive safety system with comprehensive logic for obstacle proximity detection, incorporating multiple safety mechanisms, user controls, and automatic state management based on vehicle conditions.
