---
id: "zep-fifos-implementation"
type: "concept"
domain: "rtos"
title: "FIFOs: Implementation"
summary: "A FIFO is defined using a variable of type k_fifo. It must then be initialized by calling k_fifo_init."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/data_passing/fifos.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/data_passing/fifos.rst"
license: "Apache-2.0"
mode: "V"
---

### Defining a FIFO


A FIFO is defined using a variable of type `k_fifo`.
It must then be initialized by calling `k_fifo_init`.

The following code defines and initializes an empty FIFO.

```c

struct k_fifo my_fifo;

k_fifo_init(&my_fifo);
```
Alternatively, an empty FIFO can be defined and initialized at compile time
by calling `K_FIFO_DEFINE`.

The following code has the same effect as the code segment above.

```c

K_FIFO_DEFINE(my_fifo);
```

### Writing to a FIFO


A data item is added to a FIFO by calling `k_fifo_put`.

The following code builds on the example above, and uses the FIFO
to send data to one or more consumer threads.

```c

struct data_item_t {
    void *fifo_reserved;   /* 1st word reserved for use by FIFO */
    ...
};

struct data_item_t tx_data;

void producer_thread(int unused1, int unused2, int unused3)
{
    while (1) {
        /* create data item to send */
        tx_data = ...

        /* send data to consumers */
        k_fifo_put(&my_fifo, &tx_data);

        ...
    }
}
```
Additionally, a singly-linked list of data items can be added to a FIFO
by calling `k_fifo_put_list` or `k_fifo_put_slist`.

Finally, a data item can be added to a FIFO with `k_fifo_alloc_put`.
With this API, there is no need to reserve space for the kernel's use in
the data item, instead additional memory will be allocated from the calling
thread's resource pool until the item is read.


### Reading from a FIFO


A data item is removed from a FIFO by calling `k_fifo_get`.

The following code builds on the example above, and uses the FIFO
to obtain data items from a producer thread,
which are then processed in some manner.

```c

void consumer_thread(int unused1, int unused2, int unused3)
{
    struct data_item_t  *rx_data;

    while (1) {
        rx_data = k_fifo_get(&my_fifo, K_FOREVER);

        /* process FIFO data item */
        ...
    }
}
```
