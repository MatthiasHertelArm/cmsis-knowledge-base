---
id: "alp-analyze-ethos-u-models-with-mlia-4-analyze-tosa-with-vela-what-tosa-is"
type: "concept"
domain: "edge-ai"
title: "Analyze machine learning models for Arm Ethos-U with Arm ML Inference Advisor: Analyze TOSA IR artifacts with MLIA and Vela: What TOSA is"
summary: "Tensor Operator Set Architecture (TOSA) is an intermediate representation (IR) for machine learning graphs. It's a stable set of tensor operators that can sit between a model framework and a target backend."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/4-analyze-tosa-with-vela.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/4-analyze-tosa-with-vela/#what-tosa-is"
license: "CC-BY-SA-4.0"
mode: "V"
---

Tensor Operator Set Architecture (TOSA) is an intermediate representation (IR) for machine learning graphs. It's a stable set of tensor operators that can sit between a model framework and a target backend. The [TOSA specification](https://www.mlplatform.org/tosa/tosa_spec.html) defines the operator set and semantics.

Instead of asking every backend to understand every framework operator directly, a conversion flow can lower supported parts of a model into TOSA. Backend tools can then analyze or compile that TOSA graph for a target.

TOSA can appear in more than one kind of ML workflow. Some compiler flows for LiteRT models can use TOSA as an intermediate representation. Other LiteRT flows hand a `.tflite` file directly to a backend tool such as Vela. In the ExecuTorch Arm Ethos-U flow, supported PyTorch graph regions are lowered to TOSA before Vela compiles them for Ethos-U.
