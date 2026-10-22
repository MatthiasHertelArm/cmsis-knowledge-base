---
id: "rtos2-thread-management-osthreadgetaffinitymask"
type: "concept"
domain: "rtos"
title: "Thread Management: osThreadGetAffinityMask"
summary: "The function osThreadGetAffinityMask returns the affinity mask of the thread specified by parameter thread_id. In case of an error, it returns 0."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t osThreadGetAffinityMask (osThreadId_t thread_id);
```


The function **osThreadGetAffinityMask** returns the affinity mask of the thread specified by parameter _thread_id._ 
In case of an error, it returns `0`.

**Note:** This function **cannot** be called from Interrupt Service Routines.

**Code Example**
```
#include "cmsis_os2.h"
 
void Thread_1 (void const *arg) {               // Thread function
  osThreadId_t id;                              // id for the currently running thread
  uint32_t     affinity_mask;                   // thread affinity mask
   
  id = osThreadGetId();                         // Obtain ID of current running thread
  affinity_mask = osThreadGetAffinityMask(id);  // Obtain the thread affinity mask
}
```
