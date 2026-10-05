---
id: "rtx-event-functions-evrrtxmessagequeueputpending"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMessageQueuePutPending"
summary: "The event MessageQueuePutPending is generated when the function osMessageQueuePut starts waiting to put message into the queue."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMessageQueuePutPending (osMessageQueueId_t mq_id, const void *msg_ptr, uint32_t timeout)
```


The event **MessageQueuePutPending** is generated when the function osMessageQueuePut starts waiting to put message into the queue.

**Value** in the Event Recorder shows:
  - **mq_id** : message queue ID.
  - **msg_ptr** : memory address of message buffer.
  - **timeout** : CMSIS_RTOS_TimeOutValue.
