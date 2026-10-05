---
id: "vela-supported-ops-ethos-u85-tflite-unidirectional-sequence"
type: "concept"
domain: "edge-ai"
title: "Supported Ops: Ethos-U85 Specific Operator Constraints / Ethos-U85 TFLite UNIDIRECTIONAL_SEQUENCE_LSTM Constraints"
summary: "Part of: Ethos-U85 Specific Operator Constraints"
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@eb9cf0d:SUPPORTED_OPS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/SUPPORTED_OPS.md#ethos-u85-tflite-unidirectional-sequence-lstm-constraints"
license: "Apache-2.0"
mode: "V"
---

_Part of: Ethos-U85 Specific Operator Constraints_

This is a list of constraints that the UNIDIRECTIONAL_SEQUENCE_LSTM operator must satisfy in order to be scheduled on the NPU.

- Gate normalization is not supported.
- Implicit gate calculation is not supported.
- Input(s), Output and Weight tensors must have quantization parameters.
- Peephole variant is not supported.
- Projection is not supported.
- Quantization scale of any tensor must be positive.
