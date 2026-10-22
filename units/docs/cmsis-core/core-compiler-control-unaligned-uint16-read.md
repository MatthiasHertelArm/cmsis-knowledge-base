---
id: "core-compiler-control-unaligned-uint16-read"
type: "concept"
domain: "core"
title: "Compiler Control: __UNALIGNED_UINT16_READ"
summary: "Pointer for unaligned read of a uint16_t variable."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
license: "Apache-2.0"
mode: "V"
---

```c
__UNALIGNED_UINT16_READ
```

 Pointer for unaligned read of a uint16_t variable.

Defines a pointer to a uint16_t from an address that does not need to be aligned. This can then be used in read
operations. The compiler will generate the appropriate access (aligned or non-aligned) depending on the underlying Arm
processor core and compiler settings.

**Code Example:**
```
uint16_t val16;

void test (uint8_t *ptr) {
   val16 = __UNALIGNED_UINT16_READ(ptr);
}
```
