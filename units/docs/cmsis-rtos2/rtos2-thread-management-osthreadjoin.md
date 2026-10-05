---
id: "rtos2-thread-management-osthreadjoin"
type: "concept"
domain: "rtos"
title: "Thread Management: osThreadJoin"
summary: "The function osThreadJoin waits for the thread specified by thread_id to terminate. If that thread has already terminated, then osThreadJoin returns immediately. The thread must be joinable. By default threads are created with the attribute osThreadDetached."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osThreadJoin (osThreadId_t thread_id)
```


The function **osThreadJoin** waits for the thread specified by **thread_id** to terminate. If that thread has already
terminated, then osThreadJoin returns immediately. The thread must be joinable. By default threads are created with the
attribute osThreadDetached.

Possible osStatus_t return values:
    - **osOK:** if the thread has already been terminated and joined or once the thread has been terminated and the join
      operations succeeds.
    - **osErrorParameter:** _thread_id_ is `NULL` or invalid.
    - **osErrorResource:** the thread is in an invalid state (ex: not joinable).
    - **osErrorISR:** the function **osThreadJoin** cannot be called from interrupt service routines.
    - **osErrorSafetyClass:** the calling thread safety class is lower than the safety class of the specified thread.

**Note:** This function **cannot** be called from Interrupt Service Routines. 

**Note:** Only one thread shall call **osThreadJoin** to join the target thread. If multiple threads try to join simultaneously with the same thread,
       the results are undefined.
