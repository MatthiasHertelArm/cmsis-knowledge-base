---
id: "rtx-event-functions-evrrtxmemorypoolalloctimeout"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMemoryPoolAllocTimeout"
summary: "The event MemoryPoolAllocTimeout is generated when wait for memory pool to become available is aborted due to expired wait timeout."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMemoryPoolAllocTimeout (osMemoryPoolId_t mp_id)
```


The event **MemoryPoolAllocTimeout** is generated when wait for memory pool to become available is aborted due to expired wait timeout.

**Value** in the Event Recorder shows:
  - **mp_id** : memory pool ID.
