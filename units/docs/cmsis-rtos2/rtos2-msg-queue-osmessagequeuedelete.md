---
id: "rtos2-msg-queue-osmessagequeuedelete"
type: "concept"
domain: "rtos"
title: "msg queue: osMessageQueueDelete"
summary: "The function osMessageQueueDelete deletes a message queue object specified by parameter mq_id. It releases internal memory obtained for message queue handling. After this call, the mq_id is no longer valid and cannot be used."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_msg_queue.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_msg_queue.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osMessageQueueDelete (osMessageQueueId_t mq_id)
```


The function **osMessageQueueDelete** deletes a message queue object specified by parameter _mq_id._ It releases internal
memory obtained for message queue handling. After this call, the _mq_id_ is no longer valid and cannot be used. The
message queue may be created again using the function osMessageQueueNew.

Possible osStatus_t return values:
 - **osOK:** the message queue object has been deleted.
 - **osErrorParameter:** parameter **mq_id** is `NULL` or invalid.
 - **osErrorResource:** the message queue is in an invalid state.
 - **osErrorISR:** **osMessageQueueDelete** cannot be called from interrupt service routines.
 - **osErrorSafetyClass:** the calling thread safety class is lower than the safety class of the specified message queue.

**Note:** This function **cannot** be called from Interrupt Service Routines.
