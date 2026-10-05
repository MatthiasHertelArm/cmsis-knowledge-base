---
id: "rtx-event-functions-evrrtxkernelgetsystimercount"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxKernelGetSysTimerCount"
summary: "The event KernelGetSysTimerCount is generated when the function osKernelGetSysTimerCount is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxKernelGetSysTimerCount (uint32_t count)
```


The event **KernelGetSysTimerCount** is generated when the function osKernelGetSysTimerCount is called.

**Value** in the Event Recorder shows:
  - **count** : retrieved kernel current system timer count as 32-bit value.
