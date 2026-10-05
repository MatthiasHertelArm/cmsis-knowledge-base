---
id: "rtos2-thread-management-osthreadgetstate"
type: "concept"
domain: "rtos"
title: "Thread Management: osThreadGetState"
summary: "The function osThreadGetState returns the state of the thread identified by parameter thread_id."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osThreadState_t osThreadGetState (osThreadId_t thread_id)
```


The function **osThreadGetState** returns the state of the thread identified by parameter _thread_id._ In case it fails or
if it is called from an ISR, it will return `osThreadError,` otherwise it returns the thread state (refer to
osThreadState_t for the list of thread states).
 
**Note:** This function **cannot** be called from Interrupt Service Routines.
