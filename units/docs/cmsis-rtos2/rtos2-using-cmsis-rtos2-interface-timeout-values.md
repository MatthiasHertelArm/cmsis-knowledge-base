---
id: "rtos2-using-cmsis-rtos2-interface-timeout-values"
type: "concept"
domain: "rtos"
title: "Using CMSIS-RTOS2 Interface: Timeout Values"
summary: "Timeout value is an argument in many API functions that allows to set the maximum time delay for resolving a request. The timeout value specifies the number of timer ticks until the time delay elapses."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/using.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/using.md#timeout-values"
license: "Apache-2.0"
mode: "V"
---

Timeout value is an argument in many API functions that allows to set the maximum time delay for resolving a request. The timeout value specifies the number of timer ticks until the time delay elapses. The value is an upper bound and depends on the actual time elapsed since the last timer tick.

Examples:

 - timeout value **0** : the system does not wait, even when no resource is available the RTOS function returns instantly. 
 - timeout value **1** : the system waits until the next timer tick occurs; depending on the previous timer tick, it may be a very short wait time.
 - timeout value **2** : actual wait time is between 1 and 2 timer ticks.
 - timeout value osWaitForever : system waits infinite until a resource becomes available. Or one forces the thread to resume using osThreadResume which is discouraged.

(figure: Example of timeout using osDelay())

 - CPU time can be scheduled with the following functionalities:
   - A _timeout_ parameter is incorporated in many CMSIS-RTOS2 functions to avoid system lockup. When a timeout is specified, the system waits until a resource is available or an event occurs. While waiting, other threads are scheduled.
   - The osDelay and osDelayUntil functions put a thread into the **WAITING** state for a specified period of time.
   - The osThreadYield provides co-operative thread switching and passes execution to another thread of the same priority.
