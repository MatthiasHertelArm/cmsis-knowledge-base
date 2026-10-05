---
id: "rtx-event-functions-evrrtxthreadflagssetdone"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadFlagsSetDone"
summary: "The event ThreadFlagsSetDone is generated when thread flags are successfully set."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadFlagsSetDone (osThreadId_t thread_id, uint32_t thread_flags)
```


The event **ThreadFlagsSetDone** is generated when thread flags are successfully set.

**Value** in the Event Recorder shows:
  - **thread_id** : thread ID.
  - **thread_flags** : thread flags after setting.
