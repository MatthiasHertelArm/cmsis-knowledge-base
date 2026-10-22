---
id: "rtos2-thread-flags-osthreadflagsclear"
type: "concept"
domain: "rtos"
title: "Thread Flags: osThreadFlagsClear"
summary: "The function osThreadFlagsClear clears the specified flags for the currently running thread. It returns the flags before clearing, or an error code if highest bit is set (refer to flags_error_codes)."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread_flags.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread_flags.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t osThreadFlagsClear (uint32_t flags)
```


The function **osThreadFlagsClear** clears the specified flags for the currently running thread. It returns the
flags before clearing, or an error code if highest bit is set (refer to flags_error_codes).

Possible flags_error_codes return values:
    - **osFlagsErrorUnknown:** unspecified error, i.e. not called from a running threads context.
    - **osFlagsErrorParameter:** parameter **flags** has highest bit set.
    - **osFlagsErrorISR:** the function **osThreadFlagsClear** cannot be called from interrupt service routines.

**Note:** This function **cannot** be called from Interrupt Service Routines.
