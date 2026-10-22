---
id: "tfm-floating-point-support-fp-abi-type-for-spe-and-nspe"
type: "concept"
domain: "security"
title: "Floating-Point Support: FP ABI type for SPE and NSPE"
summary: "FP design in Armv8.0-M [9] architecture requires consistent FP ABI types between SPE and NSPE. Furthermore, both sides shall set up CPACR individually when FPU is used."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/tfm_fpu_support.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/tfm_fpu_support.html#fp-abi-type-for-spe-and-nspe"
license: "BSD-3-Clause"
mode: "V"
---

FP design in Armv8.0-M [9]_ architecture requires consistent FP ABI types
between SPE and NSPE. Furthermore, both sides shall set up CPACR individually
when FPU is used. Otherwise, No Coprocessor (NOCP) usage fault will be asserted
during FP context switch between security states.

Secure and non-secure libraries are compiled with `COMPILER_CP_FLAG` and
linked with `LINKER_CP_OPTION` for different FP ABI types. All those
libraries shall be built with `COMPLIER_CP_FLAG`.

If FP ABI types mismatch error is generated during build, please check whether
the library is compiled with `COMPILER_CP_FLAG`.
Example:

```cmake

target_compile_options(lib
    PRIVATE
        ${COMPILER_CP_FLAG}
)

## CMake configurations for FP support

The following CMake configurations configure `COMPILER_CP_FLAG` in TF-M SPE.

* `CONFIG_TFM_ENABLE_FP` is used to enable/disable FPU usage.

  +--------------------------+---------------------------+
  | CONFIG_TFM_ENABLE_FP     | FP support                |
  +==========================+===========================+
  | off (default)            | FP disabled               |
  +--------------------------+---------------------------+
  | on                       | FP enabled                |
  +--------------------------+---------------------------+

`CONFIG_TFM_FLOAT_ABI` depends on `CONFIG_TFM_ENABLE_FP`. If
`CONFIG_TFM_ENABLE_FP is set `CONFIG_TFM_FLOAT_ABI`` is automatically
set to `hard`.
If TF-M SPE is built with `CONFIG_TFM_ENABLE_FP=on`, then SPE takes care of
enabling floating point coprocessors CP10 and CP11 on the NS side. This is
done to avoid NOCP usage fault.
* `CONFIG_TFM_LAZY_STACKING` is used to enable/disable lazy stacking
  feature. This feature is only valid for FP hardware ABI type.
  NSPE is not allowed to enable/disable this feature. Let SPE decide the
  secure/non-secure shared setting of lazy stacking to avoid the possible
  side-path brought by flexibility.

  +------------------------------+---------------------------+
  | CONFIG_TFM_LAZY_STACKING     | Description               |
  +==============================+===========================+
  | 0FF                          | Disable lazy stacking     |
  +------------------------------+---------------------------+
  | ON (default)                 | Enable lazy stacking      |
  +------------------------------+---------------------------+

* `CONFIG_TFM_FP_ARCH` specifies which FP architecture is available on the
  target, valid for FP hardware ABI type.

  FP architecture is processor dependent. For GNUARM compiler, example value
  are: auto, fpv5-d16, fpv5-sp-d16, etc. For armclang, example value are: none,
  softvfp, fpv5-d16, fpv5-sp-d16, etc.

  This parameter shall be specified by platform in preload.cmake. Please check
  compiler reference manual and processor hardware manual for more details to
  set correct FPU configuration for platform.

* `CONFIG_TFM_FP_ARCH_ASM` specifies the target FPU architecture name shared
  by Arm Compiler armasm and armlink. It is only used in the `--fpu=` argument
  by Arm Compiler and shall be aligned with `CONFIG_TFM_FP_ARCH`.

  FP architecture is processor dependent. For armasm and armlink, example value
  are: SoftVFP, FPv5_D16, etc.

  This parameter shall be specified by platform in preload.cmake. Please check
  compiler reference manual and processor hardware manual for more details to
  set correct FPU configuration for platform.


### Reference

.. [1] [High-Performance Hardware Support for Floating-Point Operations](https://www.arm.com/why-arm/technologies/floating-point)

.. [2] [Float Point ABI](https://www.keil.com/support/man/docs/armclang_ref/armclang_ref_chr1417451577871.htm)

.. [3] [GNU Arm Embedded Toolchain](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm)

.. [4] [VLLDM instruction Security Vulnerability](https://developer.arm.com/support/arm-security-updates/vlldm-instruction-security-vulnerability)

.. [5] [Arm® Platform Security Architecture Firmware Framework 1.0](https://developer.arm.com/documentation/den0063/latest/)

.. [6] Secure Interrupt Integration Guide

.. [8] [GCC Issue on '-mcpu=cortex-m55' conflicts with '-march=armv8.1-m.main' Warning](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=97327)

.. [9] [Armv8-M Architecture Reference Manual](https://developer.arm.com/documentation/ddi0553/latest)

.. [10] [Arm Compiler for Embedded](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Embedded)

.. [11] [FF-M v1.1 Extension](https://developer.arm.com/documentation/aes0039/latest/)

--------------

*Copyright (c) 2021-2023, Arm Limited. All rights reserved.*
