---
id: "rtos2-thread-management-osthreadfeedwatchdog"
type: "concept"
domain: "rtos"
title: "Thread Management: osThreadFeedWatchdog"
summary: "The function osThreadFeedWatchdog restarts watchdog of the current running thread. If the thread watchdog is not fed again within the ticks interval osWatchdogAlarm_Handler will be called."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osThreadFeedWatchdog (uint32_t ticks);
```


The function **osThreadFeedWatchdog** restarts watchdog of the current running thread. If the thread watchdog is not fed again within the _ticks_ interval osWatchdogAlarm_Handler will be called.

Possible osStatus_t return values:
    - **osOK:** the watchdog timer was restarted successfully.
    - **osError:** cannot be executed (kernel not running).
    - **osErrorISR:** the function **osThreadFeedWatchdog** cannot be called from interrupt service routines.

**Note:** This function **cannot** be called from Interrupt Service Routines.

**Code Example:**
```
#include "cmsis_os2.h"
 
void Thread_1 (void const *arg) {          // Thread function
  osStatus_t status;                       // Status of the executed function
  :
  while (1) {
    status = osThreadFeedWatchdog(500U);   // Feed thread watchdog for 500 ticks
    // verify status value here
    :
  }
}
```
