---
id: "rtos2-thread-management-osthreadstate-t"
type: "concept"
domain: "rtos"
title: "Thread Management: osThreadState_t"
summary: "State of a thread as retrieved by osThreadGetState. In case osThreadGetState fails or if it is called from an ISR, it will return osThreadError, otherwise it returns the thread state."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osThreadState_t
```


State of a thread as retrieved by osThreadGetState. In case **osThreadGetState** fails or if it is called from an ISR, it
will return `osThreadError,` otherwise it returns the thread state.
