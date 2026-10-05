---
id: "rtx-cmsis-rtos2-api-osrtxthreadcbsize"
type: "concept"
domain: "rtos"
title: "CMSIS-RTOS2 API: osRtxThreadCbSize"
summary: "This macro exposes the minimum amount of memory needed for an RTX5 Thread Control Block, see osThreadAttrt::cbmem and osThreadAttrt::cbsize."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_os.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_os.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osRtxThreadCbSize
```

 Thread Control Block size

This macro exposes the minimum amount of memory needed for an RTX5 Thread Control Block,
see osThreadAttr_t::cb_mem and osThreadAttr_t::cb_size.

Example:
```
// Used-defined memory for thread control block
static uint32_t thread_cb[osRtxThreadCbSize/4U];
```
