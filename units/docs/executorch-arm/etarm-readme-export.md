---
id: "etarm-readme-export"
type: "concept"
domain: "edge-ai"
title: "README: Export"
summary: "The export folder contains the Executorch AOT pt2 quantization and lowering using the Cortex-M backend."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@658390c:examples/arm/person_detection_example_cortex_m/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/658390c/examples/arm/person_detection_example_cortex_m/README.md#export"
license: "BSD-3-Clause"
mode: "V"
---

The export folder contains the Executorch AOT pt2 quantization and lowering using the Cortex-M backend. Addtionally the general QuantizeInputs/Outputs passes are applied to make the graph run directly on the int8 data provided by the camera, rather than the standard float inputs/outputs and quantization/ dequantization operators.

A testing script similar the one used when training is also provided to easily compare the accuracy between the original and lowered model.
