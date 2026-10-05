---
id: "zep-threads-thread-states"
type: "concept"
domain: "rtos"
title: "Threads: Thread States"
summary: "A thread that has no factors that prevent its execution is deemed to be ready, and is eligible to be selected as the current thread."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/threads/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/threads/index.rst"
license: "Apache-2.0"
mode: "V"
---

A thread that has no factors that prevent its execution is deemed
to be **ready**, and is eligible to be selected as the current thread.

A thread that has one or more factors that prevent its execution
is deemed to be **unready**, and cannot be selected as the current thread.

The following factors make a thread unready:

* The thread has not been started.
* The thread is waiting for a kernel object to complete an operation.
  (For example, the thread is taking a semaphore that is unavailable.)
* The thread is waiting for a timeout to occur.
* The thread has been suspended.
* The thread has terminated or aborted.


**Note:** Although the diagram above may appear to suggest that both **Ready** and **Running** are distinct thread states, that is not the correct interpretation. **Ready** is a thread state, and **Running** is a schedule state that only applies to **Ready** threads.
