---
id: "rtos2-mutex-management-osmutexprioinherit"
type: "concept"
domain: "rtos"
title: "Mutex Management: osMutexPrioInherit"
summary: "Priority inheritance flag in osMutexAttr_t."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mutex.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mutex.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osMutexPrioInherit
```


Priority inheritance flag in osMutexAttr_t.

A mutex using priority inheritance protocol transfers a waiting threads priority to the
current mutex owner if the owners thread priority is lower. This assures that a low priority
thread does not block a high priority thread.

Otherwise a low priority thread might hold a mutex but is not granted execution time due to
another mid priority thread. Without priority inheritance the high priority thread waiting
for the mutex would be blocked by the mid priority thread, called priority inversion.

**Code Example**

This example reveals a blocked high priority thread if osMutexPrioInherit is removed.

```
#include "cmsis_os2.h"
 
osMutexId_t mutex_id;  
 
const osMutexAttr_t Thread_Mutex_attr = {
  "myThreadMutex",     // human readable mutex name
  osMutexPrioInherit,  // attr_bits
  NULL,                // memory for control block   
  0U                   // size for control block
};
 
void HighPrioThread(void *argument) {
  osDelay(1000U); // wait 1s until start actual work
  while(1) {
    osMutexAcquire(mutex_id, osWaitForever); // try to acquire mutex
    // do stuff
    osMutexRelease(mutex_id);
  }
}
 
void MidPrioThread(void *argument) {
  osDelay(1000U); // wait 1s until start actual work
  while(1) {
    // do non blocking stuff
  }
}
 
void LowPrioThread(void *argument) {
  while(1) {
    osMutexAcquire(mutex_id, osWaitForever);
    osDelay(5000U); // block mutex for 5s
    osMutexRelease(mutex_id);
    osDelay(5000U); // sleep for 5s
  }
}
```

During the first second the high and mid priority threads are delayed. Thus the low priority
thread can start its work, acquires the mutex and delays while holding it.

After the first second the high and mid priority threads become ready. Thus the high priority
thread gets precedence and tries to acquire the mutex. Because the mutex is already owned by
the low priority thread the high priority thread gets blocked.

Finally the mid priority thread gets executed and start doing a lot of non-blocking stuff,
i.e. it does not call any blocking RTOS functionality.

Without osMutexPrioInherit we would stuck here forever. Even if the low priority thread
gets ready after 5s. Due to its low priority the mid priority thread always gets precedence.
The effect called priority inversion leads to the mid priority thread blocking the high
priority thread indirectly.

Using osMutexPrioInherit as shown in the example code we get rid of this situation. Due
to the priority inheritance protocol the low priority thread inherits the high priority
while holding the mutex. Thus the low priority thread gets precedence over the mid priority
thread until it release the mutex. On osMutexRelease the high priority thread get ready and
is scheduled immediately.
