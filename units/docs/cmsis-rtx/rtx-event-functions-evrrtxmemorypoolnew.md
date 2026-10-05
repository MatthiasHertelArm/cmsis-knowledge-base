---
id: "rtx-event-functions-evrrtxmemorypoolnew"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMemoryPoolNew"
summary: "The event MemoryPoolNew is generated when the function osMemoryPoolNew is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMemoryPoolNew (uint32_t block_count, uint32_t block_size, const osMemoryPoolAttr_t *attr)
```


The event **MemoryPoolNew** is generated when the function osMemoryPoolNew is called.

**Value** in the Event Recorder shows:
  - **block_count** : maximum number of memory blocks in memory pool.
  - **block_size** : memory block size in bytes.
  - **attr** : memory address of Memory Pool attributes or 0 when they are not specified.
