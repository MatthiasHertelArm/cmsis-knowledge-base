---
id: "tflm-pre-allocated-tensors-proposed-implementation"
type: "concept"
domain: "edge-ai"
title: "Pre-allocated tensors: Proposed implementation"
summary: "MicroAllocator initializes all tensors to nullptr, and during the allocation process only allocates the tensors whose data field is nullptr. The application tells the MicroInterpreter which tensor is preallocated, and supplies a memory buffer using the RegisterPreallocatedTensor() function."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@f7ed40d:tensorflow/lite/micro/docs/rfc/001_preallocated_tensors.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/f7ed40d/tensorflow/lite/micro/docs/rfc/001_preallocated_tensors.md#proposed-implementation"
license: "Apache-2.0"
mode: "V"
---

MicroAllocator initializes all tensors to nullptr, and during the allocation
process only allocates the tensors whose data field is nullptr. The application
tells the MicroInterpreter which tensor is preallocated, and supplies a memory
buffer using the RegisterPreallocatedTensor() function.

The MicroInterpreter then assigns the pre-allocated buffer to the tensor
data-field. If the tensor in question is marked as offline planned, as described
in this [RFC](https://docs.google.com/document/d/16aTSHL5wxsq99t6adVbBz1U3K8Y5tBDAvs16iroZDEU),
the MicroInterpreter should not pre-allocated it, and instead return an error.

If multiple tensors are to be pre-allocated, multiple calls to
RegisterPreallocatedTensor() are required. An example can be seen in the MSC
below.

(figure: MSC)
