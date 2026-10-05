---
id: "rtos2-msg-queue-mq-size"
type: "concept"
domain: "rtos"
title: "msg queue: mq_size"
summary: "The size (in bytes) of memory block passed with mq_mem. The minimum memory block size is msg_count  msg_size (parameters of the osMessageQueueNew function)."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_msg_queue.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_msg_queue.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osMessageQueueAttr_t::mq_size
```


The size (in bytes) of memory block passed with mq_mem. The minimum memory block size is `msg_count * msg_size` (parameters of the osMessageQueueNew function). The **msg_size** is rounded up to a double even number to ensure 32-bit alignment of the memory blocks.

Default: 0 as the default is no memory provided with mq_mem.
