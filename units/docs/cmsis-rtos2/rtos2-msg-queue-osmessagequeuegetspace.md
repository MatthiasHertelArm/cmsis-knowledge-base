---
id: "rtos2-msg-queue-osmessagequeuegetspace"
type: "concept"
domain: "rtos"
title: "msg queue: osMessageQueueGetSpace"
summary: "The function osMessageQueueGetSpace returns the number available slots for messages in the message queue object specified by parameter mq_id or 0 in case of an error."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_msg_queue.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_msg_queue.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t osMessageQueueGetSpace (osMessageQueueId_t mq_id)
```


The function **osMessageQueueGetSpace** returns the number available slots for messages in the message queue object specified
by parameter _mq_id_ or `0` in case of an error.

**Note:** This function may be called from Interrupt Service Routines.
