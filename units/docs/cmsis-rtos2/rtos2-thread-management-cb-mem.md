---
id: "rtos2-thread-management-cb-mem"
type: "concept"
domain: "rtos"
title: "Thread Management: cb_mem"
summary: "Pointer to a memory for the thread control block object. Refer to CMSIS_RTOS_MemoryMgmt_Manual for more information."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osThreadAttr_t::cb_mem
```


Pointer to a memory for the thread control block object. Refer to CMSIS_RTOS_MemoryMgmt_Manual for more information.

Default: `NULL` to use CMSIS_RTOS_MemoryMgmt_Automatic for the thread control block.
