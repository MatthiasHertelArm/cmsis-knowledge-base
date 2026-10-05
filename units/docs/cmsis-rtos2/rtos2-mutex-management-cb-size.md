---
id: "rtos2-mutex-management-cb-size"
type: "concept"
domain: "rtos"
title: "Mutex Management: cb_size"
summary: "The size (in bytes) of memory block passed with cb_mem. Required value depends on the underlying kernel implementation."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mutex.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mutex.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osMutexAttr_t::cb_size
```


The size (in bytes) of memory block passed with cb_mem. Required value depends on the underlying kernel implementation.

Default: `0` as the default is no memory provided with cb_mem.
