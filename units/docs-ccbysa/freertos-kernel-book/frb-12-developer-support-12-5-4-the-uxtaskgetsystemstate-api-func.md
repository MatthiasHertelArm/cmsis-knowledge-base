---
id: "frb-12-developer-support-12-5-4-the-uxtaskgetsystemstate-api-func"
type: "concept"
domain: "rtos"
title: "12 Developer Support: 12.5 Viewing Run-time and Task State Information / 12.5.4 The uxTaskGetSystemState() API Function"
summary: "Part of: 12.5 Viewing Run-time and Task State Information"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch12.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch12.md#12-5-4-the-uxtaskgetsystemstate-api-function"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 12.5 Viewing Run-time and Task State Information_

`uxTaskGetSystemState()` provides a snapshot of status information for
each task under the control of the FreeRTOS scheduler. The information
is provided as an array of `TaskStatus_t` structures, with one index in
the array for each task. `TaskStatus_t` is described by Listing 12.5 and
below.




```c
UBaseType_t uxTaskGetSystemState( TaskStatus_t * const pxTaskStatusArray,
                                  const UBaseType_t uxArraySize,
                                  configRUN_TIME_COUNTER_TYPE * const pulTotalRunTime );
```
***Listing 12.4*** *The uxTaskGetSystemState() API function prototype*

> Note: `configRUN_TIME_COUNTER_TYPE` defaults to `uint32_t` for backward compatibility, but can be 
> overridden in FreeRTOSConfig.h if `uint32_t` is too restrictive.


**uxTaskGetSystemState() parameters and return value**

- `pxTaskStatusArray`

  A pointer to an array of `TaskStatus_t` structures.

  The array must contain at least one `TaskStatus_t` structure for each
  task. The number of tasks can be determined using the
  `uxTaskGetNumberOfTasks()` API function.

  The `TaskStatus_t` structure is shown in Listing 12.5, and the
  TaskStatus\_t structure members are described in the next list.

- `uxArraySize`

  The size of the array pointed to by the `pxTaskStatusArray` parameter.
  The size is specified as the number of indexes in the array (the number
  of `TaskStatus_t` structures contained in the array), not by the number of
  bytes in the array.

- `pulTotalRunTime`

  If `configGENERATE_RUN_TIME_STATS` is set to 1 in `FreeRTOSConfig.h`,
  then `*pulTotalRunTime` is set by `uxTaskGetSystemState()` to the total run
  time (as defined by the run-time statistics clock provided by the
  application) since the target booted.

  `pulTotalRunTime` is optional, and can be set to NULL if the total run
  time is not required.

- Return value

  The number of `TaskStatus_t` structures that were populated by
  `uxTaskGetSystemState()` is returned.

  The returned value should equal the number returned by the
  `uxTaskGetNumberOfTasks()` API function, but will be zero if the value
  passed in the `uxArraySize` parameter was too small.




```c
typedef struct xTASK_STATUS
{
    TaskHandle_t xHandle;
    const char *pcTaskName;
    UBaseType_t xTaskNumber;
    eTaskState eCurrentState;
    UBaseType_t uxCurrentPriority;
    UBaseType_t uxBasePriority;
    configRUN_TIME_COUNTER_TYPE ulRunTimeCounter;
    StackType_t * pxStackBase;
    #if ( ( portSTACK_GROWTH > 0 ) || ( configRECORD_STACK_HIGH_ADDRESS == 1 ) )
        StackType_t * pxTopOfStack;
        StackType_t * pxEndOfStack;
    #endif
    uint16_t usStackHighWaterMark;
    #if ( ( configUSE_CORE_AFFINITY == 1 ) && ( configNUMBER_OF_CORES > 1 ) )
        UBaseType_t uxCoreAffinityMask;
    #endif
} TaskStatus_t;
```
***Listing 12.5*** *The TaskStatus\_t structure*

**TaskStatus_t structure members**

- `xHandle`

  The handle of the task to which the information in the structure relates.

- `pcTaskName`

  The human readable text name of the task.

- `xTaskNumber`

  Each task has a unique `xTaskNumber` value.

  If an application creates and deletes tasks at run time then it is
  possible that a task will have the same handle as a task that was
  previously deleted. `xTaskNumber` is provided to allow application code,
  and kernel aware debuggers, to distinguish between a task that is still
  valid, and a deleted task that had the same handle as the valid
  task.

- `eCurrentState`

  An enumerated type that holds the state of the task.
  `eCurrentState` can be one of the following values: 
  
  - `eRunning`
  - `eReady`
  - `eBlocked`
  - `eSuspended`
  - `eDeleted`

  A task will only be reported as being in the `eDeleted` state for the
  short period between the time the task was deleted by a call to
  `vTaskDelete()`, and the time the Idle task frees the memory that was
  allocated to the deleted task's internal data structures and stack.
  After that time, the task will no longer exist in any way, and it is
  invalid to attempt to use its handle.

- `uxCurrentPriority`

  The priority at which the task was running at the time
  `uxTaskGetSystemState()` was called. `uxCurrentPriority` will only be higher
  than the priority assigned to the task by the application writer if the
  task has temporarily been assigned a higher priority in accordance with
  the priority inheritance mechanism described in section
  [8.3 Mutexes (and Binary Semaphores)](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch08.md#83-mutexes-and-binary-semaphores).

- `uxBasePriority`

  The priority assigned to the task by the application writer.
  `uxBasePriority` is only valid if `configUSE_MUTEXES` is set to 1 in
  FreeRTOSConfig.h.

- `ulRunTimeCounter`

  The total run time used by the task since the task was created. The
  total run time is provided as an absolute time that uses the clock
  provided by the application writer for the collection of run-time
  statistics. `ulRunTimeCounter` is only valid if
  `configGENERATE_RUN_TIME_STATS` is set to 1 in FreeRTOSConfig.h.
  
- `pxStackBase`

   Points to the base address of the stack region allotted to this task.

- `pxTopOfStack`

   Points to the current top address of the stack region allotted to this task.
   The field `pxTopOfStack` is only valid if either the stack grows upwards (i.e.
   `portSTACK_GROWTH` is greater than zero) or `configRECORD_STACK_HIGH_ADDRESS`
   is set to 1 in FreeRTOSConfig.h.

- `pxEndOfStack`

   Points to the end address of the of the stack region allotted to this task.
   The field `pxEndOfStack` is only valid if either the stack grows upwards (i.e.
   `portSTACK_GROWTH` is greater than zero) or `configRECORD_STACK_HIGH_ADDRESS`
   is set to 1 in FreeRTOSConfig.h.

- `usStackHighWaterMark`

  The task's stack high water mark. This is the minimum amount of
  stack space that has remained for the task since the task was created.
  It is an indication of how close the task has come to overflowing its
  stack; the closer this value is to zero, the closer the task has come to
  overflowing its stack. `usStackHighWaterMark` is specified in bytes.
  
- `uxCoreAffinityMask`

   A bitwise value that indicates the cores on which the task can run. 
   Cores are numbered from 0 to `configNUMBER_OF_CORES` - 1. For example, a
   task that can run on core 0 and core 1 will have its `uxCoreAffinityMask`
   set to 0x03. The field `uxCoreAffinityMask` is only available if both
   `configUSE_CORE_AFFINITY` is set to 1 and `configNUMBER_OF_CORES`
   is set to greater than 1 in FreeRTOSConfig.h.
