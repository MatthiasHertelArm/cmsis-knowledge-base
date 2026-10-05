---
id: "rtos2-using-cmsis-rtos2-interface-functionality-overview"
type: "concept"
domain: "rtos"
title: "Using CMSIS-RTOS2 Interface: Functionality overview"
summary: "The CMSIS-RTOS2 defines APIs for common RTOS services as listed below:"
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/using.md"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/using.md#functionality-overview"
license: "Apache-2.0"
mode: "V"
---

The CMSIS-RTOS2 defines APIs for common RTOS services as listed below:

 - CMSIS_RTOS_KernelCtrl provides system information and controls the RTOS Kernel.
 - CMSIS_RTOS_ThreadMgmt allows you to define, create, and control RTOS threads (tasks).
 - CMSIS_RTOS_Wait for controlling time delays. Also see CMSIS_RTOS_TimeOutValue.
 - CMSIS_RTOS_TimerMgmt functions are used to trigger the execution of functions.
 - Three different event types support communication between multiple threads and/or ISR:
   - Thread Flags: may be used to indicate specific conditions to a thread.
   - Event Flags: may be used to indicate events to a thread or ISR.
   - Messages: can be sent to a thread or an ISR. Messages are buffered in a queue.
 - CMSIS_RTOS_MutexMgmt and CMSIS_RTOS_SemaphoreMgmt are incorporated.

The referenced pages contain theory of operation for corresponding services as well as detailed API description with example code.
