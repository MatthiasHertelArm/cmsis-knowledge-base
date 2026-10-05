---
id: "core-compiler-control"
type: "concept"
domain: "core"
title: "Compiler Control"
summary: "Compiler agnostic \\#define symbols for generic C/C++ source code"
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
license: "Apache-2.0"
mode: "V"
---

Compiler agnostic \#define symbols for generic C/C++ source code

The CMSIS-Core provides the header file **cmsis_compiler.h** with consistent \#define symbols for generate C or C++ source files that should be compiler agnostic.
Each CMSIS compliant compiler should support the functionality described in this section.

The header file **cmsis_compiler.h** is also included by each device_h_pg so that these definitions are available.
