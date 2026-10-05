---
id: "tflm-tflm-compression-support-quantized-dimension"
type: "concept"
domain: "edge-ai"
title: "TFLM Compression Support: Quantized Dimension"
summary: "Each per-channel quantized tensor will have as part of its model schema quantization information, a quantized_dimension field. This field specifies which dimension of the tensor shape along which the scale and zero-point are to be applied."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@3f787dc:tensorflow/lite/micro/docs/compression.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/compression.md#quantized-dimension"
license: "Apache-2.0"
mode: "V"
---

Each per-channel quantized tensor will have as part of its model schema quantization
information, a `quantized_dimension` field.  This field specifies which dimension
of the tensor shape along which the scale and zero-point are to be applied. This
dimension within the shape is sometimes referred to as the `quantization axis`.

The importance of the `quantization axis` is in how the
tensor data is interpreted with respect to channel number.
The tensor decompression methods use `LookupTableData.use_alternate_axis` to
determine the correct `value table` channel for each tensor element.  When the
`quantized_dimension` field is 0 (zero) then `use_alternate_axis` is `false`.
If the `quantized_dimension` field is set to 3 (three) (ex. DEPTHWISE_CONV), then
`use_alternate_axis` will be `true`.

For a tensor with shape [4, 2, 2, 1] and `use_alternate_axis` equal to `false`,
the tensor data is assumed to be arranged as follows:
```
element number:  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
channel number:  0  0  0  0  1  1  1  1  2  2  2  2  3  3  3  3
```

For a tensor with shape [1, 2, 2, 4] and `use_alternate_axis` equal to `true`,
the tensor data is assumed to be arranged as follows:
```
element number:  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
channel number:  0  1  2  3  0  1  2  3  0  1  2  3  0  1  2  3
```
