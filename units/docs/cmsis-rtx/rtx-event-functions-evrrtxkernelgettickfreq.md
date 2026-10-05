---
id: "rtx-event-functions-evrrtxkernelgettickfreq"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxKernelGetTickFreq"
summary: "The event KernelGetTickFreq is generated when the function osKernelGetTickFreq called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxKernelGetTickFreq (uint32_t freq)
```


The event **KernelGetTickFreq** is generated when the function osKernelGetTickFreq called.

**Value** in the Event Recorder shows:
  - **freq** : retrieved frequency of the kernel tick in Hz.
