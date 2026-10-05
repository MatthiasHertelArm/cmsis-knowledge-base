---
id: "rtos2-thread-management-osthreadsuspend"
type: "concept"
domain: "rtos"
title: "Thread Management: osThreadSuspend"
summary: "The function osThreadSuspend suspends the execution of the thread identified by parameter threadid. The thread is put into the BLOCKED state (osThreadBlocked). Suspending the running thread will cause a context switch to another thread in READY state immediately."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osThreadSuspend (osThreadId_t thread_id)
```


The function **osThreadSuspend** suspends the execution of the thread identified by parameter **thread_id.** The thread is put
into the BLOCKED state (osThreadBlocked). Suspending the running thread will cause a context switch to another
thread in READY state immediately. The suspended thread is not executed until explicitly resumed with the function osThreadResume. 

Threads that are already BLOCKED are removed from any wait list and become ready when they are resumed.
Thus it is not recommended to suspend an already blocked thread.

Possible osStatus_t return values:
    - **osOK:** the thread has been suspended successfully.
    - **osErrorParameter:** _thread_id_ is `NULL` or invalid.
    - **osErrorResource:** the thread is in an invalid state.
    - **osErrorISR:** the function **osThreadSuspend** cannot be called from interrupt service routines.
    - **osErrorSafetyClass:** the calling thread safety class is lower than the safety class of the specified thread.

**Note:** This function **cannot** be called from Interrupt Service Routines.
**Note:** This function **must not** be called to suspend the running thread when the kernel is locked, i.e. osKernelLock.
