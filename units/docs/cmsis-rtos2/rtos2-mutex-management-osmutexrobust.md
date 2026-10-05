---
id: "rtos2-mutex-management-osmutexrobust"
type: "concept"
domain: "rtos"
title: "Mutex Management: osMutexRobust"
summary: "Robust mutexes are automatically released if the owning thread is terminated (either by osThreadExit or osThreadTerminate). Non-robust mutexes are not released and the user must assure mutex release manually."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mutex.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mutex.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osMutexRobust
```


Robust flag in osMutexAttr_t.

Robust mutexes are automatically released if the owning thread is terminated (either by
osThreadExit or osThreadTerminate). Non-robust mutexes are not released and the user must
assure mutex release manually.

**Code Example**

This example reveals a blocked mutex if osMutexRobust is removed.

```
#include "cmsis_os2.h"
 
osMutexId_t mutex_id;
 
const osMutexAttr_t Thread_Mutex_attr = {
  "myThreadMutex",     // human readable mutex name
  osMutexRobust,       // attr_bits
  NULL,                // memory for control block   
  0U                   // size for control block
};
 
void Thread(void *argument) {
  osMutexAcquire(mutex_id, osWaitForever);
  osThreadExit();
}
```

Due to osMutexRobust the mutex gets released automatically. A non-robust mutex would stay locked and cannot be released anymore.
