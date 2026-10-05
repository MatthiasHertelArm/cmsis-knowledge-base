---
id: "dsp-cmsis-dsp-code-size"
type: "concept"
domain: "optimization"
title: "CMSIS-DSP: Code size"
summary: "Previous versions of the library were using compilation directives to control the code size. It was too complex and not available in case CMSIS-DSP is only delivered as a static library."
status: "draft"
collection: "cmsis-dsp"
source: "ARM-software/CMSIS-DSP@83a2d7b:README.md"
doc_source: "https://github.com/ARM-software/CMSIS-DSP/blob/83a2d7b/README.md#code-size"
license: "Apache-2.0"
mode: "V"
---

Previous versions of the library were using compilation directives to control the code size. It was too complex and not available in case CMSIS-DSP is only delivered as a static library.

Now, the library relies again on the linker to do the code size optimization. But, this implies some constraints on the code you write and new functions had to be introduced.

If you know the size of your FFT in advance, use initializations functions like `arm_cfft_init_64_f32` instead of using the generic initialization functions `arm_cfft_init_f32`. Using the generic function will prevent the linker from being able to deduce which functions and tables must be kept for the FFT and everything will be included.

There are similar functions for RFFT, MFCC ...

If the flag `ARM_DSP_CONFIG_TABLES` is still set, you'll now get a compilation error to remind you that this flag no more have any effect on code size and that you may have to rework the initializations.
