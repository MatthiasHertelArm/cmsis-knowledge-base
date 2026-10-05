---
id: "frb-4-task-management-4-4-task-creation"
type: "concept"
domain: "rtos"
title: "4 Task Management: 4.4 Task Creation"
summary: "Six API functions may be used to create tasks: xTaskCreate(), xTaskCreateStatic(), xTaskCreateRestricted(), xTaskCreateRestrictedStatic(), xTaskCreateAffinitySet(), and xTaskCreateStaticAffinitySet()"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch04.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch04.md#4-4-task-creation"
license: "CC-BY-SA-4.0"
mode: "V"
---

Six API functions may be used to create tasks:
`xTaskCreate()`,
`xTaskCreateStatic()`,
`xTaskCreateRestricted()`,
`xTaskCreateRestrictedStatic()`,
`xTaskCreateAffinitySet()`, and
`xTaskCreateStaticAffinitySet()`

Each task requires two blocks of RAM: one to hold its Task Control Block (TCB)
and one to store its stack. FreeRTOS API functions with "Static" in their names
use pre-allocated blocks of RAM passed into the functions as parameters.
Conversely, API functions without "Static" in their names allocate the required
RAM dynamically at runtime from the system heap.

Some FreeRTOS ports support tasks running in a "restricted" or "unprivileged" mode.
FreeRTOS API functions with "Restricted" in their names create tasks that
execute with limited access to the system's memory. API functions without
"Restricted" in their names create tasks that execute in "privileged mode" and
have access to the system's entire memory map.

FreeRTOS ports that support Symmetric Multi Processing (SMP) allow different tasks
to run simultaneously on multiple cores of the same CPU. For these ports, you may
specify which core a task will run on by using functions with "Affinity" in the name.

The FreeRTOS task creation API functions are quite complex. Most examples in this
document use `xTaskCreate()` because it is the simplest of these functions.
