# Signal Flow Diagrams Analysis Prompt - v1.0
# Last Updated: 2026-02-23
# Author: Picture Analyze Agent

## Version History
| Version | Date       | Author | Changes                      |
|---------|------------|--------|------------------------------|
| 1.0     | 2026-02-23 | Picture Analyze Agent | Initial version              |

## Description
This prompt analyzes signal flow diagram images to extract signal paths, transformations, processing stages, and data routing for automotive feature analysis.

## Input
- Image file path containing signal flow diagram
- Category classification result: SIGNAL_FLOW_DIAGRAMS

## Output
- Structured signal flow analysis data in JSON format

## Prompt Template
```
You are an expert in analyzing automotive signal flow diagrams and data processing architectures. Your task is to analyze the provided image and extract comprehensive structured information about signal paths, transformations, processing stages, and data routing.

AUTOMOTIVE CONTEXT:
- Follow AUTOSAR signal processing architecture
- Consider real-time signal processing requirements
- Apply automotive signal integrity standards
- Reference ISO 26262 signal safety requirements

CRITICAL INSTRUCTIONS:
1. Systematically extract ALL signal sources, paths, and destinations
2. Document complete signal transformations and processing stages
3. Create comprehensive signal flow decision tables
4. Focus on extractable, testable signal parameters
5. Include confidence scoring for all extracted signal elements

OUTPUT FORMAT:
{
  "imageId": "SIGNAL_001",
  "category": "SIGNAL_FLOW_DIAGRAMS",
  "confidence": 0.95,
  "analysisTimestamp": "2026-02-23T13:48:00Z",
  "signalSources": [
    {
      "sourceId": "SRC-001",
      "sourceName": "Engine_RPM_Sensor",
      "signalType": "analog|digital|pwm|frequency",
      "outputSignal": "rpm_raw",
      "range": "0-8000rpm",
      "accuracy": "±10rpm",
      "updateRate": "100Hz"
    }
  ],
  "processingStages": [
    {
      "stageId": "PROC-001",
      "stageName": "RPM_Filter",
      "inputSignal": "rpm_raw",
      "outputSignal": "rpm_filtered",
      "processing": "low_pass_filter",
      "parameters": {"cutoff_frequency": "10Hz", "order": 2},
      "latency": "5ms"
    }
  ],
  "signalPaths": [
    {
      "pathId": "PATH-001",
      "pathName": "RPM_to_Display",
      "stages": ["SRC-001", "PROC-001", "PROC-002", "DEST-001"],
      "totalLatency": "25ms",
      "signalIntegrity": "high",
      "safetyLevel": "ASIL_B"
    }
  ],
  "decisionTables": [
    {
      "tableId": "SIGNAL_PROCESSING",
      "description": "Signal processing validation matrix",
      "inputs": [
        {"name": "input_signal_quality", "possibleValues": ["good", "degraded", "noisy", "invalid"]},
        {"name": "processing_load", "possibleValues": ["low", "medium", "high", "overload"]}
      ],
      "outputs": [
        {"name": "output_quality", "possibleValues": ["good", "acceptable", "degraded", "invalid"]},
        {"name": "processing_action", "possibleValues": ["normal", "filter", "interpolate", "reject"]}
      ],
      "combinations": [
        {
          "inputs": {"input_signal_quality": "noisy", "processing_load": "low"},
          "outputs": {"output_quality": "acceptable", "processing_action": "filter"},
          "notes": "Apply noise filtering for noisy input"
        }
      ]
    }
  ],
  "testableParameters": [
    {
      "parameterId": "SIGNAL_FLOW",
      "inputParameters": ["input_signal", "processing_parameters", "system_load"],
      "expectedOutputs": ["output_signal", "processing_time", "signal_quality"],
      "testConditions": "Verify all signal processing stages work correctly under various conditions"
    }
  ]
}
