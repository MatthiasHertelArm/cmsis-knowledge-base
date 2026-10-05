---
id: "rtos2-thread-management-osthreaddetach"
type: "concept"
domain: "rtos"
title: "Thread Management: osThreadDetach"
summary: "The function osThreadDetach changes the attribute of a thread (specified by thread_id) to osThreadDetached. Detached threads are not joinable with osThreadJoin. When a detached thread is terminated, all resources are returned to the system."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osThreadDetach (osThreadId_t thread_id)
```


The function **osThreadDetach** changes the attribute of a thread (specified by **thread_id)** to osThreadDetached.
Detached threads are not joinable with osThreadJoin. When a detached thread is terminated, all resources are returned to
the system. The behavior of osThreadDetach on an already detached thread is undefined.

Possible osStatus_t return values:
    - **osOK:** the attribute of the specified thread has been changed to detached successfully.
    - **osErrorParameter:** _thread_id_ is `NULL` or invalid.
    - **osErrorResource:** the thread is in an invalid state.
    - **osErrorISR:** the function **osThreadDetach** cannot be called from interrupt service routines.
    - **osErrorSafetyClass:** the calling thread safety class is lower than the safety class of the specified thread.

**Note:** This function **cannot** be called from Interrupt Service Routines.
