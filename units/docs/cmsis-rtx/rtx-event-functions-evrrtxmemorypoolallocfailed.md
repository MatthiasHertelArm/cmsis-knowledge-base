---
id: "rtx-event-functions-evrrtxmemorypoolallocfailed"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMemoryPoolAllocFailed"
summary: "The event MemoryPoolAllocFailed is generated when the function osMemoryPoolAlloc fails to allocate the memory block due to out of available memory."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMemoryPoolAllocFailed (osMemoryPoolId_t mp_id)
```


The event **MemoryPoolAllocFailed** is generated when the function osMemoryPoolAlloc fails to allocate the memory block due to out of available memory.

**Value** in the Event Recorder shows:
  - **mp_id** : memory pool ID.
