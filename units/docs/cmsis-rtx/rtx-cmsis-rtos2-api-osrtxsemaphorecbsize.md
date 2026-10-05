---
id: "rtx-cmsis-rtos2-api-osrtxsemaphorecbsize"
type: "concept"
domain: "rtos"
title: "CMSIS-RTOS2 API: osRtxSemaphoreCbSize"
summary: "This macro exposes the minimum amount of memory needed for an RTX5 Semaphore Control Block, see osSemaphoreAttr_t::cb_mem and osSemaphoreAttr_t::cb_size."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_os.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_os.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osRtxSemaphoreCbSize
```

 Semaphore Control Block size

This macro exposes the minimum amount of memory needed for an RTX5 Semaphore Control Block,
see osSemaphoreAttr_t::cb_mem and osSemaphoreAttr_t::cb_size.

Example:
```
// Used-defined memory for semaphore control block
static uint32_t sema_cb[osRtxSemaphoreCbSize/4U];
```
