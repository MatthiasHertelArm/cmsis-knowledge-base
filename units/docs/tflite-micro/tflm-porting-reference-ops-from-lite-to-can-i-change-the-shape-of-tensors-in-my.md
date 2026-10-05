---
id: "tflm-porting-reference-ops-from-lite-to-can-i-change-the-shape-of-tensors-in-my"
type: "concept"
domain: "edge-ai"
title: "Porting Reference Ops from Lite to Micro: Can I change the shape of tensors in my operator code?"
summary: "Yes. The new shape must be exactly equal to the storage space indicated by the old shape. Because tensor shape values may live in non-volatile memory that is not directly writable (ex."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@3f787dc:tensorflow/lite/micro/docs/porting_reference_ops.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/porting_reference_ops.md#can-i-change-the-shape-of-tensors-in-my-operator-code"
license: "Apache-2.0"
mode: "V"
---

Yes.  The new shape must be exactly equal to the storage space indicated by the
old shape.
Because tensor shape values may live in non-volatile memory that is not directly 
writable (ex. Flash, ROM), a special method must be called before modification
is attempted.  The `tflite::micro::CreateWritableTensorDimsWithCopy` method will
move the tensor shape values to guaranteed persistent writable memory.

An example code snippet looks like ([l2_pool_2d.cc](https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/../kernels/l2_pool_2d.cc)):
```C++
// the output variable is a TfLiteTensor*
TfLiteEvalTensor* output_eval =
      tflite::micro::GetEvalOutput(context, node, kOutputTensor);
TF_LITE_ENSURE_OK(context, tflite::micro::CreateWritableTensorDimsWithCopy(
                               context, output, output_eval));
output->dims->data[kBatchRank] = batches;
output->dims->data[kHeightRank] = out_height;
output->dims->data[kWidthRank] = out_width;
output->dims->data[kChannelRank] = channels_out;
```
