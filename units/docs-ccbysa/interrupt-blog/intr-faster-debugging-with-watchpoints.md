---
id: "intr-faster-debugging-with-watchpoints"
type: "concept"
domain: "debug"
title: "Faster Debugging with Watchpoints"
summary: "One of the most challenging types of issues to debug is memory corruption!"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-09-16-cortex-m-watchpoints.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-watchpoints"
license: "CC-BY-SA-4.0"
mode: "V"
---

One of the most challenging types of issues to debug is memory corruption! Memory corruption can be caused for a variety of reasons including when data is used after it has been freed, a read or write goes past the end of a buffer, thread safety constructs are missing, or a linker script is misconfigured. By the time the system finally faults or encounters an error, the original operation which spiraled the system into the bad state is often lost!

Data breakpoints ("Watchpoints") can be used to catch memory corruption at the source and have personally saved me a tremendous amount of time debugging nefarious issues over the years. Whether you are a watchpoint power user or haven't used them before, I hope this article can teach you something new!



In this post we will explore how to save time debugging by making the most of watchpoints. We will walk through a few classic use cases of watchpoints by debugging an example application with GDB. Then, we will dive into how watchpoints are implemented for ARM Cortex-M based MCUs with the Data Watchpoint & Trace (**DWT**) unit and explore some advanced features.



> Note: While the examples in this article will use ARM Cortex-M hardware, the
> general ideas presented about watchpoints can be applied to any compiled language and debugger.
