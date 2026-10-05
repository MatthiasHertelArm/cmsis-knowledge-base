---
id: "zep-condition-variables-implementation"
type: "concept"
domain: "rtos"
title: "Condition Variables: Implementation"
summary: "A condition variable is defined using a variable of type k_condvar. It must then be initialized by calling k_condvar_init."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/synchronization/condvar.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/synchronization/condvar.rst"
license: "Apache-2.0"
mode: "V"
---

### Defining a Condition Variable


A condition variable is defined using a variable of type `k_condvar`.
It must then be initialized by calling `k_condvar_init`.

The following code defines a condition variable:

```c

struct k_condvar my_condvar;

k_condvar_init(&my_condvar);
```
Alternatively, a condition variable can be defined and initialized at compile time
by calling `K_CONDVAR_DEFINE`.

The following code has the same effect as the code segment above.

```c

K_CONDVAR_DEFINE(my_condvar);
```

### Waiting on a Condition Variable


A thread can wait on a condition by calling `k_condvar_wait`.

The following code waits on the condition variable.


```c

K_MUTEX_DEFINE(mutex);
K_CONDVAR_DEFINE(condvar)

int main(void)
{
    k_mutex_lock(&mutex, K_FOREVER);

    /* block this thread until another thread signals cond. While
     * blocked, the mutex is released, then re-acquired before this
     * thread is woken up and the call returns.
     */
    k_condvar_wait(&condvar, &mutex, K_FOREVER);
    ...
    k_mutex_unlock(&mutex);
}
```

### Signaling a Condition Variable


A condition variable is signaled on by calling `k_condvar_signal` for
one thread or by calling `k_condvar_broadcast` for multiple threads.

The following code builds on the example above.

```c

void worker_thread(void)
{
    k_mutex_lock(&mutex, K_FOREVER);

    /*
     * Do some work and fulfill the condition
     */
    ...
    ...
    k_condvar_signal(&condvar);
    k_mutex_unlock(&mutex);
}
```
