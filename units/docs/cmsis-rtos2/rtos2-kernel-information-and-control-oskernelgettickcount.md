---
id: "rtos2-kernel-information-and-control-oskernelgettickcount"
type: "concept"
domain: "rtos"
title: "Kernel Information and Control: osKernelGetTickCount"
summary: "The function osKernelGetTickCount returns the current RTOS kernel tick count."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_kernel.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_kernel.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t osKernelGetTickCount (void)
```


The function **osKernelGetTickCount** returns the current RTOS kernel tick count.

**Note:** This function may be called from Interrupt Service Routines.

**Code** **Example**
```
#include "cmsis_os2.h"
 
void Thread_1 (void *arg)  {                // Thread function
  uint32_t tick;

  tick = osKernelGetTickCount();            // retrieve the number of system ticks
  for (;;) {
    tick += 1000;                           // delay 1000 ticks periodically
    osDelayUntil(tick);
    // ...
  }
}\endcode

Due to the limited value range used for the tick count it may overflow during runtime,
i.e. after 2<sup>32</sup> ticks which are roughly 49days @ 1ms. Typically one has not to
take special care of this unless a monotonic counter is needed. For such a case an additional
64bit tick counter can be implemented as follows. The given example needs GetTick() called at
least twice per tick overflow to work properly.

\b Code \b Example
```
uint64_t GetTick(void) {
  static uint32_t tick_h = 0U;
  static uint32_t tick_l = 0U;
         uint32_t tick;

  tick = osKernelGetTickCount();
  if (tick < tick_l) {
    tick_h++;
  }
  tick_l = tick;

  return (((uint64_t)tick_h << 32) | tick_l);
}
```


### osKernelGetTickFreq

```c
uint32_t osKernelGetTickFreq (void)
```


The function **osKernelGetTickFreq** returns the frequency of the current RTOS kernel tick.

**Note:** This function may be called from Interrupt Service Routines.


### osKernelGetSysTimerCount

```c
uint32_t osKernelGetSysTimerCount (void)
```


The function **osKernelGetSysTimerCount** returns the current RTOS kernel system timer as a 32-bit value. 
The value is a rolling 32-bit counter that is composed of the kernel system interrupt timer value
and the counter that counts these interrupts (RTOS kernel ticks).

This function allows the implementation of very short timeout checks below the RTOS tick granularity.
Such checks might be required when checking for a busy status in a device or peripheral initialization
routine, see code example below.

**Note:** This function may be called from Interrupt Service Routines.

<b>Code Example</b>
```c
#include "cmsis_os2.h"
 
void SetupDevice (void)  {
  uint32_t tick;
  
  // Calculating 100us timeout in system timer ticks
  const uint32_t timeout = 100U * osKernelGetSysTimerFreq() / 1000000u;
  
  tick = osKernelGetSysTimerCount();             // get start value of the Kernel system tick
  Device.Setup ();                               // initialize a device or peripheral
  do {                                           // poll device busy status for 100 microseconds
    if (!Device.Busy) break;                     // check if device is correctly initialized
  } while ((osKernelGetSysTimerCount() - tick) < timeout));
  if (Device.Busy)  {              
    ;                                            // in case device still busy, signal error
  }
                                                 // start interacting with device
}

```


### osKernelGetSysTimerFreq

```c
uint32_t osKernelGetSysTimerFreq (void)
```


The function **osKernelGetSysTimerFreq** returns the frequency of the current RTOS kernel system timer.

**Note:** This function may be called from Interrupt Service Routines.


### osKernelProtect

```c
osStatus_t osKernelProtect (uint32_t safety_class);
```


The function **osKernelProtect** configures kernel access protection. After its successful execution, only threads with
safety class equal or higher than the _safety_class_ specified in the argument can execute kernel control functions.
- osKernelLock
- osKernelUnlock
- osKernelRestoreLock
- osKernelSuspend
- osKernelResume
- osKernelProtect

Possible osStatus_t return values:
- **osOK** in case of success.
- **osErrorParameter** if _safety_class_ is invalid.
- **osError** if kernel is not in ready or running state.
- **osErrorISR** if called from an Interrupt Service Routine.
- **osErrorSafetyClass** if the calling thread safety class is lower than the kernel protect safety class.

**Note:** This function **cannot** be called from Interrupt Service Routines.

<b>Code Example:</b>
```
#include "cmsis_os2.h"
 
void ProtectKernelControlFunctions (void) {
  osStatus_t status;
 
  status = osKernelProtect(4U); // Enable Kernel Control for threads with safety class 4 or higher
  // verify status value here.
}
```


### osKernelDestroyClass

```c
osStatus_t osKernelDestroyClass (uint32_t safety_class, uint32_t mode);
```


The function **osKernelDestroyClass** destroys RTOS objects based on safety class assignment. _safety_class_ provides the reference safety class value, while _mode_ is considered as a bitmap that additionally specifies the safety classes to be destroyed.

If osSafetyWithSameClass is set in _mode_ than the RTOS objects with safety class value equal to _safety_class_ will be destroyed.
<br>
If osSafetyWithLowerClass is set in _mode_ than the RTOS objects with safety class value lower than _safety_class_ will be destroyed.

Possible osStatus_t return values:
- **osOK** in case of success.
- **osErrorParameter** if _safety_class_ is invalid.
- **osErrorResource** if no other READY thread exists.
- **osErrorISR** if called from interrupt other than osWatchdogAlarm_Handler.
- **osErrorSafetyClass** if the calling thread safety class is lower than the kernel protect safety class.

<b>Code Example:</b>
```
#include "cmsis_os2.h"
 
void DestroyNonCriticalClasses (void) {
  osStatus_t status;
 
  status = osKernelDestroyClass(4U, osSafetyWithSameClass | osSafetyWithLowerClass); // Destroy objects with safety class 4 or lower
  // verify status value here.
}
```


### osFaultResume

```c
void osFaultResume (void);
```


Resume normal RTOS operation when exiting exception faults.

<b>Code Example:</b>
```
void HardFault_Handler (void) {
  __ASM volatile (
    "...                          \n\t" // Enter assembly and handle faults
    "...                          \n\t"
    "ldr  r0,=osFaultResume       \n\t" // Before exiting the handler load and
    "bx   r0                      \n\t" // jump to osFaultResume
  );
}
```
