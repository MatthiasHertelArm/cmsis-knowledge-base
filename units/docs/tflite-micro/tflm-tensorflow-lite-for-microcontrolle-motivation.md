---
id: "tflm-tensorflow-lite-for-microcontrolle-motivation"
type: "concept"
domain: "edge-ai"
title: "TensorFlow Lite for Microcontrollers Port of 16x8 Quantized Operators: Motivation"
summary: "Some networks that suffer unacceptable degradation when quantized with 8 bit weights and 8 bit activations perform adequately when quantized with 8 bit weights and 16 bit activations. The TensorFlow Lite documentation states the following:"
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@bd621c2:tensorflow/lite/micro/docs/rfc/002_16x8_quantization_port.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/bd621c2/tensorflow/lite/micro/docs/rfc/002_16x8_quantization_port.md#motivation"
license: "Apache-2.0"
mode: "V"
---

Some networks that suffer unacceptable degradation when quantized with 8 bit weights
and 8 bit activations perform adequately when quantized with 8 bit weights and 16
bit activations. The [TensorFlow Lite documentation](https://www.tensorflow.org/lite/performance/post_training_integer_quant_16x8) states the following:

> [16x8 quantization] mode can improve accuracy of the quantized model significantly, when activations are sensitive to the quantization, while still achieving almost 3-4x reduction in model size. Moreover, this fully quantized model can be consumed by integer-only hardware accelerators.

Edge Impulse, a company that deploys TensorFlow Lite for Microcontrollers as part of its embedded
machine learning pipeline, has gathered feedback from customers with production models for which 8 bit
quantization results in unacceptable degradation but for whom 16x8 is fine.

While 16x8 quantization is well supported within TensorFlow Lite, it is not currently supported
within TensorFlow Lite for Microcontrollers. Porting the TensorFlow Lite reference kernels is
relatively straightforward and will improve adoption of TensorFlow Lite for Microcontrollers with users
for whom degradation is too severe with full 8 bit quantization.
