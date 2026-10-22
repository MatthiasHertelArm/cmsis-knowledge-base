---
id: "vela-supported-ops-ethos-u55-and-ethos-u65-tflite-resize-bi"
type: "concept"
domain: "edge-ai"
title: "Supported Ops: Ethos-U55 and Ethos-U65 Specific Operator constraints / Ethos-U55 and Ethos-U65 TFLite RESIZE_BILINEAR Constraints"
summary: "Part of: Ethos-U55 and Ethos-U65 Specific Operator constraints"
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@4bd6685:SUPPORTED_OPS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/SUPPORTED_OPS.md#ethos-u55-and-ethos-u65-tflite-resize-bilinear-constraints"
license: "Apache-2.0"
mode: "V"
---

_Part of: Ethos-U55 and Ethos-U65 Specific Operator constraints_

This is a list of constraints that the RESIZE_BILINEAR operator must satisfy in order to be scheduled on the NPU.

- 32-bit feature-maps are not supported.
- IF not (IFM H == IFM W == 1) AND not IFM Shape == OFM Shape:
  - IF W Scale-factor != H Scale-factor:
    - OFM W or H must be 1, and scaling in the dim that is must also be 1
  - IF align corners:
    - Scale-factor is defined as OFM H-1 / IFM H-1
  - ELSE:
    - Scale-factor is defined as OFM H/IFM H
  - IF half pixel centers:
    - Scale-factor needs to be 2x
  - Else:
    - Scale-factor needs to be one of: 2x/4x/8x
