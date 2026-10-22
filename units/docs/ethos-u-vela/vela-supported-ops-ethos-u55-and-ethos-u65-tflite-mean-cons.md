---
id: "vela-supported-ops-ethos-u55-and-ethos-u65-tflite-mean-cons"
type: "concept"
domain: "edge-ai"
title: "Supported Ops: Ethos-U55 and Ethos-U65 Specific Operator constraints / Ethos-U55 and Ethos-U65 TFLite MEAN Constraints"
summary: "Part of: Ethos-U55 and Ethos-U65 Specific Operator constraints"
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@4bd6685:SUPPORTED_OPS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/SUPPORTED_OPS.md#ethos-u55-and-ethos-u65-tflite-mean-constraints"
license: "Apache-2.0"
mode: "V"
---

_Part of: Ethos-U55 and Ethos-U65 Specific Operator constraints_

This is a list of constraints that the MEAN operator must satisfy in order to be scheduled on the NPU.

- 32-bit feature-maps are not supported.
- Amount of reduced elements cannot exceed: 16777216(Int8), 8388608(UInt8), 65536(Int16).
- Batch must be 1.
- IFM precision must be one of: (Int8, UInt8, Int16)
- Parameter tensors must be constant
- Reduced axis must be less than 4096
- Reduction over depth is only supported if any of h,w,c == 1
