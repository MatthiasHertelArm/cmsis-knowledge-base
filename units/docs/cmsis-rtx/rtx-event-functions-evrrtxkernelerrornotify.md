---
id: "rtx-event-functions-evrrtxkernelerrornotify"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxKernelErrorNotify"
summary: "The event KernelErrorNotify is generated when the function osRtxErrorNotify is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxKernelErrorNotify (uint32_t code, void *object_id)
```


The event **KernelErrorNotify** is generated when the function osRtxErrorNotify is called.

**Value** in the Event Recorder shows:
  - **code** : error code. 
  - **object_id** : object that caused the error.
