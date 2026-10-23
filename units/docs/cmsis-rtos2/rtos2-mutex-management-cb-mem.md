---
id: "rtos2-mutex-management-cb-mem"
type: "concept"
domain: "rtos"
title: "Mutex Management: cb_mem"
summary: "Pointer to a memory for the mutex control block object. Refer to CMSIS_RTOS_MemoryMgmt_Manual for more information."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mutex.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mutex.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osMutexAttr_t::cb_mem
```


Pointer to a memory for the mutex control block object. Refer to CMSIS_RTOS_MemoryMgmt_Manual for more information.

Default: `NULL` to use CMSIS_RTOS_MemoryMgmt_Automatic for the mutex control block.
