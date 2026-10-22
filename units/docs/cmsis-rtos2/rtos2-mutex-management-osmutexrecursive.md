---
id: "rtos2-mutex-management-osmutexrecursive"
type: "concept"
domain: "rtos"
title: "Mutex Management: osMutexRecursive"
summary: "The same thread can consume a mutex multiple times without locking itself. Each time the owning thread acquires the mutex the lock count is incremented. The mutex must be released multiple times as well until the lock count reaches zero."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mutex.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mutex.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osMutexRecursive
```


Recursive flag in osMutexAttr_t.

The same thread can consume a mutex multiple times without locking itself.
Each time the owning thread acquires the mutex the lock count is incremented. The mutex must
be released multiple times as well until the lock count reaches zero. At reaching zero the
mutex is actually released and can be acquired by other threads.

**Note:** The maximum amount of recursive locks possible is implementation specific, i.e. the type size used for the lock count.
If the maximum amount of recursive locks is depleted mutex acquire might fail.

**Code Example**
```
#include "cmsis_os2.h"
 
osMutexId_t mutex_id; 
 
const osMutexAttr_t Thread_Mutex_attr = {
  "myThreadMutex",     // human readable mutex name
  osMutexRecursive,    // attr_bits
  NULL,                // memory for control block   
  0U                   // size for control block
};
 
// must be called from a thread context
void UseMutexRecursively(int count) {
  osStatus_t result = osMutexAcquire(mutex_id, osWaitForever);  // lock count is incremented, might fail when lock count is depleted
  if (result == osOK) {
    if (count < 10) {
      UseMutexRecursively(count + 1);
    }
    osMutexRelease(mutex_id); // lock count is decremented, actually releases the mutex on lock count zero
  }
}
```
