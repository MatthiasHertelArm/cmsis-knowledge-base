---
id: "vela-supported-ops-ethos-u85-tflite-summary-table"
type: "concept"
domain: "edge-ai"
title: "Supported Ops: Ethos-U85 TFLite Summary Table"
summary: "The table below contains TFLite operators that can be placed on the Ethos-U85. If the constraints are not met, then that operator will be scheduled on the CPU instead."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@4bd6685:SUPPORTED_OPS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/SUPPORTED_OPS.md#ethos-u85-tflite-summary-table"
license: "Apache-2.0"
mode: "V"
---

The table below contains TFLite operators that can be placed on the Ethos-U85.  
If the constraints are not met, then that operator will be scheduled on the CPU instead.  
For any other TFLite operator not listed, will be left untouched and scheduled on the CPU.  
Please check the supported operator list for your chosen runtime for further information.  

| Operator | TFLite Constraints |
| --- | --- |
| ABS | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-abs-constraints) |
| ADD | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-add-constraints) |
| ARG_MAX | [Generic](#ethos-u85-tflite-generic-constraints) |
| ASSIGN_VARIABLE | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-assign_variable-constraints) |
| AVERAGE_POOL_2D | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-average_pool_2d-constraints) |
| BATCH_MATMUL | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-batch_matmul-constraints) |
| CAST | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-cast-constraints) |
| CONCATENATION | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-concatenation-constraints) |
| CONV_2D | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-conv_2d-constraints) |
| DEPTHWISE_CONV_2D | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-depthwise_conv_2d-constraints) |
| DIV | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-div-constraints) |
| ELU | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-elu-constraints) |
| EQUAL | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-equal-constraints) |
| EXP | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-exp-constraints) |
| EXPAND_DIMS | [Generic](#ethos-u85-tflite-generic-constraints) |
| FULLY_CONNECTED | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-fully_connected-constraints) |
| GATHER | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-gather-constraints) |
| GELU | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-gelu-constraints) |
| GREATER | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-greater-constraints) |
| GREATER_EQUAL | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-greater_equal-constraints) |
| HARD_SWISH | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-hard_swish-constraints) |
| LEAKY_RELU | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-leaky_relu-constraints) |
| LESS | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-less-constraints) |
| LESS_EQUAL | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-less_equal-constraints) |
| LOG | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-log-constraints) |
| LOGICAL_AND | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-logical_and-constraints) |
| LOGICAL_NOT | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-logical_not-constraints) |
| LOGICAL_OR | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-logical_or-constraints) |
| LOGISTIC | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-logistic-constraints) |
| MAXIMUM | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-maximum-constraints) |
| MAX_POOL_2D | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-max_pool_2d-constraints) |
| MEAN | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-mean-constraints) |
| MINIMUM | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-minimum-constraints) |
| MIRROR_PAD | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-mirror_pad-constraints) |
| MUL | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-mul-constraints) |
| NEG | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-neg-constraints) |
| NOT_EQUAL | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-not_equal-constraints) |
| PACK | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-pack-constraints) |
| PAD | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-pad-constraints) |
| PADV2 | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-padv2-constraints) |
| PRELU | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-prelu-constraints) |
| QUANTIZE | [Generic](#ethos-u85-tflite-generic-constraints) |
| READ_VARIABLE | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-read_variable-constraints) |
| REDUCE_ALL | [Generic](#ethos-u85-tflite-generic-constraints) |
| REDUCE_ANY | [Generic](#ethos-u85-tflite-generic-constraints) |
| REDUCE_MAX | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-reduce_max-constraints) |
| REDUCE_MIN | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-reduce_min-constraints) |
| RELU | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-relu-constraints) |
| RELU6 | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-relu6-constraints) |
| RELU_0_TO_1 | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-relu_0_to_1-constraints) |
| RELU_N1_TO_1 | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-relu_n1_to_1-constraints) |
| RESHAPE | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-reshape-constraints) |
| RESIZE_BILINEAR | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-resize_bilinear-constraints) |
| RESIZE_NEAREST_NEIGHBOR | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-resize_nearest_neighbor-constraints) |
| REVERSE_V2 | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-reverse_v2-constraints) |
| RSQRT | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-rsqrt-constraints) |
| SCATTER_ND | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-scatter_nd-constraints) |
| SELECT | [Generic](#ethos-u85-tflite-generic-constraints) |
| SELECT_V2 | [Generic](#ethos-u85-tflite-generic-constraints) |
| SLICE | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-slice-constraints) |
| SOFTMAX | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-softmax-constraints) |
| SPLIT | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-split-constraints) |
| SPLIT_V | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-split_v-constraints) |
| SQUARED_DIFFERENCE | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-squared_difference-constraints) |
| SQUEEZE | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-squeeze-constraints) |
| STRIDED_SLICE | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-strided_slice-constraints) |
| SUB | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-sub-constraints) |
| SUM | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-sum-constraints) |
| TANH | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-tanh-constraints) |
| TILE | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-tile-constraints) |
| TRANSPOSE | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-transpose-constraints) |
| TRANSPOSE_CONV | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-transpose_conv-constraints) |
| UNIDIRECTIONAL_SEQUENCE_LSTM | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-unidirectional_sequence_lstm-constraints) |
| UNPACK | [Generic](#ethos-u85-tflite-generic-constraints), [Specific](#ethos-u85-tflite-unpack-constraints) |
