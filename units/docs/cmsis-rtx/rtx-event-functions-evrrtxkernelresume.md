---
id: "rtx-event-functions-evrrtxkernelresume"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxKernelResume"
summary: "The event KernelResume is generated when the function osKernelResume is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxKernelResume (uint32_t sleep_ticks)
```


The event **KernelResume** is generated when the function osKernelResume is called.

**Value** in the Event Recorder shows:
  - **sleep_ticks** : time in ticks, for how long the system was in sleep or power-down mode.
