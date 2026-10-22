---
id: "rtos2-msg-queue-osmessagequeuenew"
type: "concept"
domain: "rtos"
title: "msg queue: osMessageQueueNew"
summary: "The function osMessageQueueNew creates and initializes a message queue object. The function returns a message queue object identifier or NULL in case of an error."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_msg_queue.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_msg_queue.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osMessageQueueId_t osMessageQueueNew (uint32_t msg_count, uint32_t msg_size, const osMessageQueueAttr_t *attr)
```


The function osMessageQueueNew creates and initializes a message queue object.
The function returns a message queue object identifier or `NULL` in case of an error. 

The function can be called after kernel initialization with osKernelInitialize. It is possible to 
create message queue objects before the RTOS kernel is started with osKernelStart.

The total amount of memory required for the message queue data is at least `msg_count * msg_size`.
The **msg_size** is rounded up to a double even number to ensure 32-bit alignment of the memory blocks.

The memory blocks allocated from the message queue have a fixed size defined with the parameter `msg_size.`

**Note:** This function **cannot** be called from Interrupt Service Routines.

**Code Example**

Refer to osMessageQueuePut
