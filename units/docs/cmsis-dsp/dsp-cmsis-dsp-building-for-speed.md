---
id: "dsp-cmsis-dsp-building-for-speed"
type: "concept"
domain: "optimization"
title: "CMSIS-DSP: Building for speed"
summary: "CMSIS-DSP is used when you need performance. As consequence CMSIS-DSP should be compiled with the options giving the best performance:"
status: "draft"
collection: "cmsis-dsp"
source: "ARM-software/CMSIS-DSP@83a2d7b:README.md"
doc_source: "https://github.com/ARM-software/CMSIS-DSP/blob/83a2d7b/README.md#building-for-speed"
license: "Apache-2.0"
mode: "V"
---

CMSIS-DSP is used when you need performance. As consequence CMSIS-DSP should be compiled with the options giving the best performance:

### Options to use

* `-O3 -ffast-math` must be used for best performances.
* When using Helium it is strongly advised to use `-O3 -ffast-math`
* `GCC` is currently not giving good performances when targeting Helium. You should use the Arm compiler

When float are used, then the fpu should be selected to ensure that the compiler is not using a software float emulation.

When building with Helium support, it will be automatically detected by CMSIS-DSP. For Neon, it is not the case and you must enable the option `-DARM_MATH_NEON` for the C compilation. With `cmake` this option is controlled with `-DNEON=ON`.

* `-DLOOPUNROLL=ON` can also be used when compiling with cmake
* It corresponds to the C options `-DARM_MATH_LOOPUNROLL`

Compilers are doing unrolling. So this option may not be needed but it is highly dependent on the compiler. With some compilers, this option is needed to get better performances.

Speed of memory is important. If you can map the data and the constant tables used by CMSIS-DSP in `DTCM` memory then it is better. If you have a cache, enable it.

### Options to avoid

* `-fno-builtin`
* `-ffreestanding` because it enables previous options

The library is doing some type [punning](https://en.wikipedia.org/wiki/Type_punning) to process word 32 from memory as a pair of `q15` or a quadruple of `q7`.  Those type manipulations are done through `memcpy` functions. Most compilers should be able to optimize out those function calls when the length to copy is small (4 bytes).

This optimization will **not** occur when `-fno-builtin` is used and it will have a **very bad** impact on the performances.

Some compiler may also require the use of option `-munaligned-access` to specify that unaligned accesses are used.
