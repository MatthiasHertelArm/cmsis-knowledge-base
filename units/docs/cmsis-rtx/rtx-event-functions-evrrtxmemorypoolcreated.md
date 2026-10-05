---
id: "rtx-event-functions-evrrtxmemorypoolcreated"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMemoryPoolCreated"
summary: "The event MemoryPoolCreated is generated when the function osMemoryPoolNew successfully creates a memory pool object."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMemoryPoolCreated (osMemoryPoolId_t mp_id, const char *name)
```


The event **MemoryPoolCreated** is generated when the function osMemoryPoolNew successfully creates a memory pool object.

**Value** in the Event Recorder shows:
  - **mp_id** : memory pool ID.
