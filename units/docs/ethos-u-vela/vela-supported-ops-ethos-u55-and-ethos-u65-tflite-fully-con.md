---
id: "vela-supported-ops-ethos-u55-and-ethos-u65-tflite-fully-con"
type: "concept"
domain: "edge-ai"
title: "Supported Ops: Ethos-U55 and Ethos-U65 Specific Operator constraints / Ethos-U55 and Ethos-U65 TFLite FULLY_CONNECTED Constraints"
summary: "Part of: Ethos-U55 and Ethos-U65 Specific Operator constraints"
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@4bd6685:SUPPORTED_OPS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/SUPPORTED_OPS.md#ethos-u55-and-ethos-u65-tflite-fully-connected-constraints"
license: "Apache-2.0"
mode: "V"
---

_Part of: Ethos-U55 and Ethos-U65 Specific Operator constraints_

This is a list of constraints that the FULLY_CONNECTED operator must satisfy in order to be scheduled on the NPU.

- Bias tensors must be constant
- Bias tensors precision must be Int32 or Int64
- Bias values must be stored in the channel axis
- FullyConnected weights must be on the form O,1,1,..,1,I.
- IF Matmul or (FC with dynamic weights): IFM precision must be Int8
- IF Matmul or (FC with dynamic weights): OFM depth must be less than or equal to 2^16
- IF Matmul or (FC with dynamic weights): Reduced axis must be less than or equal to 2^16
- Int64 bias must be smaller than 1099511627775
- Kernel stride must be in the range (1,3).
- Weight tensors must be 8-bit precision
- Weigth sum constraints:
  - IF 8-bit IFM:
    - The sum of absolute weights cannot exceed 8323072
  - IF 16-bit IFM:
    - The sum of absolute weights cannot exceed 8323072
