---
id: "core-compiler-control-weak"
type: "concept"
domain: "core"
title: "Compiler Control: __WEAK"
summary: "Export a function or variable weakly to allow overwrites."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
license: "Apache-2.0"
mode: "V"
---

```c
__WEAK
```

 Export a function or variable weakly to allow overwrites.

Functions defined with **__WEAK** export their symbols weakly. A weakly defined function behaves like a normally defined
function unless a non-weakly defined function of the same name is linked into the same image. If both a non-weakly defined
function and a weakly defined function exist in the same image then all calls to the function resolve to call the non-weak
function.

Functions declared with **__WEAK** and then defined without **__WEAK** behave as non-weak functions.

**Code Example:**
```
__WEAK void SystemInit(void)
{
  SystemCoreSetup();
  SystemCoreClockSetup();
}
```
