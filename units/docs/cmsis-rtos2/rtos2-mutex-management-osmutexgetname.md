---
id: "rtos2-mutex-management-osmutexgetname"
type: "concept"
domain: "rtos"
title: "Mutex Management: osMutexGetName"
summary: "The function osMutexGetName returns the pointer to the name string of the mutex identified by parameter mutex_id or NULL in case of an error."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mutex.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mutex.txt"
license: "Apache-2.0"
mode: "V"
---

```c
const char *osMutexGetName (osMutexId_t mutex_id)
```


The function **osMutexGetName** returns the pointer to the name string of the mutex identified by parameter _mutex_id_ or
`NULL` in case of an error.

**Note:** This function may be called from Interrupt Service Routines.
