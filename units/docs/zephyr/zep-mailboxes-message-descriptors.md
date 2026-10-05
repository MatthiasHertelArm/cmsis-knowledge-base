---
id: "zep-mailboxes-message-descriptors"
type: "concept"
domain: "rtos"
title: "Mailboxes: Implementation / Message Descriptors"
summary: "A message descriptor is a structure of type k_mbox_msg. Only the fields listed below should be used; any other fields are for internal mailbox use only."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/data_passing/mailboxes.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/data_passing/mailboxes.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Implementation_

A message descriptor is a structure of type `k_mbox_msg`.
Only the fields listed below should be used; any other fields are for
internal mailbox use only.

*info*
    A 32-bit value that is exchanged by the message sender and receiver,
    and whose meaning is defined by the application. This exchange is
    bi-directional, allowing the sender to pass a value to the receiver
    during any message exchange, and allowing the receiver to pass a value
    to the sender during a synchronous message exchange.

*size*
    The message data size, in bytes. Set it to zero when sending an empty
    message, or when sending a message buffer with no actual data. When
    receiving a message, set it to the maximum amount of data desired, or to
    zero if the message data is not wanted. The mailbox updates this field with
    the actual number of data bytes exchanged once the message is received.

*tx_data*
    A pointer to the sending thread's message buffer. Set it to `NULL`
    when sending an empty message. Leave this field uninitialized when
    receiving a message.

*tx_target_thread*
    The address of the desired receiving thread. Set it to `K_ANY`
    to allow any thread to receive the message. Leave this field uninitialized
    when receiving a message. The mailbox updates this field with
    the actual receiver's address once the message is received.

*rx_source_thread*
    The address of the desired sending thread. Set it to `K_ANY`
    to receive a message sent by any thread. Leave this field uninitialized
    when sending a message. The mailbox updates this field
    with the actual sender's address when the message is put into
    the mailbox.
