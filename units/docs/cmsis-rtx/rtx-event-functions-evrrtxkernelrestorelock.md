---
id: "rtx-event-functions-evrrtxkernelrestorelock"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxKernelRestoreLock"
summary: "The event KernelRestoreLock is generated when the function osKernelRestoreLock is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxKernelRestoreLock (int32_t lock)
```


The event **KernelRestoreLock** is generated when the function osKernelRestoreLock is called.

**Value** in the Event Recorder shows:
  - **lock** : lock state obtained by osKernelLock or osKernelUnlock.
