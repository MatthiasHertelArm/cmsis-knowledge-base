---
id: "rtos2-timer-management"
type: "concept"
domain: "rtos"
title: "Timer Management"
summary: "Create and control timer and timer callback functions."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_timer.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_timer.txt"
license: "Apache-2.0"
mode: "V"
---

Create and control timer and timer callback functions.

In addition to the CMSIS_RTOS_Wait CMSIS-RTOS also supports virtual timer objects. These timer objects can trigger the execution of a function (not threads). When a timer expires, a callback function is executed to run associated code with the timer. Each timer can be configured as a one-shot or a periodic timer. A periodic timer repeats its operation until it is deleted or stopped. All timers can be started, restarted, or stopped.

**Note:** Timer management functions cannot be called from Interrupt Service Routines.

The figure below shows the behavior of a periodic timer. For one-shot timers, the timer stops after execution of the callback function.

" "Behavior of a Periodic Timer"

Working with Timers
--------------------
The following steps are required to use a software timer:
-# Define the timers:
```
osTimerId_t one_shot_id, periodic_id;
```
-# Define callback functions:
```
static void one_shot_Callback (void *argument) {
  int32_t arg = (int32_t)argument; // cast back argument '0' 
  // do something, i.e. set thread/event flags
}
static void periodic_Callback (void *argument) {
  int32_t arg = (int32_t)argument; // cast back argument '5'
  // do something, i.e. set thread/event flags
}
```
-# Instantiate and start the timers:
```
// creates a one-shot timer:
one_shot_id = osTimerNew(one_shot_Callback, osTimerOnce, (void *)0, NULL);     // (void*)0 is passed as an argument
                                                                               // to the callback function
// creates a periodic timer:
periodic_id = osTimerNew(periodic_Callback, osTimerPeriodic, (void *)5, NULL); // (void*)5 is passed as an argument
                                                                               // to the callback function
osTimerStart(one_shot_id, 500U);
osTimerStart(periodic_id, 1500U);
 
// start the one-shot timer again after it has triggered the first time:
osTimerStart(one_shot_id, 500U);
 
// when timers are not needed any longer free the resources:
osTimerDelete(one_shot_id);
osTimerDelete(periodic_id);
```
