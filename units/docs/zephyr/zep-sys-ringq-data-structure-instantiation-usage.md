---
id: "zep-sys-ringq-data-structure-instantiation-usage"
type: "concept"
domain: "rtos"
title: "sys_ringq Data Structure: Instantiation & Usage"
summary: "A sys_ringq can be declared either using the SYS_RINGQ_DEFINE(name, item_size, item_capacity) macro or in runtime using the sys_ringq_init(struct sys_ringq ringq, uint8_t data, size_t data_size, size_t item_size); function."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/data_structures/ringq.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/data_structures/ringq.rst"
license: "Apache-2.0"
mode: "V"
---

A `sys_ringq` can be declared either using the `SYS_RINGQ_DEFINE(name, item_size, item_capacity)`
macro or in runtime using the
`sys_ringq_init(struct sys_ringq *ringq, uint8_t *data, size_t data_size, size_t item_size);` function.

```c

SYS_RINGQ_DEFINE(my_ringq, item_size, item_capacity);
/* equivalent to */

static struct sys_ringq my_ringq;
static uint8_t buffer[item_size * item_capacity];
void init_fn (void) {
   sys_ringq_init(&my_ringq, buffer, sizeof(buffer), item_size);
   ....
}
```
Once the `sys_ringq` is initialized, items can be added to the ringq using the `sys_ringq_put()`
function and removed using the `sys_ringq_get()` function. The ringq maintains the order of the
items and ensures proper boundary checking of the underlying data buffer.

```c

struct my_item item_to_add = { ... };
struct my_item item_removed;

/* Add an item to the queue */
if (sys_ringq_put(&my_ringq, &item_to_add) == 0) {
    // Item added successfully
} else {
    // ringq is full
}

/* Remove an item from the queue */
if (sys_ringq_get(&my_ringq, &item_removed) == 0) {
    // Item removed successfully
} else {
    // ringq is empty
}
```
In addition to the standard data operations (sys_ringq_put() and sys_ringq_get()), the sys_ringq API provides a set
of utility functions for managing and inspecting the data structures state.

* sys_ringq_capacity() – Returns the total capacity of the sys_ringq in terms of the number of items it can hold.
* sys_ringq_empty() – Returns true if the sys_ringq contains no items.
* sys_ringq_full() – Returns true if the sys_ringq cannot accept more items.
* sys_ringq_space() – Returns the number of free slots remaining.
* sys_ringq_size() – Returns the number of items currently stored.
* sys_ringq_reset() – Resets the sys_ringq to an empty state.
