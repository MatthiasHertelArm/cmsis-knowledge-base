---
id: "cfrt-technical-data-and-limitations-limitations"
type: "concept"
domain: "rtos"
title: "Technical Data and Limitations: Limitations"
summary: "The following list briefly describes the limitations and unsupported features of the CMSIS-RTOS2 wrapper for FreeRTOS:"
status: "draft"
collection: "cmsis-freertos"
source: "ARM-software/CMSIS-FreeRTOS@c3e5dc3:Documentation/Doxygen/src/technical_data.md"
doc_source: "https://github.com/ARM-software/CMSIS-FreeRTOS/blob/c3e5dc3/Documentation/Doxygen/src/technical_data.md#limitations"
license: "Apache-2.0"
mode: "V"
---

The following list briefly describes the limitations and unsupported features of the CMSIS-RTOS2 wrapper for FreeRTOS:

- Static memory allocation will only work if *all* memory (from attributes structure) is provided statically. In order to allocate object memory statically, you need to:
  - provide the memory for control blocks and stack in the `osThreadAttr_t` structure for threads.
  - provide the memory for control blocks and message data in the `osMessageQueueAttr_t` structure for memory queues.
  - provide the memory for control blocks for other objects in the object's attributes structure.
- Each timer object requires additional 8 bytes of memory:
  - to allocate all memory statically, provide the memory for control block of size (sizeof(StaticTimer_t) + 8 bytes)
  - otherwise, additional 8 bytes of dynamic memory will be used
- `osKernelSuspend` and `osKernelResume` are not supported.
- `osThreadDetach`, `osThreadJoin()` and attribute `osThreadJoinable` are not supported (`osThreadNew` returns NULL when `osThreadJoinable` attribute is specified).
- `osThreadGetStackSize` is not implemented.
- Event flags are limited to 24 bits.
- `osEventFlagsGetName` is not implemented.
- `osEventFlagsWait` cannot be called from an ISR.
- Priority inherit protocol is used as default mutex behavior (`osMutexNew` creates priority inherit mutex object by default and ignores `osMutexPrioInherit` attribute when specified).
- Robust mutex objects are not supported (`osMutexNew` returns NULL when `osMutexRobust` attribute is specified).
- `osMutexGetName` is not implemented and always returns NULL.
- `osSemaphoreGetName` is not implemented and always returns NULL.
- `osMessageQueueGetName` is not implemented and always returns NULL.
- `osMessageQueuePut` and `osMessageQueueGet` always ignore message priority.
- *Process Isolation (Functional Safety)* functions are not implemented.
