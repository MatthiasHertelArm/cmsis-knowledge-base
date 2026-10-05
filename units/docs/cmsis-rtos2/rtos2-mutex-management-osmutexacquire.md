---
id: "rtos2-mutex-management-osmutexacquire"
type: "concept"
domain: "rtos"
title: "Mutex Management: osMutexAcquire"
summary: "The blocking function osMutexAcquire waits until a mutex object specified by parameter mutexid becomes available. If no other thread has obtained the mutex, the function instantly returns and blocks the mutex object."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mutex.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mutex.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osMutexAcquire (osMutexId_t mutex_id, uint32_t timeout)
```


The blocking function **osMutexAcquire** waits until a mutex object specified by parameter _mutex_id_ becomes available. If
no other thread has obtained the mutex, the function instantly returns and blocks the mutex object. 

The parameter _timeout_ specifies how long the system waits to acquire the mutex. While the system waits, the thread that is
calling this function is put into the BLOCKED state. The parameter timeout
can have the following values:
 - when _timeout_ is `0`, the function returns instantly (i.e. try semantics).
 - when _timeout_ is set to **osWaitForever** the function will wait for an infinite time until the mutex becomes available (i.e. wait semantics).
 - all other values specify a time in kernel ticks for a timeout (i.e. timed-wait semantics).

Possible osStatus_t return values:
 - **osOK:** the mutex has been obtained.
 - **osErrorTimeout:** the mutex could not be obtained in the given time.
 - **osErrorResource:** the mutex could not be obtained when no _timeout_ was specified.
 - **osErrorParameter:** parameter **mutex_id** is `NULL` or invalid.
 - **osErrorISR:** cannot be called from interrupt service routines.
 - **osErrorSafetyClass:** the calling thread safety class is lower than the safety class of the specified mutex.

**Note:** This function **cannot** be called from Interrupt Service Routines.

**Code Example**
```
#include "cmsis_os2.h"
 
void WaitMutex (void) {
  osMutexId_t mutex_id;
  osStatus_t  status;
 
  mutex_id = osMutexNew(NULL);
  if (mutex_id != NULL) {
    status = osMutexAcquire(mutex_id, 0U);
    if (status != osOK)  {
      // handle failure code
    }
  }
}
```
