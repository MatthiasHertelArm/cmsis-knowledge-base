---
id: "rtx-event-functions-evrrtxthreadflagswaitpending"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadFlagsWaitPending"
summary: "The event ThreadFlagsWaitPending is generated when the function osThreadFlagsWait starts waiting for thread flags to become signaled."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadFlagsWaitPending (uint32_t flags, uint32_t options, uint32_t timeout)
```


The event **ThreadFlagsWaitPending** is generated when the function osThreadFlagsWait starts waiting for thread flags to become signaled.

**Value** in the Event Recorder shows:
  - **flags** : flags to wait for.
  - **options** : flags options (refer to thread flags options).
  - **timeout** : CMSIS_RTOS_TimeOutValue.
