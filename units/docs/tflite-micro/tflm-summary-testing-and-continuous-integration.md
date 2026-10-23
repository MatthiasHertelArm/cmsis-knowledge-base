---
id: "tflm-summary-testing-and-continuous-integration"
type: "concept"
domain: "edge-ai"
title: "Summary: Testing and Continuous Integration"
summary: "The kernel tests are the primary method of ensuring that the optimized kernel implementations are accurate."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@f7ed40d:tensorflow/lite/micro/docs/optimized_kernel_implementations.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/f7ed40d/tensorflow/lite/micro/docs/optimized_kernel_implementations.md#testing-and-continuous-integration"
license: "Apache-2.0"
mode: "V"
---

The kernel tests are the primary method of ensuring that the optimized kernel
implementations are accurate.

Currently, most of the tests require the optimizations to be bit-exact to the
quantized reference implementation. We can revisit this requirement if it ends
up having a high associated cost on the latency.

We strongly encourage optimized kernel implementations to have an associated
continuous build that runs through all the unit tests and publishes a build
badge to the
[TFLM community supported platforms](https://github.com/tensorflow/tflite-micro/blob/f7ed40d/tensorflow/lite/micro/docs/../../../../README.md#community--contributing)
table. Running the units tests once a day is often a good place to start.
