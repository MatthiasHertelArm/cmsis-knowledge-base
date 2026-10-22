---
id: "core-intrinsic-functions-for-cpu-instru"
type: "concept"
domain: "core"
title: "Intrinsic Functions for CPU Instructions"
summary: "Functions that generate specific Cortex-M CPU Instructions."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_cm_instr.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_cm_instr.txt"
license: "Apache-2.0"
mode: "V"
---

Functions that generate specific Cortex-M CPU Instructions.

The following functions generate specific Cortex-M instructions that cannot be directly accessed by the C/C++ Compiler.
Refer to the Cortex-M Generic User Guides for detailed information about these Cortex-M instructions.

**Note:**
When using the **Arm Compiler Version 5 Toolchain** the following intrinsic_CPU_gr are implemented using the Embedded Assembler.
As the Embedded Assembler may cause side effects (Refer to **Arm Compiler v5.xx User Guide - Using the Inline and Embedded Assemblers of the Arm Compiler** for more information)
it is possible to disable the following intrinsic functions and therefore the usage of the Embedded Assembler with the **_define __NO_EMBEDDED_ASM_**:
 - __REV16
 - __REVSH
 - __RRX
