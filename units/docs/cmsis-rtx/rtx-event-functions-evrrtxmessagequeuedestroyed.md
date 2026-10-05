---
id: "rtx-event-functions-evrrtxmessagequeuedestroyed"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMessageQueueDestroyed"
summary: "The event MessageQueueDestroyed is generated when the function osMessageQueueDelete successfully deletes the message queue object."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMessageQueueDestroyed (osMessageQueueId_t mq_id)
```


The event **MessageQueueDestroyed** is generated when the function osMessageQueueDelete successfully deletes the message queue object.

**Value** in the Event Recorder shows:
  - **mq_id** : message queue ID.
