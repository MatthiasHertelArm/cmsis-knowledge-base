---
id: "vela-supported-ops-ethos-u55-and-ethos-u65-tflite-generic-c"
type: "concept"
domain: "edge-ai"
title: "Supported Ops: Ethos-U55 and Ethos-U65 TFLite Generic Constraints"
summary: "This is a list of constraints that most operators must satisfy in order to be scheduled on the NPU. (Operators excluded from certain constraints are listed as exceptions )"
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@eb9cf0d:SUPPORTED_OPS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/SUPPORTED_OPS.md#ethos-u55-and-ethos-u65-tflite-generic-constraints"
license: "Apache-2.0"
mode: "V"
---

This is a list of constraints that most operators must satisfy in order to be scheduled on the NPU.  
(Operators excluded from certain constraints are listed as exceptions )

- Only the first dimension of tensors can be dynamic.
- Feature-map dataTypes must be one of {"INT16", "INT32", "INT64", "INT8", "UINT8"}
- Tensors must have constant shape.
- Operations must have at least one IFM.
- Operations must have at least one OFM.
- Input(s), Output and Weight tensors must have quantization parameters.
  - Exceptions: [ARGMAX, EXPAND_DIMS, MIRROR_PAD, PAD, PADV2, QUANTIZE, TRANSPOSE]
- Quantization scale of any tensor must be positive.
  - Exceptions: [ARGMAX, EXPAND_DIMS, MIRROR_PAD, PAD, PADV2, QUANTIZE, TRANSPOSE]
- Per-axis quantization is not supported.
  - Exceptions: [CONV_2D, DEPTHWISE_CONV_2D, FULLY_CONNECTED, TRANSPOSE_CONV]
- 64-bit feature-maps are not supported.
  - Exceptions: [ARGMAX]
- Zero-points must be 0 for Int32 and non-negative for unsigned dataTypes
  - Exceptions: [AVERAGE_POOL_2D, RESIZE_BILINEAR, RESIZE_NEAREST_NEIGHBOR, UNIDIRECTIONAL_SEQUENCE_LSTM]
