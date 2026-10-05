---
id: "rtx-event-functions-evrrtxmessagequeuecreated"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMessageQueueCreated"
summary: "The event MessageQueueCreated is generated when the function osMessageQueueNew successfully creates a message queue object."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMessageQueueCreated (osMessageQueueId_t mq_id, const char *name)
```


The event **MessageQueueCreated** is generated when the function osMessageQueueNew successfully creates a message queue object.

**Value** in the Event Recorder shows:
  - **mq_id** : message queue ID.
