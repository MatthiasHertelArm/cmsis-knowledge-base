---
id: "vela-supported-ops-ethos-u55-and-ethos-u65-tflite-batch-mat"
type: "concept"
domain: "edge-ai"
title: "Supported Ops: Ethos-U55 and Ethos-U65 Specific Operator constraints / Ethos-U55 and Ethos-U65 TFLite BATCH_MATMUL Constraints"
summary: "Part of: Ethos-U55 and Ethos-U65 Specific Operator constraints"
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@eb9cf0d:SUPPORTED_OPS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/SUPPORTED_OPS.md#ethos-u55-and-ethos-u65-tflite-batch-matmul-constraints"
license: "Apache-2.0"
mode: "V"
---

_Part of: Ethos-U55 and Ethos-U65 Specific Operator constraints_

This is a list of constraints that the BATCH_MATMUL operator must satisfy in order to be scheduled on the NPU.

- IF Matmul or (FC with dynamic weights): IFM precision must be Int8
- IF Matmul or (FC with dynamic weights): OFM depth must be less than or equal to 2^16
- IF Matmul or (FC with dynamic weights): Reduced axis must be less than or equal to 2^16
