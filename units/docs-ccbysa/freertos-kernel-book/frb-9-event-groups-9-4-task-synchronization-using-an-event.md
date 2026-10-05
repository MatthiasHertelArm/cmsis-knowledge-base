---
id: "frb-9-event-groups-9-4-task-synchronization-using-an-event"
type: "concept"
domain: "rtos"
title: "9 Event Groups: 9.4 Task Synchronization Using an Event Group"
summary: "Sometimes the design of an application requires two or more tasks to synchronize with each other."
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch09.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch09.md#9-4-task-synchronization-using-an-event-group"
license: "CC-BY-SA-4.0"
mode: "V"
---

Sometimes the design of an application requires two or more tasks to
synchronize with each other. For example, consider a design where Task A
receives an event, then delegates some of the processing necessitated by
the event to three other tasks: Task B, Task C and Task D. If Task A
cannot receive another event until tasks B, C and D have all completed
processing the previous event, then all four tasks will need to
synchronize with each other. Each task's synchronization point will be
after that task has completed its processing, and cannot proceed further
until each of the other tasks have done the same. Task A can only
receive another event after all four tasks have reached their
synchronization point.

A less abstract example of the need for this type of task
synchronization is found in one of the FreeRTOS+TCP demonstration
projects. The demonstration shares a TCP socket between two tasks; one
task sends data to the socket, and a different task receives data from
the same socket[^25]. It is not safe for either task to close the TCP
socket until it is sure the other task will not attempt to access the
socket again. If either of the two tasks wishes to close the socket,
then it must inform the other task of its intent, and then wait for the
other task to stop using the socket before proceeding. The scenario
where it is the task that sends data to the socket that wishes to close
the socket is demonstrated by the pseudo code shown in Listing 9.10.

[^25]: At the time of writing, this is the only way a single
FreeRTOS+TCP socket can be shared between tasks.

The scenario demonstrated by Listing 9.10 is trivial, as there are only
two tasks that need to synchronize with each other, but it is easy to
see how the scenario would become more complex, and require more tasks
to join the synchronization, if other tasks were performing processing
that was dependent on the socket being open.




```c
void SocketTxTask( void *pvParameters )
{
    xSocket_t xSocket;
    uint32_t ulTxCount = 0UL;

    for( ;; )
    {
        /* Create a new socket. This task will send to this socket, and another
           task will receive from this socket. */
        xSocket = FreeRTOS_socket( ... );

        /* Connect the socket. */
        FreeRTOS_connect( xSocket, ... );

        /* Use a queue to send the socket to the task that receives data. */
        xQueueSend( xSocketPassingQueue, &xSocket, portMAX_DELAY );

        /* Send 1000 messages to the socket before closing the socket. */
        for( ulTxCount = 0; ulTxCount < 1000; ulTxCount++ )
        {
            if( FreeRTOS_send( xSocket, ... ) < 0 )
            {
                /* Unexpected error - exit the loop, after which the socket
                   will be closed. */
                break;
            }
        }

        /* Let the Rx task know the Tx task wants to close the socket. */
        TxTaskWantsToCloseSocket();

        /* This is the Tx task's synchronization point. The Tx task waits here
           for the Rx task to reach its synchronization point. The Rx task will
           only reach its synchronization point when it is no longer using the
           socket, and the socket can be closed safely. */
        xEventGroupSync( ... );

        /* Neither task is using the socket. Shut down the connection, then
           close the socket. */
        FreeRTOS_shutdown( xSocket, ... );
        WaitForSocketToDisconnect();
        FreeRTOS_closesocket( xSocket );
    }
}
/*-----------------------------------------------------------*/

void SocketRxTask( void *pvParameters )
{
    xSocket_t xSocket;

    for( ;; )
    {
        /* Wait to receive a socket that was created and connected by the Tx
           task. */
        xQueueReceive( xSocketPassingQueue, &xSocket, portMAX_DELAY );

        /* Keep receiving from the socket until the Tx task wants to close the
           socket. */
        while( TxTaskWantsToCloseSocket() == pdFALSE )
        {
           /* Receive then process data. */
           FreeRTOS_recv( xSocket, ... );
           ProcessReceivedData();
        }

        /* This is the Rx task's synchronization point - it only reaches here
           when it is no longer using the socket, and it is therefore safe for
           the Tx task to close the socket. */
        xEventGroupSync( ... );
    }
}
```
***Listing 9.11*** *Pseudo code for two tasks that synchronize with each other to ensure a shared TCP socket is no longer in use by either task before the socket is closed*


An event group can be used to create a synchronization point:

- Each task that must participate in the synchronization is assigned a
  unique event bit within the event group.

- Each task sets its own event bit when it reaches the synchronization
  point.

- Having set its own event bit, each task blocks on the event group to
  wait for the event bits that represent all the other synchronizing
  tasks to also become set.

However, the `xEventGroupSetBits()` and `xEventGroupWaitBits()` API
functions cannot be used in this scenario. If they were used, then the
setting of a bit (to indicate a task had reached its synchronization
point) and the testing of bits (to determine if the other synchronizing
tasks had reached their synchronization point) would be performed as two
separate operations. To see why that would be a problem, consider a
scenario where Task A, Task B and Task C attempt to synchronize using an
event group:

1. Task A and Task B have already reached the synchronization point, so
   their event bits are set in the event group, and they are in the
   Blocked state to wait for task C's event bit to also become set.

2. Task C reaches the synchronization point, and uses
   `xEventGroupSetBits()` to set its bit in the event group. As soon as
   Task C's bit is set, Task A and Task B leave the Blocked state, and
   clear all three event bits.

3. Task C then calls `xEventGroupWaitBits()` to wait for all three event
   bits to become set, but by that time, all three event bits have
   already been cleared, Task A and Task B have left their respective
   synchronization points, and so the synchronization has failed.

To successfully use an event group to create a synchronization point,
the setting of an event bit, and the subsequent testing of event bits,
must be performed as a single uninterruptable operation. The
`xEventGroupSync()` API function is provided for that purpose.
