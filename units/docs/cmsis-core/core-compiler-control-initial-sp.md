---
id: "core-compiler-control-initial-sp"
type: "concept"
domain: "core"
title: "Compiler Control: __INITIAL_SP"
summary: "Compiler/linker symbol specifying the location of the main stack (MSP)."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
license: "Apache-2.0"
mode: "V"
---

```c
__INITIAL_SP
```

 Compiler/linker symbol specifying the location of the main stack (MSP).

The address of the specified symbol is used to initialize the main stack pointer (MSP) during low
level init. This is compiler/linker specific. CMSIS specifies common default for supported compilers.

**Note:** This define is only intended to be used by the startup_c_pg.
