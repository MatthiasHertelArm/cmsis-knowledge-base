---
id: "rtos2-msg-queue-osmessagequeueget"
type: "concept"
domain: "rtos"
title: "msg queue: osMessageQueueGet"
summary: "The function osMessageQueueGet retrieves a message from the message queue specified by the parameter mqid and saves it to the buffer pointed to by the parameter msgptr. The message priority is stored to parameter msgprio if not token{NULL}."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_msg_queue.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_msg_queue.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osMessageQueueGet (osMessageQueueId_t mq_id, void *msg_ptr, uint8_t *msg_prio, uint32_t timeout)
```


The function **osMessageQueueGet** retrieves a message from the message queue specified by the parameter _mq_id_ and saves it
to the buffer pointed to by the parameter _msg_ptr._ The message priority is stored to parameter _msg_prio_ if not token{NULL}.

The parameter _timeout_ specifies how long the system waits to retrieve the message from the queue. While the system waits,
the thread that is calling this function is put into the BLOCKED state. The parameter
timeout can have the following values:
 - when _timeout_ is `0`, the function returns instantly (i.e. try semantics).
 - when _timeout_ is set to **osWaitForever** the function will wait for an infinite time until the message is retrieved (i.e. wait semantics).
 - all other values specify a time in kernel ticks for a timeout (i.e. timed-wait semantics).

Possible osStatus_t return values:
 - **osOK:** the message has been retrieved from the queue.
 - **osErrorTimeout:** the message could not be retrieved from the queue in the given time (timed-wait semantics).
 - **osErrorResource:** nothing to get from the queue (try semantics).
 - **osErrorParameter:** parameter **mq_id** is `NULL` or invalid, non-zero timeout specified in an ISR.
 - **osErrorSafetyClass:** the calling thread safety class is lower than the safety class of the specified message queue.

**Note:** May be called from Interrupt Service Routines if the parameter _timeout_ is set to
`0`.

**Code Example**

Refer to osMessageQueuePut
