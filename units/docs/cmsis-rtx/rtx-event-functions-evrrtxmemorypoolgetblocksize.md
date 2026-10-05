---
id: "rtx-event-functions-evrrtxmemorypoolgetblocksize"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMemoryPoolGetBlockSize"
summary: "The event MemoryPoolGetBlockSize is generated when the function osMemoryPoolGetBlockSize is called and its execution result is known."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMemoryPoolGetBlockSize (osMemoryPoolId_t mp_id, uint32_t block_size)
```


The event **MemoryPoolGetBlockSize** is generated when the function osMemoryPoolGetBlockSize is called and its execution result is known.

**Value** in the Event Recorder shows:
  - **mp_id** : memory pool ID.
  - **block_size** : retrieved memory block size in bytes (0 in case of a failure).
