---
id: "rtos2-semaphores-ossemaphoredelete"
type: "concept"
domain: "rtos"
title: "Semaphores: osSemaphoreDelete"
summary: "The function osSemaphoreDelete deletes a semaphore object specified by parameter semaphoreid. It releases internal memory obtained for semaphore handling. After this call, the semaphoreid is no longer valid and cannot be used."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_sema.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_sema.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osSemaphoreDelete (osSemaphoreId_t semaphore_id)
```


The function **osSemaphoreDelete** deletes a semaphore object specified by parameter _semaphore_id._ It releases internal
memory obtained for semaphore handling. After this call, the _semaphore_id_ is no longer valid and cannot be used. The
semaphore may be created again using the function osSemaphoreNew.

Possible osStatus_t return values:
 - **osOK:** the semaphore object has been deleted.
 - **osErrorParameter:** the parameter _semaphore_id_ is `NULL` or invalid.
 - **osErrorResource:** the semaphore is in an invalid state.
 - **osErrorISR:** **osSemaphoreDelete** cannot be called from interrupt service routines.
 - **osErrorSafetyClass:** the calling thread safety class is lower than the safety class of the specified semaphore.

**Note:** This function **cannot** be called from Interrupt Service Routines.
