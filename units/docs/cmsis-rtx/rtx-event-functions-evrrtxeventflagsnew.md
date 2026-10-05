---
id: "rtx-event-functions-evrrtxeventflagsnew"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxEventFlagsNew"
summary: "The event EventFlagsNew is generated when the function osEventFlagsNew is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxEventFlagsNew (const osEventFlagsAttr_t *attr)
```


The event **EventFlagsNew** is generated when the function osEventFlagsNew is called.

**Value** in the Event Recorder shows:
  - **attr** : memory address of Event Flags attributes or 0 when they are not specified.
