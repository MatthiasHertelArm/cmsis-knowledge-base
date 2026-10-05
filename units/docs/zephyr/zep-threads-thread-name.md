---
id: "zep-threads-thread-name"
type: "concept"
domain: "rtos"
title: "Threads: Thread Name"
summary: "When CONFIG_THREAD_NAME is enabled, a human-readable name can be associated with each thread. Names are primarily an aid for debugging, logging, and shell introspection; the kernel does not use them for scheduling."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/threads/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/threads/index.rst"
license: "Apache-2.0"
mode: "V"
---

When `CONFIG_THREAD_NAME` is enabled, a human-readable name can
be associated with each thread. Names are primarily an aid for debugging,
logging, and shell introspection; the kernel does not use them for scheduling.

A thread name may be assigned in one of two ways:

* Statically, by passing a name to `K_THREAD_DEFINE`.
* At run time, using `k_thread_name_set`. The supplied string must
  remain valid for the lifetime of the thread, as only a pointer to it is
  retained.

A thread's name can be retrieved with `k_thread_name_get`, which returns
a pointer to the name string, or with `k_thread_name_copy`, which copies
the name into a caller-supplied buffer. The copying variant is the safe choice
from user mode, where the calling thread may not have access to the memory
backing another thread's name.

If `CONFIG_THREAD_NAME` is not enabled,
`k_thread_name_set` returns an error and `k_thread_name_get`
returns `NULL`.
