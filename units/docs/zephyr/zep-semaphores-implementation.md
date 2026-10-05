---
id: "zep-semaphores-implementation"
type: "concept"
domain: "rtos"
title: "Semaphores: Implementation"
summary: "A semaphore is defined using a variable of type k_sem. It must then be initialized by calling k_sem_init."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/synchronization/semaphores.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/synchronization/semaphores.rst"
license: "Apache-2.0"
mode: "V"
---

### Defining a Semaphore


A semaphore is defined using a variable of type `k_sem`.
It must then be initialized by calling `k_sem_init`.

The following code defines a semaphore, then configures it as a binary
semaphore by setting its count to 0 and its limit to 1.

```c

struct k_sem my_sem;

k_sem_init(&my_sem, 0, 1);
```
Alternatively, a semaphore can be defined and initialized at compile time
by calling `K_SEM_DEFINE`.

The following code has the same effect as the code segment above.

```c

K_SEM_DEFINE(my_sem, 0, 1);
```

### Giving a Semaphore


A semaphore is given by calling `k_sem_give`.

The following code builds on the example above, and gives the semaphore to
indicate that a unit of data is available for processing by a consumer thread.

```c

void input_data_interrupt_handler(void *arg)
{
    /* notify thread that data is available */
    k_sem_give(&my_sem);

    ...
}
```

### Taking a Semaphore


A semaphore is taken by calling `k_sem_take`.

The following code builds on the example above, and waits up to 50 milliseconds
for the semaphore to be given.
A warning is issued if the semaphore is not obtained in time.

```c

void consumer_thread(void)
{
    ...

    if (k_sem_take(&my_sem, K_MSEC(50)) != 0) {
        printk("Input data not available!");
    } else {
        /* fetch available data */
        ...
    }
    ...
}
```
