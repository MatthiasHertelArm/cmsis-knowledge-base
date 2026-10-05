---
id: "intr-how-do-breakpoints-even-work-cortex-m-hardware-breakpoints"
type: "concept"
domain: "debug"
title: "How do breakpoints even work?: Cortex-M Hardware Breakpoints"
summary: "Now that we have a pretty good idea of how GDB sets and removes breakpoints let's see if we can figure out how the gdbserver is actually installing them for the nRF52 Cortex-M target."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-17-cortex-m-breakpoints.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-breakpoints#cortex-m-hardware-breakpoints"
license: "CC-BY-SA-4.0"
mode: "V"
---

Now that we have a pretty good idea of how GDB sets and removes breakpoints let's see if we can figure out how the gdbserver is actually installing them for the nRF52 Cortex-M target.
