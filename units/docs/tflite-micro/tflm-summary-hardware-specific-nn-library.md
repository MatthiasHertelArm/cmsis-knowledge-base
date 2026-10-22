---
id: "tflm-summary-hardware-specific-nn-library"
type: "concept"
domain: "edge-ai"
title: "Summary: Hardware-specific NN library"
summary: "This library uses knowledge of the hardware and compiler to implement the underlying operations. Examples of this are CMSIS-NN from Arm and NNLib from Cadence."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@bd621c2:tensorflow/lite/micro/docs/optimized_kernel_implementations.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/bd621c2/tensorflow/lite/micro/docs/optimized_kernel_implementations.md#hardware-specific-nn-library"
license: "Apache-2.0"
mode: "V"
---

This library uses knowledge of the hardware and compiler to implement the
underlying operations. Examples of this are
[CMSIS-NN](https://github.com/ARM-software/CMSIS-NN) from Arm and
[NNLib](https://github.com/foss-xtensa/nnlib-hifi4) from Cadence.

The benefits of having this API separation are:

1.  The NN library does not need to follow the style guide of the rest of the
    TFLM code.
1.  Releases of the NN library can be made independent of TFLM
1.  The same NN library can be used and tested independent of TFLM.
1.  The maintainers of the NN library have full control over the development
    process that they would like to follow.
