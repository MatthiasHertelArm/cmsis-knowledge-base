---
id: "cfrt-technical-data-and-limitations-validation-suite-results"
type: "concept"
domain: "rtos"
title: "Technical Data and Limitations: Validation Suite Results"
summary: "CMSIS provides a CMSIS-RTOS2 validation suite that can be used to test a real-time operating system for compliance to the standard. The test suite has been executed successfully on the CMSIS-FreeRTOS implementation (see results)."
status: "draft"
collection: "cmsis-freertos"
source: "ARM-software/CMSIS-FreeRTOS@c3e5dc3:Documentation/Doxygen/src/technical_data.md"
doc_source: "https://github.com/ARM-software/CMSIS-FreeRTOS/blob/c3e5dc3/Documentation/Doxygen/src/technical_data.md#validation-suite-results"
license: "Apache-2.0"
mode: "V"
---

CMSIS provides a [CMSIS-RTOS2 validation suite](https://arm-software.github.io/CMSIS_6/latest/RTOS2/rtosValidation.html) that can be used to test a real-time operating system for compliance to the standard. The test suite has been executed successfully on the CMSIS-FreeRTOS implementation ([see results](https://github.com/ARM-software/CMSIS-FreeRTOS/blob/c3e5dc3/Documentation/Doxygen/src/cmsis_rtos2_validation.txt)).

The following table explains the exceptions:

| Test Case                  | Result         | Reason               | Summary                                                                 |
|----------------------------|----------------|----------------------|-------------------------------------------------------------------------|
| TC_osKernelGetState_2      | not executed   | unsupported feature  | Test attempts to call `osKernelGetState` after a `osKernelSuspend` call. `osKernelSuspend` is not implemented. |
| TC_osKernelLock_2          | not executed   | unsupported feature  | Test attempts to call `osKernelLock` after a `osKernelSuspend` call. `osKernelSuspend` is not implemented. |
| TC_osKernelUnlock_2        | not executed   | unsupported feature  | Test attempts to call `osKernelUnlock` after a `osKernelSuspend` call. `osKernelSuspend` is not implemented. |
| TC_osKernelSuspend_1       | not executed   | unsupported feature  | Test validates `osKernelSuspend` which is not implemented. |
| TC_osKernelResume_1        | not executed   | unsupported feature  | Test validates `osKernelResume` which is not implemented. |
| TC_osThreadNew_3           | not executed   | unsupported feature  | Test attempts to create joinable thread using `osThreadJoinable` attribute. FreeRTOS does not support joinable threads. |
| TC_osThreadGetName_1       | failed         | deviation            | Test attempt to retrieve a name on an unnamed thread. An empty string is returned instead of NULL pointer. |
| TC_osThreadGetState_3      | not executed   | unsupported feature  | Test attempts to retrieve a state of a terminated joinable thread. FreeRTOS does not support joinable threads. |
| TC_osThreadDetach_1        | not executed   | unsupported feature  | Test validates `osThreadDetach` which is not implemented. |
| TC_osThreadDetach_2        | not executed   | unsupported feature  | Test validates `osThreadDetach` which is not implemented. |
| TC_osThreadJoin_1          | not executed   | unsupported feature  | Test validates `osThreadJoin` which is not implemented. |
| TC_osThreadJoin_2          | not executed   | unsupported feature  | Test validates `osThreadJoin` which is not implemented. |
| TC_osThreadJoin_3          | not executed   | unsupported feature  | Test validates `osThreadJoin` which is not implemented. |
| TC_osThreadGetStackSize_1  | not executed   | unsupported feature  | Test validates `osThreadGetStackSize` which is not implemented. |
| TC_ThreadReturn            | not executed   | unsupported feature  | Test attempts to terminate a thread by just returning from a thread. FreeRTOS threads may not return. |
| TC_osEventFlagsSet_1       | failed         | deviation            | Test attempts to set event flags by calling `osEventFlagsSet` multiple times without leaving ISR handler. To process ISR requests, FreeRTOS uses timer deamon which wakes-up after ISR execution. |
| TC_osEventFlagsClear_1     | failed         | deviation            | Test attempts to clear event flags by calling `osEventFlagsClear` multiple times without leaving ISR handler. To process ISR requests, FreeRTOS uses timer deamon which wakes-up after ISR execution. |
| TC_osEventFlagsWait_1      | failed         | unsupported feature  | Test attempts to wait for flags from ISR with zero timeout (try-semantic). FreeRTOS does not support such operation. |
| TC_osEventFlagsGetName_1   | not executed   | unsupported feature  | Test validates `osEventFlagsGetName` which is not implemented. |
| TC_osMutexNew_4            | not executed   | unsupported feature  | Test attempts to create a robust mutex. FreeRTOS implementation does not support robust mutexes. |
| TC_osMutexGetName_1        | not executed   | unsupported feature  | Test validates `osMutexGetName` which is not implemented. |
| TC_MutexRobust             | not executed   | unsupported feature  | Test attempts to validate robust mutex behavior. FreeRTOS implementation does not support robust mutexes. |
| TC_MutexOwnership          | not executed   | unsupported feature  | Test attempts to release a mutex from a thread which is not the mutex owner. FreeRTOS implementation does not verify ownership on mutex release. |
| TC_osSemaphoreGetName_1    | not executed   | unsupported feature  | Test validates `osSemaphoreGetName` which is not implemented. |
| TC_osMessageQueueGetName_1 | not executed   | unsupported feature  | Test validates `osMessageQueueGetName` which is not implemented. |
