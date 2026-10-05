---
id: "nn-cmsis-nn-software-library-introduction"
type: "concept"
domain: "optimization"
title: "CMSIS NN Software Library: Introduction"
summary: "This user manual describes the CMSIS NN software library, a collection of efficient neural network kernels developed to maximize the performance and minimize the memory footprint of neural networks on Arm Cortex-M processors."
status: "draft"
collection: "cmsis-nn"
source: "ARM-software/CMSIS-NN@71cbe3d:Documentation/Doxygen/src/mainpage.md"
doc_source: "https://github.com/ARM-software/CMSIS-NN/blob/71cbe3d/Documentation/Doxygen/src/mainpage.md#introduction"
license: "Apache-2.0"
mode: "V"
---

This user manual describes the CMSIS NN software library, a collection of efficient neural network kernels developed to maximize the performance and minimize the memory footprint of neural networks on Arm Cortex-M processors.

### Experimental Floating-Point Extension

CMSIS-NN also includes an experimental floating-point extension covering `float32`
and `float16` APIs.

The floating-point API surface is disabled by default and should only be enabled
for builds that explicitly require it. This keeps the default code size and API
surface aligned with the established integer CMSIS-NN usage model.

The floating-point API style intentionally follows the existing integer CMSIS-NN
conventions, including the TensorFlow Lite Micro influenced parameter structure,
even though `float16` is not part of the TensorFlow Lite Micro API contract.

These floating-point kernels are primarily intended for Cortex-M processors with
Helium (MVE) and hardware floating-point support. Scalar reference paths exist
for validation and fallback, but they are not the primary deployment target.
Floating-point inference should be reserved for specific use cases where integer
quantization is not possible or not acceptable, and for neural networks with
modest size and runtime requirements.

The floating-point code can also be compiled for Arm A-class processors with
`float16` support and may benefit from NEON or SVE auto-vectorization.
However, this is not an intended deployment target for CMSIS-NN float support,
and the resulting performance is expected to be suboptimal compared to libraries
designed for that class of processor. For Arm A-class CPUs, prefer optimized
inference libraries such as Arm Compute Library or XNNPACK.

The library is divided into a number of functions each covering a specific category:

 - NNConv
 - Acti
 - FC
 - SVDF
 - Pooling
 - Softmax
 - groupElementwise
 - LSTM

The figure below illustrates the CMSIS-NN block diagram.

(figure: CMSIS-NN Block Diagram)
