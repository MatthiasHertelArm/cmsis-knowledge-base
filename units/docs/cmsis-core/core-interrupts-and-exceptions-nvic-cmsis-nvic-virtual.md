---
id: "core-interrupts-and-exceptions-nvic-cmsis-nvic-virtual"
type: "concept"
domain: "core"
title: "Interrupts and Exceptions (NVIC): CMSIS_NVIC_VIRTUAL"
summary: "When CMSIS_NVIC_VIRTUAL is defined, the NVIC access functions in the table below must be implemented for virtualizing NVIC access. These functions should be implemented in a separate source module. The original CMSIS-Core _NVIC functions are always available independent of CMSIS_NVIC_VIRTUAL."
status: "draft"
collection: "cmsis-core"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Core/src/ref_nvic.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Core/src/ref_nvic.txt"
license: "Apache-2.0"
mode: "V"
---

```c
CMSIS_NVIC_VIRTUAL
```

When CMSIS_NVIC_VIRTUAL is defined, the NVIC access functions in the table below must be implemented
for virtualizing NVIC access.  These functions should be implemented
in a separate source module.
The original CMSIS-Core __NVIC functions are always available independent of CMSIS_NVIC_VIRTUAL.

NVIC Access Functions     | CMSIS-Core Functions
--------------------------|---------------------------------------------
NVIC_EnableIRQ            | __NVIC_EnableIRQ
NVIC_GetEnableIRQ         | __NVIC_GetEnableIRQ
NVIC_DisableIRQ           | __NVIC_DisableIRQ
NVIC_GetPendingIRQ        | __NVIC_GetPendingIRQ
NVIC_SetPendingIRQ        | __NVIC_SetPendingIRQ
NVIC_ClearPendingIRQ      | __NVIC_ClearPendingIRQ
NVIC_GetActive            | __NVIC_GetActive
NVIC_SetPriority          | __NVIC_SetPriority
NVIC_GetPriority          | __NVIC_GetPriority
NVIC_SetPriorityGrouping  | __NVIC_SetPriorityGrouping
NVIC_GetPriorityGrouping  | __NVIC_GetPriorityGrouping
