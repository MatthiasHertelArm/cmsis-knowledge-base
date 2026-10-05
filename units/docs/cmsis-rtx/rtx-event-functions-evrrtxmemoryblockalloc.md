---
id: "rtx-event-functions-evrrtxmemoryblockalloc"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMemoryBlockAlloc"
summary: "The event MemoryBlockAlloc is generated when allocation of a fixed size memory block completes."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMemoryBlockAlloc (osRtxMpInfo_t *mp_info, void *block)
```


The event **MemoryBlockAlloc** is generated when allocation of a fixed size memory block completes.

**Value** in the Event Recorder shows:
  - **mp_info** : memory address of memory pool info.
  - **block** : memory address of the allocated memory block or 0 in case of no memory is available.
