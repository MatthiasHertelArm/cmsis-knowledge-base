---
id: "rtx-event-functions-evrrtxmessagequeuenotretrieved"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMessageQueueNotRetrieved"
summary: "The event MessageQueueNotRetrieved is generated when the function osMessageQueueGet is called without the wait timeout and there is no message available in queue."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMessageQueueNotRetrieved (osMessageQueueId_t mq_id, void *msg_ptr)
```


The event **MessageQueueNotRetrieved** is generated when the function osMessageQueueGet is called without the wait timeout and there is no message available in queue.

**Value** in the Event Recorder shows:
  - **mq_id** : message queue ID.
  - **msg_ptr** : memory address of buffer for message.
