---
id: "vela-supported-ops-ethos-u85-tflite-strided-slice-constrain"
type: "concept"
domain: "edge-ai"
title: "Supported Ops: Ethos-U85 Specific Operator Constraints / Ethos-U85 TFLite STRIDED_SLICE Constraints"
summary: "Part of: Ethos-U85 Specific Operator Constraints"
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@4bd6685:SUPPORTED_OPS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/SUPPORTED_OPS.md#ethos-u85-tflite-strided-slice-constraints"
license: "Apache-2.0"
mode: "V"
---

_Part of: Ethos-U85 Specific Operator Constraints_

This is a list of constraints that the STRIDED_SLICE operator must satisfy in order to be scheduled on the NPU.

- Input(s), Output and Weight tensors must have quantization parameters.
- Parameter tensors must be constant
- Quantization scale of any tensor must be positive.
- Slice must represent a volume. Stride must be non-negative (and over W or H).
