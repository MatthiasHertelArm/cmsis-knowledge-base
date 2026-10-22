---
id: "rtos2-event-flags-oseventflagswait"
type: "concept"
domain: "rtos"
title: "Event Flags: osEventFlagsWait"
summary: "The function osEventFlagsWait suspends the execution of the currently RUNNING thread until any or all event flags specified by the parameter flags in the event object specified by parameter ef_id are set."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_event.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_event.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t osEventFlagsWait (osEventFlagsId_t ef_id, uint32_t flags, uint32_t options, uint32_t timeout)
```


The function **osEventFlagsWait** suspends the execution of the currently RUNNING thread until any or all event flags
specified by the parameter _flags_ in the event object specified by parameter _ef_id_ are set. When these event flags are
already set, the function returns instantly. Otherwise, the thread is put into the state BLOCKED. 

The **options** parameter specifies the wait condition:
|Option              |                                                       |
|--------------------|-------------------------------------------------------|
|**osFlagsWaitAny**   |   Wait for any flag (default).                        |
|**osFlagsWaitAll**   |   Wait for all flags.                                 |
|**osFlagsNoClear**   |   Do not clear flags which have been specified to wait for.  |

If `osFlagsNoClear` is set in the options osEventFlagsClear can be used to clear flags manually.

The parameter _timeout_ specifies how long the system waits for event flags. While the system waits, the thread
that is calling this function is put into the BLOCKED state. The parameter CMSIS_RTOS_TimeOutValue
"timeout" can have the following values:
 - when _timeout_ is `0`, the function returns instantly (i.e. try semantics).
 - when _timeout_ is set to **osWaitForever** the function will wait for an infinite time until the event flags become
   available (i.e. wait semantics).
 - all other values specify a time in kernel ticks for a timeout (i.e. timed-wait semantics).

The function returns the event flags before clearing or an error code (highest bit is set, refer to flags_error_codes).

Possible flags_error_codes return values:
    - **osFlagsErrorUnknown:** unspecified error.
    - **osFlagsErrorTimeout:** awaited flags have not been set in the given time.
    - **osFlagsErrorResource:** awaited flags have not been set when no _timeout_ was specified.
    - **osFlagsErrorParameter:** parameter _ef_id_ does not identify a valid event flags object or **flags** has highest bit set. 
    - **osFlagsErrorSafetyClass:** the calling thread safety class is lower than the safety class of the specified event flags object.

**Note:** May be called from Interrupt Service Routines if the parameter _timeout_ is set to
`0`.

**Code** **Example**
```
#include "cmsis_os2.h"                          // CMSIS RTOS header file
 
osEventFlagsId_t evt_id;                        // event flags id
 
void Thread_EventReceiver (void *argument) {
  uint32_t flags;
 
  while (1) {
    flags = osEventFlagsWait(evt_id, 0x00000001U, osFlagsWaitAny, osWaitForever);
    //handle event
  }
}
```
