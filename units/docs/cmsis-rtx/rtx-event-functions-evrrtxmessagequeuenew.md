---
id: "rtx-event-functions-evrrtxmessagequeuenew"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMessageQueueNew"
summary: "The event MessageQueueNew is generated when the function osMessageQueueNew is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMessageQueueNew (uint32_t msg_count, uint32_t msg_size, const osMessageQueueAttr_t *attr)
```


The event **MessageQueueNew** is generated when the function osMessageQueueNew is called.

**Value** in the Event Recorder shows:
  - **msg_count** : maximum number of messages in queue.
  - **msg_size** : maximum message size in bytes.
  - **attr** : memory address of Message Queue attributes or 0 when they are not specified.
