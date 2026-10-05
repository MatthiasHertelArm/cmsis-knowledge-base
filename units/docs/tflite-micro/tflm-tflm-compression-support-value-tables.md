---
id: "tflm-tflm-compression-support-value-tables"
type: "concept"
domain: "edge-ai"
title: "TFLM Compression Support: Value Tables"
summary: "A value table contains the unique data values from an original (uncompressed) tensor. For each compressed tensor, an additional buffer is added to the model, and the value table resides as a contiguous sequence of data values within that buffer."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@3f787dc:tensorflow/lite/micro/docs/compression.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/compression.md#value-tables"
license: "Apache-2.0"
mode: "V"
---

A `value table` contains the unique data values from an original (uncompressed)
tensor.  For each compressed tensor, an additional buffer is added to the model,
and the `value table` resides as a contiguous sequence of data values within
that buffer.  Each element in the `value table` is unique, and is of the same type
(INT16, FLOAT32, etc.) as the uncompressed tensor.  The order of values within
the `value table` does not have to match the order in which they appeared in
the uncompressed tensor data.

Example (tensor type is INT16, value table size is 12 bytes):
```
tensor data: [2, 4, 4, 10, 1, 7, 99, 10, 2, 4]
value table: [99, 2, 10, 4, 1, 7]
```
A suitable tensor bitstring (bit width 3) for the example would be:
```
bitstring: 00101101101010010100001000101100
             |  |  |  |  |  |  |  |  |  | |
index:       1  3  3  2  4  5  0  2  1  3 padding
value:       2  4  4 10  1  7 99 10  2  4
```

### Per-channel Quantized Tensor Value Tables

For per-channel quantized tensors, a `value table` is present for each channel.
All of the `value tables` are concatenated together into a single contiguous
set of values. The number of elements in each `value table` is always identical,
with zero value padding added to the end of a `value table` as necessary.

Using the previous example tensor (above) with 2 channels:
```
tensor data: [2, 4, 4, 10, 1, 7, 99, 10, 2, 4]
channel:      |______0_____|  |______1______|
              |            |  |             |
value table: [1, 10, 2, 4, 0, 99, 10, 2, 7, 4]
                           |
                           |__padding
```
A suitable tensor bitstring (bit width 3) for the example would be:
```
bitstring: 01001101100100001100000101010000
             |  |  |  |  |  |  |  |  |  | |
index:       2  3  3  1  0  3  0  1  2  4 padding
value:       2  4  4 10  1  7 99 10  2  4
channel:     0  0  0  0  0  1  1  1  1  1
```

Note that in the above example, compressed tensor indices are specific to a `value table` channel.

Also note that channel 0 (zero) in the `value table` is padded with a single
zero value at the end.

# The MicroInterpreter and Tensor Decompression

The model schema `Metadata` is first searched for the `COMPRESSION_METADATA` key.
If found, the associated buffer is decoded using the [compression schema](https://github.com/tensorflow/tflite-micro/tree/main/tensorflow/lite/micro/compression/metadata.fbs).  For each `LutTensor` in the compression schema,
a `LookupTableData` ([compression.h](https://github.com/tensorflow/tflite-micro/blob/main/tensorflow/lite/micro/compression.h))
structure is instantiated.

```cpp
struct LookupTableData {
  static constexpr size_t kMaxBitWidth = 7;
  static constexpr size_t kMaxValueTableChannelStride = 128;

  const void* value_table;             // Pointer into FlatBuffer Values.
  uint8_t value_table_channel_stride;  // elements per channel
  uint8_t compressed_bit_width : 3;    // 1 to 7 bits
  bool is_per_channel_quantized : 1;   // tensor is per-channel quantized
  bool use_alternate_axis : 1;         // shape default channel:
                                       // 0 = first, 1 = last
  uint8_t reserved : 3;
};
```

* `value_table`: Pointer to the buffer memory containing the `value table`.
Determined from the `LutTensor.value_buffer` and converted to a model schema
buffer vector.
* `value_table_channel_stride`: The number of elements (not bytes) between
`value table` channels.  Only valid for per-channel quantized tensors.
* `compressed_bit_width`: Number of bits for each `value table` index.
Determined from `LutTensor.index_bitwidth`.
* `is_per_channel_quantized`: Will be `true` for per-channel quantized
tensors.  Determined by inspecting the tensor quantization scale vector size in
the model schema.
If the vector size is greater than 1 (one) then the tensor is assumed to be
per-channel quantized.
Default value is `false`.
* `use_alternate_axis`: Arrangement of tensor data vs. channel number.
See the quantized dimension section below for additional explanation.
Only valid for per-channel quantized tensors.  Default value is `false`.
