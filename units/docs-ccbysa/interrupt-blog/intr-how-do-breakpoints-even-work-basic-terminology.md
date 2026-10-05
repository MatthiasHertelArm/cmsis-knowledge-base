---
id: "intr-how-do-breakpoints-even-work-basic-terminology"
type: "concept"
domain: "debug"
title: "How do breakpoints even work?: Basic Terminology"
summary: "There are two classes of breakpoints known as the \"hardware breakpoint\" and \"software breakpoint\"."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-17-cortex-m-breakpoints.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-breakpoints#basic-terminology"
license: "CC-BY-SA-4.0"
mode: "V"
---

There are two classes of breakpoints known as the "hardware breakpoint" and "software breakpoint".

### Hardware Breakpoint

Hardware breakpoints are implemented by the chipset being used. At the silicon level, they are comparators that compare the instruction being fetched against an instruction configured in a peripheral register. When the instructions match, the hardware will trigger a debug event, halting the core or generating an exception. There's usually a small, fixed number of hardware breakpoints available for any given chip. If you've ever used a debugger where you ran out of breakpoints, this is why!

### Software Breakpoint

Software breakpoints, on the other hand, are implemented by your debugger. They work by **patching** the code you are trying to execute with an instruction that triggers a debug event in some fashion. This is accomplished by injecting a breakpoint instruction or when that is not supported by inserting an instruction that causes a fault that halts the core.

With software breakpoints, a debugger can essentially expose an "unlimited" number of breakpoints. There are some challenges to deal with though:

- Not all code regions are patchable (i.e Read-Only-Memory (ROM))
- If the debugger crashes, the code can be left in a bad state (patched instruction instead of the actual code!).
