---
id: "core-compiler-control-restrict"
type: "concept"
domain: "core"
title: "Compiler Control: __RESTRICT"
summary: "restrict pointer qualifier to enable additional optimizations."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
license: "Apache-2.0"
mode: "V"
---

```c
__RESTRICT
```

 restrict pointer qualifier to enable additional optimizations.

The __RESTRICT keyword corresponds to the **restrict** pointer qualifier that has been introduced in C99.
__RESTRICT is a hint to the compiler that enables additional optimizations. It specifies that for the lifetime
of the pointer, only the pointer itself or a value directly derived from it (such as pointer + 1) is used to access
the object. The compiler may therefore ignore potential pointer aliasing effects and perform additional optimizations.

**Note:**
For compilers that do not support the restrict keyword, __RESTRICT is defined as an empty macro and a warning is issued.

**Code Example:**
```
__STATIC_INLINE void ARM_MPU_OrderedMemcpy (volatile uint32_t* dst, const uint32_t* __RESTRICT src, uint32_t len)
{
  uint32_t i;
  for (i = 0U; i < len; ++i)
  {
    dst[i] = src[i];   // Since src is restrict, the compiler can assume that dst and src are not overlapping may load multiple values at a time
  }
}
```
