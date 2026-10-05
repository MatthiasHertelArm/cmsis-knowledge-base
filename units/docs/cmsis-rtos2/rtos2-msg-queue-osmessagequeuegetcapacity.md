---
id: "rtos2-msg-queue-osmessagequeuegetcapacity"
type: "concept"
domain: "rtos"
title: "msg queue: osMessageQueueGetCapacity"
summary: "The function osMessageQueueGetCapacity returns the maximum number of messages in the message queue object specified by parameter mqid or 0 in case of an error."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_msg_queue.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_msg_queue.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t osMessageQueueGetCapacity (osMessageQueueId_t mq_id)
```


The function **osMessageQueueGetCapacity** returns the maximum number of messages in the message queue object specified by
parameter _mq_id_ or `0` in case of an error.

**Note:** This function may be called from Interrupt Service Routines.
