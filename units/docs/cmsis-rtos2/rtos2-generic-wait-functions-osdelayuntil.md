---
id: "rtos2-generic-wait-functions-osdelayuntil"
type: "concept"
domain: "rtos"
title: "Generic Wait Functions: osDelayUntil"
summary: "The function osDelayUntil waits until an absolute time (specified in kernel ticks) is reached."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_wait.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_wait.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osDelayUntil (uint32_t ticks)
```


The function **osDelayUntil** waits until an absolute time (specified in kernel _ticks)_ is reached.

The corner case when the kernel tick counter overflows is handled by **osDelayUntil.** Thus it is absolutely legal
to provide a value which is lower than the current tick value, i.e. returned by osKernelGetTickCount. Typically
as a user you do not have to take care about the overflow. The only limitation you have to have in mind is that the
maximum delay is limited to (231)-1 ticks.

The delayed thread is put into the BLOCKED state and a context switch occurs immediately. The thread
is automatically put back to the READY state when the given time is reached. If the thread will
have the highest priority in READY state it will be scheduled immediately.

Possible osStatus_t return values:
 - **osOK:** the time delay is executed.
 - **osErrorParameter:** the time cannot be handled (out of bounds).
 - **osErrorISR:** osDelayUntil cannot be called from Interrupt Service Routines.
 - **osError:** osDelayUntil cannot be executed (kernel not running or no READY thread exists).

**Note:** This function **cannot** be called from Interrupt Service Routines.

**Code Example**
```
#include "cmsis_os2.h"
 
void Thread_1 (void *arg) {             // Thread function
  uint32_t tick;
 
  tick = osKernelGetTickCount();        // retrieve the number of system ticks
  for (;;) {
    tick += 1000U;                      // delay 1000 ticks periodically
    osDelayUntil(tick);
    // ...
  }
}
```
