---
id: "rtos2-event-flags-oseventflagsnew"
type: "concept"
domain: "rtos"
title: "Event Flags: osEventFlagsNew"
summary: "The function osEventFlagsNew creates a new event flags object that is used to send events across threads and returns the pointer to the event flags object identifier or NULL in case of an error."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_event.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_event.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osEventFlagsId_t osEventFlagsNew (const osEventFlagsAttr_t *attr)
```


The function **osEventFlagsNew** creates a new event flags object that is used to send events across threads and returns the
pointer to the event flags object identifier or `NULL` in case of an error. It can be safely called before the RTOS is
started (call to osKernelStart), but not before it is initialized (call to osKernelInitialize).

The parameter _attr_ sets the event flags attributes (refer to osEventFlagsAttr_t).  Default attributes will be used if
set to `NULL`, i.e. kernel memory allocation is used for the event control block.

**Note:** Cannot be called from Interrupt Service Routines.

**Code Example**
```
#include "cmsis_os2.h"                          // CMSIS RTOS header file
 
osEventFlagsId_t evt_id;                        // event flags id
 
int Init_Events (void) {
 
  evt_id = osEventFlagsNew(NULL);
  if (evt_id == NULL) {
    ; // Event Flags object not created, handle failure
    return(-1);
  }

  return(0);
}
```
