---
id: "rtx-event-functions-evrrtxthreadpriorityupdated"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadPriorityUpdated"
summary: "The event ThreadPriorityUpdated is generated when the function osThreadSetPriority successfully updated the specified thread priority."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadPriorityUpdated (osThreadId_t thread_id, osPriority_t priority)
```


The event **ThreadPriorityUpdated** is generated when the function osThreadSetPriority successfully updated the specified thread priority.

**Value** in the Event Recorder shows:
  - **thread_id** : thread ID.
  - **priority** : new priority value for the thread function.
