---
id: "rtx-cmsis-rtos2-api-osrtxtimercbsize"
type: "concept"
domain: "rtos"
title: "CMSIS-RTOS2 API: osRtxTimerCbSize"
summary: "This macro exposes the minimum amount of memory needed for an RTX5 Timer Control Block, see osTimerAttrt::cbmem and osTimerAttrt::cbsize."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_os.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_os.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osRtxTimerCbSize
```

 Timer Control Block size

This macro exposes the minimum amount of memory needed for an RTX5 Timer Control Block,
see osTimerAttr_t::cb_mem and osTimerAttr_t::cb_size.

Example:
```
// Used-defined memory for timer control block
static uint32_t timer_cb[osRtxTimerCbSize/4U];
```
