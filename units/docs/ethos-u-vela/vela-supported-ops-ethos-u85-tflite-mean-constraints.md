---
id: "vela-supported-ops-ethos-u85-tflite-mean-constraints"
type: "concept"
domain: "edge-ai"
title: "Supported Ops: Ethos-U85 Specific Operator Constraints / Ethos-U85 TFLite MEAN Constraints"
summary: "Part of: Ethos-U85 Specific Operator Constraints"
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@4bd6685:SUPPORTED_OPS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/SUPPORTED_OPS.md#ethos-u85-tflite-mean-constraints"
license: "Apache-2.0"
mode: "V"
---

_Part of: Ethos-U85 Specific Operator Constraints_

This is a list of constraints that the MEAN operator must satisfy in order to be scheduled on the NPU.

- Amount of reduced elements cannot exceed: 16777216(Int8), 8388608(UInt8), 65536(Int16).
- Batch must be 1.
- IFM precision must be one of: (Int8, UInt8, Int16)
- Input(s), Output and Weight tensors must have quantization parameters.
- Parameter tensors must be constant
- Quantization scale of any tensor must be positive.
- Reduced axis must be less than 4096
- Reduction over depth is only supported if any of h,w,c == 1
