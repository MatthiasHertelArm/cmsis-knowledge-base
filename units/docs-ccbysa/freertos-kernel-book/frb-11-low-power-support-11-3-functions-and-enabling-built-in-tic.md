---
id: "frb-11-low-power-support-11-3-functions-and-enabling-built-in-tic"
type: "concept"
domain: "rtos"
title: "11 Low Power Support: 11.3 Functions and Enabling Built-in Tickless Idle Functionality"
summary: "The Built-in Tickless Idle functionality is enabled by defining configUSE_TICKLESS_IDLE as 1 in FreeRTOSConfig.h (for ports that support this feature)."
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch11.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch11.md#11-3-functions-and-enabling-built-in-tickless-idle-functionality"
license: "CC-BY-SA-4.0"
mode: "V"
---

The Built-in Tickless Idle functionality is enabled by defining `configUSE_TICKLESS_IDLE` as 1 in FreeRTOSConfig.h 
(for ports that support this feature). User defined tickless idle functionality can be provided for any 
FreeRTOS port (including those that include a built in implementation) by defining `configUSE_TICKLESS_IDLE` 
to 2 in FreeRTOSConfig.h. 

When the tickless idle functionality is enabled, the kernel will call the `portSUPPRESS_TICKS_AND_SLEEP()` 
macro when the following two conditions are satisfied:

1. The Idle task is the only task able to run because all the application tasks are either in the Blocked 
   state or in the Suspended state.

2. At least n further complete tick periods will pass before the kernel is due to transition an application 
   task out of the Blocked state, where n is set by the `configEXPECTED_IDLE_TIME_BEFORE_SLEEP` definition 
   in FreeRTOSConfig.h.


### 11.3.1 The portSUPPRESS\_TICKS\_AND\_SLEEP() Macro



```c
portSUPPRESS_TICKS_AND_SLEEP( xExpectedIdleTime )
```
***Listing 11.1*** *The prototype for the portSUPPRESS\_TICKS\_AND\_SLEEP macro*

The value of the `xExpectedIdleTime` parameter in `portSUPPRESS_TICKS_AND_SLEEP()` equals the total number 
of tick periods before a task is due to be moved into the Ready state. The parameter value is therefore the 
time the microcontroller can safely remain in a deep sleep state, with the tick interrupt suppressed. 


### 11.3.2 The vPortSuppressTicksAndSleep Function

The `vPortSuppressTicksAndSleep()` function is defined in FreeRTOS and it can be used to implement the 
tickless mode. This function is weakly defined in the FreeRTOS Cortex-M port layer and can be overridden 
by the application writer.



```c
void vPortSuppressTicksAndSleep( TickType_t xExpectedIdleTime );
```
***Listing 11.2*** *The vPortSuppressTicksAndSleep API function prototype*


### 11.3.3 The eTaskConfirmSleepModeStatus Function

The API *eTaskConfirmSleepModeStatus* returns the sleep mode status to determine if it is ok to proceed 
with the sleep and if it is ok to sleep indefinitely. This functionality is only available when `configUSE_TICKLESS_IDLE` 
is set to 1.


 
```c
eSleepModeStatus eTaskConfirmSleepModeStatus( void );
```
***Listing 11.3*** *The eTaskConfirmSleepModeStatus API function prototype*


If `eTaskConfirmSleepModeStatus()` returns `eNoTasksWaitingTimeout` when it is called from 
within `portSUPPRESS_TICKS_AND_SLEEP()`, then the microcontroller can remain in a deep sleep state 
indefinitely. `eTaskConfirmSleepModeStatus()` will only return `eNoTasksWaitingTimeout` when the 
following conditions are true:

+ Software timers are not being used, so the scheduler is not due to execute a timer callback function 
  at any time in the future.

+ All the application tasks are either in the Suspended state, or in the Blocked state with a timeout value 
  of `portMAX_DELAY`, so the scheduler is not due to transition a task out of the Blocked state at any fixed 
  time in the future.

To avoid race conditions, the FreeRTOS scheduler is suspended before `portSUPPRESS_TICKS_AND_SLEEP()` is 
called, and resumed when `portSUPPRESS_TICKS_AND_SLEEP()` completes. This ensures application tasks cannot 
execute between the microcontroller exiting its low power state and `portSUPPRESS_TICKS_AND_SLEEP()` 
completing its execution. Further, it is necessary for the `portSUPPRESS_TICKS_AND_SLEEP()` function to 
create a small critical section between the timer being stopped and the sleep mode being entered to ensure 
it is ok to proceed into the sleep mode. `eTaskConfirmSleepModeStatus()` should be called from this critical 
section.

In addition, FreeRTOS provides users with two other interface functions defined in FreeRTOSConfig.h. These 
macros allow the application writer to add additional steps before and after the MCU is placed into the low 
power state, respectively.


### 11.3.4 The configPRE\_SLEEP\_PROCESSING configuration



```c
configPRE_SLEEP_PROCESSING( xExpectedIdleTime )
```
***Listing 11.4*** *The prototype for the configPRE\_SLEEP\_PROCESSING macro*


Before the user can make the MCU enter the low-power mode, `configPRE_SLEEP_PROCESSING()` must be called to 
configure the system parameters to reduce the system power consumption, such as turning off other peripheral 
clocks, reducing the system frequency. 


### 11.3.5 The configPOST\_SLEEP\_PROCESSING configuration



```c
configPOST_SLEEP_PROCESSING( xExpectedIdleTime )
```
***Listing 11.5*** *The prototype for the configPOST\_SLEEP\_PROCESSING macro*


After exiting the low-power mode, the user should call the `configPOST_SLEEP_PROCESSING()` function 
to restore the system's main frequency and peripheral functions.
