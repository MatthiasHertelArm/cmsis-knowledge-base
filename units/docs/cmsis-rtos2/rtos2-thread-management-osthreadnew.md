---
id: "rtos2-thread-management-osthreadnew"
type: "concept"
domain: "rtos"
title: "Thread Management: osThreadNew"
summary: "The function osThreadNew starts a thread function by adding it to the list of active threads and sets it to state READY. Arguments for the thread function are passed using the parameter pointer argument."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osThreadId_t osThreadNew (osThreadFunc_t func, void *argument, const osThreadAttr_t *attr)
```


The function **osThreadNew** starts a thread function by adding it to the list of active threads and sets it to state
READY. Arguments for the thread function are passed using the parameter pointer _*argument._ When the priority of the
created thread function is higher than the current RUNNING thread, the created thread function starts instantly and
becomes the new RUNNING thread. Thread attributes are defined with the parameter pointer _attr._ Attributes include
settings for thread priority, stack size, or memory allocation.

The function can be safely called before the RTOS is
started (call to osKernelStart), but not before it is initialized (call to osKernelInitialize).

The function **osThreadNew** returns the pointer to the thread object identifier or `NULL` in case of an error.

**Note:** Cannot be called from Interrupt Service Routines.

**Code** **Example**

Refer to the Thread Examples section.
