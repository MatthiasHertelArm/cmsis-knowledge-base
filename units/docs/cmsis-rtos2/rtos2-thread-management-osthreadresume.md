---
id: "rtos2-thread-management-osthreadresume"
type: "concept"
domain: "rtos"
title: "Thread Management: osThreadResume"
summary: "The function osThreadResume puts the thread identified by parameter threadid (which has to be in BLOCKED state) back to the READY state. If the resumed thread has a higher priority than the running thread a context switch occurs immediately."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osThreadResume (osThreadId_t thread_id)
```


The function **osThreadResume** puts the thread identified by parameter **thread_id** (which has to be in BLOCKED state)
back to the READY state. If the resumed thread has a higher priority than the running thread a context switch occurs immediately.

The thread becomes ready regardless of the reason why the thread was blocked. Thus it is not recommended to resume a thread not suspended
by osThreadSuspend.

Functions that will put a thread into BLOCKED state are:
osEventFlagsWait and osThreadFlagsWait,
osDelay and osDelayUntil,
osMutexAcquire and osSemaphoreAcquire,
osMessageQueueGet,
osMemoryPoolAlloc,
osThreadJoin,
osThreadSuspend.

Possible osStatus_t return values:
    - **osOK:** the thread has been resumed successfully.
    - **osErrorParameter:** _thread_id_ is `NULL` or invalid.
    - **osErrorResource:** the thread is in an invalid state.
    - **osErrorISR:** the function **osThreadResume** cannot be called from interrupt service routines.
    - **osErrorSafetyClass:** the calling thread safety class is lower than the safety class of the specified thread.

**Note:** This function **cannot** be called from Interrupt Service Routines.
**Note:** This function **may be** called when kernel is locked (osKernelLock). Under this circumstances
	a potential context switch is delayed until the kernel gets unlocked, i.e. osKernelUnlock or osKernelRestoreLock.
