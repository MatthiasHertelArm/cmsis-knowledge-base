---
id: "rtx-event-functions-evrrtxkernelsuspended"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxKernelSuspended"
summary: "The event KernelSuspended is generated when the function osKernelSuspend successfully suspends RTOS kernel execution."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxKernelSuspended (uint32_t sleep_ticks)
```


The event **KernelSuspended** is generated when the function osKernelSuspend successfully suspends RTOS kernel execution.

**Value** in the Event Recorder shows:
  - **sleep_ticks** : time in ticks, for how long the system can sleep or power-down.
