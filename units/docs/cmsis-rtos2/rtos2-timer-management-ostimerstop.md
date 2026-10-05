---
id: "rtos2-timer-management-ostimerstop"
type: "concept"
domain: "rtos"
title: "Timer Management: osTimerStop"
summary: "The function osTimerStop stops a timer specified by the parameter timer_id."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_timer.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_timer.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osTimerStop (osTimerId_t timer_id)
```


The function **osTimerStop** stops a timer specified by the parameter _timer_id._

Possible osStatus_t return values:
 - **osOK:** the specified timer has been stopped.
 - **osErrorISR:** **osTimerStop** cannot be called from interrupt service routines.
 - **osErrorParameter:** parameter _timer_id_ is either `NULL` or invalid.
 - **osErrorResource:** the timer is not running (you can only stop a running timer).
 - **osErrorSafetyClass:** the calling thread safety class is lower than the safety class of the specified timer.

**Note:** This function **cannot** be called from Interrupt Service Routines.

**Code Example**
```
#include "cmsis_os2.h"
 
void Timer_Callback (void *arg);                // prototype for timer callback function
 
uint32_t exec;                                  // argument for the timer call back function
 
void TimerStop_example (void) {
  osTimerId_t id;                               // timer id
  osStatus_t  status;                           // function return status
 
  // Create periodic timer
  exec = 1U;
  id = osTimerNew(Timer_Callback, osTimerPeriodic, &exec, NULL);
  osTimerStart(id, 1000U);                      // start timer
  :
  status = osTimerStop(id);                     // stop timer
  if (status != osOK) {
    // Timer could not be stopped
  }
  ;
  osTimerStart(id, 1000U);                      // start timer again
  ;
}
```
