---
id: "rtx-cmsis-rtos2-api-osrtxmutexcbsize"
type: "concept"
domain: "rtos"
title: "CMSIS-RTOS2 API: osRtxMutexCbSize"
summary: "This macro exposes the minimum amount of memory needed for an RTX5 Mutex Control Block, see osMutexAttrt::cbmem and osMutexAttrt::cbsize."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_os.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_os.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osRtxMutexCbSize
```

 Mutex Control Block size

This macro exposes the minimum amount of memory needed for an RTX5 Mutex Control Block,
see osMutexAttr_t::cb_mem and osMutexAttr_t::cb_size.

Example:
```
// Used-defined memory for mutex control block
static uint32_t mutex_cb[osRtxMutexCbSize/4U];
```
