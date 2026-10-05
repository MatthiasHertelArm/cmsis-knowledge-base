---
id: "rtx-event-functions-evrrtxkernelprotect"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxKernelProtect"
summary: "The event KernelProtect is generated when the function osKernelProtect is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxKernelProtect (uint32_t safety_class)
```


The event **KernelProtect** is generated when the function osKernelProtect is called.

**Value** in the Event Recorder shows:
  - **safety_class** : safety class value.
