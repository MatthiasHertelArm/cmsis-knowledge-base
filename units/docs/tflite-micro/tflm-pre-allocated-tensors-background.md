---
id: "tflm-pre-allocated-tensors-background"
type: "concept"
domain: "edge-ai"
title: "Pre-allocated tensors: Background"
summary: "Tensors are allocated differently depending on the type of tensor. Weight tensors are located in the flatbuffer, which is allocated by the application that calls TensorFlow Lite Micro."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@3f787dc:tensorflow/lite/micro/docs/rfc/001_preallocated_tensors.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/rfc/001_preallocated_tensors.md#background"
license: "Apache-2.0"
mode: "V"
---

Tensors are allocated differently depending on the type of tensor. Weight
tensors are located in the flatbuffer, which is allocated by the application
that calls TensorFlow Lite Micro. EvalTensors are allocated in the tensor arena,
either offline planned as specified in the flatbuffers metadata (described in
this
[RFC](https://docs.google.com/document/d/16aTSHL5wxsq99t6adVbBz1U3K8Y5tBDAvs16iroZDEU)),
or allocated during runtime by the
[memory planner](https://github.com/tensorflow/tflite-micro/tree/main/tensorflow/lite/micro/memory_planner)
(online planned), see
[RFC](https://docs.google.com/document/d/1akpqu0uiPQshmCrnV6dOEFgYM4tCCnI8Zce85PnjHMI).
The tensor arena is allocated by MicroAllocator in TensorFlow Lite Micro, and
the model buffer (represented by a .tflite-file) is allocated by the application
using TensorFlow Lite Micro. An illustration of this can be seen in the image
below.

(figure: Image of two blocks)

Is some use cases it could be advantageous to place some of the EvalTensors
outside of the tensor arena, for example: * When sensor output data is stored in
its own defined buffer, outside the tensor arena, and therefore needs to be
copied into the tensor arena before inference. * When the tensor is to be
consumed from a memory location outside the tensor arena, e.g. a separate memory
bank DSP. \
Details regarding the impact on the number of clock cycles and memory
consumption can be found under “Performance overview”. In this RFC we present an
option to allow an application to provide pre-allocated buffers to TensorFlow
Lite Micro for selected tensors. An illustration of the resulting memory layout
with pre-allocated tensors can be seen in the figure below.

(figure: Image of three blocks)
