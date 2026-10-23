---
id: "rtos2-generic-wait-functions-osdelay"
type: "concept"
domain: "rtos"
title: "Generic Wait Functions: osDelay"
summary: "The function osDelay waits for a time period specified in kernel ticks. For a value of 1 the system waits until the next timer tick occurs."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_wait.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_wait.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osDelay (uint32_t ticks)
```


The function **osDelay** waits for a time period specified in kernel _ticks._ For a value of `1` the system waits
until the next timer tick occurs. The actual time delay may be up to one timer tick less than specified, i.e. calling 
`osDelay(1)` right before the next system tick occurs the thread is rescheduled immediately.

The delayed thread is put into the BLOCKED state and a context switch occurs immediately. The thread
is automatically put back to the READY state after the given amount of ticks has elapsed. If the thread
will have the highest priority in READY state it will be scheduled immediately.

Possible osStatus_t return values:
 - **osOK:** the time delay is executed.
 - **osErrorParameter:** the time cannot be handled (zero value).
 - **osErrorISR:** osDelay cannot be called from Interrupt Service Routines.
 - **osError:** osDelay cannot be executed (kernel not running or no READY thread exists).

**Note:** This function **cannot** be called from Interrupt Service Routines.

**Code Example**
```
#include "cmsis_os2.h"
 
void Thread_1 (void *arg) {             // Thread function
  osStatus_t status;                    // capture the return status
  uint32_t   delayTime;                 // delay time in milliseconds
 
  delayTime = 1000U;                    // delay 1 second
  status = osDelay(delayTime);          // suspend thread execution
}
```
