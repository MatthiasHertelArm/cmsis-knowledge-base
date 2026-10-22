---
id: "vela-supported-ops-ethos-u55-and-ethos-u65-tflite-depthwise"
type: "concept"
domain: "edge-ai"
title: "Supported Ops: Ethos-U55 and Ethos-U65 Specific Operator constraints / Ethos-U55 and Ethos-U65 TFLite DEPTHWISE_CONV_2D Constraints"
summary: "Part of: Ethos-U55 and Ethos-U65 Specific Operator constraints"
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@4bd6685:SUPPORTED_OPS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/SUPPORTED_OPS.md#ethos-u55-and-ethos-u65-tflite-depthwise-conv-2d-constraints"
license: "Apache-2.0"
mode: "V"
---

_Part of: Ethos-U55 and Ethos-U65 Specific Operator constraints_

This is a list of constraints that the DEPTHWISE_CONV_2D operator must satisfy in order to be scheduled on the NPU.

- 32-bit feature-maps are not supported.
- Bias tensors must be constant
- Bias tensors precision must be Int32 or Int64
- Bias values must be stored in the channel axis
- Int64 bias must be smaller than 1099511627775
- Kernel stride must be in the range (1,3).
- Weight tensors must be 8-bit precision
- Weigth sum constraints:
  - IF 8-bit IFM:
    - The sum of absolute weights cannot exceed 8323072
  - IF 16-bit IFM:
    - The sum of absolute weights cannot exceed 8323072
