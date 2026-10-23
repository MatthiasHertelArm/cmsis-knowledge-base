---
id: "nn-cmsis-nn-software-library-pre-processor-macros"
type: "concept"
domain: "optimization"
title: "CMSIS NN Software Library: Pre-processor Macros"
summary: "The macros below are defined in a build system based on feature flags for a chosen processor or architecture input to a compiler. These tie in to the classification in Macros."
status: "draft"
collection: "cmsis-nn"
source: "ARM-software/CMSIS-NN@18bb0fd:Documentation/Doxygen/src/mainpage.md"
doc_source: "https://github.com/ARM-software/CMSIS-NN/blob/18bb0fd/Documentation/Doxygen/src/mainpage.md#pre-processor-macros"
license: "Apache-2.0"
mode: "V"
---

**Feature flag based macros**

The macros below are defined in a build system based on feature flags for a chosen processor or architecture input to a compiler. These tie in to the classification in Macros.

For a CMSIS-NN file compiled as `armclang -mcpu=cortex-m4 --target=arm-arm-none-eabi -I<CMSIS Core Include> -Ofast -O file.c` , the macro `ARM_MATH_DSP` is enabled as Cortex-M4 has the DSP extension as a feature.

 - `ARM_MATH_DSP`
   - Selects code for processors with DSP extension.

 - `ARM_MATH_MVEI`
   - Selects code for processors which supports MVE instructions.

 - `ARM_MATH_MVEF`
   - Selects code for processors which support MVE with floating-point instructions.

 - `ARM_MATH_MVE_FLOAT16`
   - Selects code for processors which support MVE with float16 instructions.

**User set macros**

 - `ARM_MATH_AUTOVECTORIZE`
   - Applicable when ARM_MATH_MVEI is active to let the compiler auto vectorize functions, if available, that uses inline assembly. This has to be explicitly set at compile time.

 - `ARM_NN_ENABLE_F32`
   - Enables the experimental `float32` API and implementation set.

 - `ARM_NN_ENABLE_F16`
   - Enables the experimental `float16` API and implementation set.

 - `NN_DISABLE_SPECIALIZATION`
   - Disables optional shape/layout-specific fast paths and forces the corresponding generic implementation path.
   - Useful when validating specialized kernels against the generic reference-style path.

 - `ARM_NN_USE_EXP_LUT`
   - Selects the LUT-based scalar float softmax exp approximation. This is the default if no softmax exp macro is defined.
   - Adds one 257-entry lookup table per enabled float precision:
     - float16: 257 half-words, about 514 bytes
     - float32: 257 words, about 1028 bytes

 - `ARM_NN_USE_EXP_TAYLOR`
   - Selects the Taylor/Estrin scalar float softmax exp approximation to avoid the extra lookup-table storage.
   - `ARM_NN_USE_EXP_LUT` and `ARM_NN_USE_EXP_TAYLOR` are mutually exclusive.
