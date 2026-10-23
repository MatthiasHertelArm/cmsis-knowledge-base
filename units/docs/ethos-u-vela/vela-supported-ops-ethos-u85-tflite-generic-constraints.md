---
id: "vela-supported-ops-ethos-u85-tflite-generic-constraints"
type: "concept"
domain: "edge-ai"
title: "Supported Ops: Ethos-U85 TFLite Generic Constraints"
summary: "This is a list of constraints that most operators must satisfy in order to be scheduled on the NPU. (Operators excluded from certain constraints are listed as exceptions )"
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@4bd6685:SUPPORTED_OPS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/SUPPORTED_OPS.md#ethos-u85-tflite-generic-constraints"
license: "Apache-2.0"
mode: "V"
---

This is a list of constraints that most operators must satisfy in order to be scheduled on the NPU.  
(Operators excluded from certain constraints are listed as exceptions )


- Only the first dimension of tensors can be dynamic.
- Feature-map dataTypes must be one of {"BOOL", "INT16", "INT32", "INT64", "INT8", "UINT8"}
  - Exceptions: [ASSIGN_VARIABLE, READ_VARIABLE]
- Tensors must have constant shape.
  - Exceptions: [ASSIGN_VARIABLE, READ_VARIABLE]
- Operations must have at least one IFM.
  - Exceptions: [READ_VARIABLE]
- Operations must have at least one OFM.
  - Exceptions: [ASSIGN_VARIABLE]
- Per-axis quantization is not supported.
  - Exceptions: [CONV_2D, DEPTHWISE_CONV_2D, FULLY_CONNECTED, TRANSPOSE_CONV]
- IFM Zero-points must be in the range:
  - Int8: (-128 <= zp <= 127).
  - UInt8: (0 <= zp <= 255).
  - UInt16: zp must be 0 or 32768.
  - Other: zp must be 0.
  - Exceptions: [AVERAGE_POOL_2D, DIV, RESIZE_BILINEAR, RESIZE_NEAREST_NEIGHBOR, UNIDIRECTIONAL_SEQUENCE_LSTM]
- OFM Zero-points must be in the range:
  - Signed-integer: (-128 <= zp <= 127)
  - Unsigned-integer: (0 <= zp <= 255) OR zp == 32768.
  - Exceptions: [AVERAGE_POOL_2D, DIV, RESIZE_BILINEAR, RESIZE_NEAREST_NEIGHBOR, UNIDIRECTIONAL_SEQUENCE_LSTM]
