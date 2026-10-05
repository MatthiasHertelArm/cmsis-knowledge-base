---
id: "frb-8-resource-management-8-3-1-the-xsemaphorecreatemutex-api-func"
type: "concept"
domain: "rtos"
title: "8 Resource Management: 8.3 Mutexes (and Binary Semaphores) / 8.3.1 The xSemaphoreCreateMutex() API Function"
summary: "Part of: 8.3 Mutexes (and Binary Semaphores)"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch08.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch08.md#8-3-1-the-xsemaphorecreatemutex-api-function"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 8.3 Mutexes (and Binary Semaphores)_

FreeRTOS also includes the `xSemaphoreCreateMutexStatic()`
function, which allocates the memory required to create a mutex
statically at compile time: A mutex is a type of semaphore. Handles to
all the various types of FreeRTOS semaphore are stored in a variable of
type `SemaphoreHandle_t`.

Before a mutex can be used, it must be created. To create a mutex type
semaphore, use the `xSemaphoreCreateMutex()` API function.




```c
SemaphoreHandle_t xSemaphoreCreateMutex( void );
```
***Listing 8.10*** *The xSemaphoreCreateMutex() API function prototype*


**xSemaphoreCreateMutex() return value**

- Return value

  If NULL is returned, then the mutex could not be created because
  there is insufficient heap memory available for FreeRTOS to allocate the
  mutex data structures. Chapter 3 provides more information on heap
  memory management.

  A non-NULL return value indicates that the mutex has been created
  successfully. The returned value should be stored as the handle to the
  created mutex.



---
***Example 8.1*** *Rewriting vPrintString() to use a semaphore*

---

This example creates a new version of `vPrintString()` called
`prvNewPrintString()`, then calls the new function from multiple tasks.
`prvNewPrintString()` is functionally identical to `vPrintString()`, but
controls access to standard out using a mutex, rather than by locking
the scheduler. The implementation of `prvNewPrintString()` is shown in
Listing 8.11.




```c
static void prvNewPrintString( const char *pcString )
{
    /* The mutex is created before the scheduler is started, so already exists
       by the time this task executes.

       Attempt to take the mutex, blocking indefinitely to wait for the mutex
       if it is not available straight away. The call to xSemaphoreTake() will
       only return when the mutex has been successfully obtained, so there is 
       no need to check the function return value. If any other delay period 
       was used then the code must check that xSemaphoreTake() returns pdTRUE 
       before accessing the shared resource (which in this case is standard 
       out). As noted earlier in this book, indefinite time outs are not 
       recommended for production code. */
    xSemaphoreTake( xMutex, portMAX_DELAY );
    {
        /* The following line will only execute once the mutex has been 
           successfully obtained. Standard out can be accessed freely now as 
           only one task can have the mutex at any one time. */
        printf( "%s", pcString );
        fflush( stdout );

        /* The mutex MUST be given back! */
    }
    xSemaphoreGive( xMutex );
}
```
***Listing 8.11*** *The implementation of prvNewPrintString()*


`prvNewPrintString()` is called repeatedly by two instances of a task
implemented by `prvPrintTask()`. A random delay time is used between each
call. The task parameter is used to pass a unique string into each
instance of the task. The implementation of `prvPrintTask()` is shown in
Listing 8.12.




```c
static void prvPrintTask( void *pvParameters )
{
    char *pcStringToPrint;
    const TickType_t xMaxBlockTimeTicks = 0x20;

    /* Two instances of this task are created. The string printed by the task 
       is passed into the task using the task's parameter. The parameter is 
       cast to the required type. */
    pcStringToPrint = ( char * ) pvParameters;

    for( ;; )
    {
        /* Print out the string using the newly defined function. */
        prvNewPrintString( pcStringToPrint );

        /* Wait a pseudo random time. Note that rand() is not necessarily
           reentrant, but in this case it does not really matter as the code 
           does not care what value is returned. In a more secure application 
           a version of rand() that is known to be reentrant should be used - 
           or calls to rand() should be protected using a critical section. */
        vTaskDelay( ( rand() % xMaxBlockTimeTicks ) );
    }
}
```
***Listing 8.12*** *The implementation of prvPrintTask() for Example 8.1*


As normal, `main()` simply creates the mutex, creates the tasks, then
starts the scheduler. The implementation is shown in Listing 8.13.

The two instances of `prvPrintTask()` are created at different priorities,
so the lower priority task will sometimes be pre-empted by the higher
priority task. As a mutex is used to ensure each task gets mutually
exclusive access to the terminal, even when pre-emption occurs, the
strings that are displayed will be correct and in no way corrupted. The
frequency of pre-emption can be increased by reducing the maximum time
the tasks spend in the Blocked state, which is set by the
`xMaxBlockTimeTicks` constant.

Notes specific to using Example 8.1 with the FreeRTOS Windows port:

- Calling `printf()` generates a Windows system call. Windows system
  calls are outside the control of FreeRTOS, and can introduce
  instability.

- The way in which Windows system calls execute mean it is rare to see
  a corrupted string, even when the mutex is not used.




```c
int main( void )
{
    /* Before a semaphore is used it must be explicitly created. In this
       example a mutex type semaphore is created. */
    xMutex = xSemaphoreCreateMutex();

    /* Check the semaphore was created successfully before creating the
       tasks. */
    if( xMutex != NULL )
    {
        /* Create two instances of the tasks that write to stdout. The string
           they write is passed in to the task as the task's parameter. The 
           tasks are created at different priorities so some pre-emption will 
           occur. */
        xTaskCreate( prvPrintTask, "Print1", 1000,
                     "Task 1 ***************************************\r\n",
                     1, NULL );

        xTaskCreate( prvPrintTask, "Print2", 1000,
                     "Task 2 ---------------------------------------\r\n", 
                     2, NULL );

        /* Start the scheduler so the created tasks start executing. */
        vTaskStartScheduler();
    }

    /* If all is well then main() will never reach here as the scheduler will
       now be running the tasks. If main() does reach here then it is likely 
       that there was insufficient heap memory available for the idle task to 
       be created.  Chapter 3 provides more information on heap memory 
       management. */
    for( ;; );
}
```
***Listing 8.13*** *The implementation of main() for Example 8.1*


The output produced when Example 8.1 is executed is shown in Figure 8.2. A
possible execution sequence is described in Figure 8.3.



* * *
   
***Figure 8.2*** *The output produced when Example 8.1 is executed*
* * *

Figure 8.2 shows that, as expected, there is no corruption in the strings
that are displayed on the terminal. The random ordering is a result of
the random delay periods used by the tasks.




* * *
   
***Figure 8.3*** *A possible sequence of execution for Example 8.1*
* * *
