---
id: "rtos2-thread-management-osthreadgetpriority"
type: "concept"
domain: "rtos"
title: "Thread Management: osThreadGetPriority"
summary: "The function osThreadGetPriority returns the priority of an active thread specified by the parameter thread_id."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osPriority_t osThreadGetPriority (osThreadId_t thread_id)
```


The function **osThreadGetPriority** returns the priority of an active thread specified by the parameter _thread_id._

Possible osPriority_t return values:
    - **priority:** the priority of the specified thread.
    - **osPriorityError:** priority cannot be determined or is illegal. It is also returned when the function is called from
      Interrupt Service Routines.

**Note:** This function **cannot** be called from Interrupt Service Routines.

**Code Example**
```
#include "cmsis_os2.h"
 
void Thread_1 (void const *arg) {               // Thread function
  osThreadId_t id;                              // id for the currently running thread
  osPriority_t priority;                        // thread priority
   
  id = osThreadGetId();                         // Obtain ID of current running thread
  priority = osThreadGetPriority(id);           // Obtain the thread priority
}
```
