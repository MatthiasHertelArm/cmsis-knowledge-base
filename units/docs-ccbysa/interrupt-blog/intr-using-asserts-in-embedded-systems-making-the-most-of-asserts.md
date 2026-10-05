---
id: "intr-using-asserts-in-embedded-systems-making-the-most-of-asserts"
type: "concept"
domain: "debug"
title: "Using Asserts in Embedded Systems: Making the Most of Asserts"
summary: "To get the most value from asserting, it is important to set up some postmortem infrastructure."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-05-asserts-in-embedded-systems.md"
doc_source: "https://interrupt.memfault.com/blog/asserts-in-embedded-systems#making-the-most-of-asserts"
license: "CC-BY-SA-4.0"
mode: "V"
---

To get the most value from asserting, it is important to set up some postmortem
infrastructure. When an assert takes place (or even a system fault), there is _a
lot_ of context and data one can capture to help debug these issues. These
include but are not limited to:

- the file and line number the assert took place at
- the registers at the time of assert
- values or function pointers on the stack, to help reassemble the backtrace.
- the logs that took place before the assert and possibly after the reboot took
  place
- for those using MyNewt[^1], ESP-IDF[^2], or have Memfault[^3] integrated, a
  coredump can be captured at the time of the assert, which will provide a full
  dump of system memory and registers, allowing one to clearly see why and how
  the system triggered an assert

With all of the above, especially coredumps, it becomes advantageous to add as
many asserts to the system as possible, especially for capturing those 1 in
10,000 hour bugs. This allows developers to quickly track down and investigate
bugs affecting users in the field, all without having to reproduce the issue on
a development board.
