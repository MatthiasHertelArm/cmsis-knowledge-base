---
id: "zep-scheduling-implementation"
type: "concept"
domain: "rtos"
title: "Scheduling: Implementation"
summary: "Making the CPU idle is simple: call the k_cpu_idle API. The CPU will stop executing instructions until an event occurs. Most likely, the function will be called within a loop."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/scheduling/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/scheduling/index.rst"
license: "Apache-2.0"
mode: "V"
---

### Making the CPU idle


Making the CPU idle is simple: call the `k_cpu_idle` API. The CPU will stop
executing instructions until an event occurs. Most likely, the function will
be called within a loop. Note that in certain architectures, upon return,
`k_cpu_idle` unconditionally unmasks interrupts.

```c

static k_sem my_sem;

void my_isr(void *unused)
{
    k_sem_give(&my_sem);
}

int main(void)
{
    k_sem_init(&my_sem, 0, 1);

    /* wait for semaphore from ISR, then do related work */

    for (;;) {

        /* wait for ISR to trigger work to perform */
        if (k_sem_take(&my_sem, K_NO_WAIT) == 0) {

            /* ... do processing */

        }

        /* put CPU to sleep to save power */
        k_cpu_idle();
    }
}
```

### Making the CPU idle in an atomic fashion


It is possible that there is a need to do some work atomically before making
the CPU idle. In such a case, `k_cpu_atomic_idle` should be used instead.

In fact, there is a race condition in the previous example: the interrupt could
occur between the time the semaphore is taken, finding out it is not available
and making the CPU idle again. In some systems, this can cause the CPU to idle
until *another* interrupt occurs, which might be *never*, thus hanging the
system completely. To prevent this, `k_cpu_atomic_idle` should have been used,
like in this example.

```c

static k_sem my_sem;

void my_isr(void *unused)
{
    k_sem_give(&my_sem);
}

int main(void)
{
    k_sem_init(&my_sem, 0, 1);

    for (;;) {

        unsigned int key = irq_lock();

        /*
         * Wait for semaphore from ISR; if acquired, do related work, then
         * go to next loop iteration (the semaphore might have been given
         * again); else, make the CPU idle.
         */

        if (k_sem_take(&my_sem, K_NO_WAIT) == 0) {

            irq_unlock(key);

            /* ... do processing */


        } else {
            /* put CPU to sleep to save power */
            k_cpu_atomic_idle(key);
        }
    }
}
```
