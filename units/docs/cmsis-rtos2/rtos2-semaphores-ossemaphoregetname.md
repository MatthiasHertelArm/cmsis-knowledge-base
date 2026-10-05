---
id: "rtos2-semaphores-ossemaphoregetname"
type: "concept"
domain: "rtos"
title: "Semaphores: osSemaphoreGetName"
summary: "The function osSemaphoreGetName returns the pointer to the name string of the semaphore identified by parameter \\a semaphoreid or NULL in case of an error."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_sema.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_sema.txt"
license: "Apache-2.0"
mode: "V"
---

```c
const char *osSemaphoreGetName (osSemaphoreId_t semaphore_id)
```


The function **osSemaphoreGetName** returns the pointer to the name string of the semaphore identified by parameter \a
semaphore_id or `NULL` in case of an error.

**Note:** This function may be called from Interrupt Service Routines.
