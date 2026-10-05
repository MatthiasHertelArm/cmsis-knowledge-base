---
id: "core-compiler-control-no-init"
type: "concept"
domain: "core"
title: "Compiler Control: __NO_INIT"
summary: "Specifies a section name for a variable to simplify variable placement into a non-initialized memory"
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
license: "Apache-2.0"
mode: "V"
---

```c
__NO_INIT
```

 Specifies a section name for a variable to simplify variable placement into a non-initialized memory

Specifies a section name (e.g, .bss.noinit or .noinit) for a variable that can be used by a linker-script
to position that variable into a non-initialized memory.

**Code Example:**
The EventBuffer in the example must not be copy- or zero-initialized. By adding
__NO_INIT at variable declaration/definition, and with appropriate linker-script, this variable is
positioned into a non-initialized memory.

```
static EventRecord_t EventBuffer[EVENT_RECORD_COUNT] __NO_INIT __ALIGNED(16);
```
