---
id: "tflm-tensorflow-lite-for-microcontrolle-objective"
type: "concept"
domain: "edge-ai"
title: "TensorFlow Lite for Microcontrollers Port of 16x8 Quantized Operators: Objective"
summary: "TensorFlow Lite has kernel implementations that support 8 bit quantized weights but use 16 bit activations. We wish to port these implementations to TensorFlow Lite for Microcontrollers. The increased precision available for activations can improve performance for some quantized models."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@f7ed40d:tensorflow/lite/micro/docs/rfc/002_16x8_quantization_port.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/f7ed40d/tensorflow/lite/micro/docs/rfc/002_16x8_quantization_port.md#objective"
license: "Apache-2.0"
mode: "V"
---

TensorFlow Lite has kernel implementations that support 8 bit quantized weights
but use 16 bit activations. We wish to port these implementations to TensorFlow
Lite for Microcontrollers. The increased precision available for activations can
improve performance for some quantized models.

Arm have agreed to support the initiative by adding the necessary 16x8 APIs to
CMSIS-NN and porting the CMSIS-NN kernels.

### Goals
- Port a subset of 16x8 reference kernels from TensorFlow Lite to TensorFlow Lite Micro
- Avoid increasing default code size or arena size of TensorFlow Lite Micro
- Lay the groundwork for creating a CMSIS-NN port of the 16x8 kernels

### Non-goals
- Port every single operator to 16x8; we only plan to port a subset of those with existing reference implementations
