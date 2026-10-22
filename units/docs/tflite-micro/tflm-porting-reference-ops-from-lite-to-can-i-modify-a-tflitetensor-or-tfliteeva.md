---
id: "tflm-porting-reference-ops-from-lite-to-can-i-modify-a-tflitetensor-or-tfliteeva"
type: "concept"
domain: "edge-ai"
title: "Porting Reference Ops from Lite to Micro: Can I modify a `TfLiteTensor` or `TfLiteEvalTensor`?"
summary: "No. The tflite::MicroInterpreter is the owner and manipulator of these data structures. Your code should not modify these data structures. The only directly allowed modification of tensors is to change their data values, or their shape values."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@bd621c2:tensorflow/lite/micro/docs/porting_reference_ops.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/bd621c2/tensorflow/lite/micro/docs/porting_reference_ops.md#can-i-modify-a-tflitetensor-or-tfliteevaltensor"
license: "Apache-2.0"
mode: "V"
---

No.  The `tflite::MicroInterpreter` is the owner and manipulator of these data
structures.  Your code should not modify these data structures.  The only
directly allowed modification of tensors is to change their data values, or
their shape values.
