---
id: "rtx-system-requirements-supported-toolchains"
type: "concept"
domain: "rtos"
title: "System Requirements: Supported Toolchains"
summary: "\\if FuSaRTS FuSa RTX5 RTOS is validated using the compiler version referenced in Tested and Verified Toolchains section for the Arm FuSa Run-time System. \\endif"
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/system_reqs.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/system_reqs.md#supported-toolchains"
license: "Apache-2.0"
mode: "V"
---

\if FuSaRTS
FuSa RTX5 RTOS is validated using the compiler version referenced in **Tested and Verified Toolchains** section for the Arm FuSa Run-time System.
\endif

\ifnot FuSaRTS

Keil RTX5 is developed and tested using the common toolchains and development environments.

Current development is verified to work with the following toolchains versions:

- Arm Compiler 6.20
- IAR Embedded Workbench 9.40.2
- GNU Arm Embedded Toolchain 12.3.1
- CLANG (LLVM): 17.0.1

But in most cases, RTX would work well with other versions of these toolchains as well.

\endif
