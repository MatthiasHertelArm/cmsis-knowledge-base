---
id: "rtx-event-functions-evrrtxkernelunlocked"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxKernelUnlocked"
summary: "The event KernelUnlocked is generated when the function osKernelUnlock successfully completes its execution."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxKernelUnlocked (int32_t lock)
```


The event **KernelUnlocked** is generated when the function osKernelUnlock successfully completes its execution.

**Value** in the Event Recorder shows:
  - **lock** : previous lock state (1 - locked, 0 - not locked).
