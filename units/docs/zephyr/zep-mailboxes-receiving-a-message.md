---
id: "zep-mailboxes-receiving-a-message"
type: "concept"
domain: "rtos"
title: "Mailboxes: Implementation / Receiving a Message"
summary: "A thread receives a message by first creating a message descriptor that characterizes the message it wants to receive. It then calls one of the mailbox receive APIs."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/data_passing/mailboxes.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/data_passing/mailboxes.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Implementation_

A thread receives a message by first creating a message descriptor that
characterizes the message it wants to receive. It then calls one of the
mailbox receive APIs. The mailbox searches its send queue and takes the message
from the first compatible thread it finds. If no compatible thread exists,
the receiving thread may choose to wait for one. If no compatible thread
appears before the waiting period specified by the receiving thread is reached,
the receive operation fails.
Once a receive operation completes successfully the receiving thread
can examine the message descriptor to determine which thread sent the message,
how much data was exchanged,
and the application-defined info value supplied by the sending thread.

Any number of receiving threads may wait simultaneously on a mailboxes'
receive queue. The threads are sorted according to their priority;
threads of equal priority are sorted so that the one that started waiting
first can receive a message first.


**Note:** Receiving threads do not always receive messages in a first in, first out (FIFO) order, due to the thread compatibility constraints specified by the message descriptors. For example, if thread A waits to receive a message only from thread X and then thread B waits to receive a message from thread Y, an incoming message from thread Y to any thread will be given to thread B and thread A will continue to wait.

The receiving thread controls both the quantity of data it retrieves from an
incoming message and where the data ends up. The thread may choose to take
all of the data in the message, to take only the initial part of the data,
or to take no data at all. Similarly, the thread may choose to have the data
copied into a message buffer of its choice.

The following sections outline various approaches a receiving thread may use
when retrieving message data.


#### Retrieving Data at Receive Time


The most straightforward way for a thread to retrieve message data is to
specify a message buffer when the message is received. The thread indicates
both the location of the message buffer (which must not be `NULL`)
and its size.

The mailbox copies the message's data to the message buffer as part of the
receive operation. If the message buffer is not big enough to contain all of the
message's data, any uncopied data is lost. If the message is not big enough
to fill all of the buffer with data, the unused portion of the message buffer is
left unchanged. In all cases the mailbox updates the receiving thread's
message descriptor to indicate how many data bytes were copied (if any).

The immediate data retrieval technique is best suited for small messages
where the maximum size of a message is known in advance.

The following code uses a mailbox to process variable-sized requests from any
producing thread, using the immediate data retrieval technique. The message
"info" field is used to exchange information about the maximum size
message buffer that each thread can handle.

```c

void consumer_thread(void)
{
    struct k_mbox_msg recv_msg;
    char buffer[100];

    int i;
    int total;

    while (1) {
        /* prepare to receive message */
        recv_msg.info = 100;
        recv_msg.size = 100;
        recv_msg.rx_source_thread = K_ANY;

        /* get a data item, waiting as long as needed */
        k_mbox_get(&my_mailbox, &recv_msg, buffer, K_FOREVER);

        /* info, size, and rx_source_thread fields have been updated */

        /* verify that message data was fully received */
        if (recv_msg.info != recv_msg.size) {
            printf("some message data dropped during transfer!");
            printf("sender tried to send %d bytes", recv_msg.info);
        }

        /* compute sum of all message bytes (from 0 to 100 of them) */
        total = 0;
        for (i = 0; i < recv_msg.size; i++) {
            total += buffer[i];
        }
    }
}
```

#### Retrieving Data Later Using a Message Buffer


A receiving thread may choose to defer message data retrieval at the time
the message is received, so that it can retrieve the data into a message buffer
at a later time.
The thread does this by specifying a message buffer location of `NULL`
and a size indicating the maximum amount of data it is willing to retrieve
later.

The mailbox does not copy any message data as part of the receive operation.
However, the mailbox still updates the receiving thread's message descriptor
to indicate how many data bytes are available for retrieval.

The receiving thread must then respond as follows:

* If the message descriptor size is zero, then either the sender's message
  contained no data or the receiving thread did not want to receive any data.
  The receiving thread does not need to take any further action, since
  the mailbox has already completed data retrieval and deleted the message.

* If the message descriptor size is non-zero and the receiving thread still
  wants to retrieve the data, the thread must call `k_mbox_data_get`
  and supply a message buffer large enough to hold the data. The mailbox copies
  the data into the message buffer and deletes the message.

* If the message descriptor size is non-zero and the receiving thread does *not*
  want to retrieve the data, the thread must call `k_mbox_data_get`
  and specify a message buffer of `NULL`. The mailbox deletes
  the message without copying the data.

The subsequent data retrieval technique is suitable for applications where
immediate retrieval of message data is undesirable. For example, it can be
used when memory limitations make it impractical for the receiving thread to
always supply a message buffer capable of holding the largest possible
incoming message.

The following code uses a mailbox's deferred data retrieval mechanism
to get message data from a producing thread only if the message meets
certain criteria, thereby eliminating unneeded data copying. The message
"info" field supplied by the sender is used to classify the message.

```c

void consumer_thread(void)
{
    struct k_mbox_msg recv_msg;
    char buffer[10000];

    while (1) {
        /* prepare to receive message */
        recv_msg.size = 10000;
        recv_msg.rx_source_thread = K_ANY;

        /* get message, but not its data */
        k_mbox_get(&my_mailbox, &recv_msg, NULL, K_FOREVER);

        /* get message data for only certain types of messages */
        if (is_message_type_ok(recv_msg.info)) {
            /* retrieve message data and delete the message */
            k_mbox_data_get(&recv_msg, buffer);

            /* process data in "buffer" */
            ...
        } else {
            /* ignore message data and delete the message */
            k_mbox_data_get(&recv_msg, NULL);
        }
    }
}
```
