---
id: "rtx-event-functions-evrrtxmessagequeuegettimeout"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMessageQueueGetTimeout"
summary: "The event MessageQueueGetTimeout is generated when the function osMessageQueueGet is called and there is no message available in queue until timeout expires."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMessageQueueGetTimeout (osMessageQueueId_t mq_id)
```


The event **MessageQueueGetTimeout** is generated when the function osMessageQueueGet is called and there is no message available in queue until timeout expires.

**Value** in the Event Recorder shows:
  - **mq_id** : message queue ID.
