---
id: "rtos2-thread-management-osthreadgetstacksize"
type: "concept"
domain: "rtos"
title: "Thread Management: osThreadGetStackSize"
summary: "The function osThreadGetStackSize returns the stack size of the thread specified by parameter thread_id. In case of an error, it returns 0."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t osThreadGetStackSize (osThreadId_t thread_id)
```


The function **osThreadGetStackSize** returns the stack size of the thread specified by parameter _thread_id._ In case of an
error, it returns `0`.

**Note:** This function **cannot** be called from Interrupt Service Routines.
