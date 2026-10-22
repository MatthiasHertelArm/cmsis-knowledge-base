---
id: "core-compiler-control-alias"
type: "concept"
domain: "core"
title: "Compiler Control: __ALIAS"
summary: "Creates a symbol as alias to another symbol."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
license: "Apache-2.0"
mode: "V"
---

```c
__ALIAS
```

 Creates a symbol as alias to another symbol.

**Code Example:**
The example declares the function Interrupt0_Handler. By default it is just an alias
pointing to Default_Handler. In combination with __WEAK modifier this allows giving
the function definition at a later point if required.

```
void Interrupt0_Handler     (void) __WEAK __ALIAS("Default_Handler");
```
