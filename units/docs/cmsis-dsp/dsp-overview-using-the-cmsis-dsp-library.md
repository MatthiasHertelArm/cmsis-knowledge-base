---
id: "dsp-overview-using-the-cmsis-dsp-library"
type: "concept"
domain: "optimization"
title: "Overview: Using the CMSIS-DSP Library"
summary: "The library is released in source form. It is strongly advised to compile the library using -Ofast optimization to have the best performances."
status: "draft"
collection: "cmsis-dsp"
source: "ARM-software/CMSIS-DSP@83a2d7b:Documentation/Doxygen/src/mainpage.md"
doc_source: "https://github.com/ARM-software/CMSIS-DSP/blob/83a2d7b/Documentation/Doxygen/src/mainpage.md#using-the-cmsis-dsp-library"
license: "Apache-2.0"
mode: "V"
---

The library is released in source form. It is strongly advised to compile the library using `-Ofast` optimization to have the best performances.

Following options should be avoided:

* `-fno-builtin`
* `-ffreestanding` because it enables previous options

The library is doing some type [punning](https://en.wikipedia.org/wiki/Type_punning) to process word 32 from memory as a pair of `q15` or a quadruple of `q7`.  Those type manipulations are done through `memcpy` functions. Most compilers should be able to optimize out those function calls when the length to copy is small (4 bytes).

This optimization will **not** occur when `-fno-builtin` is used and it will have a **very bad** impact on the performances.


The library functions are declared in the public file `Include/arm_math.h`. Simply include this file to use the CMSIS-DSP library. If you don't want to include everything, you can also rely on individual header files from the `Include/dsp/` folder and include only those that are needed in the project.
