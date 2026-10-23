---
id: "core-compiler-control-compiler-barrier"
type: "concept"
domain: "core"
title: "Compiler Control: __COMPILER_BARRIER"
summary: "Barrier to prevent compiler from reordering instructions."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
license: "Apache-2.0"
mode: "V"
---

```c
__COMPILER_BARRIER
```

 Barrier to prevent compiler from reordering instructions.

This barrier limits the compilers reordering optimizations. It prevents the compiler from swapping
instructions resulting from code before and after the barrier.

**Code Example:**
The assignments in the example are independent. Hence the compiler could choose a different order of
execution, e.g. for a better pipeline utilization. Using the barrier in between prevents this type
of reordering.

```
void test (uint8_t *ptr) {
  var1 = 1;
  __COMPILE_BARRIER();
  var2 = var3 + 1;
}
```
