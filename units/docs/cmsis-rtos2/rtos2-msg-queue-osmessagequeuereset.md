---
id: "rtos2-msg-queue-osmessagequeuereset"
type: "concept"
domain: "rtos"
title: "msg queue: osMessageQueueReset"
summary: "The function osMessageQueueReset resets the message queue specified by the parameter mqid."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_msg_queue.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_msg_queue.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osMessageQueueReset (osMessageQueueId_t mq_id)
```


The function **osMessageQueueReset** resets the message queue specified by the parameter _mq_id._

Possible osStatus_t return values:
 - **osOK:** the message queue has been rest.
 - **osErrorParameter:** parameter **mq_id** is `NULL` or invalid.
 - **osErrorResource:** the message queue is in an invalid state.
 - **osErrorISR:** **osMessageQueueReset** cannot be called from interrupt service routines.
 - **osErrorSafetyClass:** the calling thread safety class is lower than the safety class of the specified message queue.

**Note:** This function **cannot** be called from Interrupt Service Routines.
