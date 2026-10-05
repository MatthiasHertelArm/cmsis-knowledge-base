---
id: "rtos2-thread-management-osthreadgetstackspace"
type: "concept"
domain: "rtos"
title: "Thread Management: osThreadGetStackSpace"
summary: "The function osThreadGetStackSpace returns the size of unused stack space for the thread specified by parameter thread_id. In case of an error, it returns 0."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t osThreadGetStackSpace (osThreadId_t thread_id);
```


The function **osThreadGetStackSpace** returns the size of unused stack space for the thread specified by parameter _thread_id._ In case of an error, it returns `0`.

**Note:** This function **cannot** be called from Interrupt Service Routines.
