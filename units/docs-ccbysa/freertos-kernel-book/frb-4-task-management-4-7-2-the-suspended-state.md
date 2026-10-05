---
id: "frb-4-task-management-4-7-2-the-suspended-state"
type: "concept"
domain: "rtos"
title: "4 Task Management: 4.7 Expanding the *Not Running* State / 4.7.2 The *Suspended* State"
summary: "Part of: 4.7 Expanding the Not Running State"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch04.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch04.md#4-7-2-the-suspended-state"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 4.7 Expanding the *Not Running* State_

*Suspended* is also a sub-state of *Not Running*. Tasks in the Suspended
state are not available to the scheduler. The only way to enter the
Suspended state is through a call to the `vTaskSuspend()` API function,
and the only way out is through a call to the `vTaskResume()` or
`xTaskResumeFromISR()` API functions. Most applications do not use the
Suspended state.
