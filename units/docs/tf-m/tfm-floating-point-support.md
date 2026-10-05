---
id: "tfm-floating-point-support"
type: "concept"
domain: "security"
title: "Floating-Point Support"
summary: "TF-M adds several configuration flags to control Floating point (FP) [1] support in TF-M Secure Processing Environment (SPE) and Non Secure Processing Environment (NSPE)."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/tfm_fpu_support.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/tfm_fpu_support.html"
license: "BSD-3-Clause"
mode: "V"
---

TF-M adds several configuration flags to control Floating point (FP) [1]_
support in TF-M Secure Processing Environment (SPE) and Non Secure Processing
Environment (NSPE).

* Support FP in SPE or NSPE.
* Support FP Application Binary Interface (ABI) [2]_ types: software, hardware.
  SPE and NSPE shall use the same FP ABI type.
* Support lazy stacking enable/disable in SPE only, NSPE is not allowed to
  enable/disable this feature.
* Support GNU Arm Embedded Toolchain [3]_. ``GNU Arm Embedded Toolchain 10.3-
  2021.10`` and later version shall be used to mitigate VLLDM instruction
  security vulnerability [4]_.
* Support both IPC [5]_ and SFN [11]_ models in TF-M.
* Support Armv8-M mainline.
* Support isolation level 1,2,3.
* Support Arm Compiler for Embedded [10]_. `Arm Compiler for Embedded 6.17`
  and later version shall be used to mitigate VLLDM instruction security
  vulnerability [4]_.
* Does not support use FPU in First-Level Interrupt Handling (FLIH) [6]_ at
  current stage.

Please refer to Arm AN521 or AN552 platform as a reference implementation when
you enable FP support on your platforms.

Alternatively, if you intend to use FP in your own NSPE application but the
TF-M SPE services that you enable do not require FP, you can set the CMake
configuration `CONFIG_TFM_ENABLE_CP10CP11` to `ON` and **ignore** any
configurations described below.
CONFIG_TFM_DISABLE_CP10CP11 can be set to ON to disable CP10/CP11 coprocessors
in cases when it's expected that FPU must not be used neither by secure
nor by non-secure images.
`GNU Arm Embedded Toolchain 10.3-2021.10` may have issue that reports
`'-mcpu=cortex-m55' conflicts with '-march=armv8.1-m.main'` warning [8]_.
This issue has been fixed in the later version.
