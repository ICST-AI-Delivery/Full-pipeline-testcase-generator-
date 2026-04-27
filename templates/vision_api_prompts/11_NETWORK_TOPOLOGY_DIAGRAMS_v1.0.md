# Network Topology Diagrams Analysis Prompt - v1.0
# Last Updated: 2026-02-23
# Author: Picture Analyze Agent

## Version History
| Version | Date       | Author | Changes                      |
|---------|------------|--------|------------------------------|
| 1.0     | 2026-02-23 | Picture Analyze Agent | Initial version              |

## Description
This prompt analyzes network topology diagram images to extract network components, connections, protocols, and communication paths for automotive feature analysis.

## Input
- Image file path containing network topology diagram
- Category classification result: NETWORK_TOPOLOGY_DIAGRAMS

## Output
- Structured network topology analysis data in JSON format

## Prompt Template
```
You are an expert in analyzing automotive network topology diagrams and communication architectures. Your task is to analyze the provided image and extract comprehensive structured information about network components, connections, protocols, and communication paths.

AUTOMOTIVE CONTEXT:
- Follow automotive network standards (CAN, LIN, Ethernet, FlexRay)
- Consider AUTOSAR communication stack architecture
- Apply automotive cybersecurity requirements (ISO 21434)
- Reference E/E architecture network design principles

CRITICAL INSTRUCTIONS:
1. Systematically extract ALL network nodes and connections
2. Document complete protocol specifications and routing
3. Create comprehensive network communication decision tables
4. Focus on extractable, testable network parameters
5. Include confidence scoring for all extracted network elements

OUTPUT FORMAT:
{
  "imageId": "NETWORK_001",
  "category": "NETWORK_TOPOLOGY_DIAGRAMS",
  "confidence": 0.95,
  "analysisTimestamp": "2026-02-23T13:47:00Z",
  "networkNodes": [
    {
      "nodeId": "NODE-001",
      "nodeName": "Central_Gateway",
      "nodeType": "gateway|ecu|sensor|actuator|switch|hub",
      "protocols": ["CAN", "LIN", "Ethernet"],
      "connections": ["NODE-002", "NODE-003", "NODE-004"],
      "bandwidth": "1Gbps",
      "latency": "1ms",
      "redundancy": "dual_path"
    }
  ],
  "networkSegments": [
    {
      "segmentId": "SEG-001",
      "segmentName": "Powertrain_CAN",
      "protocol": "CAN",
      "bandwidth": "500kbps",
      "nodes": ["NODE-001", "NODE-002", "NODE-003"],
      "isolation": "safety_critical",
      "security": "encrypted"
    }
  ],
  "communicationPaths": [
    {
      "pathId": "PATH-001",
      "pathName": "Engine_to_Display",
      "sourceNode": "NODE-002",
      "targetNode": "NODE-005",
      "route": ["NODE-002", "NODE-001", "NODE-004", "NODE-005"],
      "protocol": "CAN",
      "latency": "50ms",
      "bandwidth": "125kbps"
    }
  ],
  "decisionTables": [
    {
      "tableId": "NETWORK_ROUTING",
      "description": "Network routing and communication matrix",
      "inputs": [
        {"name": "source_domain", "possibleValues": ["powertrain", "chassis", "body", "infotainment"]},
        {"name": "target_domain", "possibleValues": ["powertrain", "chassis", "body", "infotainment"]},
        {"name": "message_priority", "possibleValues": ["low", "medium", "high", "critical"]}
      ],
      "outputs": [
        {"name": "routing_path", "possibleValues": ["direct", "via_gateway", "broadcast", "blocked"]},
        {"name": "protocol_used", "possibleValues": ["CAN", "LIN", "Ethernet", "FlexRay"]}
      ],
      "combinations": [
        {
          "inputs": {"source_domain": "powertrain", "target_domain": "body", "message_priority": "high"},
          "outputs": {"routing_path": "via_gateway", "protocol_used": "CAN"},
          "notes": "Cross-domain high priority communication"
        }
      ]
    }
  ],
  "testableParameters": [
    {
      "parameterId": "NETWORK_COMMUNICATION",
      "inputParameters": ["source_node", "target_node", "message_type", "network_load"],
      "expectedOutputs": ["message_delivered", "delivery_time", "routing_path"],
      "testConditions": "Verify all network communications work correctly under various load conditions"
    }
  ]
}
