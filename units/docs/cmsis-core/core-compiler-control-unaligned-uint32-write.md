---
id: "core-compiler-control-unaligned-uint32-write"
type: "concept"
domain: "core"
title: "Compiler Control: __UNALIGNED_UINT32_WRITE"
summary: "Pointer for unaligned write of a uint32_t variable."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
license: "Apache-2.0"
mode: "V"
---

```c
__UNALIGNED_UINT32_WRITE
```

 Pointer for unaligned write of a uint32_t variable.

Defines a pointer to a uint32_t from an address that does not need to be aligned. This can then be used in write
operations. The compiler will generate the appropriate access (aligned or non-aligned) depending on the underlying Arm
processor core and compiler settings.

**Code Example:**
```
uint32_t val32 = 0U;

void test (uint8_t *ptr) {
   __UNALIGNED_UINT32_WRITE(ptr, val32);
}
```
