---
id: "rtos2-timer-management-ostimernew"
type: "concept"
domain: "rtos"
title: "Timer Management: osTimerNew"
summary: "The function osTimerNew creates an one-shot or periodic timer and associates it with a callback function with argument. The timer is in stopped state until it is started with osTimerStart."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_timer.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_timer.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osTimerId_t osTimerNew (osTimerFunc_t func, osTimerType_t type, void *argument, const osTimerAttr_t *attr)
```


The function **osTimerNew** creates an one-shot or periodic timer and associates it with a callback function with _argument._
The timer is in stopped state until it is started with osTimerStart. The function can be safely called before the RTOS
is started (call to osKernelStart), but not before it is initialized (call to osKernelInitialize).

The function **osTimerNew** returns the pointer to the timer object identifier or `NULL` in case of an error.

**Note:** This function **cannot** be called from Interrupt Service Routines.

**Code Example**
```
#include "cmsis_os2.h"
 
void Timer1_Callback (void *arg);               // prototypes for timer callback function
void Timer2_Callback (void *arg);               // prototypes for timer callback function
 
uint32_t exec1;                                 // argument for the timer call back function
uint32_t exec2;                                 // argument for the timer call back function
 
void TimerCreate_example (void)  {
  osTimerId_t id1;                              // timer id
  osTimerId_t id2;                              // timer id
 
  // Create one-shoot timer
  exec1 = 1U;
  id1 = osTimerNew(Timer1_Callback, osTimerOnce, &exec1, NULL);
  if (id1 != NULL) {
    // One-shoot timer created
  }
 
  // Create periodic timer
  exec2 = 2U;
  id2 = osTimerNew(Timer2_Callback, osTimerPeriodic, &exec2, NULL);
  if (id2 != NULL) {
    // Periodic timer created
  }
  :
}
```
