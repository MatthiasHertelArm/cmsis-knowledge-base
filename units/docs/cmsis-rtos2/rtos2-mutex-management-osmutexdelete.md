---
id: "rtos2-mutex-management-osmutexdelete"
type: "concept"
domain: "rtos"
title: "Mutex Management: osMutexDelete"
summary: "The function osMutexDelete deletes a mutex object specified by parameter mutex_id. It releases internal memory obtained for mutex handling. After this call, the mutex_id is no longer valid and cannot be used."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mutex.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mutex.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osMutexDelete (osMutexId_t mutex_id)
```


The function **osMutexDelete** deletes a mutex object specified by parameter _mutex_id._ It releases internal memory obtained
for mutex handling. After this call, the _mutex_id_ is no longer valid and cannot be used. The mutex may be created again
using the function osMutexNew.

Possible osStatus_t return values:
 - **osOK:** the mutex object has been deleted.
 - **osErrorParameter:** parameter **mutex_id** is `NULL` or invalid.
 - **osErrorResource:** the mutex is in an invalid state.
 - **osErrorISR:** **osMutexDelete** cannot be called from interrupt service routines.
 - **osErrorSafetyClass:** the calling thread safety class is lower than the safety class of the specified mutex.

**Note:** This function **cannot** be called from Interrupt Service Routines.

**Code Example**
```
#include "cmsis_os2.h"
 
osMutexId_t mutex_id;                           // Mutex id populated by the function osMutexNew()
 
void DeleteMutex (osMutexId_t mutex_id)  {
  osStatus_t status;
 
  if (mutex_id != NULL)  {
    status = osMutexDelete(mutex_id);
    if (status != osOK)  {
      // handle failure code
    }
  }
}
```
