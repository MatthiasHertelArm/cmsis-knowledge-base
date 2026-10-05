---
id: "vela-supported-ops-ethos-u85-tflite-gelu-constraints"
type: "concept"
domain: "edge-ai"
title: "Supported Ops: Ethos-U85 Specific Operator Constraints / Ethos-U85 TFLite GELU Constraints"
summary: "Part of: Ethos-U85 Specific Operator Constraints"
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@eb9cf0d:SUPPORTED_OPS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/SUPPORTED_OPS.md#ethos-u85-tflite-gelu-constraints"
license: "Apache-2.0"
mode: "V"
---

_Part of: Ethos-U85 Specific Operator Constraints_

This is a list of constraints that the GELU operator must satisfy in order to be scheduled on the NPU.

- IFM and OFM datatypes must match, and must be Int8 or UInt8
- IFM and OFM shapes must match
- Input(s), Output and Weight tensors must have quantization parameters.
- Quantization scale of any tensor must be positive.
