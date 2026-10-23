---
id: "rtos2-msg-queue-osmessagequeueput"
type: "concept"
domain: "rtos"
title: "msg queue: osMessageQueuePut"
summary: "The blocking function osMessageQueuePut puts the message pointed to by msg_ptr into the the message queue specified by parameter mq_id. The parameter msg_prio is used to sort message according their priority (higher numbers indicate a higher priority) on insertion."
status: "draft"
collection: "cmsis-rtos2"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_msg_queue.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/RTOS2/src/ref_cmsis_os2_msg_queue.txt"
license: "Apache-2.0"
mode: "V"
---

```c
osStatus_t osMessageQueuePut (osMessageQueueId_t mq_id, const void *msg_ptr, uint8_t msg_prio, uint32_t timeout)
```


The blocking function **osMessageQueuePut** puts the message pointed to by _msg_ptr_ into the the message queue specified
by parameter _mq_id._ The parameter _msg_prio_ is used to sort message according their priority (higher numbers indicate
a higher priority) on insertion.

The parameter _timeout_ specifies how long the system waits to put the message into the queue. While the system waits, the
thread that is calling this function is put into the BLOCKED state. The parameter timeout
can have the following values:
 - when _timeout_ is `0`, the function returns instantly (i.e. try semantics).
 - when _timeout_ is set to **osWaitForever** the function will wait for an infinite time until the message is delivered (i.e. wait semantics).
 - all other values specify a time in kernel ticks for a timeout (i.e. timed-wait semantics).

Possible osStatus_t return values:
 - **osOK:** the message has been put into the queue.
 - **osErrorTimeout:** the message could not be put into the queue in the given time (wait-timed semantics).
 - **osErrorResource:** not enough space in the queue (try semantics).
 - **osErrorParameter:** parameter **mq_id** is `NULL` or invalid, non-zero timeout specified in an ISR.
 - **osErrorSafetyClass:** the calling thread safety class is lower than the safety class of the specified message queue.

**Note:** May be called from Interrupt Service Routines if the parameter _timeout_ is set to
`0`.

**Code Example:**
```
#include "cmsis_os2.h"                          // CMSIS RTOS header file
 
/*----------------------------------------------------------------------------
     Message Queue creation & usage
---------------------------------------------------------------------------*/
 
#define MSGQUEUE_OBJECTS 16                     // number of Message Queue Objects
 
typedef struct {                                // object data type
  uint8_t Buf[32];
  uint8_t Idx;
} MSGQUEUE_OBJ_t;
 
osMessageQueueId_t mid_MsgQueue;                // message queue id
 
osThreadId_t tid_Thread_MsgQueue1;              // thread id 1
osThreadId_t tid_Thread_MsgQueue2;              // thread id 2
 
void Thread_MsgQueue1 (void *argument);         // thread function 1
void Thread_MsgQueue2 (void *argument);         // thread function 2
 
int Init_MsgQueue (void) {
 
  mid_MsgQueue = osMessageQueueNew(MSGQUEUE_OBJECTS, sizeof(MSGQUEUE_OBJ_t), NULL);
  if (mid_MsgQueue == NULL) {
    ; // Message Queue object not created, handle failure
  }
 
  tid_Thread_MsgQueue1 = osThreadNew(Thread_MsgQueue1, NULL, NULL);
  if (tid_Thread_MsgQueue1 == NULL) {
    return(-1);
  }
  tid_Thread_MsgQueue2 = osThreadNew(Thread_MsgQueue2, NULL, NULL);
  if (tid_Thread_MsgQueue2 == NULL) {
    return(-1);
  }
 
  return(0);
}
 
void Thread_MsgQueue1 (void *argument) {
  MSGQUEUE_OBJ_t msg;
 
  while (1) {
    ; // Insert thread code here...
    msg.Buf[0] = 0x55U;                                         // do some work...
    msg.Idx    = 0U;
    osMessageQueuePut(mid_MsgQueue, &msg, 0U, 0U);
    osThreadYield();                                            // suspend thread
  }
}
 
void Thread_MsgQueue2 (void *argument) {
  MSGQUEUE_OBJ_t msg;
  osStatus_t status;
 
  while (1) {
    ; // Insert thread code here...
    status = osMessageQueueGet(mid_MsgQueue, &msg, NULL, 0U);   // wait for message
    if (status == osOK) {
      ; // process data
    }
  }
}
```
