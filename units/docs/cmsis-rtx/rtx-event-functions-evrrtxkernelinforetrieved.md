---
id: "rtx-event-functions-evrrtxkernelinforetrieved"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxKernelInfoRetrieved"
summary: "The event KernelInfoRetrieved is generated when the function osKernelGetInfo successfully retrieves kernel information."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxKernelInfoRetrieved (const osVersion_t *version, const char *id_buf, uint32_t id_size)
```


The event **KernelInfoRetrieved** is generated when the function osKernelGetInfo successfully retrieves kernel information.

**Value** in the Event Recorder shows:
  - **ver_api** : API version.
  - **ver_kernel** : kernel version.
  - **id** : kernel identification string (Detail).
