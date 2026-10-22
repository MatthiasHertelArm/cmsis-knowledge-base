---
id: "vela-supported-ops-ethos-u55-and-ethos-u65-tosa-summary-tab"
type: "concept"
domain: "edge-ai"
title: "Supported Ops: Ethos-U55 and Ethos-U65 TOSA Summary Table"
summary: "The table below contains TOSA operators for Ethos-U55 and Ethos-U65. For TOSA operators, CPU fallback is not supported and unsupported operators/configurations result in a compiler error."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@4bd6685:SUPPORTED_OPS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/SUPPORTED_OPS.md#ethos-u55-and-ethos-u65-tosa-summary-table"
license: "Apache-2.0"
mode: "V"
---

The table below contains TOSA operators for Ethos-U55 and Ethos-U65.  
For TOSA operators, CPU fallback is not supported and unsupported operators/configurations result in a compiler error.  

| Operator | TOSA Constraints |
| --- | --- |
| ABS | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints) |
| ADD | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints) |
| ARGMAX | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tosa-argmax-constraints) |
| ARITHMETIC_RIGHT_SHIFT | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tosa-arithmetic_right_shift-constraints) |
| AVG_POOL2D | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tosa-avg_pool2d-constraints) |
| CAST | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tosa-cast-constraints) |
| CLAMP | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints) |
| CLZ | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints) |
| CONCAT | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tosa-concat-constraints) |
| CONST | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints) |
| CONV2D | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tosa-conv2d-constraints) |
| CONV3D | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tosa-conv3d-constraints) |
| IDENTITY | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tosa-identity-constraints) |
| LOGICAL_LEFT_SHIFT | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tosa-logical_left_shift-constraints) |
| MATMUL | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tosa-matmul-constraints) |
| MAXIMUM | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints) |
| MAX_POOL2D | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tosa-max_pool2d-constraints) |
| MINIMUM | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints) |
| MUL | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints) |
| NEGATE | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints) |
| PAD | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tosa-pad-constraints) |
| REDUCE_MAX | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tosa-reduce_max-constraints) |
| REDUCE_MIN | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tosa-reduce_min-constraints) |
| REDUCE_SUM | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tosa-reduce_sum-constraints) |
| RESCALE | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tosa-rescale-constraints) |
| RESHAPE | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tosa-reshape-constraints) |
| RESIZE | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tosa-resize-constraints) |
| REVERSE | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tosa-reverse-constraints) |
| SLICE | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tosa-slice-constraints) |
| SUB | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints) |
| TABLE | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tosa-table-constraints) |
| TILE | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tosa-tile-constraints) |
| TRANSPOSE | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tosa-transpose-constraints) |
| TRANSPOSE_CONV2D | [Generic](#ethos-u55-and-ethos-u65-tosa-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tosa-transpose_conv2d-constraints) |
