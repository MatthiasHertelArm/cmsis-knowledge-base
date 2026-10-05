---
id: "rtos2-cmsis-rtos2-api-cmsis-rtos2-function-reference"
type: "concept"
domain: "rtos"
title: "CMSIS-RTOS2 API: CMSIS-RTOS2 Function Reference"
summary: "The following CMSIS-RTOS C API v2 functions can be called from threads and Interrupt Service Routines (ISR): - osKernelGetInfo, osKernelGetState, osKernelGetTickCount, osKernelGetTickFreq, osKernelGetSysTimerCount, osKernelGetSysTimerFreq - osThreadGetName, osThreadGetId, osThreadFlagsSet - osTimerGetName - osEventFlagsGetName, osEventFlagsSet, osEventFlagsClear, osEventFlagsGet, osEventFlagsWait - osMutexGetName …"
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_groups.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_groups.txt"
license: "Apache-2.0"
mode: "V"
---

- CMSIS_RTOS_KernelCtrl
   - osKernelGetInfo :  osKernelGetInfo
   - osKernelGetState :  osKernelGetState
   - osKernelGetSysTimerCount :  osKernelGetSysTimerCount
   - osKernelGetSysTimerFreq :  osKernelGetSysTimerFreq
   - osKernelInitialize :  osKernelInitialize
   - osKernelLock :  osKernelLock
   - osKernelUnlock :  osKernelUnlock
   - osKernelRestoreLock :  osKernelRestoreLock
   - osKernelResume :  osKernelResume
   - osKernelStart :  osKernelStart
   - osKernelSuspend :  osKernelSuspend
   - osKernelGetTickCount :  osKernelGetTickCount
   - osKernelGetTickFreq :  osKernelGetTickFreq
   - osKernelDestroyClass :  osKernelDestroyClass
   - osKernelProtect :  osKernelProtect
   - osFaultResume :  osFaultResume



 - CMSIS_RTOS_ThreadMgmt
   - osThreadDetach :  osThreadDetach
   - osThreadEnumerate :  osThreadEnumerate
   - osThreadExit :  osThreadExit
   - osThreadGetCount :  osThreadGetCount
   - osThreadGetId :  osThreadGetId
   - osThreadGetName :  osThreadGetName
   - osThreadGetPriority :  osThreadGetPriority
   - osThreadGetStackSize :  osThreadGetStackSize
   - osThreadGetStackSpace :  osThreadGetStackSpace
   - osThreadGetState :  osThreadGetState
   - osThreadJoin :  osThreadJoin
   - osThreadNew :  osThreadNew
   - osThreadResume :  osThreadResume
   - osThreadSetPriority :  osThreadSetPriority
   - osThreadSuspend :  osThreadSuspend
   - osThreadTerminate :  osThreadTerminate
   - osThreadYield :  osThreadYield
   - osThreadGetClass :  osThreadGetClass
   - osThreadGetZone :  osThreadGetZone
   - osThreadFeedWatchdog :  osThreadFeedWatchdog
   - osThreadProtectPrivileged :  osThreadProtectPrivileged
   - osThreadResumeClass :  osThreadResumeClass
   - osThreadSuspendClass :  osThreadSuspendClass
   - osThreadTerminateZone :  osThreadTerminateZone
   - osWatchdogAlarm_Handler :  osWatchdogAlarm_Handler
   - osZoneSetup_Callback :  osZoneSetup_Callback



 - CMSIS_RTOS_ThreadFlagsMgmt
   - osThreadFlagsSet :  osThreadFlagsSet
   - osThreadFlagsClear :  osThreadFlagsClear
   - osThreadFlagsGet :  osThreadFlagsGet
   - osThreadFlagsWait :  osThreadFlagsWait



 - CMSIS_RTOS_EventFlags
   - osEventFlagsGetName :  osEventFlagsGetName
   - osEventFlagsNew :  osEventFlagsNew
   - osEventFlagsDelete :  osEventFlagsDelete
   - osEventFlagsSet :  osEventFlagsSet
   - osEventFlagsClear :  osEventFlagsClear
   - osEventFlagsGet :  osEventFlagsGet
   - osEventFlagsWait :  osEventFlagsWait



 - CMSIS_RTOS_Wait
   - osDelay :  osDelay
   - osDelayUntil :  osDelayUntil



 - CMSIS_RTOS_TimerMgmt
   - osTimerDelete :  osTimerDelete
   - osTimerGetName :  osTimerGetName
   - osTimerIsRunning :  osTimerIsRunning
   - osTimerNew :  osTimerNew
   - osTimerStart :  osTimerStart
   - osTimerStop :  osTimerStop



 - CMSIS_RTOS_MutexMgmt
   - osMutexAcquire :  osMutexAcquire
   - osMutexDelete :  osMutexDelete
   - osMutexGetName :  osMutexGetName
   - osMutexGetOwner :  osMutexGetOwner
   - osMutexNew :  osMutexNew
   - osMutexRelease :  osMutexRelease



 - CMSIS_RTOS_SemaphoreMgmt
   - osSemaphoreAcquire :  osSemaphoreAcquire
   - osSemaphoreDelete :  osSemaphoreDelete
   - osSemaphoreGetCount :  osSemaphoreGetCount
   - osSemaphoreGetName :  osSemaphoreGetName
   - osSemaphoreNew :  osSemaphoreNew
   - osSemaphoreRelease :  osSemaphoreRelease



 - CMSIS_RTOS_PoolMgmt
   - osMemoryPoolAlloc :  osMemoryPoolAlloc
   - osMemoryPoolDelete :  osMemoryPoolDelete
   - osMemoryPoolFree :  osMemoryPoolFree
   - osMemoryPoolGetBlockSize :  osMemoryPoolGetBlockSize
   - osMemoryPoolGetCapacity :  osMemoryPoolGetCapacity
   - osMemoryPoolGetCount :  osMemoryPoolGetCount
   - osMemoryPoolGetName :  osMemoryPoolGetName
   - osMemoryPoolGetSpace :  osMemoryPoolGetSpace
   - osMemoryPoolNew :  osMemoryPoolNew



 - CMSIS_RTOS_Message
   - osMessageQueueDelete :  osMessageQueueDelete
   - osMessageQueueGet :  osMessageQueueGet
   - osMessageQueueGetCapacity :  osMessageQueueGetCapacity
   - osMessageQueueGetCount :  osMessageQueueGetCount
   - osMessageQueueGetMsgSize :  osMessageQueueGetMsgSize
   - osMessageQueueGetName :  osMessageQueueGetName
   - osMessageQueueGetSpace :  osMessageQueueGetSpace
   - osMessageQueueNew :  osMessageQueueNew
   - osMessageQueuePut :  osMessageQueuePut
   - osMessageQueueReset :  osMessageQueueReset
 
The following CMSIS-RTOS C API v2 functions can be called from threads and Interrupt Service Routines
(ISR):
   - osKernelGetInfo, osKernelGetState,
     osKernelGetTickCount, osKernelGetTickFreq, osKernelGetSysTimerCount, osKernelGetSysTimerFreq
   - osThreadGetName, osThreadGetId, osThreadFlagsSet
   - osTimerGetName
   - osEventFlagsGetName, osEventFlagsSet, osEventFlagsClear, osEventFlagsGet, osEventFlagsWait
   - osMutexGetName
   - osSemaphoreGetName, osSemaphoreAcquire, osSemaphoreRelease, osSemaphoreGetCount
   - osMemoryPoolGetName, osMemoryPoolAlloc, osMemoryPoolFree,
     osMemoryPoolGetCapacity, osMemoryPoolGetBlockSize, osMemoryPoolGetCount, osMemoryPoolGetSpace
   - osMessageQueueGetName, osMessageQueuePut, osMessageQueueGet, osMessageQueueGetCapacity,
     osMessageQueueGetMsgSize, osMessageQueueGetCount, osMessageQueueGetSpace
