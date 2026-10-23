---
id: "core-compiler-control-asm"
type: "concept"
domain: "core"
title: "Compiler Control: __ASM"
summary: "Pass information from the compiler to the assembler."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
license: "Apache-2.0"
mode: "V"
---

```c
__ASM
```

 Pass information from the compiler to the assembler.

The **__ASM** keyword can declare or define an embedded assembly function or incorporate inline assembly into a function
(shown in the code example below).

**Code Example:**
```
// Reverse bit order of value

__attribute__( ( always_inline ) ) __STATIC_INLINE uint32_t __RBIT(uint32_t value)
{
  uint32_t result;

   __ASM volatile ("rbit %0, %1" : "=r" (result) : "r" (value) );
   return(result);
}
```
