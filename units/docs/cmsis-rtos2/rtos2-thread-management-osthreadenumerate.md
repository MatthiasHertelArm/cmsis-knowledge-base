---
id: "rtos2-thread-management-osthreadenumerate"
type: "concept"
domain: "rtos"
title: "Thread Management: osThreadEnumerate"
summary: "The function osThreadEnumerate returns the number of enumerated threads or 0 in case of an error."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t osThreadEnumerate (osThreadId_t *thread_array, uint32_t array_items)
```


The function **osThreadEnumerate** returns the number of enumerated threads or `0` in case of an error.

**Note:** This function **cannot** be called from Interrupt Service Routines.
