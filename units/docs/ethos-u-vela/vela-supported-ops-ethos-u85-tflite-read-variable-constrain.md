---
id: "vela-supported-ops-ethos-u85-tflite-read-variable-constrain"
type: "concept"
domain: "edge-ai"
title: "Supported Ops: Ethos-U85 Specific Operator Constraints / Ethos-U85 TFLite READ_VARIABLE Constraints"
summary: "Part of: Ethos-U85 Specific Operator Constraints"
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@4bd6685:SUPPORTED_OPS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/SUPPORTED_OPS.md#ethos-u85-tflite-read-variable-constraints"
license: "Apache-2.0"
mode: "V"
---

_Part of: Ethos-U85 Specific Operator Constraints_

This is a list of constraints that the READ_VARIABLE operator must satisfy in order to be scheduled on the NPU.

- Variable handle tensors must be Resource. Variable data tensors must be one of {"BOOL", "INT16", "INT32", "INT64", "INT8", "UINT8"}
