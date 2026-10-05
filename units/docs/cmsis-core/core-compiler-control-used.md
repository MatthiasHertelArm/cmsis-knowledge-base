---
id: "core-compiler-control-used"
type: "concept"
domain: "core"
title: "Compiler Control: __USED"
summary: "Inform that a variable shall be retained in executable image."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/ref_compiler_ctrl.txt"
license: "Apache-2.0"
mode: "V"
---

```c
__USED
```

 Inform that a variable shall be retained in executable image.

Definitions tagged with **__USED** in the source code should be not removed by the linker when detected as unused.

**Code Example:**
```
/* Export following variables for debugging */
__USED uint32_t const CMSIS_RTOS_API_Version = osCMSIS;
__USED uint32_t const CMSIS_RTOS_RTX_Version = osCMSIS_RTX;
__USED uint32_t const os_clockrate = OS_TICK;
__USED uint32_t const os_timernum  = 0;
```
