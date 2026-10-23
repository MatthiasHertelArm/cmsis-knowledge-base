---
id: "tflm-online-memory-allocation-overview-finish-model-allocation-phase"
type: "concept"
domain: "edge-ai"
title: "Online Memory Allocation Overview in TensorFlow Lite Micro: Finish Model Allocation Phase"
summary: "The last phase of online memory planning is handled in MicroAllocator::FinishModelAllocation(). This function performs the following tasks"
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@f7ed40d:tensorflow/lite/micro/docs/online_memory_allocation_overview.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/f7ed40d/tensorflow/lite/micro/docs/online_memory_allocation_overview.md#finish-model-allocation-phase"
license: "Apache-2.0"
mode: "V"
---

The last phase of online memory planning is handled in
`MicroAllocator::FinishModelAllocation()`. This function performs the following
tasks

*   Allocates space in the tail for all persistent buffer requests that are
    currently in the head.
*   Commits Static Memory Plan
    *   Uses the `GreedyMemoryPlanner` to optimize the non-persistent space in
        the head.
    *   Optimizes for the operator that requires the largest byte-width buffer.
    *   Allocates pointers in the tail that provide pointers into shared space
        and offsets in the head.
    *   Sets the size of the head based on the result of
        `GreedyMemoryPlanner::GetMaximumMemorySize()`.
*   Allocates variable tensor buffers in the tail section.

Once TFLM has finalized online model allocation, all buffers are prepared and
ready for optimal speed for inference. The system no longer enables operator
implementations to allocate scratch buffers after this point.
