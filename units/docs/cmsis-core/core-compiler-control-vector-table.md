---
id: "core-compiler-control-vector-table"
type: "concept"
domain: "core"
title: "Compiler Control: __VECTOR_TABLE"
summary: "Symbol name used for the (static) interrupt vector table."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
license: "Apache-2.0"
mode: "V"
---

```c
__VECTOR_TABLE
```

 Symbol name used for the (static) interrupt vector table.

The given name is used for defining the static (compiler time) interrupt vector table. The name
must comply with any compiler/linker conventions, e.g. if used for vector table relocation or debugger
awareness. CMSIS specifies common default for supported compilers.

**Note:** This define is only intended to be used by the startup_c_pg.
