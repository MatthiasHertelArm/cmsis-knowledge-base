---
id: "vela-supported-ops-ethos-u55-and-ethos-u65-tflite-summary-t"
type: "concept"
domain: "edge-ai"
title: "Supported Ops: Ethos-U55 and Ethos-U65 TFLite Summary Table"
summary: "The table below contains TFLite operators that can be placed on the Ethos-U55 and Ethos-U65. If the constraints are not met, then that operator will be scheduled on the CPU instead."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@eb9cf0d:SUPPORTED_OPS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/SUPPORTED_OPS.md#ethos-u55-and-ethos-u65-tflite-summary-table"
license: "Apache-2.0"
mode: "V"
---

The table below contains TFLite operators that can be placed on the Ethos-U55 and Ethos-U65.  
If the constraints are not met, then that operator will be scheduled on the CPU instead.  
For any other TFLite operator not listed, will be left untouched and scheduled on the CPU.  
Please check the supported operator list for your chosen runtime for further information.

| Operator | TFLite Constraints |
| --- | --- |
| ABS | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-abs-constraints) |
| ADD | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints) |
| ARG_MAX | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-arg_max-constraints) |
| AVERAGE_POOL_2D | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-average_pool_2d-constraints) |
| BATCH_MATMUL | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-batch_matmul-constraints) |
| CONCATENATION | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-concatenation-constraints) |
| CONV_2D | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-conv_2d-constraints) |
| DEPTHWISE_CONV_2D | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-depthwise_conv_2d-constraints) |
| ELU | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-elu-constraints) |
| EXP | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-exp-constraints) |
| EXPAND_DIMS | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints) |
| FULLY_CONNECTED | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-fully_connected-constraints) |
| GELU | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-gelu-constraints) |
| HARD_SWISH | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-hard_swish-constraints) |
| LEAKY_RELU | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-leaky_relu-constraints) |
| LOG | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-log-constraints) |
| LOGISTIC | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-logistic-constraints) |
| MAXIMUM | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-maximum-constraints) |
| MAX_POOL_2D | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-max_pool_2d-constraints) |
| MEAN | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-mean-constraints) |
| MINIMUM | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-minimum-constraints) |
| MIRROR_PAD | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-mirror_pad-constraints) |
| MUL | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints) |
| NEG | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints) |
| PACK | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-pack-constraints) |
| PAD | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-pad-constraints) |
| PADV2 | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-padv2-constraints) |
| PRELU | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-prelu-constraints) |
| QUANTIZE | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-quantize-constraints) |
| REDUCE_MAX | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-reduce_max-constraints) |
| REDUCE_MIN | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-reduce_min-constraints) |
| RELU | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-relu-constraints) |
| RELU6 | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-relu6-constraints) |
| RELU_0_TO_1 | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-relu_0_to_1-constraints) |
| RELU_N1_TO_1 | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-relu_n1_to_1-constraints) |
| RESHAPE | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints) |
| RESIZE_BILINEAR | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-resize_bilinear-constraints) |
| RESIZE_NEAREST_NEIGHBOR | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-resize_nearest_neighbor-constraints) |
| REVERSE_V2 | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-reverse_v2-constraints) |
| RSQRT | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-rsqrt-constraints) |
| SLICE | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-slice-constraints) |
| SOFTMAX | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-softmax-constraints) |
| SPLIT | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-split-constraints) |
| SPLIT_V | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-split_v-constraints) |
| SQUARED_DIFFERENCE | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-squared_difference-constraints) |
| SQUEEZE | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints) |
| STRIDED_SLICE | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-strided_slice-constraints) |
| SUB | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints) |
| SUM | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-sum-constraints) |
| TANH | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-tanh-constraints) |
| TILE | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-tile-constraints) |
| TRANSPOSE | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-transpose-constraints) |
| TRANSPOSE_CONV | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-transpose_conv-constraints) |
| UNIDIRECTIONAL_SEQUENCE_LSTM | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-unidirectional_sequence_lstm-constraints) |
| UNPACK | [Generic](#ethos-u55-and-ethos-u65-tflite-generic-constraints), [Specific](#ethos-u55-and-ethos-u65-tflite-unpack-constraints) |
