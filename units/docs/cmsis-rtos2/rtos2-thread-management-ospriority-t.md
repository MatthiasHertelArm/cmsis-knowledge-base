---
id: "rtos2-thread-management-ospriority-t"
type: "concept"
domain: "rtos"
title: "Thread Management: osPriority_t"
summary: "The osPriority_t value specifies the priority for a thread. The default thread priority should be osPriorityNormal. If an active thread becomes ready that has a higher priority than the currently running thread then a thread switch occurs immediately."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osPriority_t
```



The **osPriority_t** value specifies the priority for a thread. The default thread priority should be _osPriorityNormal._
If an active thread becomes ready that has a higher priority than the currently running thread then a thread switch occurs
immediately. The system continues executing the thread with the higher priority.

To prevent from a priority inversion, a CMSIS-RTOS compliant OS may optionally implement a **priority inheritance**
method. A priority inversion occurs when a high priority thread is waiting for a resource or event that is controlled by a
thread with a lower priority. Thus causing the high priority thread potentially being blocked forever by another thread
with lower priority. To come over this issue the low priority thread controlling the resource should be treated as having
the higher priority until it releases the resource.

**Note:** Priority inheritance only applies to mutexes.
