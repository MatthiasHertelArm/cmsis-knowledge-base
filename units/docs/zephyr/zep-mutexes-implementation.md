---
id: "zep-mutexes-implementation"
type: "concept"
domain: "rtos"
title: "Mutexes: Implementation"
summary: "A mutex is defined using a variable of type k_mutex. It must then be initialized by calling k_mutex_init."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/synchronization/mutexes.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/synchronization/mutexes.rst"
license: "Apache-2.0"
mode: "V"
---

### Defining a Mutex


A mutex is defined using a variable of type `k_mutex`.
It must then be initialized by calling `k_mutex_init`.

The following code defines and initializes a mutex.

```c

struct k_mutex my_mutex;

k_mutex_init(&my_mutex);
```
Alternatively, a mutex can be defined and initialized at compile time
by calling `K_MUTEX_DEFINE`.

The following code has the same effect as the code segment above.

```c

K_MUTEX_DEFINE(my_mutex);
```

### Locking a Mutex


A mutex is locked by calling `k_mutex_lock`.

The following code builds on the example above, and waits indefinitely
for the mutex to become available if it is already locked by another thread.

```c

k_mutex_lock(&my_mutex, K_FOREVER);
```
The following code waits up to 100 milliseconds for the mutex to become
available, and gives a warning if the mutex does not become available.

```c

if (k_mutex_lock(&my_mutex, K_MSEC(100)) == 0) {
    /* mutex successfully locked */
} else {
    printf("Cannot lock XYZ display\n");
}
```

### Unlocking a Mutex


A mutex is unlocked by calling `k_mutex_unlock`.

The following code builds on the example above,
and unlocks the mutex that was previously locked by the thread.

```c

k_mutex_unlock(&my_mutex);
```
