---
id: "intr-faster-debugging-with-watchpoints-basic-terminology"
type: "concept"
domain: "debug"
title: "Faster Debugging with Watchpoints: Basic Terminology"
summary: "Watchpoints are very similar to breakpoints and are often referred to as \"data breakpoints\"."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-09-16-cortex-m-watchpoints.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-watchpoints#basic-terminology"
license: "CC-BY-SA-4.0"
mode: "V"
---

Watchpoints are very similar to breakpoints and are often referred to as "data breakpoints". Where breakpoints allow you to halt program flow based on a certain instruction being executed, watchpoints allow you to halt flow based on a particular data access. Watchpoints can be used to monitor "write", "read" or "read/write" accesses. For example, a watchpoint might be configured to trip when a variable gets updated, a region of the stack is written to, or a particular buffer is read from.

In order for watchpoints to work and system execution to not grind to a halt, native hardware support for this functionality is required. This is implemented at the silicon level with a comparator. Every time a data access is made, the address accessed is compared against the value in the watchpoint comparator which can be done in parallel to the normal execution flow. If the value of the comparator matches the address being accessed, the system emits an event and the MCU is halted. If they do not match, the system keeps running as normal and there is no overhead to the operation!
