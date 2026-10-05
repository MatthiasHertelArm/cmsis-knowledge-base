---
id: "core-compiler-control-static-forceinline"
type: "concept"
domain: "core"
title: "Compiler Control: __STATIC_FORCEINLINE"
summary: "Define a static function that should be always inlined by the compiler."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
license: "Apache-2.0"
mode: "V"
---

```c
__STATIC_FORCEINLINE
```

 Define a static function that should be always inlined by the compiler.

Defines a static function that should be always inlined by the compiler.

**Note:**
For compilers that do not allow to force function inlining, the macro maps to __STATIC_INLINE.

**Code Example:**
```
\\ Get Interrupt Vector
__STATIC_FORCEINLINE uint32_t NVIC_GetVector(IRQn_Type IRQn)
{
    uint32_t *vectors = (uint32_t *) ((uintptr_t) SCB->VTOR);
    return vectors[(int32_t)IRQn + NVIC_USER_IRQ_OFFSET];
}
```
