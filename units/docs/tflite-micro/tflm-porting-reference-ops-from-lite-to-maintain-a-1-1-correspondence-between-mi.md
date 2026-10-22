---
id: "tflm-porting-reference-ops-from-lite-to-maintain-a-1-1-correspondence-between-mi"
type: "concept"
domain: "edge-ai"
title: "Porting Reference Ops from Lite to Micro: Maintain a 1:1 correspondence between Micro and Lite versions of unit tests"
summary: "To the extent possible, maintain a 1:1 correspondence between Micro and Lite versions of unit tests. Avoid cleanup of merely stylistic issues, e.g., by replacing the hardcoded literal 3.40282e+038 with std::numeric_limits<float>::max()."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@bd621c2:tensorflow/lite/micro/docs/porting_reference_ops.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/bd621c2/tensorflow/lite/micro/docs/porting_reference_ops.md#maintain-a-1-1-correspondence-between-micro-and-lite-versions-of-unit-tests"
license: "Apache-2.0"
mode: "V"
---

To the extent possible, maintain a 1:1 correspondence between Micro and Lite
versions of unit tests. Avoid cleanup of merely stylistic issues, e.g., by
replacing the hardcoded literal `3.40282e+038` with
`std::numeric_limits<float>::max()`. Any changes between the Micro and Lite
versions of a test put a burden on future maintainers to figure out whether the
differences are actually significant or just stylistic.

# Notes

*   There was discussion of commits vs. PRs in [#45387](https://github.com/tensorflow/tensorflow/issues/45387).

*   [TensorFlow Lite 8-bit quantization specification](https://www.tensorflow.org/lite/performance/quantization_spec)

# Frequently Asked Questions
