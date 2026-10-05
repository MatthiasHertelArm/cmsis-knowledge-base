---
id: "rtos2-timer-management-ostimerstart"
type: "concept"
domain: "rtos"
title: "Timer Management: osTimerStart"
summary: "The function osTimerStart starts or restarts a timer specified by the parameter timer_id. The parameter ticks specifies the value of the timer in time ticks."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_timer.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_timer.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osTimerStart (osTimerId_t timer_id, uint32_t ticks)
```


The function **osTimerStart** starts or restarts a timer specified by the parameter _timer_id._ The parameter _ticks_
specifies the value of the timer in time ticks.

Possible osStatus_t return values:
 - **osOK:** the specified timer has been started or restarted.
 - **osErrorISR:** **osTimerStart** cannot be called from interrupt service routines.
 - **osErrorParameter:** parameter _timer_id_ is either `NULL` or invalid or _ticks_ is incorrect.
 - **osErrorResource:** the timer is in an invalid state.
 - **osErrorSafetyClass:** the calling thread safety class is lower than the safety class of the specified timer.

**Note:** This function **cannot** be called from Interrupt Service Routines.

**Code Example**
```
#include "cmsis_os2.h"
 
void Timer_Callback (void *arg) {               // timer callback function
                                                // arg contains &exec
                                                // called every second after osTimerStart
}
 
uint32_t exec;                                  // argument for the timer call back function
 
void TimerStart_example (void) {
  osTimerId_t id;                               // timer id
  uint32_t    timerDelay;                       // timer value
  osStatus_t  status;                           // function return status
 
  // Create periodic timer
  exec = 1U;
  id = osTimerNew(Timer_Callback, osTimerPeriodic, &exec, NULL);
  if (id != NULL)  {
    timerDelay = 1000U;
    status = osTimerStart(id, timerDelay);       // start timer
    if (status != osOK) {
      // Timer could not be started
    }
  }
  ;
}
```
