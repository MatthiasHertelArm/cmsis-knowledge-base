---
id: "tflm-online-memory-allocation-overview-arena"
type: "concept"
domain: "edge-ai"
title: "Online Memory Allocation Overview in TensorFlow Lite Micro: Arena"
summary: "Online memory planning strategically places allocations in a single uint8_t buffer array. The buffer is split into two main sections: the “head” and the “tail”."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@bd621c2:tensorflow/lite/micro/docs/online_memory_allocation_overview.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/bd621c2/tensorflow/lite/micro/docs/online_memory_allocation_overview.md#arena"
license: "Apache-2.0"
mode: "V"
---

Online memory planning strategically places allocations in a single `uint8_t`
buffer array. The buffer is split into two main sections: the “head” and the
“tail”. Generally, non-persistent allocations are placed in the “head” and
persistent allocations are placed in the “tail”. More details about the arena
can be [found here](https://github.com/tensorflow/tflite-micro/blob/bd621c2/tensorflow/lite/micro/docs/memory_management.md#tensor-arena).
