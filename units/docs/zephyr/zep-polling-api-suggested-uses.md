---
id: "zep-polling-api-suggested-uses"
type: "concept"
domain: "rtos"
title: "Polling API: Suggested Uses"
summary: "Use k_poll to consolidate multiple threads that would be pending on one object each, saving possibly large amounts of stack space."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/polling.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/polling.rst"
license: "Apache-2.0"
mode: "V"
---

Use `k_poll` to consolidate multiple threads that would be pending
on one object each, saving possibly large amounts of stack space.

Use a poll signal as a lightweight binary semaphore if only one thread pends on
it.


**Note:** Because objects are only signaled if no other thread is waiting for them to become available and only one thread can poll on a specific object, polling is best used when objects are not subject of contention between multiple threads, basically when a single thread operates as a main "server" or "dispatcher" for multiple objects and is the only one trying to acquire these objects.
