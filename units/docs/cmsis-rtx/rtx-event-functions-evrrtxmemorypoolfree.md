---
id: "rtx-event-functions-evrrtxmemorypoolfree"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMemoryPoolFree"
summary: "The event MemoryPoolFree is generated when the function osMemoryPoolFree is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMemoryPoolFree (osMemoryPoolId_t mp_id, void *block)
```


The event **MemoryPoolFree** is generated when the function osMemoryPoolFree is called.

**Value** in the Event Recorder shows:
  - **mp_id** : memory pool ID.
  - **block** : memory address of the memory block to be returned to the memory pool.
