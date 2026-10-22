---
id: "core-compiler-control-program-start"
type: "concept"
domain: "core"
title: "Compiler Control: __PROGRAM_START"
summary: "Entry function into the user application or library startup."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
license: "Apache-2.0"
mode: "V"
---

```c
__PROGRAM_START
```

 Entry function into the user application or library startup.

Gives the function to be jumped into right after low level initialization, i.e. SystemInit. This
is compiler and library specific. CMSIS specifies common default for supported compilers.

**Note:** This define is only intended to be used by the startup_c_pg.

**Code Example:**
```
void Reset_Handler(void)
{
  SystemInit();                             /* CMSIS System Initialization */
  __PROGRAM_START();                        /* Enter PreMain (C library entry point) */
}
```
