---
id: "rtx-event-functions-evrrtxmemorypoolgetcount"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMemoryPoolGetCount"
summary: "The event MemoryPoolGetCount is generated when the function osMemoryPoolGetCount is called and its execution result is known."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMemoryPoolGetCount (osMemoryPoolId_t mp_id, uint32_t count)
```


The event **MemoryPoolGetCount** is generated when the function osMemoryPoolGetCount is called and its execution result is known.

**Value** in the Event Recorder shows:
  - **mp_id** : memory pool ID.
  - **count** : retrieved number of memory block used (0 in case of a failure).
