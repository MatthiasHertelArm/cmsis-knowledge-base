---
id: "zep-mailboxes-concepts"
type: "concept"
domain: "rtos"
title: "Mailboxes: Concepts"
summary: "Any number of mailboxes can be defined (limited only by available RAM). Each mailbox is referenced by its memory address."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/data_passing/mailboxes.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/data_passing/mailboxes.rst"
license: "Apache-2.0"
mode: "V"
---

Any number of mailboxes can be defined (limited only by available RAM). Each
mailbox is referenced by its memory address.

A mailbox has the following key properties:

* A **send queue** of messages that have been sent but not yet received.

* A **receive queue** of threads that are waiting to receive a message.

A mailbox must be initialized before it can be used. This sets both of its
queues to empty.

A mailbox allows threads, but not ISRs, to exchange messages.
A thread that sends a message is known as the **sending thread**,
while a thread that receives the message is known as the **receiving thread**.
Each message may be received by only one thread (i.e. point-to-multipoint and
broadcast messaging is not supported).

Messages exchanged using a mailbox are handled non-anonymously,
allowing both threads participating in an exchange to know
(and even specify) the identity of the other thread.


### Message Format


A **message descriptor** is a data structure that specifies where a message's
data is located, and how the message is to be handled by the mailbox.
Both the sending thread and the receiving thread supply a message descriptor
when accessing a mailbox. The mailbox uses the message descriptors to perform
a message exchange between compatible sending and receiving threads.
The mailbox also updates certain message descriptor fields during the exchange,
allowing both threads to know what has occurred.

A mailbox message contains zero or more bytes of **message data**.
The size and format of the message data is application-defined, and can vary
from one message to the next.

A **message buffer** is an area of memory provided by the thread that sends or
receives the message data. An array or structure variable can often be used for
this purpose.

A message that has neither form of message data is called an **empty message**.


**Note:** A message whose message buffer exists, but contains zero bytes of actual data, is *not* an empty message.


### Message Lifecycle


The life cycle of a message is straightforward. A message is created when
it is given to a mailbox by the sending thread. The message is then owned
by the mailbox until it is given to a receiving thread. The receiving thread
may retrieve the message data when it receives the message from the mailbox,
or it may perform data retrieval during a second, subsequent mailbox operation.
Only when data retrieval has occurred is the message deleted by the mailbox.


### Thread Compatibility


A sending thread can specify the address of the thread to which the message
is sent, or send it to any thread by specifying `K_ANY`.
Likewise, a receiving thread can specify the address of the thread from which
it wishes to receive a message, or it can receive a message from any thread
by specifying `K_ANY`.
A message is exchanged only when the requirements of both the sending thread
and receiving thread are satisfied; such threads are said to be **compatible**.

For example, if thread A sends a message to thread B (and only thread B)
it will be received by thread B if thread B tries to receive a message
from thread A or if thread B tries to receive from any thread.
The exchange will not occur if thread B tries to receive a message
from thread C. The message can never be received by thread C,
even if it tries to receive a message from thread A (or from any thread).


### Message Flow Control


Mailbox messages can be exchanged **synchronously** or **asynchronously**.
In a synchronous exchange, the sending thread blocks until the message
has been fully processed by the receiving thread. In an asynchronous exchange,
the sending thread does not wait until the message has been received
by another thread before continuing; this allows the sending thread to do
other work (such as gather data that will be used in the next message)
*before* the message is given to a receiving thread and fully processed.
The technique used for a given message exchange is determined
by the sending thread.

The synchronous exchange technique provides an implicit form of flow control,
preventing a sending thread from generating messages faster than they can be
consumed by receiving threads. The asynchronous exchange technique provides an
explicit form of flow control, which allows a sending thread to determine
if a previously sent message still exists before sending a subsequent message.
