---
id: "zep-message-queues-suggested-uses"
type: "concept"
domain: "rtos"
title: "Message Queues: Suggested Uses"
summary: "Use a message queue to transfer small data items between threads in an asynchronous manner."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/data_passing/message_queues.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/data_passing/message_queues.rst"
license: "Apache-2.0"
mode: "V"
---

Use a message queue to transfer small data items between threads
in an asynchronous manner.


**Note:** A message queue can be used to transfer large data items, if desired. However, this can increase interrupt latency as interrupts are locked while a data item is written or read. The time to write or read a data item increases linearly with its size since the item is copied in its entirety to or from the buffer in memory. For this reason, it is usually preferable to transfer large data items by exchanging a pointer to the data item, rather than the data item itself. A synchronous transfer can be achieved by using the kernel's mailbox object type.
