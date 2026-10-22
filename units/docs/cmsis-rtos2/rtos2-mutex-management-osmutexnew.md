---
id: "rtos2-mutex-management-osmutexnew"
type: "concept"
domain: "rtos"
title: "Mutex Management: osMutexNew"
summary: "The function osMutexNew creates and initializes a new mutex object and returns the pointer to the mutex object identifier or NULL in case of an error."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mutex.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_mutex.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osMutexId_t osMutexNew (const osMutexAttr_t *attr)
```


The function **osMutexNew** creates and initializes a new mutex object and returns the pointer to the mutex object identifier
or `NULL` in case of an error. It can be safely called before the RTOS is
started (call to osKernelStart), but not before it is initialized (call to osKernelInitialize).

The parameter _attr_ sets the mutex object attributes (refer to osMutexAttr_t). Default attributes will be used if set
to `NULL`.

**Note:** This function **cannot** be called from Interrupt Service Routines.

**Code Example**
```
#include "cmsis_os2.h"
 
osMutexId_t mutex_id;  
 
const osMutexAttr_t Thread_Mutex_attr = {
  "myThreadMutex",                          // human readable mutex name
  osMutexRecursive | osMutexPrioInherit,    // attr_bits
  NULL,                                     // memory for control block   
  0U                                        // size for control block
};
 
void CreateMutex (void)  {
  mutex_id = osMutexNew(&Thread_Mutex_attr);
  if (mutex_id != NULL)  {
    // Mutex object created
  }
}
```
