---
id: "intr-zephyr-deep-dive-ring-buffers-ring-buffer-weaknesses"
type: "concept"
domain: "debug"
title: "Zephyr Deep Dive: Ring Buffers: Ring Buffer Weaknesses"
summary: "There are a few weaknesses present in ring buffers. First, they require concurrency protections when their usage expands to multiple producers or consumers."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-05-24-zephyr-ring-buffers.md"
doc_source: "https://interrupt.memfault.com/blog/zephyr-ring-buffers#ring-buffer-weaknesses"
license: "CC-BY-SA-4.0"
mode: "V"
---

There are a few weaknesses present in ring buffers. First, they require
concurrency protections when their usage expands to multiple producers or
consumers. It is safe to use with a single producer and a single consumer, but
expanding beyond this simple case will require additional design, especially if
used in an interrupt context. The ring buffer does have separate state variables
for reading and writing. These allow for the scenario where an interrupt handler
is the only producer, allowing it to write without acquiring a lock, while
multiple consumer threads must use a lock for exclusive access.

The second weakness is ring buffers lack synchronization capabilities. Producers
cannot wait until space is available in the buffer. Consumers cannot wait until
data is available in the buffer. The ring buffer APIs are non-blocking, they
return immediately. We could use the `ring_buf_is_empty` function to poll for a
change, but this introduces many undesirable effects. A better option would be
to use a kernel synchronization primitive, such as a semaphore, to augment the
ring buffer.
