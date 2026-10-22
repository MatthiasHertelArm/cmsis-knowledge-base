---
id: "rtos2-semaphores-ossemaphoreacquire"
type: "concept"
domain: "rtos"
title: "Semaphores: osSemaphoreAcquire"
summary: "The blocking function osSemaphoreAcquire waits until a token of the semaphore object specified by parameter semaphore_id becomes available. If a token is available, the function instantly returns and decrements the token count."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_sema.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_sema.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osSemaphoreAcquire (osSemaphoreId_t semaphore_id, uint32_t timeout)
```


The blocking function **osSemaphoreAcquire** waits until a token of the semaphore object specified by parameter
_semaphore_id_ becomes available. If a token is available, the function instantly returns and decrements the token count. 

The parameter _timeout_ specifies how long the system waits to acquire the token. While the system waits, the thread
that is calling this function is put into the BLOCKED state. The parameter CMSIS_RTOS_TimeOutValue
"timeout" can have the following values:
 - when _timeout_ is `0`, the function returns instantly (i.e. try semantics).
 - when _timeout_ is set to **osWaitForever** the function will wait for an infinite time until the semaphore becomes
   available (i.e. wait semantics).
 - all other values specify a time in kernel ticks for a timeout (i.e. timed-wait semantics).

Possible osStatus_t return values:
 - **osOK:** the token has been obtained and the token count decremented.
 - **osErrorTimeout:** the token could not be obtained in the given time.
 - **osErrorResource:** the token could not be obtained when no _timeout_ was specified.
 - **osErrorParameter:** the parameter _semaphore_id_ is `NULL` or invalid.
 - **osErrorSafetyClass:** the calling thread safety class is lower than the safety class of the specified semaphore.

**Note:** May be called from Interrupt Service Routines if the parameter _timeout_ is set to
`0`.
 
**Code Example**

Refer to osSemaphoreNew.
