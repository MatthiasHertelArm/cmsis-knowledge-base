---
id: "rtos2-thread-management-osthreadunprivileged"
type: "concept"
domain: "rtos"
title: "Thread Management: osThreadUnprivileged"
summary: "Bitmask for a thread that runs in unprivileged mode. Intended for use in attr_bits of osThreadAttr_t type argument for osThreadNew function."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osThreadUnprivileged
```


Bitmask for a thread that runs in unprivileged mode.
Intended for use in _attr_bits_ of osThreadAttr_t type argument for osThreadNew function.

In **unprivileged** processor mode, a thread:
- has limited access to the MSR and MRS instructions, and cannot use the CPS instruction.
- cannot access the system timer, NVIC, or system control block.
- might have restricted access to memory or peripherals.

**Note:** Ignored on processors that only run in privileged mode.

Refer to the target processor User's Guide for details.
