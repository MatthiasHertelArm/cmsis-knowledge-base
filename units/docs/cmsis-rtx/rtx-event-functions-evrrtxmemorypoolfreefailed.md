---
id: "rtx-event-functions-evrrtxmemorypoolfreefailed"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMemoryPoolFreeFailed"
summary: "The event MemoryPoolFreeFailed is generated when the function osMemoryPoolFree fails to deallocate the memory block."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMemoryPoolFreeFailed (osMemoryPoolId_t mp_id, void *block)
```


The event **MemoryPoolFreeFailed** is generated when the function osMemoryPoolFree fails to deallocate the memory block.

**Value** in the Event Recorder shows:
  - **mp_id** : memory pool ID.
  - **block** : memory address of the memory block to be returned to the memory pool.
