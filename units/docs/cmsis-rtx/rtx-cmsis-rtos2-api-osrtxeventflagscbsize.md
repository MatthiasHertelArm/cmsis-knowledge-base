---
id: "rtx-cmsis-rtos2-api-osrtxeventflagscbsize"
type: "concept"
domain: "rtos"
title: "CMSIS-RTOS2 API: osRtxEventFlagsCbSize"
summary: "This macro exposes the minimum amount of memory needed for an RTX5 Event Flags Control Block, see osEventFlagsAttrt::cbmem and osEventFlagsAttrt::cbsize."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_os.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_os.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osRtxEventFlagsCbSize
```

 Event Flags Control Block size

This macro exposes the minimum amount of memory needed for an RTX5 Event Flags Control Block,
see osEventFlagsAttr_t::cb_mem and osEventFlagsAttr_t::cb_size.

Example:
```
// Used-defined memory for event flags control block
static uint32_t evflags_cb[osRtxEventFlagsCbSize/4U];
```
