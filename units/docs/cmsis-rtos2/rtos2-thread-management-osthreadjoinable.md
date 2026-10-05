---
id: "rtos2-thread-management-osthreadjoinable"
type: "concept"
domain: "rtos"
title: "Thread Management: osThreadJoinable"
summary: "Bitmask for a thread that can be joined. Intended for use in attrbits of osThreadAttrt type argument for osThreadNew function."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osThreadJoinable
```


Bitmask for a thread that can be joined.
Intended for use in _attr_bits_ of osThreadAttr_t type argument for osThreadNew function.

A thread in this state can be joined using osThreadJoin.
