---
id: "rtos2-event-flags"
type: "concept"
domain: "rtos"
title: "Event Flags"
summary: "The event flags management functions in CMSIS-RTOS allow you to control or wait for event flags. Each signal has up to 31 event flags."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_event.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_event.txt"
license: "Apache-2.0"
mode: "V"
---

Synchronize threads using event flags.
 
The event flags management functions in CMSIS-RTOS allow you to control or wait for event flags. Each signal has up to 31
event flags.

A thread
- can wait for event flags to be set (using osEventFlagsWait). Using this function, it enters the
  BLOCKED state.
- may set one or more flags in any other given thread (using osEventFlagsSet).
- may clear its own signals or the signals of other threads (using osEventFlagsClear).

When a thread wakes up and resumes execution, its signal flags are automatically cleared (unless event flags option
osFlagsNoClear is specified).

**Note:** The functions osEventFlagsSet, osEventFlagsClear, osEventFlagsGet, and osEventFlagsWait can be
called from Interrupt Service Routines.

Working with Events
--------------------
Here is a simple example that shows how two thread can communicate with each others using event flags:

 "Simple event communication"

The following steps are required to use event flags:
-# In the thread that is supposed to send an event with id sig1_id, call the set function:
```
osDelay(1000U);                                           // wait for 1 second
osEventFlagsSet(sig1_id, 0x0001U);                        // set the flag 0x0001U for event sig1_id
```
-# In another thread (or threads) that are supposed to wait for the event, call the wait function:
```
osEventFlagsWait(sig1_id, 0x0001U, NULL, osWaitForever);  // wait forever for any flag
```

**Code Example**
```
#include "cmsis_os2.h"                          // CMSIS RTOS header file
 
/*----------------------------------------------------------------------------
 Event Flags creation & usage
---------------------------------------------------------------------------*/
 
#define FLAGS_MSK1 0x00000001U
 
osEventFlagsId_t evt_id;                        // event flags id
 
osThreadId_t tid_Thread_EventSender;            // thread id 1
osThreadId_t tid_Thread_EventReceiver;          // thread id 2
 
void Thread_EventSender   (void *argument);     // thread function 1
void Thread_EventReceiver (void *argument);     // thread function 2
 
int Init_Events (void) {
 
  evt_id = osEventFlagsNew(NULL);
  if (evt_id == NULL) {
    ; // Event Flags object not created, handle failure
  }
 
  tid_Thread_EventSender = osThreadNew(Thread_EventSender, NULL, NULL);
  if (tid_Thread_EventSender == NULL) {
    return(-1);
  }
  tid_Thread_EventReceiver = osThreadNew(Thread_EventReceiver, NULL, NULL);
  if (tid_Thread_EventReceiver == NULL) {
    return(-1);
  }

  return(0);
}
 
void Thread_EventSender (void *argument) {
 
  while (1) {    
    osEventFlagsSet(evt_id, FLAGS_MSK1);
    osThreadYield();                            // suspend thread
  }
}
 
void Thread_EventReceiver (void *argument) {
  uint32_t flags;
 
  while (1) {
    flags = osEventFlagsWait(evt_id, FLAGS_MSK1, osFlagsWaitAny, osWaitForever);
    //handle event
  }
}
```
