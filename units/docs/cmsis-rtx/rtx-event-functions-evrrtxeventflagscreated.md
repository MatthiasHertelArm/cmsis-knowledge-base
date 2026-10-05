---
id: "rtx-event-functions-evrrtxeventflagscreated"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxEventFlagsCreated"
summary: "The event EventFlagsCreated is generated when the function osEventFlagsNew successfully creates a event flags object."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxEventFlagsCreated (osEventFlagsId_t ef_id, const char *name)
```


The event **EventFlagsCreated** is generated when the function osEventFlagsNew successfully creates a event flags object.

**Value** in the Event Recorder shows:
  - **ef_id** : event flags ID.
