---
id: "rtos2-semaphores-ossemaphorerelease"
type: "concept"
domain: "rtos"
title: "Semaphores: osSemaphoreRelease"
summary: "The function osSemaphoreRelease releases a token of the semaphore object specified by parameter semaphore_id. Tokens can only be released up to the maximum count specified at creation time, see osSemaphoreNew."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_sema.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_sema.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osSemaphoreRelease (osSemaphoreId_t semaphore_id)
```


The function **osSemaphoreRelease** releases a token of the semaphore object specified by parameter _semaphore_id._ Tokens
can only be released up to the maximum count specified at creation time, see osSemaphoreNew. Other threads that
currently wait for a token of this semaphore object will be put into the READY state.

Possible osStatus_t return values:
 - **osOK:** the token has been released and the count incremented.
 - **osErrorResource:** the token could not be released (maximum token count has been reached).
 - **osErrorParameter:** the parameter _semaphore_id_ is `NULL` or invalid.
 - **osErrorSafetyClass:** the calling thread safety class is lower than the safety class of the specified semaphore.

**Note:** This function may be called from Interrupt Service Routines.

**Code Example**

Refer to osSemaphoreNew.
