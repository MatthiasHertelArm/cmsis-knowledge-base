---
id: "rtos2-thread-flags-osthreadflagsget"
type: "concept"
domain: "rtos"
title: "Thread Flags: osThreadFlagsGet"
summary: "The function osThreadFlagsGet returns the flags currently set for the currently running thread. If called without a active and currently running thread osThreadFlagsGet return zero."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread_flags.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread_flags.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t osThreadFlagsGet (void)
```


The function **osThreadFlagsGet** returns the flags currently set for the currently running thread. 
If called without a active and currently running thread **osThreadFlagsGet** return zero.

**Note:** This function **cannot** be called from Interrupt Service Routines.
