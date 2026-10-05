---
id: "rtx-event-functions-evrrtxkernellockrestored"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxKernelLockRestored"
summary: "The event KernelLockRestored is generated when the function osKernelRestoreLock successfully completes its execution."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxKernelLockRestored (int32_t lock)
```


The event **KernelLockRestored** is generated when the function osKernelRestoreLock successfully completes its execution.

**Value** in the Event Recorder shows:
  - **lock** : new lock state (1 - locked, 0 - not locked).
