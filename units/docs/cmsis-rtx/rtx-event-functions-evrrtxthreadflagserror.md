---
id: "rtx-event-functions-evrrtxthreadflagserror"
type: "concept"
domain: "rtos"
title: "Event functions: EvrRtxThreadFlagsError"
summary: "The event ThreadFlagsError is generated when CMSIS_RTOS_ThreadFlagsMgmt routines complete their execution due to an error."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/ref_rtx_evr.txt"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/ref_rtx_evr.txt"
license: "Apache-2.0"
mode: "V"
---

```c
void EvrRtxThreadFlagsError (osThreadId_t thread_id, int32_t status)
```


The event **ThreadFlagsError** is generated when CMSIS_RTOS_ThreadFlagsMgmt routines complete their execution due to an error.

The status parameter indicates the execution status and can be one of the osStatus_t codes or one
of the extended execution status codes which are summarized in the table below.

|      Extended Status Code       | Description |
|:--------------------------------|:------------|
| osRtxErrorKernelNotReady        | Kernel scheduler is not in Ready state. |
| osRtxErrorKernelNotRunning      | Kernel scheduler is not executing - there is no running thread. |
| osRtxErrorInvalidControlBlock   | Object control block with invalid alignment or size was specified. |
| osRtxErrorInvalidDataMemory     | Object data memory with invalid alignment or size was specified. |
| osRtxErrorInvalidThreadStack    | Thread stack memory with invalid alignment or size was specified. |
| osRtxErrorInvalidPriority       | Invalid thread priority was specified. |
| osRtxErrorInvalidPrivilegedMode | Privileged thread cannot be created - kernel protect privileged is active. |
| osRtxErrorThreadNotJoinable     | Specified thread is not joinable. |
| osRtxErrorMutexNotOwned         | Specified mutex is not owned by the current running thread. |
| osRtxErrorMutexNotLocked        | Specified mutex is not locked. |
| osRtxErrorMutexLockLimit        | Maximum number of recursive mutex locks reached. |
| osRtxErrorSemaphoreCountLimit   | Semaphore count limit reached. |
| osRtxErrorTZ_InitContext_S      | Secure context memory system initialization failed. |
| osRtxErrorTZ_AllocContext_S     | Secure context memory allocation failed. |
| osRtxErrorTZ_FreeContext_S      | Secure context memory deallocation failed. |
| osRtxErrorTZ_LoadContext_S      | Secure context load failed. |
| osRtxErrorTZ_SaveContext_S      | Secure context save failed. |

**Value** in the Event Recorder shows:
  - **thread_id** : thread ID.
  - **status** : execution status code.
