---
id: "tflm-online-memory-allocation-overview-existing-buffers-in-the-flatbuffer"
type: "concept"
domain: "edge-ai"
title: "Online Memory Allocation Overview in TensorFlow Lite Micro: Existing buffers in the flatbuffer"
summary: "The TFLite flatbuffer model contains a variety of information required to run a model in TFLite or TFLM."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@3f787dc:tensorflow/lite/micro/docs/online_memory_allocation_overview.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/online_memory_allocation_overview.md#existing-buffers-in-the-flatbuffer"
license: "Apache-2.0"
mode: "V"
---

The TFLite flatbuffer model contains a variety of information required to run a
model in TFLite or TFLM. The TFLM online memory planner will walk the main
subgraph and find all tensors required for the model (represented as
`TfLiteTensor` and `TfLiteEvalTensor` C structs at runtime). Persistent tensors
in the flatbuffer (e.g. weight tensors) will point at a buffer inlined in the
flatbuffer. These buffers are reused during online memory planning. The
corresponding C structures will point back at the buffer packed into the
flatbuffer.
