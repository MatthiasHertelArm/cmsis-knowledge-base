---
id: "rtx-event-functions-evrrtxmessagequeueinsertpending"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMessageQueueInsertPending"
summary: "The event MessageQueueInsertPending is generated when the function osMessageQueuePut is called from ISR and message is registered to be put into the queue."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMessageQueueInsertPending (osMessageQueueId_t mq_id, const void *msg_ptr)
```


The event **MessageQueueInsertPending** is generated when the function osMessageQueuePut is called from ISR and message is registered to be put into the queue. 

**Value** in the Event Recorder shows:
  - **mq_id** : message queue ID.
  - **msg_ptr** : memory address of message buffer.
