---
id: "zep-lifos-implementation"
type: "concept"
domain: "rtos"
title: "LIFOs: Implementation"
summary: "A LIFO is defined using a variable of type k_lifo. It must then be initialized by calling k_lifo_init."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/data_passing/lifos.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/data_passing/lifos.rst"
license: "Apache-2.0"
mode: "V"
---

### Defining a LIFO


A LIFO is defined using a variable of type `k_lifo`.
It must then be initialized by calling `k_lifo_init`.

The following defines and initializes an empty LIFO.

```c

struct k_lifo my_lifo;

k_lifo_init(&my_lifo);
```
Alternatively, an empty LIFO can be defined and initialized at compile time
by calling `K_LIFO_DEFINE`.

The following code has the same effect as the code segment above.

```c

K_LIFO_DEFINE(my_lifo);
```

### Writing to a LIFO


A data item is added to a LIFO by calling `k_lifo_put`.

The following code builds on the example above, and uses the LIFO
to send data to one or more consumer threads.

```c

struct data_item_t {
    void *LIFO_reserved;   /* 1st word reserved for use by LIFO */
    ...
};

struct data_item_t tx data;

void producer_thread(int unused1, int unused2, int unused3)
{
    while (1) {
        /* create data item to send */
        tx_data = ...

        /* send data to consumers */
        k_lifo_put(&my_lifo, &tx_data);

        ...
    }
}
```
A data item can be added to a LIFO with `k_lifo_alloc_put`.
With this API, there is no need to reserve space for the kernel's use in
the data item, instead additional memory will be allocated from the calling
thread's resource pool until the item is read.


### Reading from a LIFO


A data item is removed from a LIFO by calling `k_lifo_get`.

The following code builds on the example above, and uses the LIFO
to obtain data items from a producer thread,
which are then processed in some manner.

```c

void consumer_thread(int unused1, int unused2, int unused3)
{
    struct data_item_t  *rx_data;

    while (1) {
        rx_data = k_lifo_get(&my_lifo, K_FOREVER);

        /* process LIFO data item */
        ...
    }
}
```
