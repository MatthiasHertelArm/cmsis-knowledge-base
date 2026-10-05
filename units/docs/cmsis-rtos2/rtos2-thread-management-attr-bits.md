---
id: "rtos2-thread-management-attr-bits"
type: "concept"
domain: "rtos"
title: "Thread Management: attr_bits"
summary: "The following bit masks can be used to set options: - osThreadDetached : create thread in a detached mode (default). - osThreadJoinable : create thread in joinable mode. - osThreadUnprivileged : create thread to execute in unprivileged mode."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osThreadAttr_t::attr_bits
```


The following bit masks can be used to set options:
 - osThreadDetached : create thread in a detached mode (default).
 - osThreadJoinable : create thread in joinable mode.  
 - osThreadUnprivileged : create thread to execute in unprivileged mode.
 - osThreadPrivileged : create thread to execute in privileged mode.  
 - osThreadZone (m) : create thread assigned to MPU zone `m`.
 - osSafetyClass (n) : create thread with safety class `n` assigned to it.

Default: `0` no options set. Safety class and MPU Zone are inherited from running thread. Thread privilege mode is set based on configuration threadConfig_procmode.
