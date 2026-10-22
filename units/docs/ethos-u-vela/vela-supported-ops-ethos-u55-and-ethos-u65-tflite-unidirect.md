---
id: "vela-supported-ops-ethos-u55-and-ethos-u65-tflite-unidirect"
type: "concept"
domain: "edge-ai"
title: "Supported Ops: Ethos-U55 and Ethos-U65 Specific Operator constraints / Ethos-U55 and Ethos-U65 TFLite UNIDIRECTIONAL_SEQUENCE_LSTM Constraints"
summary: "Part of: Ethos-U55 and Ethos-U65 Specific Operator constraints"
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@4bd6685:SUPPORTED_OPS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/SUPPORTED_OPS.md#ethos-u55-and-ethos-u65-tflite-unidirectional-sequence-lstm-constraints"
license: "Apache-2.0"
mode: "V"
---

_Part of: Ethos-U55 and Ethos-U65 Specific Operator constraints_

This is a list of constraints that the UNIDIRECTIONAL_SEQUENCE_LSTM operator must satisfy in order to be scheduled on the NPU.

- 32-bit feature-maps are not supported.
- Gate normalization is not supported.
- Implicit gate calculation is not supported.
- Peephole variant is not supported.
- Projection is not supported.
