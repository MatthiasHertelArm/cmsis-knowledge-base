---
id: "tflm-porting-reference-ops-from-lite-to-how-do-i-allocate-persistent-memory"
type: "concept"
domain: "edge-ai"
title: "Porting Reference Ops from Lite to Micro: How do I allocate persistent memory?"
summary: "Use TfLiteContext::AllocatePersistentBuffer to allocate persistent memory. Memory allocated by this method will remain valid throughout the lifetime of the tflite::MicroInterpreter instance."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@bd621c2:tensorflow/lite/micro/docs/porting_reference_ops.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/bd621c2/tensorflow/lite/micro/docs/porting_reference_ops.md#how-do-i-allocate-persistent-memory"
license: "Apache-2.0"
mode: "V"
---

Use `TfLiteContext::AllocatePersistentBuffer` to allocate persistent memory.
Memory allocated by this method will remain valid throughout the lifetime of
the `tflite::MicroInterpreter` instance.

An example code snippet looks like ([leaky_relu.cc](https://github.com/tensorflow/tflite-micro/blob/bd621c2/tensorflow/lite/micro/docs/../kernels/leaky_relu.cc)):
```C++
void* LeakyReluInit(TfLiteContext* context, const char* buffer, size_t length) {
  return context->AllocatePersistentBuffer(context, sizeof(LeakyReluOpData));
}
```
