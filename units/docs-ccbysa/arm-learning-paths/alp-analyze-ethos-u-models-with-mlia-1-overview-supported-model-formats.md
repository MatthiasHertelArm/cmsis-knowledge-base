---
id: "alp-analyze-ethos-u-models-with-mlia-1-overview-supported-model-formats"
type: "concept"
domain: "edge-ai"
title: "Analyze machine learning models for Arm Ethos-U with Arm ML Inference Advisor: Understand where MLIA fits in model preparation: Supported model formats"
summary: "MLIA can analyze different kinds of model artifacts depending on what workflow you are using and the stage that you want to analyze:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/1-overview.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/1-overview/#supported-model-formats"
license: "CC-BY-SA-4.0"
mode: "V"
---

MLIA can analyze different kinds of model artifacts depending on what workflow you are using and the stage that you want to analyze:

| Format | Where it fits |
| --- | --- |
| `.pte` | Serialized ExecuTorch program. Ethos-U `.pte` performance analysis uses Corstone backends. |
| `.tflite` | LiteRT model format used in many Ethos-U and embedded ML workflows. |
| `.tosa` | Intermediate representation consumed by compiler or backend flows such as Ethos-U Vela. |
