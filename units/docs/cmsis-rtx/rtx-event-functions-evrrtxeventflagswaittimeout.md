---
id: "rtx-event-functions-evrrtxeventflagswaittimeout"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxEventFlagsWaitTimeout"
summary: "The event EventFlagsWaitTimeout is generated when wait for event flags to become signaled is aborted due to expired wait timeout."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxEventFlagsWaitTimeout (osEventFlagsId_t ef_id)
```


The event **EventFlagsWaitTimeout** is generated when wait for event flags to become signaled is aborted due to expired wait timeout.

**Value** in the Event Recorder shows:
  - **ef_id** : event flags ID.
