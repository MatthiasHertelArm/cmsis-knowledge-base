---
id: "rtos2-using-cmsis-rtos2-interface-calls-from-interrupt-service-routines"
type: "concept"
domain: "rtos"
title: "Using CMSIS-RTOS2 Interface: Calls from Interrupt Service Routines"
summary: "The following CMSIS-RTOS2 functions can be called from threads and Interrupt Service Routines (ISR):"
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/using.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/using.md#calls-from-interrupt-service-routines"
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

Functions that cannot be called from an ISR are verifying the interrupt status and return the status code osErrorISR, in case they are called from an ISR context. In some implementations, this condition might be caught using the HARD_FAULT
