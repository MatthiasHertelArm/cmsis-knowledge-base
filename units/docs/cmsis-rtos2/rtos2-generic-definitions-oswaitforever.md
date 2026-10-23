---
id: "rtos2-generic-definitions-oswaitforever"
type: "concept"
domain: "rtos"
title: "Generic Definitions: osWaitForever"
summary: "A special CMSIS_RTOS_TimeOutValue that informs the RTOS to wait infinite until a resource becomes available."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_status.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_status.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osWaitForever
```

 A special CMSIS_RTOS_TimeOutValue that informs the RTOS to wait infinite until a resource becomes available.
It applies to the following functions: 
 - osDelay :  osDelay
 - osThreadFlagsWait :  osThreadFlagsWait 
 - osEventFlagsWait :  osEventFlagsWait
 - osMutexAcquire :  osMutexAcquire
 - osSemaphoreAcquire :  osSemaphoreAcquire
 - osMemoryPoolAlloc :  osMemoryPoolAlloc
 - osMessageQueuePut :  osMessageQueuePut
 - osMessageQueueGet :  osMessageQueueGet
