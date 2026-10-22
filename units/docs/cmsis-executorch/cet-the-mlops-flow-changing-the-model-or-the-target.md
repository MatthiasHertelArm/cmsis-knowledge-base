---
id: "cet-the-mlops-flow-changing-the-model-or-the-target"
type: "concept"
domain: "edge-ai"
title: "The MLOps flow: Changing the model or the target"
summary: "The Python side needs no changes at all."
status: "draft"
collection: "cmsis-executorch"
source: "Arm-Examples/CMSIS-Executorch@0a243f1:documentation/mlops-flow.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Executorch/blob/0a243f1/documentation/mlops-flow.md#changing-the-model-or-the-target"
license: "Apache-2.0"
mode: "V"
---

- **Another model:** edit `model/model.py`, run steps 2 and 3.
- **Another NPU configuration:** edit the `mlops:` node (and add the matching
  `target-types:` entry and board layer), run steps 1 to 3:

  ```yaml
  mlops:
    npu:
      type: Ethos-U55          # was Ethos-U85
    vela:
      system: Ethos_U55_High_End_Embedded
      memory: Shared_Sram
  ```

  The Python side needs no changes at all.
