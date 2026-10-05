---
id: "rtx-operation-calls-from-interrupt-service-routines"
type: "concept"
domain: "rtos"
title: "operation: Calls from Interrupt Service Routines"
summary: "The following CMSIS-RTOS2 functions can be called from threads and Interrupt Service Routines (ISR):"
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/operation.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/operation.md#calls-from-interrupt-service-routines"
license: "Apache-2.0"
mode: "V"
---

The following CMSIS-RTOS2 functions can be called from threads and Interrupt Service Routines (ISR):

- osKernelGetInfo, osKernelGetState, osKernelGetTickCount, osKernelGetTickFreq, osKernelGetSysTimerCount, osKernelGetSysTimerFreq
- osThreadGetName, osThreadGetId, osThreadFlagsSet
- osTimerGetName
- osEventFlagsGetName, osEventFlagsSet, osEventFlagsClear, osEventFlagsGet, osEventFlagsWait
- osMutexGetName
- osSemaphoreGetName, osSemaphoreAcquire, osSemaphoreRelease, osSemaphoreGetCount
- osMemoryPoolGetName, osMemoryPoolAlloc, osMemoryPoolFree, osMemoryPoolGetCapacity, osMemoryPoolGetBlockSize, osMemoryPoolGetCount, osMemoryPoolGetSpace
- osMessageQueueGetName, osMessageQueuePut, osMessageQueueGet, osMessageQueueGetCapacity, osMessageQueueGetMsgSize, osMessageQueueGetCount, osMessageQueueGetSpace

Functions that cannot be called from an ISR are verifying the interrupt status and return the status code osErrorISR, in case they are called from an ISR context. In some implementations, this condition might be caught using the HARD_FAULT vector.

> **Note**
>
> - RTX does not disable interrupts during critical sections for Armv7-M and Armv8-M architecture based devices, but rather uses atomic operations.
> - Therefore, there is no need to configure interrupt priorities of interrupt service routines that use RTOS functions.
