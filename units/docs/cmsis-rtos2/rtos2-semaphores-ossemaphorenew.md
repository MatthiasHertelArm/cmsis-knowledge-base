---
id: "rtos2-semaphores-ossemaphorenew"
type: "concept"
domain: "rtos"
title: "Semaphores: osSemaphoreNew"
summary: "The function osSemaphoreNew creates and initializes a semaphore object that is used to manage access to shared resources and returns the pointer to the semaphore object identifier or NULL in case of an error."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_sema.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_sema.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osSemaphoreId_t osSemaphoreNew (uint32_t max_count, uint32_t initial_count, const osSemaphoreAttr_t *attr)
```


The function **osSemaphoreNew** creates and initializes a semaphore object that is used to manage access to shared resources
and returns the pointer to the semaphore object identifier or `NULL` in case of an error. It can be safely called
before the RTOS is started (call to osKernelStart), but not before it is initialized (call to osKernelInitialize).

The parameter **max_count** specifies the maximum number of available tokens. A **max_count** value of 1 creates a binary
semaphore.

The parameter **initial_count** sets the initial number of available tokens.

The parameter **attr** specifies additional semaphore attributes. Default attributes will be used if set to `NULL`.

**Note:** This function **cannot** be called from Interrupt Service Routines.

**Code Example**
```
#include "cmsis_os2.h"                          // CMSIS RTOS header file
 
osSemaphoreId_t sid_Semaphore;                  // semaphore id
 
osThreadId_t tid_Thread_Semaphore;              // thread id
 
void Thread_Semaphore (void *argument);         // thread function
 
int Init_Semaphore (void) {
 
  sid_Semaphore = osSemaphoreNew(2U, 2U, NULL);
  if (sid_Semaphore == NULL) {
    ; // Semaphore object not created, handle failure
  }
 
  tid_Thread_Semaphore = osThreadNew(Thread_Semaphore, NULL, NULL);
  if (tid_Thread_Semaphore == NULL) {
    return(-1);
  }
 
  return(0);
}
 
void Thread_Semaphore (void *argument) {
  osStatus_t val;
 
  while (1) {
    ; // Insert thread code here...
 
    val = osSemaphoreAcquire(sid_Semaphore, 10U);       // wait for max. 10 ticks for semaphore token to get available
    switch (val) {
      case osOK:
        ; // Use protected code here...
        osSemaphoreRelease(sid_Semaphore);              // return a token back to a semaphore
        break;
      case osErrorResource:
        break;
      case osErrorParameter:
        break;
      default:
        break;
    }
 
    osThreadYield();                                    // suspend thread
  }
}
```
