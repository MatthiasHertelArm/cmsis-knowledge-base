---
id: "frb-10-task-notifications-10-3-9-task-notifications-used-directly"
type: "concept"
domain: "rtos"
title: "10 Task Notifications: 10.3 Using Task Notifications / 10.3.9 Task Notifications Used Directly Within an Application"
summary: "Part of: 10.3 Using Task Notifications"
status: "draft"
collection: "freertos-kernel-book"
source: "FreeRTOS/FreeRTOS-Kernel-Book@ba20b2f:ch10.md"
doc_source: "https://github.com/FreeRTOS/FreeRTOS-Kernel-Book/blob/ba20b2f/ch10.md#10-3-9-task-notifications-used-directly-within-an-application"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: 10.3 Using Task Notifications_

This section reinforces the power of task notifications by demonstrating
their use in a hypothetical application that includes the following
functionality:

- The application communicates across a slow internet connection to
  send data to, and request data from, a remote data server. From here
  on, the remote data server is referred to as the *cloud server*.

- After requesting data from the cloud server, the requesting task
  must wait in the Blocked state for the requested data to be
  received.

- After sending data to the cloud server, the sending task must wait
  in the Blocked state for an acknowledgement that the cloud server
  received the data correctly.

A schematic of the software design is shown in Figure 10.6. In Figure 10.6:

- The complexity of handling multiple internet connections to the
  cloud server is encapsulated within a single FreeRTOS task. The task
  acts as a proxy server within the FreeRTOS application, and is
  referred to as the *server task*.

- Application tasks read data from the cloud server by calling
  `CloudRead()`. `CloudRead()` does not communicate with the cloud server
  directly, but instead sends the read request to the server task on a
  queue, and receives the requested data from the server task as a
  task notification.

- Application tasks write data to the cloud server by calling
  `CloudWrite()`. `CloudWrite()` does not communicate with the cloud
  server directly, but instead sends the write request to the server
  task on a queue, and receives the result of the write operation from
  the server task as a task notification.

The structure sent to the server task by the `CloudRead()` and
`CloudWrite()` functions is shown in Listing 10.14.




* * *
    
***Figure 10.6*** *The communication paths from the application tasks to the cloud server, and back again*
* * *





```c
typedef enum CloudOperations
{
    eRead, /* Send data to the cloud server. */
    eWrite /* Receive data from the cloud server. */
} Operation_t;

typedef struct CloudCommand
{
    Operation_t eOperation; /* The operation to perform (read or write). */
    uint32_t ulDataID; /* Identifies the data being read or written. */
    uint32_t ulDataValue; /* Only used when writing data to the cloud server. */
    TaskHandle_t xTaskToNotify;/* The handle of the task performing the operation. */
} CloudCommand_t;
```

***Listing 10.14*** *The structure and data type sent on a queue to the server task*

Pseudo code for `CloudRead()` is shown in Listing 10.15. The function sends
its request to the server task, then calls `xTaskNotifyWait()` to wait in
the Blocked state until it is notified that the requested data is
available.

Pseudo code showing how the server task manages a read request is shown
in Listing 10.16. When the data has been received from the cloud server,
the server task unblocks the application task, and sends the received
data to the application task, by calling `xTaskNotify()` with the `eAction`
parameter set to `eSetValueWithOverwrite`.

Listing 10.16 shows a simplified scenario, as it assumes `GetCloudData()`
does not have to wait to obtain a value from the cloud server.





```c
/* ulDataID identifies the data to read. pulValue holds the address of the 
   variable into which the data received from the cloud server is to be written. */
BaseType_t CloudRead( uint32_t ulDataID, uint32_t *pulValue )
{
    CloudCommand_t xRequest;
    BaseType_t xReturn;

    /* Set the CloudCommand_t structure members to be correct for this read
       request. */
    xRequest.eOperation = eRead; /* This is a request to read data. */
    xRequest.ulDataID = ulDataID; /* A code that identifies the data to read. */
    xRequest.xTaskToNotify = xTaskGetCurrentTaskHandle(); /* Handle of the
                                                             calling task. */

    /* Ensure there are no notifications already pending by reading the
       notification value with a block time of 0, then send the structure to 
       the server task. */
    xTaskNotifyWait( 0, 0, NULL, 0 );
    xQueueSend( xServerTaskQueue, &xRequest, portMAX_DELAY );

    /* Wait for a notification from the server task. The server task writes
       the value received from the cloud server directly into this task's 
       notification value, so there is no need to clear any bits in the 
       notification value on entry to or exit from the xTaskNotifyWait() 
       function. The received value is written to *pulValue, so pulValue is
       passed as the address to which the notification value is written. */
    xReturn = xTaskNotifyWait( 0, /* No bits cleared on entry */
                               0, /* No bits to clear on exit */
                               pulValue, /* Notification value into *pulValue */
                               pdMS_TO_TICKS( 250 ) ); /* Wait 250ms maximum */

    /* If xReturn is pdPASS, then the value was obtained. If xReturn is pdFAIL,
       then the request timed out. */
    return xReturn;
}
```

***Listing 10.15*** *The Implementation of the Cloud Read API Function*





```c
void ServerTask( void *pvParameters )
{
    CloudCommand_t xCommand;
    uint32_t ulReceivedValue;

    for( ;; )
    {
        /* Wait for the next CloudCommand_t structure to be received from a task */
        xQueueReceive( xServerTaskQueue, &xCommand, portMAX_DELAY );

        switch( xCommand.eOperation ) /* Was it a read or write request? */
        {
            case eRead:

                /* Obtain the requested data item from the remote cloud server */
                ulReceivedValue = GetCloudData( xCommand.ulDataID );

                /* Call xTaskNotify() to send both a notification and the value
                   received from the cloud server to the task that made the 
                   request. The handle of the task is obtained from the 
                   CloudCommand_t structure. */
                xTaskNotify( xCommand.xTaskToNotify, /* The task's handle is in
                                                        the structure */
                             ulReceivedValue, /* Cloud data sent as notification 
                                                 value */
                             eSetValueWithOverwrite );
                break;

                /* Other switch cases go here. */
        }
    }
}
```

***Listing 10.16*** *The Server Task Processing a Read Request*

Pseudo code for `CloudWrite()` is shown in Listing 10.17. For the purpose of
demonstration, `CloudWrite()` returns a bitwise status code, where each
bit in the status code is assigned a unique meaning. Four example status
bits are shown by the \#define statements at the top of Listing 10.17.

The task clears the four status bits, sends its request to the server
task, then calls `xTaskNotifyWait()` to wait in the Blocked state for the
status notification.





```c
/* Status bits used by the cloud write operation. */
#define SEND_SUCCESSFUL_BIT ( 0x01 << 0 )
#define OPERATION_TIMED_OUT_BIT ( 0x01 << 1 )
#define NO_INTERNET_CONNECTION_BIT ( 0x01 << 2 )
#define CANNOT_LOCATE_CLOUD_SERVER_BIT ( 0x01 << 3 )

/* A mask that has the four status bits set. */
#define CLOUD_WRITE_STATUS_BIT_MASK ( SEND_SUCCESSFUL_BIT |
                                      OPERATION_TIMED_OUT_BIT |
                                      NO_INTERNET_CONNECTION_BIT |
                                      CANNOT_LOCATE_CLOUD_SERVER_BIT )

uint32_t CloudWrite( uint32_t ulDataID, uint32_t ulDataValue )
{
    CloudCommand_t xRequest;
    uint32_t ulNotificationValue;

    /* Set the CloudCommand_t structure members to be correct for this
       write request. */
    xRequest.eOperation = eWrite; /* This is a request to write data */
    xRequest.ulDataID = ulDataID; /* A code that identifies the data being
                                     written */
    xRequest.ulDataValue = ulDataValue; /* Value of the data written to the
                                           cloud server. */
    xRequest.xTaskToNotify = xTaskGetCurrentTaskHandle(); /* Handle of the 
                                                             calling task. */

    /* Clear the three status bits relevant to the write operation by calling
       xTaskNotifyWait() with the ulBitsToClearOnExit parameter set to
       CLOUD_WRITE_STATUS_BIT_MASK, and a block time of 0. The current
       notification value is not required, so the pulNotificationValue 
       parameter is set to NULL. */
    xTaskNotifyWait( 0, CLOUD_WRITE_STATUS_BIT_MASK, NULL, 0 );

    /* Send the request to the server task. */
    xQueueSend( xServerTaskQueue, &xRequest, portMAX_DELAY );

    /* Wait for a notification from the server task. The server task writes
       a bitwise status code into this task's notification value, which is 
       written to ulNotificationValue. */
    xTaskNotifyWait( 0, /* No bits cleared on entry. */
                     CLOUD_WRITE_STATUS_BIT_MASK, /* Clear relevant bits to 0 on exit. */
                     &ulNotificationValue, /* Notified value. */
                     pdMS_TO_TICKS( 250 ) ); /* Wait a maximum of 250ms. */

    /* Return the status code to the calling task. */
    return ( ulNotificationValue & CLOUD_WRITE_STATUS_BIT_MASK );
}
```

***Listing 10.17*** *The Implementation of the Cloud Write API Function*

Pseudo code demonstrating how the server task manages a write request is
shown in Listing 10.18. When the data has been sent to the cloud server,
the server task unblocks the application task, and sends the bitwise
status code to the application task, by calling `xTaskNotify()` with the
`eAction` parameter set to `eSetBits`. Only the bits defined by the
`CLOUD_WRITE_STATUS_BIT_MASK` constant can get altered in the receiving
task's notification value, so the receiving task can use other bits in
its notification value for other purposes.

Listing 10.18 shows a simplified scenario, as it assumes `SetCloudData()`
does not have to wait to obtain an acknowledgement from the remote cloud
server.





```c
void ServerTask( void *pvParameters )
{
    CloudCommand_t xCommand;
    uint32_t ulBitwiseStatusCode;

    for( ;; )
    {
        /* Wait for the next message. */
        xQueueReceive( xServerTaskQueue, &xCommand, portMAX_DELAY );

        /* Was it a read or write request? */
        switch( xCommand.eOperation )
        {
            case eWrite:

            /* Send the data to the remote cloud server. SetCloudData() returns
               a bitwise status code that only uses the bits defined by the
               CLOUD_WRITE_STATUS_BIT_MASK definition (shown in Listing 10.17). */
            ulBitwiseStatusCode = SetCloudData( xCommand.ulDataID,
                                                xCommand.ulDataValue );

            /* Send a notification to the task that made the write request. 
               The eSetBits action is used so any status bits set in 
               ulBitwiseStatusCode will be set in the notification value of 
               the task being notified. All the other bits remain unchanged. 
               The handle of the task is obtained from the CloudCommand_t
               structure. */
            xTaskNotify( xCommand.xTaskToNotify, /* The task's handle is in 
                                                    the structure. */
                         ulBitwiseStatusCode,    /* Cloud data sent as 
                                                    notification value. */
                         eSetBits );
            break;

            /* Other switch cases go here. */
        }
    }
}
```

***Listing 10.18*** *The Server Task Processing a Send Request*
