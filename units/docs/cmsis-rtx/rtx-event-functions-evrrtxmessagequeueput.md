---
id: "rtx-event-functions-evrrtxmessagequeueput"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMessageQueuePut"
summary: "The event MessageQueuePut is generated when the function osMessageQueuePut is called."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMessageQueuePut (osMessageQueueId_t mq_id, const void *msg_ptr, uint8_t msg_prio, uint32_t timeout)
```


The event **MessageQueuePut** is generated when the function osMessageQueuePut is called.

**Value** in the Event Recorder shows:
  - **mq_id** : message queue ID.
  - **msg_ptr** : memory address of message buffer.
  - **msg_prio** : message priority.
  - **timeout** : CMSIS_RTOS_TimeOutValue.
