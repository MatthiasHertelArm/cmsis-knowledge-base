---
id: "tflm-summary-optimized-kernels"
type: "concept"
domain: "edge-ai"
title: "Summary: Optimized Kernels"
summary: "These will be (hopefully thin) wrappers that act as the glue between TFLM and the NN library."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@bd621c2:tensorflow/lite/micro/docs/optimized_kernel_implementations.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/bd621c2/tensorflow/lite/micro/docs/optimized_kernel_implementations.md#optimized-kernels"
license: "Apache-2.0"
mode: "V"
---

These will be (hopefully thin) wrappers that act as the glue between TFLM and
the NN library.

The goal here is to delegate as much work as possible to the NN library while
still allowing the two APIs (TFLM and NN library) to be independent of each
other. If there is a performance degradation due to this (for example,
unnecessary memory copies) then we can evaluate those on a case-by-case basis.

This code will be reviewed and merged in the TFLM github repository and must
follow the development style of the TFLM codebase.

Some amount of refactoring of the existing code may be needed to ensure that
code is suitably shared between the reference and optimized kernels. There is
currently no fixed recipe for this refactor and we will evaluate on a
case-by-case basis during the PR review.

For example, to add an optimized implementation for `fully_connected` for the
Xtensa Fusion F1 the steps were: 
* [PR 1](https://github.com/tensorflow/tensorflow/pull/45464): refactor for
reference fallbacks and a baseline latency. 
* [PR 2](https://github.com/tensorflow/tensorflow/pull/46242): refactor to share
code between reference and optimized kernels. 
* [PR 3](https://github.com/tensorflow/tensorflow/pull/46411): add the code needed
to use the optimized NN lib and document the latency improvement.
