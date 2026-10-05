---
id: "rtos2-msg-queue-cb-mem"
type: "concept"
domain: "rtos"
title: "msg queue: cb_mem"
summary: "Pointer to a memory for the message queue control block object. Refer to CMSISRTOSMemoryMgmtManual for more information."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_msg_queue.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_msg_queue.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osMessageQueueAttr_t::cb_mem
```


Pointer to a memory for the message queue control block object. Refer to CMSIS_RTOS_MemoryMgmt_Manual for more information.

Default: `NULL` to use CMSIS_RTOS_MemoryMgmt_Automatic for the message queue control block.
