---
id: "core-compiler-control-stack-limit"
type: "concept"
domain: "core"
title: "Compiler Control: __STACK_LIMIT"
summary: "Compiler/linker symbol specifying the limit of the main stack (MSP)."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
license: "Apache-2.0"
mode: "V"
---

```c
__STACK_LIMIT
```

 Compiler/linker symbol specifying the limit of the main stack (MSP).

The address of the specified symbol is used to initialize the main stack pointer limit (MSPLIM on Armv8-M)
during low level init. This is compiler/linker specific. CMSIS specifies common default for supported
compilers.

**Note:** This define is only intended to be used by the startup_c_pg.

**Code Example:**
```
void Reset_Handler(void)
{
  __set_MSPLIM((uint32_t)(&__STACK_LIMIT));
  // :
  // :
}
```
