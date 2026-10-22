---
id: "tflm-online-memory-allocation-overview-model-prepare-phase"
type: "concept"
domain: "edge-ai"
title: "Online Memory Allocation Overview in TensorFlow Lite Micro: Model Prepare Phase"
summary: "After the interpreter has initialized all operator kernels, another pass through the subgraph is done. This time, each operator implementation that provides a TfLiteRegistration::prepare() function is called."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@bd621c2:tensorflow/lite/micro/docs/online_memory_allocation_overview.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/bd621c2/tensorflow/lite/micro/docs/online_memory_allocation_overview.md#model-prepare-phase"
license: "Apache-2.0"
mode: "V"
---

After the interpreter has initialized all operator kernels, another pass through
the subgraph is done. This time, each operator implementation that provides a
`TfLiteRegistration::prepare()` function is called. This phase in TFLM is used
for kernels to verify capabilities from model information, validate shapes,
allocate any scratch buffers requested (through
`TfLiteContext::GetScratchBuffer()`), and calculate quantization runtime data.

At this time, operator implementation will request tensor data through the
`TfLiteTensor` C struct. This struct is heavier and contains more information
that operators will need during this phase of initialization. Internally, TFLM
will allocate these instances per request in the temp section. The temp section
is the space between the head and the tail in the arena. During the prepare
phase, nothing has yet been placed in the head section. This extra space between
the head and tail is used to allocate buffers that are available until
`MicroAllocator::ResetTempAllocations()` is called. Additional information
[available here](https://github.com/tensorflow/tflite-micro/blob/bd621c2/tensorflow/lite/micro/docs/memory_management.md#temporary-section).

NOTE: The `TfLiteTensor` struct is only available in TFLM during
`TfLiteRegistration::prepare()`, after this allocation phase tensor data can
only be accessed via a `TfLiteEvalTensor` struct.

Additionally, at this time each operator implementation may request scratch
buffer requests through `TfLiteContext::RequestScratchBufferInArena()`. These
requests are limited to `kMaxScratchBuffersPerOp` and are stored in an instance
variable for each operator prepare block. All requests are eventually moved to
the head section when the interpreter moves to the next operator.

After each call to `TfLiteRegistration::prepare()` the `MicroInterpreter` calls
`MicroAllocator::FinishPrepareNodeAllocations()`. This method resets temp
allocations and begins to store all scratch buffer requests inside the head
section of the arena.

After all operators have been prepared, the `MicroInterpreter` calls
`MicroAllocator::FinishModelAllocation()` to begin finalizing the online memory
plan.
