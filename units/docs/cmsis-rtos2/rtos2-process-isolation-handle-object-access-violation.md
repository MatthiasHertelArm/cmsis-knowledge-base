---
id: "rtos2-process-isolation-handle-object-access-violation"
type: "concept"
domain: "rtos"
title: "Process Isolation: Handle Object Access Violation"
summary: "RTOS API call returns error code osErrorSafetyClass if the requested object manipulation cannot be performed because the target object has higher safety class than the safety class of the running thread. For example:"
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/processIsolation.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/processIsolation.md#handle-object-access-violation"
license: "Apache-2.0"
mode: "V"
---

RTOS API call returns error code osErrorSafetyClass if the requested object manipulation cannot be performed because the target object has higher safety class than the safety class of the running thread. For example:

```c
status = osEventFlagsSet(evt_flags, 1);
if (status == osErrorSafetyClass)
{
  //handle the safety class error
}
```

Following functions compare the safety class of the running thread with the safety class of the target object.

In CMSIS_RTOS_KernelCtrl functions:

Comparison is done with safety class configured with osKernelProtect

 - osKernelLock
 - osKernelRestoreLock
 - osKernelSuspend
 - osKernelProtect
 - osKernelDestroyClass

In CMSIS_RTOS_ThreadMgmt functions:

 - osThreadNew
 - osThreadSetPriority
 - osThreadSuspend
 - osThreadResume
 - osThreadDetach
 - osThreadJoin
 - osThreadTerminate
 - osThreadSuspendClass
 - osThreadResumeClass

In CMSIS_RTOS_ThreadFlagsMgmt functions:

 - osThreadFlagsSet

In CMSIS_RTOS_EventFlags functions:

 - osEventFlagsNew
 - osEventFlagsSet
 - osEventFlagsClear
 - osEventFlagsWait
 - osEventFlagsDelete

In CMSIS_RTOS_TimerMgmt functions:

 - osTimerNew
 - osTimerStart
 - osTimerStop
 - osTimerDelete

In CMSIS_RTOS_MutexMgmt functions:

 - osMutexNew
 - osMutexAcquire
 - osMutexDelete

In CMSIS_RTOS_SemaphoreMgmt functions:

 - osSemaphoreNew
 - osSemaphoreAcquire
 - osSemaphoreRelease
 - osSemaphoreDelete

In CMSIS_RTOS_PoolMgmt functions:

 - osMemoryPoolNew
 - osMemoryPoolAlloc
 - osMemoryPoolFree
 - osMemoryPoolDelete

In CMSIS_RTOS_Message functions:

 - osMessageQueueNew
 - osMessageQueuePut
 - osMessageQueueGet
 - osMessageQueueReset
 - osMessageQueueDelete

<!-- =============================================================== !-->
# Thread Watchdogs

CMSIS-RTOS defines **Thread Watchdogs** that allow to control timing constraints for thread execution [temporal isolation](https://en.wikipedia.org/wiki/Temporal_isolation).

Each thread has an independent watchdog timer that is started with the function osThreadFeedWatchdog(uint32_t ticks). The `ticks` value specifies the timeout before it expires.  Within this time interval the function osThreadFeedWatchdog must be called again within the thread to restart the watchdog timer.

If the thread watchdog is not restarted during the specified amount of ticks the Watchdog Alarm  callback osWatchdogAlarm_Handler(osThreadId_t thread_id) is triggered and can be used to recover the system or proceed to the system shutdown.

Figure below explains the concept with an example:

(figure: Example use of Thread Watchdogs)

rtos_process_isolation_faults provides more details on the available possibilities for system recovery.

> **Note**
> - If the application suspends a thread from scheduling by calling osThreadSuspend or osThreadSuspendClass, the thread watchdog still continues to run, and it is expected to expire and trigger osWatchdogAlarm_Handler because the thread will not be serviced as expected.
> - Hence it may be necessary to differentiate handling of thread watchdogs that expired unexpectedly from the thread watchdog alarms of intentionally suspended threads.

**Function references**

Summary of functions that implement thread watchdog functionality:

 - osThreadFeedWatchdog :  osThreadFeedWatchdog
 - osWatchdogAlarm_Handler :  osWatchdogAlarm_Handler

<!-- =============================================================== !-->
# Fault Handling

When a failure, or an error is detected in a system (for example memory access fault, thread watchdog alarm, or others) CMSIS-RTOS2 API allows to stop further execution of selected RTOS threads. This can be used to block malfunctioning components or free computing resources and so enable execution of the safety critical threads. 

Following approaches are available:

 - function osThreadTerminateZone can be called in case of a fault exception. It will terminate all threads from the specified MPU Protected Zone (for example, can be the zone that has caused the fault). The function cannot be called in thread context or interrupts other than faults. Note that osFaultResume can be called at the end of the handling code to return program execution into a known context and let kernel schedule the next thread ready for execution.
 - function osThreadSuspendClass can be called in case of a thread watchdog alarm or other errors handled in thread context. It allows to suspend operation of threads based on the safety class assignment. Function osThreadResumeClass can be used to resume operation of threads based on their safety class. rtos_process_isolation_thread_wdt contains an example that demonstrates fault handling concept for thread watchdogs.

Function osKernelDestroyClass fully removes RTOS objects of specific safety classes from the system. This can be useful to do before restarting operation of terminated or suspended threads.

**Function references**

Following CMSIS-RTOS2 functions and macros support fault handling:

 - osThreadGetZone :  osThreadGetZone
 - osThreadTerminateZone :  osThreadTerminateZone
 - osThreadGetClass :  osThreadGetClass
 - osSafetyWithSameClass :  osSafetyWithSameClass
 - osSafetyWithLowerClass :  osSafetyWithLowerClass
 - osThreadSuspendClass :  osThreadSuspendClass
 - osThreadResumeClass :  osThreadResumeClass
 - osKernelDestroyClass :  osKernelDestroyClass
 - osFaultResume :  osFaultResume
 - osWatchdogAlarm_Handler :  osFaultResume
