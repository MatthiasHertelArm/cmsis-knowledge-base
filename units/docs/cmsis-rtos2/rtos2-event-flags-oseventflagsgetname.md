---
id: "rtos2-event-flags-oseventflagsgetname"
type: "concept"
domain: "rtos"
title: "Event Flags: osEventFlagsGetName"
summary: "The function osEventFlagsGetName returns the pointer to the name string of the event flags object identified by parameter ef_id or NULL in case of an error."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_event.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_event.txt"
license: "Apache-2.0"
mode: "V"
---

```c
const char *osEventFlagsGetName (osEventFlagsId_t ef_id)
```


The function **osEventFlagsGetName** returns the pointer to the name string of the event flags object identified by parameter
_ef_id_ or `NULL` in case of an error.

**Note:** This function may be called from Interrupt Service Routines.

**Code Example**
```
#include "cmsis_os2.h"                          // CMSIS RTOS header file
 
osEventFlagsId_t evt_id;                        // event flags id
 
void EvtFlagsGetName_example (void)  {
  char *name;
   
  name = osEventFlagsGetName(evt_id);
  if (name == NULL) {
    // Failed to get the event flags object name
  }
}
```
