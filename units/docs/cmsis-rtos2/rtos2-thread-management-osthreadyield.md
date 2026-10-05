---
id: "rtos2-thread-management-osthreadyield"
type: "concept"
domain: "rtos"
title: "Thread Management: osThreadYield"
summary: "The function osThreadYield passes control to the next thread with the same priority that is in the READY state."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_thread.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osThreadYield (void)
```


The function **osThreadYield** passes control to the next thread with the same priority that is in the READY state. 
If there is no other thread with the same priority in state READY, then the current thread continues execution and
no thread switch occurs. **osThreadYield** does not set the thread to state BLOCKED. Thus no thread with a lower
priority will be scheduled even if threads in state READY are available.

Possible osStatus_t return values:
    - **osOK:** control has been passed to the next thread successfully.
    - **osError:** an unspecified error has occurred.
    - **osErrorISR:** the function **osThreadYield** cannot be called from interrupt service routines.

**Note:** This function **cannot** be called from Interrupt Service Routines.
**Note:** This function **has no impact** when called when the kernel is locked, see osKernelLock.

**Code Example**
```
#include "cmsis_os2.h"
 
void Thread_1 (void const *arg) {               // Thread function
  osStatus_t status;                            // status of the executed function
  :
  while (1) {
    status = osThreadYield();
    if (status != osOK) {
      // an error occurred
    }
  }
}
```
