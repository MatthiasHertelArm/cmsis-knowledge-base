---
id: "rtos2-thread-management-osthreadsetaffinitymask"
type: "concept"
domain: "rtos"
title: "Thread Management: osThreadSetAffinityMask"
summary: "The function osThreadSetAffinityMask sets the affinity mask of the thread specified by parameter thread_id to the mask specified by the parameter affinity_mask. The mask indicates on which processor(s) the thread should run (0 indicates on any processor)."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osThreadSetAffinityMask (osThreadId_t thread_id, uint32_t affinity_mask);
```


The function **osThreadSetAffinityMask** sets the affinity mask of the thread specified by parameter _thread_id_ to the mask specified by the parameter _affinity_mask._ 
The mask indicates on which processor(s) the thread should run (`0` indicates on any processor).

Possible osStatus_t return values:
    - **osOK:** the affinity mask of the specified thread has been set successfully.
    - **osErrorParameter:** _thread_id_ is `NULL` or invalid or _affinity_mask_ is incorrect.
    - **osErrorResource:** the thread is in an invalid state.
    - **osErrorISR:** the function **osThreadSetAffinityMask** cannot be called from interrupt service routines.
    - **osErrorSafetyClass:** the calling thread safety class is lower than the safety class of the specified thread.

**Note:** This function **cannot** be called from Interrupt Service Routines.

**Code Example**
```
#include "cmsis_os2.h"
 
void Thread_1 (void const *arg) {               // Thread function
  osThreadId_t id;                              // id for the currently running thread
  osStatus_t   status;                          // status of the executed function
 
  id = osThreadGetId();                         // Obtain ID of current running thread
 
  status = osThreadSetAffinityMask(id, osThreadProcessor(1));  // run thread processor #1
  if (status == osOK) {
    // Thread affinity mask set to processor number 1
  }
  else {
    // Failed to set the affinity mask
  }
}
```
