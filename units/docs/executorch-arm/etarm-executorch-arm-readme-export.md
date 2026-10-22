---
id: "etarm-executorch-arm-readme-export"
type: "concept"
domain: "edge-ai"
title: "executorch-arm README: Export"
summary: "The export folder contains the Executorch AOT pt2 quantization and lowering using the Cortex-M backend in export/export_model.py."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@6368414:examples/arm/person_detection_example_cortex_m/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/6368414/examples/arm/person_detection_example_cortex_m/README.md#export"
license: "BSD-3-Clause"
mode: "V"
---

The export folder contains the Executorch AOT pt2 quantization and lowering using the Cortex-M backend in `export/export_model.py`. Additionally the general QuantizeInputs/Outputs passes are applied to make the graph run directly on the int8 data provided by the camera, rather than the standard float inputs/outputs and quantization/ dequantization operators.

A testing script similar the one used when training is also provided to easily compare the accuracy between the original and lowered model, in the `test_exported_model.py` script.
