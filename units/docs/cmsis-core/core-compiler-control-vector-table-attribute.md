---
id: "core-compiler-control-vector-table-attribute"
type: "concept"
domain: "core"
title: "Compiler Control: __VECTOR_TABLE_ATTRIBUTE"
summary: "Additional decl specs to be used when defining the (static) interrupt vector table."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
license: "Apache-2.0"
mode: "V"
---

```c
__VECTOR_TABLE_ATTRIBUTE
```

 Additional decl specs to be used when defining the (static) interrupt vector table.

The given decl specs are used for defining the static (compiler time) interrupt vector table, e.g.
to mark the table as used and force it into a specific linker section. CMSIS specifies common default
for supported compilers.

**Note:** This define is only intended to be used by the startup_c_pg.
