---
id: "tflm-tflite-for-microcontrollers-benchm-keyword-benchmark"
type: "concept"
domain: "edge-ai"
title: "TFLite for Microcontrollers Benchmarks: Keyword benchmark"
summary: "The keyword benchmark contains a model for keyword detection with scrambled weights and biases. This model is meant to test performance on a platform only. Since the weights are scrambled, the output is meaningless."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@bd621c2:tensorflow/lite/micro/benchmarks/README.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/bd621c2/tensorflow/lite/micro/benchmarks/README.md#keyword-benchmark"
license: "Apache-2.0"
mode: "V"
---

The keyword benchmark contains a model for keyword detection with scrambled
weights and biases.  This model is meant to test performance on a platform only.
Since the weights are scrambled, the output is meaningless. In order to validate
the accuracy of optimized kernels, please run the kernel tests.
