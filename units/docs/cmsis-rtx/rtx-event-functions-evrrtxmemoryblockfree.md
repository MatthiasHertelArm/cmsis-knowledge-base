---
id: "rtx-event-functions-evrrtxmemoryblockfree"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMemoryBlockFree"
summary: "The event MemoryBlockFree is generated when deallocation of a fixed size memory block completes."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMemoryBlockFree (osRtxMpInfo_t *mp_info, void *block, int32_t status)
```


The event **MemoryBlockFree** is generated when deallocation of a fixed size memory block completes.

**Value** in the Event Recorder shows:
  - **mp_info** : memory address of memory pool info.
  - **block** : memory address of the allocated memory block to be returned to the memory pool.
  - **status** : execution status osStatus_t
