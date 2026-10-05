---
id: "vela-supported-ops-ethos-u55-and-ethos-u65-tflite-average-p"
type: "concept"
domain: "edge-ai"
title: "Supported Ops: Ethos-U55 and Ethos-U65 Specific Operator constraints / Ethos-U55 and Ethos-U65 TFLite AVERAGE_POOL_2D Constraints"
summary: "Part of: Ethos-U55 and Ethos-U65 Specific Operator constraints"
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@eb9cf0d:SUPPORTED_OPS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/SUPPORTED_OPS.md#ethos-u55-and-ethos-u65-tflite-average-pool-2d-constraints"
license: "Apache-2.0"
mode: "V"
---

_Part of: Ethos-U55 and Ethos-U65 Specific Operator constraints_

This is a list of constraints that the AVERAGE_POOL_2D operator must satisfy in order to be scheduled on the NPU.

- 32-bit feature-maps are not supported.
- Kernel constraints:
  - IF padding=VALID:
    - Kernel product must be less than or equal to 256*256
    - Kernel height must be less than or equal to 256.
  - ELSE:
    - Kernel width and height must be less than or equal to 8
- Stride>3 is only supported IF (dilation = 1 AND padding = VALID)
