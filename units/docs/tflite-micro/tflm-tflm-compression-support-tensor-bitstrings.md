---
id: "tflm-tflm-compression-support-tensor-bitstrings"
type: "concept"
domain: "edge-ai"
title: "TFLM Compression Support: Tensor Bitstrings"
summary: "Each compressed tensor has its buffer data replaced by a packed bitstring. The bitstring consists of fixed bit width groups (indices), each group representing an offset into the value table."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@bd621c2:tensorflow/lite/micro/docs/compression.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/bd621c2/tensorflow/lite/micro/docs/compression.md#tensor-bitstrings"
license: "Apache-2.0"
mode: "V"
---

Each compressed tensor has its buffer data replaced by a packed bitstring.  The
bitstring consists of fixed bit width groups (indices), each group representing an offset
into the `value table`.  The bitstring is in big-endian byte order with the most
significant bit first.  A bitstring is padded on the end, to the next byte
boundary, with zero bits.

Example (bit width 3):
```
1110000110100000
--|--|--|--|---|
  7  0  3  2   padding
```
This bitstring represents the indices 7, 0, 3, 2 as offsets into the `value table`.
Each offset is in the same units as the original (uncompressed) tensor.  So if
the tensor is INT8, each offset represents a byte in the `value table`. If the
tensor was FLOAT32, each offset would represent four bytes.

While the compressed tensor data buffer will shrink in size, the tensor shape
(dimensions) will remain the same as the uncompressed tensor.

The indices in the bitstring are in the same order as the tensor's original data.
Compression never reorders the tensor data, simplifying the decompression phase.
