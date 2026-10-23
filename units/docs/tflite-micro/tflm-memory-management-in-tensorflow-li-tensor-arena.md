---
id: "tflm-memory-management-in-tensorflow-li-tensor-arena"
type: "concept"
domain: "edge-ai"
title: "Memory Management in TensorFlow Lite Micro: Tensor Arena"
summary: "The main \"working\" space for TFLM allocations is inside a single char or int8_t buffer."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@f7ed40d:tensorflow/lite/micro/docs/memory_management.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/f7ed40d/tensorflow/lite/micro/docs/memory_management.md#tensor-arena"
license: "Apache-2.0"
mode: "V"
---

The main "working" space for TFLM allocations is inside a single `char` or
`int8_t` buffer. This buffer can be managed by passing it directly into a
`tflite::MicroInterpreter` constructor or through a `tflite::MicroAllocator`
instance that can be passed into a `tflite::MicroInterpreter` constructor.
Internally, the `tflite::MicroAllocator` classifies allocations into 3 different
sections:

*   **Head** - non-persistent allocations.
*   **Temporary** - short term "scoped" allocations.
*   **Tail** - persistent allocations.

The illustration below represents typical allocations in TFLM:

```
--------------------------------------------------------------------------------
|        |                     |                                               |
|  HEAD  |<--  TEMPORARY    -->|                    TAIL                       |
|        |                     |                                               |
--------------------------------------------------------------------------------
* Lowest Address                                               Highest Address *
```

### Head Section

This non-persistent section typically holds shared Tensor buffers. This section
does not allocate small iterative chunks, it can only be set by a specific
length for the entire section.

This allocation length of this section is managed by the
`tflite::GreedyMemoryPlanner`. That memory planner looks at the entire graph of
a model and tries to reuse as many buffers as possible to create the smallest
length for the head. The Tensor buffers for this section can be accessed via a
`TfLiteEvalTensor` or `TfLiteTensor` instance on the `tflite::MicroInterpreter`.

#### Offline planned tensor allocations

All, or a subset of, tensors can be allocated using an offline planner. An
offline planner performs tensor allocation on e.g. a host PC. The offline tensor
allocation plan is added to model metadata. See format below.

For each non-constant tensor in the `tensors:[Tensor]` list of the subgraph, a
byte offset to the start of the head section of the memory arena is given. -1
indicates that the tensor will be allocated at runtime by the
`tflite::GreedyMemoryPlanner`. The offline plan is permitted to overlap buffers
if it knows that the data will not be used at the same time.

The offline tensor allocation plan will be encoded in the `metadata:[Metadata]`
field of the model, using the following encoding:

| Metadata component | Value |
|-|-|
| name:string | “OfflineMemoryAllocation” |
| buffer:unit | Index of buffer containing offline tensor allocation data |

The buffer contents for the offline tensor allocation is a list of 32-bit
integers of the following format:

| Offset | Value |
|-|-|
| 0 | Offline allocation format version |
| 1 | Number of subgraphs |
| 2 | Number offsets following: n |
| 3 | Byte offset of tensor #0 or -1 to allocate at runtime |
| 4 | Byte offset of tensor #1 or -1 to allocate at runtime |
| ... | ... |
| 3+(n-1) | Byte offset of tensor #(n-1) or -1 to allocate at runtime |

Note that offsets 0 (the version) and 1 (the number of subgraphs) are currently
ignored by the micro memory allocator. In case of multiple subgraphs, it assumes
all tensors for all subgraphs are concatenated: all tensors for the first
subgraph are first, followed by those of the second subgraph, etc.

The `tflite::GreedyMemoryPlanner` treats the provided offline tensor allocation
plan as constant fixed offset to the start of the head section and will attempt
to fit any other tensors (such as scratch tensors added at runtime using the
`RequestScratchBufferInArena` API of `TfLiteContext`) around those fixed
offsets.

### Temporary Section

This section is used to allocate "scoped" or short-term, non-guaranteed buffers.
Allocations from this section start from the current end address of the head
section and grow towards the tail section. An allocation chain can be reset (and
must be reset before adjusting the head) and moves the current allocation start
address back to the end of the head section.

TFLM currently uses these allocations for a scope allocation of large C structs
or scratch memory that is expected to be valid for at least the lifetime of a
method call.

### Tail Section

This section holds all persistent allocations used by TFLM. This section
contains many random sized allocations and grows towards the end of the head
section. Allocations in this section come from a variety of areas inside of
TFLM. TFLM provides a [recording API](#Recording-Memory-APIs) to assist with
auditing the contents of this section.
