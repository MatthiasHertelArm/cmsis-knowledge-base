---
id: "rtos2-event-flags-oseventflagsget"
type: "concept"
domain: "rtos"
title: "Event Flags: osEventFlagsGet"
summary: "The function osEventFlagsGet returns the event flags currently set in an event flags object specified by parameter ef_id or 0 in case of an error."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_event.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_event.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t osEventFlagsGet (osEventFlagsId_t ef_id)
```


The function **osEventFlagsGet** returns the event flags currently set in an event flags object specified by parameter
_ef_id_ or `0` in case of an error.

**Note:** This function may be called from Interrupt Service Routines.
