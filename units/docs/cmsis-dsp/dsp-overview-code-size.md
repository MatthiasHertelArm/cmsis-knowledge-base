---
id: "dsp-overview-code-size"
type: "concept"
domain: "optimization"
title: "Overview: Code size"
summary: "Previous versions were using lots of compilation flags to control code size. It was enabled with ARM_DSP_CONFIG_TABLES. It was getting too complex and has been removed. Now code size optimizations are relying on the linker."
status: "draft"
collection: "cmsis-dsp"
source: "ARM-software/CMSIS-DSP@83a2d7b:Documentation/Doxygen/src/mainpage.md"
doc_source: "https://github.com/ARM-software/CMSIS-DSP/blob/83a2d7b/Documentation/Doxygen/src/mainpage.md#code-size"
license: "Apache-2.0"
mode: "V"
---

Previous versions were using lots of compilation flags to control code size. It was enabled with `ARM_DSP_CONFIG_TABLES`. It was getting too complex and has been removed. Now code size optimizations are relying on the linker.

You no more need to use any compilation flags like `ARM_TABLE_TWIDDLECOEF_F32_2048`, `ARM_FFT_ALLOW_TABLES` etc ...

They have been removed.

Constant tables can use a lot of read only memory but the linker can remove the unused functions and constant tables if it can deduce that those tables or functions are not used.

For this you need to use the right initialization functions in the library and the right options for the linker (they are compiler dependent).

For all transforms functions (CFFT, RFFT ...) instead of using a generic initialization function that works for all lengths (like `arm_cfft_init_f32`), use a dedicated initialization function for a specific size (like `arm_cfft_init_1024_f32`).

By using the right initialization function, you're telling the linker what is really used.

If you use a generic function, the linker cannot deduce the used lengths and thus will keep all the constant tables required for each length.

Then you need to use the right options for the compiler so that the unused tables and functions are removed. It is compiler dependent but generally the options are named like `-ffunction-sections`, `-fdata-sections`, `--gc-sections` ...
