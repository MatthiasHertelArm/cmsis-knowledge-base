---
id: "rtx-event-functions-evrrtxmessagequeuegetpending"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMessageQueueGetPending"
summary: "The event MessageQueueGetPending is generated when the function osMessageQueueGet starts waiting for message to be retrieved from the queue."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMessageQueueGetPending (osMessageQueueId_t mq_id, void *msg_ptr, uint32_t timeout)
```


The event **MessageQueueGetPending** is generated when the function osMessageQueueGet starts waiting for message to be retrieved from the queue.

**Value** in the Event Recorder shows:
  - **mq_id** : message queue ID.
  - **msg_ptr** : memory address of buffer for message.
  - **timeout** : CMSIS_RTOS_TimeOutValue.
