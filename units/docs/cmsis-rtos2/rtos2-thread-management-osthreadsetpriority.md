---
id: "rtos2-thread-management-osthreadsetpriority"
type: "concept"
domain: "rtos"
title: "Thread Management: osThreadSetPriority"
summary: "The function osThreadSetPriority changes the priority of an active thread specified by the parameter thread_id to the priority specified by the parameter priority."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osThreadSetPriority (osThreadId_t thread_id, osPriority_t priority)
```


The function **osThreadSetPriority** changes the priority of an active thread specified by the parameter _thread_id_ to the
priority specified by the parameter _priority._ 

Possible osStatus_t return values:
    - **osOK:** the priority of the specified thread has been changed successfully.
    - **osErrorParameter:** _thread_id_ is `NULL` or invalid or _priority_ is incorrect.
    - **osErrorResource:** the thread is in an invalid state.
    - **osErrorISR:** the function **osThreadSetPriority** cannot be called from interrupt service routines.
    - **osErrorSafetyClass:** the calling thread safety class is lower than the safety class of the specified thread.

**Note:** This function **cannot** be called from Interrupt Service Routines.

**Code Example**
```
#include "cmsis_os2.h"
 
void Thread_1 (void const *arg) {               // Thread function
  osThreadId_t id;                              // id for the currently running thread
  osStatus_t   status;                          // status of the executed function
 
  :
  id = osThreadGetId();                         // Obtain ID of current running thread
 
  status = osThreadSetPriority(id, osPriorityBelowNormal);  // Set thread priority
  if (status == osOK) {
    // Thread priority changed to BelowNormal
  }
  else {
    // Failed to set the priority
  }
  :
}
```
