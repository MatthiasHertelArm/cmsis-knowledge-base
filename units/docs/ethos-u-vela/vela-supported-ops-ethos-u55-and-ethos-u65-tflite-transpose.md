---
id: "vela-supported-ops-ethos-u55-and-ethos-u65-tflite-transpose"
type: "concept"
domain: "edge-ai"
title: "Supported Ops: Ethos-U55 and Ethos-U65 Specific Operator constraints / Ethos-U55 and Ethos-U65 TFLite TRANSPOSE Constraints"
summary: "Part of: Ethos-U55 and Ethos-U65 Specific Operator constraints"
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@4bd6685:SUPPORTED_OPS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/SUPPORTED_OPS.md#ethos-u55-and-ethos-u65-tflite-transpose-constraints"
license: "Apache-2.0"
mode: "V"
---

_Part of: Ethos-U55 and Ethos-U65 Specific Operator constraints_

This is a list of constraints that the TRANSPOSE operator must satisfy in order to be scheduled on the NPU.

- IF IFM is Int32:
  - Rank must be less than or equal to 4
  - NHWC: C <= 2^16
  - NWHC: N == 1, H <= 2^16, W <= 2^16, C <= 2^14
  - NHCW: N*H <= 2^16, W <= 2^16, C <= 2^16
  - Any other permutation vector is unsupported
- IF IFM is Int8 or Int16
  - NHWC: no shape constraints
  - ELSE IF permutation is: NWHC/NHCW/NCWH/NWCH/NCHW and the tensor is 3D, or higher-rank with all axes outside H/W/C equal to 1:
    - (H, W, C) <= (2^16, 2^16, 2^16)
  - ELSE:
    - Product of any N-2 axes in a rank N tensor must be less than or equal to 2^16. For example, for rank 4: N*H <= 2^16, N*W <= 2^16, N*C <= 2^16, H*W <= 2^16, H*C <= 2^16, W*C <= 2^16.

- Parameter tensors must be constant
- Tensor dimension must be <= 8
