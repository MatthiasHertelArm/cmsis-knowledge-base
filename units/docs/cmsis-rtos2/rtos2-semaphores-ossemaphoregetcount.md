---
id: "rtos2-semaphores-ossemaphoregetcount"
type: "concept"
domain: "rtos"
title: "Semaphores: osSemaphoreGetCount"
summary: "The function osSemaphoreGetCount returns the number of available tokens of the semaphore object specified by parameter semaphore_id. In case of an error it returns 0."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_sema.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_sema.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t osSemaphoreGetCount (osSemaphoreId_t semaphore_id)
```


The function **osSemaphoreGetCount** returns the number of available tokens of the semaphore object specified by parameter
_semaphore_id._ In case of an error it returns `0`.

**Note:** This function may be called from Interrupt Service Routines.
