---
id: "vela-supported-ops-ethos-u55-and-ethos-u65-tflite-conv-2d-c"
type: "concept"
domain: "edge-ai"
title: "Supported Ops: Ethos-U55 and Ethos-U65 Specific Operator constraints / Ethos-U55 and Ethos-U65 TFLite CONV_2D Constraints"
summary: "Part of: Ethos-U55 and Ethos-U65 Specific Operator constraints"
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@eb9cf0d:SUPPORTED_OPS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/SUPPORTED_OPS.md#ethos-u55-and-ethos-u65-tflite-conv-2d-constraints"
license: "Apache-2.0"
mode: "V"
---

_Part of: Ethos-U55 and Ethos-U65 Specific Operator constraints_

This is a list of constraints that the CONV_2D operator must satisfy in order to be scheduled on the NPU.

- 32-bit feature-maps are not supported.
- Bias tensors must be constant
- Bias tensors precision must be Int32 or Int64
- Bias values must be stored in the channel axis
- Int64 bias must be smaller than 1099511627775
- Stride>3 is only supported IF (dilation = 1 AND padding = VALID)
- Weight tensors must be 8-bit precision
- Weigth sum constraints:
  - IF 8-bit IFM:
    - The sum of absolute weights cannot exceed 8323072
  - IF 16-bit IFM:
    - The sum of absolute weights cannot exceed 8323072
