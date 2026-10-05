---
id: "vela-supported-ops-ethos-u85-tflite-transpose-conv-constrai"
type: "concept"
domain: "edge-ai"
title: "Supported Ops: Ethos-U85 Specific Operator Constraints / Ethos-U85 TFLite TRANSPOSE_CONV Constraints"
summary: "Part of: Ethos-U85 Specific Operator Constraints"
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@eb9cf0d:SUPPORTED_OPS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/SUPPORTED_OPS.md#ethos-u85-tflite-transpose-conv-constraints"
license: "Apache-2.0"
mode: "V"
---

_Part of: Ethos-U85 Specific Operator Constraints_

This is a list of constraints that the TRANSPOSE_CONV operator must satisfy in order to be scheduled on the NPU.

- Bias tensors must be constant
- Bias tensors precision must be Int32 or Int64
- Bias values must be stored in the channel axis
- Input(s), Output and Weight tensors must have quantization parameters.
- Int64 bias must be smaller than 281474976710655
- Quantization scale of any tensor must be positive.
- Shape constraints:
  - IF PADDING=SAME:
    - OFM must be equal to IFM * stride
  - ELSE:
    - OFM must be equal to IFM * stride + (kernel - stride)
- Weight tensors must be 8-bit precision
- Weigth sum constraints:
  - IF 8-bit IFM:
    - The sum of absolute weights cannot exceed 8323072
  - IF 16-bit IFM:
    - The sum of absolute weights cannot exceed 2130706432
