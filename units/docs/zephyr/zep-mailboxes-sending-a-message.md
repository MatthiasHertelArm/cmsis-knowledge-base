---
id: "zep-mailboxes-sending-a-message"
type: "concept"
domain: "rtos"
title: "Mailboxes: Implementation / Sending a Message"
summary: "A thread sends a message by first creating its message data, if any."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/data_passing/mailboxes.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/data_passing/mailboxes.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Implementation_

A thread sends a message by first creating its message data, if any.

Next, the sending thread creates a message descriptor that characterizes
the message to be sent, as described in the previous section.

Finally, the sending thread calls a mailbox send API to initiate the
message exchange. The message is immediately given to a compatible receiving
thread, if one is currently waiting. Otherwise, the message is added
to the mailbox's send queue.

Any number of messages may exist simultaneously on a send queue.
The messages in the send queue are sorted according to the priority
of the sending thread. Messages of equal priority are sorted so that
the oldest message can be received first.

For a synchronous send operation, the operation normally completes when a
receiving thread has both received the message and retrieved the message data.
If the message is not received before the waiting period specified by the
sending thread is reached, the message is removed from the mailbox's send queue
and the send operation fails. When a send operation completes successfully
the sending thread can examine the message descriptor to determine
which thread received the message, how much data was exchanged,
and the application-defined info value supplied by the receiving thread.


**Note:** A synchronous send operation may block the sending thread indefinitely, even when the thread specifies a maximum waiting period. The waiting period only limits how long the mailbox waits before the message is received by another thread. Once a message is received there is *no* limit to the time the receiving thread may take to retrieve the message data and unblock the sending thread.

For an asynchronous send operation, the operation always completes immediately.
This allows the sending thread to continue processing regardless of whether the
message is given to a receiving thread immediately or added to the send queue.
The sending thread may optionally specify a semaphore that the mailbox gives
when the message is deleted by the mailbox, for example, when the message
has been received and its data retrieved by a receiving thread.
The use of a semaphore allows the sending thread to easily implement
a flow control mechanism that ensures that the mailbox holds no more than
an application-specified number of messages from a sending thread
(or set of sending threads) at any point in time.


**Note:** A thread that sends a message asynchronously has no way to determine which thread received the message, how much data was exchanged, or the application-defined info value supplied by the receiving thread.


#### Sending an Empty Message


This code uses a mailbox to synchronously pass 4 byte random values
to any consuming thread that wants one. The message "info" field is
large enough to carry the information being exchanged, so the data
portion of the message isn't used.

```c

void producer_thread(void)
{
    struct k_mbox_msg send_msg;

    while (1) {

        /* generate random value to send */
        uint32_t random_value = sys_rand32_get();

        /* prepare to send empty message */
        send_msg.info = random_value;
        send_msg.size = 0;
        send_msg.tx_data = NULL;
        send_msg.tx_target_thread = K_ANY;

        /* send message and wait until a consumer receives it */
        k_mbox_put(&my_mailbox, &send_msg, K_FOREVER);
    }
}
```

#### Sending Data Using a Message Buffer


This code uses a mailbox to synchronously pass variable-sized requests
from a producing thread to any consuming thread that wants it.
The message "info" field is used to exchange information about
the maximum size message buffer that each thread can handle.

```c

void producer_thread(void)
{
    char buffer[100];
    int buffer_bytes_used;

    struct k_mbox_msg send_msg;

    while (1) {

        /* generate data to send */
        ...
        buffer_bytes_used = ... ;
        memcpy(buffer, source, buffer_bytes_used);

        /* prepare to send message */
        send_msg.info = buffer_bytes_used;
        send_msg.size = buffer_bytes_used;
        send_msg.tx_data = buffer;
        send_msg.tx_target_thread = K_ANY;

        /* send message and wait until a consumer receives it */
        k_mbox_put(&my_mailbox, &send_msg, K_FOREVER);

        /* info, size, and tx_target_thread fields have been updated */

        /* verify that message data was fully received */
        if (send_msg.size < buffer_bytes_used) {
            printf("some message data dropped during transfer!");
            printf("receiver only had room for %d bytes", send_msg.info);
        }
    }
}
```
