---
id: "rtx-event-functions-evrrtxkernelgetstate"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxKernelGetState"
summary: "The event KernelGetState is generated when the function osKernelGetState is called and its execution result is known."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxKernelGetState (osKernelState_t state)
```


The event **KernelGetState** is generated when the function osKernelGetState is called and its execution result is known.

**Value** in the Event Recorder shows:
  - **state** : retrieved current RTOS Kernel state.
