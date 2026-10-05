---
id: "core-compiler-control-unaligned-uint16-write"
type: "concept"
domain: "core"
title: "Compiler Control: __UNALIGNED_UINT16_WRITE"
summary: "Pointer for unaligned write of a uint16t variable."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
license: "Apache-2.0"
mode: "V"
---

```c
__UNALIGNED_UINT16_WRITE
```

 Pointer for unaligned write of a uint16_t variable.

Defines a pointer to a uint16_t from an address that does not need to be aligned. This can then be used in write
operations. The compiler will generate the appropriate access (aligned or non-aligned) depending on the underlying Arm
processor core and compiler settings.

**Code Example:**
```
uint16_t val16 = 0U;

void test (uint8_t *ptr) {
   __UNALIGNED_UINT16_WRITE(ptr, val16);
}
```
