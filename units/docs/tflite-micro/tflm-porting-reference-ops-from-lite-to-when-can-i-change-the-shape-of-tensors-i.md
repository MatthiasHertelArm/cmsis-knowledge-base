---
id: "tflm-porting-reference-ops-from-lite-to-when-can-i-change-the-shape-of-tensors-i"
type: "concept"
domain: "edge-ai"
title: "Porting Reference Ops from Lite to Micro: When can I change the shape of tensors in my operator code?"
summary: "Tensor shape values can be modified any time after the tflite::micro::CreateWritableTensorDimsWithCopy method has been called. This means that tensor shape values can be modified within the scope of your operator's Prepare or Invoke methods."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@f7ed40d:tensorflow/lite/micro/docs/porting_reference_ops.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/f7ed40d/tensorflow/lite/micro/docs/porting_reference_ops.md#when-can-i-change-the-shape-of-tensors-in-my-operator-code"
license: "Apache-2.0"
mode: "V"
---

Tensor shape values can be modified any time after the
`tflite::micro::CreateWritableTensorDimsWithCopy` method has been called.
This means that tensor shape values can be modified within the scope of
your operator's `Prepare` or `Invoke` methods.
The `tflite::micro::CreateWritableTensorDimsWithCopy` method may
only be called within the scope of your operator's `Prepare` method.
