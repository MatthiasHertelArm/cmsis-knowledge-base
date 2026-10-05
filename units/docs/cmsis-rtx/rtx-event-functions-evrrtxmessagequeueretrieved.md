---
id: "rtx-event-functions-evrrtxmessagequeueretrieved"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMessageQueueRetrieved"
summary: "The event MessageQueueRetrieved is generated when message is retrieved from the message queue."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMessageQueueRetrieved (osMessageQueueId_t mq_id, void *msg_ptr)
```


The event **MessageQueueRetrieved** is generated when message is retrieved from the message queue.

**Value** in the Event Recorder shows:
  - **mq_id** : message queue ID.
  - **msg_ptr** : memory address of buffer for message.
