---
id: "rtx-event-functions-evrrtxmessagequeuegetcapacity"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMessageQueueGetCapacity"
summary: "The event MessageQueueGetCapacity is generated when the function osMessageQueueGetCapacity is called and its execution result is known."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMessageQueueGetCapacity (osMessageQueueId_t mq_id, uint32_t capacity)
```


The event **MessageQueueGetCapacity** is generated when the function osMessageQueueGetCapacity is called and its execution result is known.

**Value** in the Event Recorder shows:
  - **mq_id** : message queue ID.
  - **capacity** : retrieved maximum number of messages (0 in case of a failure).
