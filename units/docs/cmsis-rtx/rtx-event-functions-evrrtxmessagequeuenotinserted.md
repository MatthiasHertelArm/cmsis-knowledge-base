---
id: "rtx-event-functions-evrrtxmessagequeuenotinserted"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMessageQueueNotInserted"
summary: "The event MessageQueueNotInserted is generated when the function osMessageQueuePut fails to insert a message into the queue. Usually this happens when queue is out of memory."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMessageQueueNotInserted (osMessageQueueId_t mq_id, const void *msg_ptr)
```


The event **MessageQueueNotInserted** is generated when the function osMessageQueuePut fails to insert a message into the queue.
Usually this happens when queue is out of memory.

**Value** in the Event Recorder shows:
  - **mq_id** : message queue ID.
  - **msg_ptr** : memory address of message buffer.
