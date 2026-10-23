---
id: "mlek-troubleshooting-internal-compiler-error"
type: "concept"
domain: "edge-ai"
title: "Troubleshooting: Internal Compiler Error"
summary: "There is a known issue with the Arm GNU toolchain version 12.2 (release December 22, 2022). Compiler from this toolchain throws up this error:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/troubleshooting.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/troubleshooting.md#internal-compiler-error"
license: "Apache-2.0"
mode: "V"
---

There is a known issue with the Arm GNU toolchain version 12.2 (release December 22, 2022).
Compiler from this toolchain throws up this error:

```
during RTL pass: combine
/home/user/ml-embedded-evaluation-kit/dependencies/cmsis-nn/Source/SoftmaxFunctions/arm_softmax_s8.c: In function 'arm_exp_on_negative_values_mve_32x4':
/home/user/ml-embedded-evaluation-kit/dependencies/cmsis-nn/Source/SoftmaxFunctions/arm_softmax_s8.c:74:1: internal compiler error: in trunc_int_for_mode, at explow.cc:59
   74 | }
      | ^
0x7f0343d9b082 __libc_start_main
	../csu/libc-start.c:308
Please submit a full bug report, with preprocessed source (by using -freport-bug).
Please include the complete backtrace with any bug report.
See <https://bugs.linaro.org/> for instructions.
```

It has been worked around by a CMSIS-NN patch from Dec 23, 2023. Make sure you are on a later commit of CMSIS-NN.

See
- [GCC patches: PR107987](https://gcc.gnu.org/pipermail/gcc-patches/2022-December/607963.html)
- [CMSIS-NN issue 13](https://github.com/ARM-software/CMSIS-NN/issues/13)
- [Workaround for GNU Toolchain 12.x bug ](https://github.com/ARM-software/CMSIS-NN/commit/245089501eef18e8b638865c5afd6cdf2d03386f)
