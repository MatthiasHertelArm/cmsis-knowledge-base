---
id: "rtos2-event-flags-oseventflagsdelete"
type: "concept"
domain: "rtos"
title: "Event Flags: osEventFlagsDelete"
summary: "The function osEventFlagsDelete deletes the event flags object specified by parameter ef_id and releases the internal memory obtained for the event flags handling. After this call, the ef_id is no longer valid and cannot be used."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_event.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_event.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osEventFlagsDelete (osEventFlagsId_t ef_id)
```


The function **osEventFlagsDelete** deletes the event flags object specified by parameter _ef_id_ and releases the internal
memory obtained for the event flags handling. After this call, the **ef_id** is no longer valid and cannot be used. This can
cause starvation of threads that are waiting for flags of this event object. The **ef_id** may be created again using the
function osEventFlagsNew.

Possible osStatus_t return values:
 - **osOK:** the specified event flags object has been deleted.
 - **osErrorISR:** **osEventFlagsDelete** cannot be called from interrupt service routines.
 - **osErrorParameter:** parameter _ef_id_ is `NULL` or invalid.
 - **osErrorResource:** the event flags object is in an invalid state.
 - **osFlagsErrorSafetyClass:** the calling thread safety class is lower than the safety class of the specified event flags object.

**Note:** This function **cannot** be called from Interrupt Service Routines.
