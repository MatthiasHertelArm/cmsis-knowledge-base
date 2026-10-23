---
id: "tflm-porting-reference-ops-from-lite-to-can-i-resize-the-tensors-of-my-model"
type: "concept"
domain: "edge-ai"
title: "Porting Reference Ops from Lite to Micro: Can I resize the tensors of my model?"
summary: "No. The storage space for each input/output/const tensor is a fixed, calculated value determined at the time the TensorFlow Lite (TfLite) model converter is executed."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@f7ed40d:tensorflow/lite/micro/docs/porting_reference_ops.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/f7ed40d/tensorflow/lite/micro/docs/porting_reference_ops.md#can-i-resize-the-tensors-of-my-model"
license: "Apache-2.0"
mode: "V"
---

No.  The storage space for each `input`/`output`/`const` tensor is a fixed,
calculated value determined at the time the TensorFlow Lite (TfLite) model
converter is executed.
All tensor storage is allocated by the `tflite::MicroInterpreter` instance,
using the tensor shape values of the TfLite model converter.

TFLM does not support dynamic tensors.  A dynamic tensor is one whose storage
(and shape) can change during inference.

For more information see: [Memory Allocation Overview](https://github.com/tensorflow/tflite-micro/blob/f7ed40d/tensorflow/lite/micro/docs/online_memory_allocation_overview.md)
