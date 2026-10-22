---
id: "rtos2-thread-management-void"
type: "concept"
domain: "rtos"
title: "Thread Management: void"
summary: "Entry function for threads. Setting up a new thread (osThreadNew) will start execution with a call into this entry function. The optional argument can be used to hand over arbitrary user data to the thread, i.e."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void (*osThreadFunc_t) (void *argument)
```

 Entry function for threads. Setting up a new thread (osThreadNew) will start execution with a call into this
entry function. The optional argument can be used to hand over arbitrary user data to the thread, i.e. to identify the thread
or for runtime parameters.

- `argument` (in): arbitrary user data set on osThreadNew.
