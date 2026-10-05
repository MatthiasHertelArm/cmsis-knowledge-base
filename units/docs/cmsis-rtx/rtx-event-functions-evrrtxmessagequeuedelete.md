---
id: "rtx-event-functions-evrrtxmessagequeuedelete"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMessageQueueDelete"
summary: "The event MessageQueueDelete is generated when the function osMessageQueueDelete is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMessageQueueDelete (osMessageQueueId_t mq_id)
```


The event **MessageQueueDelete** is generated when the function osMessageQueueDelete is called.

**Value** in the Event Recorder shows:
  - **mq_id** : message queue ID.
