---
id: "rtx-event-functions-evrrtxeventflagsdestroyed"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxEventFlagsDestroyed"
summary: "The event EventFlagsDestroyed is generated when the function osEventFlagsDelete successfully deletes the event flags object."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxEventFlagsDestroyed (osEventFlagsId_t ef_id)
```


The event **EventFlagsDestroyed** is generated when the function osEventFlagsDelete successfully deletes the event flags object.

**Value** in the Event Recorder shows:
  - **ef_id** : event flags ID.
