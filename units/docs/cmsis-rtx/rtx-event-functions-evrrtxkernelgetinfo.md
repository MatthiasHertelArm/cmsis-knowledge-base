---
id: "rtx-event-functions-evrrtxkernelgetinfo"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxKernelGetInfo"
summary: "The event KernelGetInfo is generated when the function osKernelGetInfo is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxKernelGetInfo (osVersion_t *version, char *id_buf, uint32_t id_size)
```


The event **KernelGetInfo** is generated when the function osKernelGetInfo is called.

**Value** in the Event Recorder shows:
  - **version** : memory address of buffer for retrieving version information.
  - **id_buf** : memory address of buffer for retrieving kernel identification string.
  - **id_size** : size of id_buf in bytes.
