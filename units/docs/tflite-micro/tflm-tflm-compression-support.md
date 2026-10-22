---
id: "tflm-tflm-compression-support"
type: "concept"
domain: "edge-ai"
title: "TFLM Compression Support"
summary: "TFLM supports fixed width compression of const-tensors using lookup tables. Const-tensors are typically those containing trained weights or biases, but can be any tensor where the values are fixed within the model and unchanging."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@bd621c2:tensorflow/lite/micro/docs/compression.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/bd621c2/tensorflow/lite/micro/docs/compression.md"
license: "Apache-2.0"
mode: "V"
---

TFLM supports fixed width compression of const-tensors using lookup tables.
Const-tensors are typically those containing trained weights or biases, but can
be any tensor where the values are fixed within the model and unchanging.

For a complete end-to-end tutorial demonstrating compression with weight clustering,
see the [MNIST Compression Tutorial](https://github.com/tensorflow/tflite-micro/blob/bd621c2/tensorflow/lite/micro/docs/../compression/tutorial/mnist_compression_tutorial.ipynb).

Const-tensors are compressed to fixed width bitstrings, and lookup tables are
added to the model schema for each tensor.

When accessing a compressed tensor, each kernel invokes a common decompression
method.  Each set of fixed width bits in the tensor bitstring are used as
indices into the tensor lookup table.  The results of the lookup table operations
are placed into a scratch buffer representing the tensor decompressed data.

Decompression results in increased latency during inference.
There will also be an increase in the size of non-persistent arena memory, due to
the use of scratch buffers to temporarily hold the decompressed data.

# Supported Tensor Types

* FLOAT32, INT8, INT16, INT32, INT64, BOOL

# Supported Kernels

* FULLY_CONNECTED
* CONV_2D
* DEPTHWISE_CONV
* TRANSPOSE_CONV
* CONCATENATION
* ASSIGN_VARIABLE

Per-channel quantized tensor support is available for:
* CONV_2D
* DEPTHWISE_CONV
* TRANSPOSE_CONV
* FULLY_CONNECTED

# Supported Platforms

* X86
* XTENSA
  * P6_VISION, HIFI_MINI, HIFI3, HIFI4, HIFI5

# Model and Metadata Schema for Compression

Models that use compression will have a string key in their `Metadata` vector
corresponding to `COMPRESSION_METADATA`.  The buffer indexed by such a `Metadata`
entry will contain the compression schema.  The complete compression schema can
be found [here](https://github.com/tensorflow/tflite-micro/tree/main/tensorflow/lite/micro/compression/metadata.fbs).

For each tensor which is compressed, the following schema element is created:
```
table LutTensor {
    // Look-Up-Table Tensor: a tensor representation where elements are
    // compressed into indices into a table of values. The indices are unsigned
    // integers, index_bitwidth-wide, in big-endian bit order, packed into the
    // buffer identified by the corresponding tflite.Tensor's buffer field. The
    // values are located in a newly-created buffer, encoded according to the
    // tflite.Tensor.type. Tensors with multiple channels have distinct values
    // tables for each channel, concatenated one after another in the buffer.
    // An element's LUT index must be looked up in the value table for its
    // channel.

    tensor:int;            // index of the corresponding tflite.Tensor
    value_buffer:uint;     // index of the buffer containing LUT values
    index_bitwidth:uint8;  // bit-width of LUT indexes
}
```

* `tensor`: the index of the tensor in the current subgraph.  This tensor will
have had its buffer data replaced with a packed bitstring (see below),
representing fixed width indices into the `value table`.
* `value_buffer`: the index of a buffer added to the model.  This buffer contains
the `value table` (see below) for the tensor, which is used to decompress the
tensor.  The elements of the `value table` are of the same type (INT8, INT16, etc.)
as the original (uncompressed) tensor.
* `index_bitwidth`: the fixed width of each bit group (index) that represents an offset
into the `value table`.  For per-channel quantized tensors, the index is an
offset into the `value table` for a specific channel.
