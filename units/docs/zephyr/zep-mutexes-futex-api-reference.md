---
id: "zep-mutexes-futex-api-reference"
type: "concept"
domain: "rtos"
title: "Mutexes: Futex API Reference"
summary: "k_futex is a lightweight mutual exclusion primitive designed to minimize kernel involvement. Uncontended operation relies only on atomic access to shared memory. k_futex are not kernel objects and do not use the kernel object permission management."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/synchronization/mutexes.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/synchronization/mutexes.rst"
license: "Apache-2.0"
mode: "V"
---

`k_futex` is a lightweight mutual exclusion primitive designed to minimize
kernel involvement. Uncontended operation relies only on atomic access
to shared memory. `k_futex` are not kernel objects and do not use the
kernel object permission management. They live in user memory and can be
used by any thread which has read-write access to this memory.
