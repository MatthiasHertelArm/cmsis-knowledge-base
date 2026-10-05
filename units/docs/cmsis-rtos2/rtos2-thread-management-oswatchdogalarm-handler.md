---
id: "rtos2-thread-management-oswatchdogalarm-handler"
type: "concept"
domain: "rtos"
title: "Thread Management: osWatchdogAlarm_Handler"
summary: "The callback function osWatchdogAlarm_Handler is called by the kernel when a thread watchdog expires. Parameter thread_id identifies the thread which has the expired thread watchdog. The function needs to be implemented in user application."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t osWatchdogAlarm_Handler (osThreadId_t thread_id);
```


The callback function **osWatchdogAlarm_Handler** is called by the kernel when a thread watchdog expires.
Parameter _thread_id_ identifies the thread which has the expired thread watchdog.
The function needs to be implemented in user application.

Return new reload value to restart the watchdog. Return `0` to stop the thread watchdog.

**Note:** The callback function is called from interrupt.

**Note:**
When multiple watchdogs expire in the same tick, this function is called for each thread with highest safety class first.

**Code Example:**
```
#include "cmsis_os2.h"
 
uint32_t osWatchdogAlarm_Handler (osThreadId_t thread_id) {
  uint32_t safety_class;
  uint32_t next_interval;

  safety_class = osThreadGetClass(thread_id);
  
  /* Handle the watchdog depending on how safety-critical is the thread */
  if (safety_class < ...){
    :
  } else {
    :
  }
 
  return next_interval;
}
```
