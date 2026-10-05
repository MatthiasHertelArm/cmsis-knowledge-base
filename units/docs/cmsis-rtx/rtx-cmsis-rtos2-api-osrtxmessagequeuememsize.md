---
id: "rtx-cmsis-rtos2-api-osrtxmessagequeuememsize"
type: "concept"
domain: "rtos"
title: "CMSIS-RTOS2 API: osRtxMessageQueueMemSize"
summary: "This macro exposes the minimum amount of memory needed for an RTX5 Message Queue Memory, see osMessageQueueAttrt::mqmem and osMessageQueueAttrt::mqsize."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_os.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_os.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osRtxMessageQueueMemSize
```

 Message Queue Memory size

This macro exposes the minimum amount of memory needed for an RTX5 Message Queue Memory,
see osMessageQueueAttr_t::mq_mem and osMessageQueueAttr_t::mq_size.

Example:
```
// Maximum number of messages
#define MSG_COUNT 16U
 
// Message data type
typedef struct {
   uint32_t value1;
   uint8_t  value2;
} msg_item_t;
 
// Used-defined memory for message queue
static uint32_t mq_mem[osRtxMessageQueueMemSize(MSG_COUNT, sizeof(msg_item_t))/4U];
```
