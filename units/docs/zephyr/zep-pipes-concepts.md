---
id: "zep-pipes-concepts"
type: "concept"
domain: "rtos"
title: "Pipes: Concepts"
summary: "Any number of pipes can be defined, limited only by available RAM. Each pipe is referenced by its memory address."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/data_passing/pipes.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/data_passing/pipes.rst"
license: "Apache-2.0"
mode: "V"
---

Any number of pipes can be defined, limited only by available RAM. Each pipe
is referenced by its memory address.

A pipe has the following key property:

* A **size** that indicates the capacity of the pipe's ring buffer. Note that a
  size of zero defines a pipe with no ring buffer.

A pipe must be initialized before it can be used. When initialized, the pipe
is empty.

Threads interact with the pipe as follows:

- **Writing**: Data is synchronously written, either in whole or in part, to
  a pipe by a thread. Accepted data is either copied directly to the waiting
  reader(s) or to the pipe's ring buffer. If the ring buffer is full or simply
  absent, the operation blocks until sufficient space becomes available or
  the specified timeout expires.

- **Reading**: Data is synchronously read, either in whole or in part, from a
  pipe by a thread. Accepted data is either copied from the pipe's ring buffer
  or directly from the waiting sender(s). If the ring buffer is empty or simply
  absent, the operation blocks until data becomes available or the specified
  timeout expires.

- **Resetting**: A thread can reset a pipe, which resets its internal state and
  ends all pending read and write operations with an error code.

Pipes are well-suited for scenarios like producer-consumer patterns or
streaming data between threads.
