---
id: "intr-how-memory-usage-patterns-can-dera-solution"
type: "concept"
domain: "debug"
title: "How Memory Usage Patterns Can Derail Real-time Performance: Solution"
summary: "To solve this problem, I implemented my own memory allocator and re-implemented malloc() and friends to use my allocator."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-08-29-memory-debugging.md"
doc_source: "https://interrupt.memfault.com/blog/memory-debugging#solution"
license: "CC-BY-SA-4.0"
mode: "V"
---

To solve this problem, I implemented my own memory allocator and re-implemented
`malloc()` and friends to use my allocator. At a high level, my allocator
pre-allocates one large block of memory using `mmap()` on startup and manages
free/used lists of smaller blocks. Calls to `malloc()` and friends then result
in allocations/deallocations using my allocator. This approach addresses the
above fragmentation issues and prevents memory-related function calls from
taking too long or varying unpredictably.

I considered using off-the-shelf allocators, but this experience made me a bit
paranoid. I decided that implementing one myself was a good exercise anyway so I
could be aware of its behavior under the hood. By implementing my own allocator
and overriding `malloc()` and friends to use my allocator, I was able to collect
and display allocation statistics and understand how my application uses memory
as I was debugging and testing it.

I also reviewed my code and re-architected parts of it to pre-allocate pools of
objects on startup, which are then re-used as much as possible.

While continuing my efforts with profiling and tracing using Tracy, I also
learned the importance of being aware of the memory allocation behavior of the
tracing code (and third-party framework code!) that you integrate into your
application. Tracy has its own allocator, which is great, but one needs to be
mindful of the tracing features enabled and the volume of data being collected
to avoid affecting the real-time behavior of the application being traced.
