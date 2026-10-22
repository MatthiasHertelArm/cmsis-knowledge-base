---
id: "tflm-tensorflow-lite-for-microcontrolle-user-benefit"
type: "concept"
domain: "edge-ai"
title: "TensorFlow Lite for Microcontrollers Port of 16x8 Quantized Operators: User Benefit"
summary: "The headline would be \"16x8 kernels improve accuracy for quantized models on microcontrollers without increasing model size\"."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@bd621c2:tensorflow/lite/micro/docs/rfc/002_16x8_quantization_port.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/bd621c2/tensorflow/lite/micro/docs/rfc/002_16x8_quantization_port.md#user-benefit"
license: "Apache-2.0"
mode: "V"
---

The headline would be "16x8 kernels improve accuracy for quantized models on microcontrollers without
increasing model size".

Users would benefit in the following ways:

- Improved accuracy for quantized models without increasing model size (in exchange for additional
  runtime memory usage)
- Improved performance under certain conditions (for example, 16x8 CMSIS-NN kernels will run faster
  than 8 bit kernels since less unpacking is required)
