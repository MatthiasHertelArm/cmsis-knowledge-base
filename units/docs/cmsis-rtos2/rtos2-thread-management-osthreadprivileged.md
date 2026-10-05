---
id: "rtos2-thread-management-osthreadprivileged"
type: "concept"
domain: "rtos"
title: "Thread Management: osThreadPrivileged"
summary: "Bitmask for a thread that runs in privileged mode. Intended for use in attr_bits of osThreadAttr_t type argument for osThreadNew function."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osThreadPrivileged
```


Bitmask for a thread that runs in privileged mode.
Intended for use in _attr_bits_ of osThreadAttr_t type argument for osThreadNew function.

In **privileged** processor mode, the application software can use all the instructions and has access to all resources.
