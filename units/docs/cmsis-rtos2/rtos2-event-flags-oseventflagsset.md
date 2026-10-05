---
id: "rtos2-event-flags-oseventflagsset"
type: "concept"
domain: "rtos"
title: "Event Flags: osEventFlagsSet"
summary: "The function osEventFlagsSet sets the event flags specified by the parameter flags in an event flags object specified by parameter ef_id."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_event.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_event.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t osEventFlagsSet (osEventFlagsId_t ef_id, uint32_t flags)
```


The function **osEventFlagsSet** sets the event flags specified by the parameter _flags_ in an event flags object specified
by parameter _ef_id._ 

The threads with highest priority waiting for the flag(s) set will be notified to resume from BLOCKED state.
The function returns the event flags stored in the event control block or an error code (highest bit is set, refer to
flags_error_codes). Further threads may be wakened in priority order when the option **osFlagsNoClear** is given to the
osEventFlagsWait call.

Possible flags_error_codes return values:
    - **osFlagsErrorUnknown:** unspecified error.
    - **osFlagsErrorParameter:** parameter _ef_id_ does not identify a valid event flags object or **flags** has highest bit set. 
    - **osFlagsErrorResource:** the event flags object is in an invalid state.
    - **osFlagsErrorSafetyClass:** the calling thread safety class is lower than the safety class of the specified event flags object.

**Note:** This function may be called from Interrupt Service Routines.

**Code Example**
```
#include "cmsis_os2.h"                          // CMSIS RTOS header file
 
osEventFlagsId_t evt_id;                        // event flags id
 
void Thread_EventSender (void *argument) {
 
  while (1) {    
    osEventFlagsSet(evt_id, 0x00000001U);
    osThreadYield();                            // suspend thread
  }
}
```
