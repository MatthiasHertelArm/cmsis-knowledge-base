---
id: "rtx-event-functions-evrrtxmessagequeuegetmsgsize"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMessageQueueGetMsgSize"
summary: "The event MessageQueueGetMsgSize is generated when the function osMessageQueueGetMsgSize is called and its execution result is known."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMessageQueueGetMsgSize (osMessageQueueId_t mq_id, uint32_t msg_size)
```


The event **MessageQueueGetMsgSize** is generated when the function osMessageQueueGetMsgSize is called and its execution result is known.

**Value** in the Event Recorder shows:
  - **mq_id** : message queue ID.
  - **msg_size** : retrieved maximum message size in bytes (0 in case of a failure).
