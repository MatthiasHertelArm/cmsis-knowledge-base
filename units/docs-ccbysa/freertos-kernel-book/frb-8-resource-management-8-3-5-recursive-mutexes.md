---
id: "frb-8-resource-management-8-3-5-recursive-mutexes"
type: "concept"
domain: "rtos"
title: "8 Resource Management: 8.3 Mutexes (and Binary Semaphores) / 8.3.5 Recursive Mutexes"
summary: "Part of: 8.3 Mutexes (and Binary Semaphores)"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch08.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch08.md#8-3-5-recursive-mutexes"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 8.3 Mutexes (and Binary Semaphores)_

It is also possible for a task to deadlock with itself. This will happen
if a task attempts to take the same mutex more than once, without first
returning the mutex. Consider the following scenario:

1. A task successfully obtains a mutex.

2. While holding the mutex, the task calls a library function.

3. The implementation of the library function attempts to take the same
   mutex, and enters the Blocked state to wait for the mutex to become
   available.

At the end of this scenario the task is in the Blocked state to wait for
the mutex to be returned, but the task is already the mutex holder. A
deadlock has occurred because the task is in the Blocked state to wait
for itself.

This type of deadlock can be avoided by using a recursive mutex in place
of a standard mutex. A recursive mutex can be 'taken' more than once by
the same task, and will be returned only after one call to 'give' the
recursive mutex has been executed for every preceding call to 'take' the
recursive mutex.

Standard mutexes and recursive mutexes are created and used in a similar
way:

- Standard mutexes are created using `xSemaphoreCreateMutex()`.
  Recursive mutexes are created using
  `xSemaphoreCreateRecursiveMutex()`. The two API functions have the
  same prototype.

- Standard mutexes are 'taken' using `xSemaphoreTake()`. Recursive
  mutexes are 'taken' using `xSemaphoreTakeRecursive()`. The two API
  functions have the same prototype.

- Standard mutexes are 'given' using `xSemaphoreGive()`. Recursive
  mutexes are 'given' using `xSemaphoreGiveRecursive()`. The two API
  functions have the same prototype.

Listing 8.14 demonstrates how to create and use a recursive mutex.




```c
/* Recursive mutexes are variables of type SemaphoreHandle_t. */
SemaphoreHandle_t xRecursiveMutex;

/* The implementation of a task that creates and uses a recursive mutex. */
void vTaskFunction( void *pvParameters )
{
    const TickType_t xMaxBlock20ms = pdMS_TO_TICKS( 20 );

    /* Before a recursive mutex is used it must be explicitly created. */
    xRecursiveMutex = xSemaphoreCreateRecursiveMutex();

    /* Check the semaphore was created successfully. configASSERT() is 
       described in section 12.2. */
    configASSERT( xRecursiveMutex );

    /* As per most tasks, this task is implemented as an infinite loop. */
    for( ;; )
    {
        /* ... */

        /* Take the recursive mutex. */
        if( xSemaphoreTakeRecursive( xRecursiveMutex, xMaxBlock20ms ) == pdPASS )
        {
            /* The recursive mutex was successfully obtained. The task can now
               access the resource the mutex is protecting. At this point the 
               recursive call count (which is the number of nested calls to 
               xSemaphoreTakeRecursive()) is 1, as the recursive mutex has 
               only been taken once. */

            /* While it already holds the recursive mutex, the task takes the 
               mutex again. In a real application, this is only likely to occur
               inside a sub-function called by this task, as there is no 
               practical reason to knowingly take the same mutex more than 
               once. The calling task is already the mutex holder, so the 
               second call to xSemaphoreTakeRecursive() does nothing more than
               increment the recursive call count to 2. */
            xSemaphoreTakeRecursive( xRecursiveMutex, xMaxBlock20ms );

            /* ... */

            /* The task returns the mutex after it has finished accessing the
               resource the mutex is protecting. At this point the recursive 
               call count is 2, so the first call to xSemaphoreGiveRecursive()
               does not return the mutex. Instead, it simply decrements the 
               recursive call count back to 1. */
            xSemaphoreGiveRecursive( xRecursiveMutex );

            /* The next call to xSemaphoreGiveRecursive() decrements the 
               recursive call count to 0, so this time the recursive mutex is 
               returned. */
            xSemaphoreGiveRecursive( xRecursiveMutex );

            /* Now one call to xSemaphoreGiveRecursive() has been executed for
               every proceeding call to xSemaphoreTakeRecursive(), so the task
               is no longer the mutex holder. */
        }
    }
}
```
***Listing 8.14*** *Creating and using a recursive mutex*
