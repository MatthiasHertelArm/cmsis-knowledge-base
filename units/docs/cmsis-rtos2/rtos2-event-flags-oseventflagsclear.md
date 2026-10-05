---
id: "rtos2-event-flags-oseventflagsclear"
type: "concept"
domain: "rtos"
title: "Event Flags: osEventFlagsClear"
summary: "The function osEventFlagsClear clears the event flags specified by the parameter flags in an event flags object specified by parameter efid. The function returns the event flags before clearing or an error code (highest bit is set, refer to flagserrorcodes)."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_event.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_event.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t osEventFlagsClear (osEventFlagsId_t ef_id, uint32_t flags)
```


The function **osEventFlagsClear** clears the event flags specified by the parameter _flags_ in an event flags object
specified by parameter _ef_id._ The function returns the event flags before clearing or an error code (highest bit is set, 
refer to flags_error_codes).

Possible flags_error_codes return values:
    - **osFlagsErrorUnknown:** unspecified error.
    - **osFlagsErrorParameter:** parameter _ef_id_ does not identify a valid event flags object or **flags** has highest bit set. 
    - **osFlagsErrorResource:** the event flags object is in an invalid state.
    - **osFlagsErrorSafetyClass:** the calling thread safety class is lower than the safety class of the specified event flags object.

**Note:** This function may be called from Interrupt Service Routines.
