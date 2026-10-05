---
id: "vela-supported-ops-ethos-u85-tflite-resize-bilinear-constra"
type: "concept"
domain: "edge-ai"
title: "Supported Ops: Ethos-U85 Specific Operator Constraints / Ethos-U85 TFLite RESIZE_BILINEAR Constraints"
summary: "Part of: Ethos-U85 Specific Operator Constraints"
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@eb9cf0d:SUPPORTED_OPS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/SUPPORTED_OPS.md#ethos-u85-tflite-resize-bilinear-constraints"
license: "Apache-2.0"
mode: "V"
---

_Part of: Ethos-U85 Specific Operator Constraints_

This is a list of constraints that the RESIZE_BILINEAR operator must satisfy in order to be scheduled on the NPU.

- Input(s), Output and Weight tensors must have quantization parameters.
- Quantization scale of any tensor must be positive.
- Scale-factor must be an integer power of two.
- Scale-factor:
  - IF align_corners:
    - Scale-factor can be maximum 2048
  - ELSE:
    - Scale-factor can be maximum 1024.
- align_corners and half_pixel_centers are mutually exclusive.
