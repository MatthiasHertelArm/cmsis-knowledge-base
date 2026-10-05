---
id: "frb-12-developer-support-12-5-7-generating-and-displaying-run-tim"
type: "concept"
domain: "rtos"
title: "12 Developer Support: 12.5 Viewing Run-time and Task State Information / 12.5.7 Generating and Displaying Run-Time Statistics, a Worked Example"
summary: "Part of: 12.5 Viewing Run-time and Task State Information"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch12.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch12.md#12-5-7-generating-and-displaying-run-time-statistics-a-worked-example"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 12.5 Viewing Run-time and Task State Information_

This example uses a hypothetical 16-bit timer to generate a 32-bit
run-time statistics clock. The counter is configured to generate an
interrupt each time the 16-bit value reaches its maximum
value—effectively creating an overflow interrupt. The interrupt service
routine counts the number of overflow occurrences.

The 32-bit value is created by using the count of overflow occurrences
as the two most significant bytes of the 32-bit value, and the current
16-bit counter value as the two least significant bytes of the 32-bit
value. Pseudo code for the interrupt service routine is shown in Listing
12.10.




```c
void TimerOverflowInterruptHandler( void )
{
    /* Just count the number of interrupts. */
    ulOverflowCount++;

    /* Clear the interrupt. */
    ClearTimerInterrupt();
}
```
***Listing 12.10*** *16-bit timer overflow interrupt handler used to count timer overflows*

Listing 12.11 shows the lines added to FreeRTOSConfig.h to enable the
collection of run-time statistics.




```c
/* Set configGENERATE_RUN_TIME_STATS to 1 to enable collection of run-time 
   statistics. When this is done, both portCONFIGURE_TIMER_FOR_RUN_TIME_STATS()
   and portGET_RUN_TIME_COUNTER_VALUE() or 
   portALT_GET_RUN_TIME_COUNTER_VALUE(x) must also be defined. */
#define configGENERATE_RUN_TIME_STATS 1

/* portCONFIGURE_TIMER_FOR_RUN_TIME_STATS() is defined to call the function 
   that sets up the hypothetical 16-bit timer (the function's implementation 
   is not shown). */
void vSetupTimerForRunTimeStats( void );
#define portCONFIGURE_TIMER_FOR_RUN_TIME_STATS()  vSetupTimerForRunTimeStats()

/* portALT_GET_RUN_TIME_COUNTER_VALUE() is defined to set its parameter to the
   current run-time counter/time value. The returned time value is 32-bits 
   long, and is formed by shifting the count of 16-bit timer overflows into 
   the top two bytes of a 32-bit number, then bitwise ORing the result with 
   the current 16-bit counter value. */
#define portALT_GET_RUN_TIME_COUNTER_VALUE( ulCountValue )                  \
{                                                                           \
    extern volatile unsigned long ulOverflowCount;                          \
                                                                            \
    /* Disconnect the clock from the counter so it does not change          \
       while its value is being used. */                                    \
    PauseTimer();                                                           \
                                                                            \
    /* The number of overflows is shifted into the most significant         \
       two bytes of the returned 32-bit value. */                           \
    ulCountValue = ( ulOverflowCount << 16UL );                             \
                                                                            \
    /* The current counter value is used as the two least significant       \
       bytes of the returned 32-bit value. */                               \
    ulCountValue |= ( unsigned long ) ReadTimerCount();                     \
                                                                            \
    /* Reconnect the clock to the counter. */                               \
    ResumeTimer();                                                          \
}
```
***Listing 12.11*** *Macros added to FreeRTOSConfig.h to enable the collection of run-time statistics*

The task shown in Listing 12.12 prints out the collected run-time statistics every 5 seconds.




```c
#define RUN_TIME_STATS_STRING_BUFFER_LENGTH       512

/* For clarity, calls to fflush() have been omitted from this code listing. */
static void prvStatsTask( void *pvParameters )
{
    TickType_t xLastExecutionTime;

    /* The buffer used to hold the formatted run-time statistics text needs to
       be quite large. It is therefore declared static to ensure it is not
       allocated on the task stack. This makes this function non re-entrant. */
    static signed char cStringBuffer[ RUN_TIME_STATS_STRING_BUFFER_LENGTH ];

    /* The task will run every 5 seconds. */
    const TickType_t xBlockPeriod = pdMS_TO_TICKS( 5000 );

    /* Initialize xLastExecutionTime to the current time. This is the only
       time this variable needs to be written to explicitly. Afterwards it is 
       updated internally within the vTaskDelayUntil() API function. */
    xLastExecutionTime = xTaskGetTickCount();

    /* As per most tasks, this task is implemented in an infinite loop. */
    for( ;; )
    {
        /* Wait until it is time to run this task again. */
        xTaskDelayUntil( &xLastExecutionTime, xBlockPeriod );

        /* Generate a text table from the run-time stats. This must fit into
           the cStringBuffer array. */
        vTaskGetRunTimeStatistics( cStringBuffer, RUN_TIME_STATS_STRING_BUFFER_LENGTH );

        /* Print out column headings for the run-time stats table. */
        printf( "\nTask\t\tAbs\t\t\t%%\n" );
        printf( "-------------------------------------------------------------\n" );

        /* Print out the run-time stats themselves. The table of data contains
           multiple lines, so the vPrintMultipleLines() function is called 
           instead of calling printf() directly. vPrintMultipleLines() simply 
           calls printf() on each line individually, to ensure the line 
           buffering works as expected. */ 
        vPrintMultipleLines( cStringBuffer );
    }
}
```
***Listing 12.12*** *The task that prints out the collected run-time statistics*
