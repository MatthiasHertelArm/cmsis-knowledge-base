---
id: "core-compiler-control-static-inline"
type: "concept"
domain: "core"
title: "Compiler Control: __STATIC_INLINE"
summary: "Define a static function that may be inlined by the compiler."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
license: "Apache-2.0"
mode: "V"
---

```c
__STATIC_INLINE
```

 Define a static function that may be inlined by the compiler.

Defines a static function that may be inlined by the compiler. If the compiler generates inline code for
all calls to this functions, no additional function implementation is generated which may further optimize space.

**Code Example:**
```
\\ Get Interrupt Vector
__STATIC_INLINE uint32_t NVIC_GetVector(IRQn_Type IRQn)
{
    uint32_t *vectors = (uint32_t *) ((uintptr_t) SCB->VTOR);
    return vectors[(int32_t)IRQn + NVIC_USER_IRQ_OFFSET];
}
```
