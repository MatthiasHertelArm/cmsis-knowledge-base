---
id: "rtos2-mutex-management-osmutexgetowner"
type: "concept"
domain: "rtos"
title: "Mutex Management: osMutexGetOwner"
summary: "The function osMutexGetOwner returns the thread ID of the thread that acquired a mutex specified by parameter \\a mutexid. In case of an error or if the mutex is not blocked by any thread, it returns NULL."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mutex.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mutex.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osThreadId_t osMutexGetOwner (osMutexId_t mutex_id)
```


The function **osMutexGetOwner** returns the thread ID of the thread that acquired a mutex specified by parameter \a
mutex_id. In case of an error or if the mutex is not blocked by any thread, it returns `NULL`.

**Note:** This function **cannot** be called from Interrupt Service Routines.
