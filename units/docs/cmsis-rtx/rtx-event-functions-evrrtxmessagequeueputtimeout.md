---
id: "rtx-event-functions-evrrtxmessagequeueputtimeout"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMessageQueuePutTimeout"
summary: "The event MessageQueuePutTimeout is generated when the function osMessageQueuePut fails to insert a message into the queue until timeout expires."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMessageQueuePutTimeout (osMessageQueueId_t mq_id)
```


The event **MessageQueuePutTimeout** is generated when the function osMessageQueuePut fails to insert a message into the queue until timeout expires.

**Value** in the Event Recorder shows:
  - **mq_id** : message queue ID.
