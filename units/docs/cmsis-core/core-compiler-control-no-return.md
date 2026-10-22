---
id: "core-compiler-control-no-return"
type: "concept"
domain: "core"
title: "Compiler Control: __NO_RETURN"
summary: "Inform the compiler that a function does not return."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
license: "Apache-2.0"
mode: "V"
---

```c
__NO_RETURN
```

 Inform the compiler that a function does not return.

Informs the compiler that the function does not return. The compiler can then perform optimizations by
removing code that is never reached. For maximum portability, this should only be used where the C/C++
standard allows it.

**Code Example:**
```
// OS idle demon (running when no other thread is ready to run).

__NO_RETURN void os_idle_demon (void);
```
