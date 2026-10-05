---
id: "rtx-cmsis-rtos2-api-osrtxmessagequeuecbsize"
type: "concept"
domain: "rtos"
title: "CMSIS-RTOS2 API: osRtxMessageQueueCbSize"
summary: "This macro exposes the minimum amount of memory needed for an RTX5 Message Queue Control Block, see osMessageQueueAttrt::cbmem and osMessageQueueAttrt::cbsize."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_os.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_os.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osRtxMessageQueueCbSize
```

 Message Queue Control Block size

This macro exposes the minimum amount of memory needed for an RTX5 Message Queue Control Block,
see osMessageQueueAttr_t::cb_mem and osMessageQueueAttr_t::cb_size.

Example:
```
// Used-defined memory for message queue control block
static uint32_t msgqueue_cb[osRtxMessageQueueCbSize/4U];
```
