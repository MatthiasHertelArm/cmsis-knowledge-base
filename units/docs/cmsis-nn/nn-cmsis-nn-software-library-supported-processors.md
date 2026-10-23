---
id: "nn-cmsis-nn-software-library-supported-processors"
type: "concept"
domain: "optimization"
title: "CMSIS NN Software Library: Supported Processors"
summary: "CMSIS-NN targets Cortex-M processors with typically three different implementations for each function. Each implementation targets a different group of processors:"
status: "draft"
collection: "cmsis-nn"
source: "ARM-software/CMSIS-NN@18bb0fd:Documentation/Doxygen/src/mainpage.md"
doc_source: "https://github.com/ARM-software/CMSIS-NN/blob/18bb0fd/Documentation/Doxygen/src/mainpage.md#supported-processors"
license: "Apache-2.0"
mode: "V"
---

CMSIS-NN targets Cortex-M processors with typically three different implementations for each function. Each implementation targets a different group of processors:

 - Processors without Single Instruction Multiple Data(SIMD) capability (e.g, Cortex-M0)
 - Processors with DSP extension (e.g Cortex-M4)
 - Processors with Arm M-Profile Vector Extension(MVE) instructions (e.g Cortex-M55)

The correct implementation is picked through feature flags and the user does not have to explicit set it.

Notes for floating-point kernels:

 - Floating-point support is mainly intended for processors with Helium and
   floating-point hardware support.
 - `float16` support is mainly intended for processors with native float16
   arithmetic support.
 - Scalar floating-point implementations are available for reference and
   fallback, but they are not the main optimization target.
 - Arm A-class CPUs with `float16`, NEON, or SVE can compile generic kernels (non-Helium variants), but
   this is not the intended deployment target. Prefer Arm Compute Library or
   XNNPACK for better performance on those processors.
