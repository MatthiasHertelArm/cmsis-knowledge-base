---
id: "tflm-online-memory-allocation-overview-model-init-phase"
type: "concept"
domain: "edge-ai"
title: "Online Memory Allocation Overview in TensorFlow Lite Micro: Model Init Phase"
summary: "Either through the first call to MicroInterpreter::Invoke() or an explicit call to MicroInterpreter::AllocateTensors() the online model allocation will begin. The MicroInterpreter instance will invoke MicroAllocator::StartModelAllocation()."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@f7ed40d:tensorflow/lite/micro/docs/online_memory_allocation_overview.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/f7ed40d/tensorflow/lite/micro/docs/online_memory_allocation_overview.md#model-init-phase"
license: "Apache-2.0"
mode: "V"
---

Either through the first call to `MicroInterpreter::Invoke()` or an explicit
call to `MicroInterpreter::AllocateTensors()` the online model allocation will
begin. The `MicroInterpreter` instance will invoke
`MicroAllocator::StartModelAllocation()`. This function will begin pulling data
out of the serialized flatbuffer and begin walking through the main subgraph.

The method `MicroAllocator::StartModelAllocation()` begins allocation in the
following order: 
* Initializes internal state for scratch buffer allocations 
* Allocates a list of `TfLiteEvalTensor` C structs based on the number of tensors
in the subgraph. 
* Allocations are persistent and stored in the tail section. 
* Tensors that reference buffers in the flatbuffer are assigned at this point. 
* Allocates a list of `TfLiteRegistration` and `TfLiteNode` C structs for every
operator in the model subgraph 
* Allocations are persistent and stored in the
tail section. 
* Walks back through the list of subgraph operators and assigns
all C structs with relevant information from the flatbuffer.

At the conclusion of this phase, the operator kernel implementations are ready
for calls to the `TfLiteRegistration::init()` function. The `MicroInterpreter`
walks through the operator list and invokes all operator implementations that
have this function. Typically, operator implementations return the object to
store in the `user_data` field of a `TfLiteNode` struct.
