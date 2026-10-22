---
id: "tflm-tensorflow-lite-for-microcontrolle-implementation-plan"
type: "concept"
domain: "edge-ai"
title: "TensorFlow Lite for Microcontrollers Port of 16x8 Quantized Operators: Implementation plan"
summary: "The work will be broken down into a series of pull requests, some for the benchmarks and some for each kernel."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@bd621c2:tensorflow/lite/micro/docs/rfc/002_16x8_quantization_port.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/bd621c2/tensorflow/lite/micro/docs/rfc/002_16x8_quantization_port.md#implementation-plan"
license: "Apache-2.0"
mode: "V"
---

The work will be broken down into a series of pull requests, some for the benchmarks and some for each kernel.

Benchmark pull requests:
- PR1: Create a new benchmark in [`tensorflow/lite/micro/benchmarks`](https://github.com/tensorflow/tensorflow/tree/975335bc83bf3cb80a71a04ed407725508709808/tensorflow/lite/micro/benchmarks) that attempts to run a 16x8 model that includes the kernels mentioned in this RFC. The model’s weights and biases can be random. The benchmark should use the MicroMutableOpResolver. The PR should include the Colab used to generate the model.
- PR2: Port the person_detection and keyword benchmarks to use the MicroMutableOpResolver.
- PR3: Add code to both benchmarks that prints the arena size using the [`RecordingMemoryAllocator`](https://github.com/tensorflow/tensorflow/blob/ee87d58a6504375c28f21ea303f0eefa29118c38/tensorflow/lite/micro/docs/memory_management.md#recording-memory-apis).

For each kernel:
- PR1: Refactor the implementation to support the new kernel variant registration API.
- PR2: Add 16x8 support and make sure that the benchmark binary and arena sizes are unchanged.

Note that @njeffrie from the TF Lite Micro team also plans to prepare PR(s) for the kernels that are of interest internally
(without using the kernel variant registration API for binary size). This will provide some quick examples of porting the kernels.
