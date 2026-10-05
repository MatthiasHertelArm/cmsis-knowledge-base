---
id: "rtos2-msg-queue-osmessagequeuegetname"
type: "concept"
domain: "rtos"
title: "msg queue: osMessageQueueGetName"
summary: "The function osMessageQueueGetName returns the pointer to the name string of the message queue identified by parameter \\a mqid or NULL in case of an error."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_msg_queue.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_msg_queue.txt"
license: "Apache-2.0"
mode: "V"
---

```c
const char *osMessageQueueGetName (osMessageQueueId_t mq_id)
```


The function **osMessageQueueGetName** returns the pointer to the name string of the message queue identified by parameter \a
mq_id or `NULL` in case of an error.

**Note:** This function may be called from Interrupt Service Routines.
