---
id: "rtos2-mutex-management-osmutexrelease"
type: "concept"
domain: "rtos"
title: "Mutex Management: osMutexRelease"
summary: "The function osMutexRelease releases a mutex specified by parameter mutexid. Other threads that currently wait for this mutex will be put into the READY state."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mutex.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mutex.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osMutexRelease (osMutexId_t mutex_id)
```


The function **osMutexRelease** releases a mutex specified by parameter _mutex_id._ Other threads that currently wait for
this mutex will be put into the READY state.

Possible osStatus_t return values:
 - **osOK:** the mutex has been correctly released.
 - **osErrorResource:** the mutex could not be released (mutex was not acquired or running thread is not the owner).
 - **osErrorParameter:** parameter **mutex_id** is `NULL` or invalid.
 - **osErrorISR:** **osMutexRelease** cannot be called from interrupt service routines.

**Note:** This function **cannot** be called from Interrupt Service Routines.

**Code Example**
```
#include "cmsis_os2.h"
 
osMutexId_t mutex_id;                                        // Mutex id populated by the function osMutexNew()
 
void ReleaseMutex (osMutexId_t mutex_id) {
  osStatus_t status;
 
  if (mutex_id != NULL)  {
    status = osMutexRelease(mutex_id);
    if (status != osOK)  {
      // handle failure code
    }
  }
}
```
