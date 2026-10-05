---
id: "rtos2-thread-management-osthreadgetcount"
type: "concept"
domain: "rtos"
title: "Thread Management: osThreadGetCount"
summary: "The function osThreadGetCount returns the number of active threads or 0 in case of an error."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t osThreadGetCount (void)
```


The function **osThreadGetCount** returns the number of active threads or `0` in case of an error.

**Note:** This function **cannot** be called from Interrupt Service Routines.
