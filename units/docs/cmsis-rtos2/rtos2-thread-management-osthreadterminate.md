---
id: "rtos2-thread-management-osthreadterminate"
type: "concept"
domain: "rtos"
title: "Thread Management: osThreadTerminate"
summary: "The function osThreadTerminate removes the thread specified by parameter thread_id from the list of active threads. If the thread is currently RUNNING, the thread terminates and the execution continues with the next READY thread."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osThreadTerminate (osThreadId_t thread_id)
```


The function **osThreadTerminate** removes the thread specified by parameter _thread_id_ from the list of active threads. If
the thread is currently RUNNING, the thread terminates and the execution continues with the next READY thread. If no
such thread exists, the function will not terminate the running thread, but return **osErrorResource.**

Possible osStatus_t return values:
    - **osOK:** the specified thread has been removed from the active thread list successfully.
    - **osErrorParameter:** _thread_id_ is `NULL` or invalid.
    - **osErrorResource:** the thread is in an invalid state or no other READY thread exists.
    - **osErrorISR:** the function **osThreadTerminate** cannot be called from interrupt service routines.
    - **osErrorSafetyClass:** the calling thread safety class is lower than the safety class of the specified thread.

**Note:** This function **cannot** be called from Interrupt Service Routines.
**Note:** Avoid calling the function with a **thread_id** that does not exist or has been terminated already.
**Note:** **osThreadTerminate** destroys non-joinable threads and removes their thread_id from the system. Subsequent access to the
thread_id (for example osThreadGetState) will return an osThreadError. Joinable threads will not be destroyed and
return the status osThreadTerminated until they are joined with osThreadJoin.

**Code Example**
```
#include "cmsis_os2.h"
 
void Thread_1 (void *arg);                      // function prototype for Thread_1
 
void ThreadTerminate_example (void) {
  osStatus_t status;
  osThreadId_t id;
 
  id = osThreadNew(Thread_1, NULL, NULL);       // create the thread
                                                // do something
  status = osThreadTerminate(id);               // stop the thread
  if (status == osOK) {
                                                // Thread was terminated successfully
  }
  else {
                                                // Failed to terminate a thread
  }
}
```
