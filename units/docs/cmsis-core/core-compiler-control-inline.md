---
id: "core-compiler-control-inline"
type: "concept"
domain: "core"
title: "Compiler Control: __INLINE"
summary: "Recommend that function should be inlined by the compiler."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
license: "Apache-2.0"
mode: "V"
---

```c
__INLINE
```

 Recommend that function should be inlined by the compiler.

Inline functions offer a trade-off between code size and performance. By default, the compiler decides during optimization whether to
inline code or not. The **__INLINE** attribute gives the compiler an hint to inline this function. Still, the compiler may decide not to inline
the function.  As the function is global an callable function is also generated.

**Code Example:**
```
const uint32_t led_mask[] = {1U << 4, 1U << 5, 1U << 6, 1U << 7};

/*------------------------------------------------------------------------------
  Switch on LEDs
------------------------------------------------------------------------------*/
__INLINE static void LED_On (uint32_t led) {

  PTD->PCOR   = led_mask[led];
}
```
