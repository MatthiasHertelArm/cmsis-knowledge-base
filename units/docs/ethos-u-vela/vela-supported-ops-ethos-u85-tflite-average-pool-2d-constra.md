---
id: "vela-supported-ops-ethos-u85-tflite-average-pool-2d-constra"
type: "concept"
domain: "edge-ai"
title: "Supported Ops: Ethos-U85 Specific Operator Constraints / Ethos-U85 TFLite AVERAGE_POOL_2D Constraints"
summary: "Part of: Ethos-U85 Specific Operator Constraints"
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@4bd6685:SUPPORTED_OPS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/SUPPORTED_OPS.md#ethos-u85-tflite-average-pool-2d-constraints"
license: "Apache-2.0"
mode: "V"
---

_Part of: Ethos-U85 Specific Operator Constraints_

This is a list of constraints that the AVERAGE_POOL_2D operator must satisfy in order to be scheduled on the NPU.

- Input(s), Output and Weight tensors must have quantization parameters.
- Kernel constraints:
  - IF padding=VALID:
    - Kernel product must be less than or equal to 256*256
    - Kernel height must be less than or equal to 256.
  - ELSE:
    - Kernel width and height must be less than or equal to 8
- Quantization scale of any tensor must be positive.
