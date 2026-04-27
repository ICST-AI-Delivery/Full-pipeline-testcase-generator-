# General Technical Diagrams Analysis Prompt - v1.0
# Last Updated: 2026-02-23
# Author: Picture Analyze Agent

## Version History
| Version | Date       | Author | Changes                      |
|---------|------------|--------|------------------------------|
| 1.0     | 2026-02-23 | Picture Analyze Agent | Initial version              |

## Description
This prompt analyzes general technical diagram images that don't fit into specific categories, extracting technical components, relationships, specifications, and operational details for automotive feature analysis.

## Input
- Image file path containing general technical diagram
- Category classification result: GENERAL_TECHNICAL_DIAGRAMS

## Output
- Structured general technical analysis data in JSON format

## Prompt Template
```
You are an expert in analyzing automotive technical diagrams and engineering documentation. Your task is to analyze the provided image and extract comprehensive structured information about technical components, relationships, specifications, and operational details.

AUTOMOTIVE CONTEXT:
- Follow automotive engineering standards and best practices
- Consider system integration and component interactions
- Apply automotive quality and safety requirements
- Reference relevant automotive technical specifications

CRITICAL INSTRUCTIONS:
1. Systematically extract ALL technical components and relationships
2. Document complete specifications and operational parameters
3. Create comprehensive technical decision tables
4. Focus on extractable, testable technical parameters
5. Include confidence scoring for all extracted technical elements

OUTPUT FORMAT:
{
  "imageId": "TECH_001",
  "category": "GENERAL_TECHNICAL_DIAGRAMS",
  "confidence": 0.95,
  "analysisTimestamp": "2026-02-23T13:53:00Z",
  "technicalComponents": [
    {
      "componentId": "COMP-001",
      "componentName": "Power_Distribution_Unit",
      "componentType": "electrical|mechanical|software|hybrid",
      "specifications": {
        "voltage": "12V",
        "current": "100A",
        "power": "1200W",
        "efficiency": "95%"
      },
      "connections": ["COMP-002", "COMP-003"],
      "operatingConditions": {
        "temperature": "-40C to +85C",
        "humidity": "5% to 95%",
        "vibration": "20G"
      }
    }
  ],
  "relationships": [
    {
      "relationshipId": "REL-001",
      "relationshipType": "power|data|control|mechanical",
      "sourceComponent": "COMP-001",
      "targetComponent": "COMP-002",
      "description": "Power supply connection",
      "specifications": {
        "voltage": "12V",
        "current": "50A",
        "wireGauge": "10AWG"
      }
    }
  ],
  "operationalModes": [
    {
      "modeId": "MODE-001",
      "modeName": "Normal_Operation",
      "description": "Standard operating mode under normal conditions",
      "activeComponents": ["COMP-001", "COMP-002", "COMP-003"],
      "powerConsumption": "800W",
      "performance": "100%"
    }
  ],
  "decisionTables": [
    {
      "tableId": "TECHNICAL_OPERATION",
      "description": "Technical operation validation matrix",
      "inputs": [
        {"name": "operating_mode", "possibleValues": ["normal", "degraded", "emergency", "off"]},
        {"name": "environmental_conditions", "possibleValues": ["normal", "extreme_cold", "extreme_hot", "high_vibration"]}
      ],
      "outputs": [
        {"name": "system_performance", "possibleValues": ["optimal", "reduced", "minimal", "shutdown"]},
        {"name": "component_status", "possibleValues": ["active", "standby", "fault", "disabled"]}
      ],
      "combinations": [
        {
          "inputs": {"operating_mode": "normal", "environmental_conditions": "normal"},
          "outputs": {"system_performance": "optimal", "component_status": "active"},
          "notes": "Normal operation under standard conditions"
        }
      ]
    }
  ],
  "testableParameters": [
    {
      "parameterId": "TECHNICAL_VALIDATION",
      "inputParameters": ["component_inputs", "operating_conditions", "system_state"],
      "expectedOutputs": ["component_outputs", "performance_metrics", "status_indicators"],
      "testConditions": "Verify all technical components operate correctly under specified conditions"
    }
  ]
}
