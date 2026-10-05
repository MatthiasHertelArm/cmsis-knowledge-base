---
id: "rtx-event-functions-evrrtxeventflagsgetname"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxEventFlagsGetName"
summary: "The event EventFlagsGetName is generated when the function osEventFlagsGetName is called and its execution result is known."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxEventFlagsGetName (osEventFlagsId_t ef_id, const char *name)
```


The event **EventFlagsGetName** is generated when the function osEventFlagsGetName is called and its execution result is known.

**Value** in the Event Recorder shows:
  - **ef_id** : event flags ID.
  - **name** : retrieved memory address of name string (0 in case of a failure).
