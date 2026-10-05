---
id: "rtx-event-functions-evrrtxmessagequeuegetname"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxMessageQueueGetName"
summary: "The event MessageQueueGetName is generated when the function osMessageQueueGetName is called and its execution result is known."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxMessageQueueGetName (osMessageQueueId_t mq_id, const char *name)
```


The event **MessageQueueGetName** is generated when the function osMessageQueueGetName is called and its execution result is known.

**Value** in the Event Recorder shows:
  - **mq_id** : message queue ID.
  - **name** : retrieved memory address of name string (0 in case of a failure).
