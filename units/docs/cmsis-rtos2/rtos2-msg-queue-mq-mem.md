---
id: "rtos2-msg-queue-mq-mem"
type: "concept"
domain: "rtos"
title: "msg queue: mq_mem"
summary: "Pointer to a memory for the message queue data. Refer to CMSIS_RTOS_MemoryMgmt_Manual for more information."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_msg_queue.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_msg_queue.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osMessageQueueAttr_t::mq_mem
```


Pointer to a memory for the message queue data. Refer to CMSIS_RTOS_MemoryMgmt_Manual for more information.

Default: `NULL` to use CMSIS_RTOS_MemoryMgmt_Automatic for the memory pool data.
