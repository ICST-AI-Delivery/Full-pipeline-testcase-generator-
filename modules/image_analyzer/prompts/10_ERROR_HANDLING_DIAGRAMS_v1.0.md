# Error Handling Diagrams Analysis Prompt - v1.0
# Last Updated: 2026-02-23
# Author: Picture Analyze Agent

## Version History
| Version | Date       | Author | Changes                      |
|---------|------------|--------|------------------------------|
| 1.0     | 2026-02-23 | Picture Analyze Agent | Initial version              |

## Description
This prompt analyzes error handling diagram images to extract error conditions, recovery procedures, fault tolerance mechanisms, and diagnostic workflows for automotive feature analysis.

## Input
- Image file path containing error handling diagram
- Category classification result: ERROR_HANDLING_DIAGRAMS

## Output
- Structured error handling analysis data in JSON format

## Prompt Template
```
You are an expert in analyzing automotive error handling diagrams and fault management systems. Your task is to analyze the provided image and extract comprehensive structured information about error conditions, recovery procedures, fault tolerance mechanisms, and diagnostic workflows.

AUTOMOTIVE CONTEXT:
- Follow ISO 26262 functional safety error handling requirements
- Consider AUTOSAR error handling and recovery mechanisms
- Apply automotive diagnostic standards (ISO 14229, UDS)
- Reference fault tolerance and fail-safe design principles

CRITICAL INSTRUCTIONS:
1. Systematically extract ALL error conditions and handling procedures
2. Document complete recovery sequences and fallback mechanisms
3. Create comprehensive error handling decision tables
4. Focus on extractable, testable error scenarios
5. Include confidence scoring for all extracted error handling logic

OUTPUT FORMAT:
{
  "imageId": "ERROR_001",
  "category": "ERROR_HANDLING_DIAGRAMS",
  "confidence": 0.95,
  "analysisTimestamp": "2026-02-23T13:46:00Z",
  "errorConditions": [
    {
      "errorId": "ERR-001",
      "errorName": "Engine_Overheat",
      "errorType": "critical|warning|information|system_fault",
      "description": "Engine temperature exceeds safe operating limits",
      "detectionMethod": "temperature_sensor_monitoring",
      "triggers": ["temperature > 115C", "coolant_flow_low"],
      "safetyLevel": "ASIL_B",
      "detectionTime": "100ms",
      "responseTime": "500ms"
    }
  ],
  "recoveryProcedures": [
    {
      "procedureId": "REC-001",
      "procedureName": "Engine_Overheat_Recovery",
      "errorId": "ERR-001",
      "steps": [
        {"step": 1, "action": "reduce_engine_power", "duration": "immediate"},
        {"step": 2, "action": "activate_warning_display", "duration": "100ms"},
        {"step": 3, "action": "increase_cooling_fan_speed", "duration": "200ms"},
        {"step": 4, "action": "log_diagnostic_event", "duration": "50ms"}
      ],
      "fallbackAction": "engine_shutdown",
      "recoveryTime": "5000ms"
    }
  ],
  "decisionTables": [
    {
      "tableId": "ERROR_HANDLING",
      "description": "Error condition handling matrix",
      "inputs": [
        {"name": "error_severity", "possibleValues": ["low", "medium", "high", "critical"]},
        {"name": "system_state", "possibleValues": ["normal", "degraded", "fault", "safe"]}
      ],
      "outputs": [
        {"name": "recovery_action", "possibleValues": ["continue", "degrade", "shutdown", "safe_stop"]},
        {"name": "user_notification", "possibleValues": ["none", "warning", "alert", "critical"]}
      ],
      "combinations": [
        {
          "inputs": {"error_severity": "critical", "system_state": "normal"},
          "outputs": {"recovery_action": "safe_stop", "user_notification": "critical"},
          "notes": "Critical error requires immediate safe stop"
        }
      ]
    }
  ],
  "testableParameters": [
    {
      "parameterId": "ERROR_RECOVERY",
      "inputParameters": ["error_condition", "system_state", "environmental_factors"],
      "expectedOutputs": ["recovery_executed", "system_stabilized", "diagnostic_logged"],
      "testConditions": "Verify all error conditions trigger appropriate recovery procedures"
    }
  ]
}
