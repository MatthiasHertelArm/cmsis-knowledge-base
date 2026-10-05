---
id: "alp-analyze-ethos-u-models-with-mlia-3-tflite-comparison-read-operator-placement"
type: "concept"
domain: "edge-ai"
title: "Analyze machine learning models for Arm Ethos-U with Arm ML Inference Advisor: Analyze LiteRT artifacts with MLIA and Vela: Read operator placement"
summary: "The summary result tells you that the model is compatible overall. To see how MLIA reached that result, look at the entities list. Each operator entity describes one analyzed operator and includes a placement field:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/3-tflite-comparison.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/3-tflite-comparison/#read-operator-placement"
license: "CC-BY-SA-4.0"
mode: "V"
---

The summary result tells you that the model is compatible overall. To see how MLIA reached that result, look at the `entities` list. Each operator entity describes one analyzed operator and includes a `placement` field:

```json
{
  "scope": "operator",
  "name": "...",
  "placement": "npu",
  "attributes": {
    "op_type": "Conv2D"
  }
}
```

Names and attributes vary by input format and MLIA version. The important part is the placement. The placement tells you where MLIA and the backend analysis expect the operator to land for this target profile.

If a future model has unsupported operators, this is where you start narrowing down the problem. Find the operator whose placement or check status differs from the expected NPU path. Then, inspect that part of the model graph or change the model before deployment.
