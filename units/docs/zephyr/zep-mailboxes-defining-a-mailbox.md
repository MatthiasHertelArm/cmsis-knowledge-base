---
id: "zep-mailboxes-defining-a-mailbox"
type: "concept"
domain: "rtos"
title: "Mailboxes: Implementation / Defining a Mailbox"
summary: "A mailbox is defined using a variable of type k_mbox. It must then be initialized by calling k_mbox_init."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/data_passing/mailboxes.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/data_passing/mailboxes.rst"
license: "Apache-2.0"
mode: "V"
---

_Part of: Implementation_

A mailbox is defined using a variable of type `k_mbox`.
It must then be initialized by calling `k_mbox_init`.

The following code defines and initializes an empty mailbox.

```c

struct k_mbox my_mailbox;

k_mbox_init(&my_mailbox);
```
Alternatively, a mailbox can be defined and initialized at compile time
by calling `K_MBOX_DEFINE`.

The following code has the same effect as the code segment above.

```c

K_MBOX_DEFINE(my_mailbox);
```
