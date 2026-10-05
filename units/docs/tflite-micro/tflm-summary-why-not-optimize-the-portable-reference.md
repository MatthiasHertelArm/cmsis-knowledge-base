---
id: "tflm-summary-why-not-optimize-the-portable-reference"
type: "concept"
domain: "edge-ai"
title: "Summary: Why Not Optimize the Portable Reference Kernels?"
summary: "We would like to explicitly point out (as have others) that the reference kernel implementations are not performant and there are plenty of opportunities to speed them up."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@3f787dc:tensorflow/lite/micro/docs/optimized_kernel_implementations.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/optimized_kernel_implementations.md#why-not-optimize-the-portable-reference-kernels"
license: "Apache-2.0"
mode: "V"
---

We would like to explicitly point out (as have others) that the reference kernel
implementations are not performant and there are plenty of opportunities to
speed them up. This is by design and the reference kernels are meant to be a
shared starting point to then be optimized in a target specific optimized kernel
implementation.

Two previous discussions on this topic are on
[PR #42477](https://github.com/tensorflow/tensorflow/pull/42477) and
[PR #45227](https://github.com/tensorflow/tensorflow/pull/45227)

Our current point of view on this topic is that while optimizing shared
reference code in a portable manner is attractive, we are making an explicit
choice to not go down that path and instead rely on target-specific optimized
implementations. The TFLM codebase has a growing list of optimized kernel
implementations, and we are investing in making the process of adding new
implementations smoother.

# Software Architecture

The optimized kernel architecture is composed of the following three modules:

1.  Hardware-specific NN library
1.  Optimized Kernels
1.  Build System Integration
