---
id: "intr-how-do-breakpoints-even-work"
type: "concept"
domain: "debug"
title: "How do breakpoints even work?"
summary: "The idea of halting program execution was invented over 70 years ago as part of the ENIAC digital computer."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-17-cortex-m-breakpoints.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-breakpoints"
license: "CC-BY-SA-4.0"
mode: "V"
---

The idea of halting program execution was invented over 70 years ago as part of the ENIAC digital computer. At the time, to pause a program and debug, you had to physically unplug one of the cables controlling program flow, which was coined a "breakpoint". [^8]

Today, breakpoints are a ubiquitous way of debugging programs and most chip architectures even have dedicated instructions to trigger them! Have you ever wondered how they actually work? Or at the very least, gotten upset when they do not?



In this article, we will discuss the basic types of breakpoints (hardware and software) and how they are utilized by the GNU Project Debugger, GDB. We will then explore how to configure hardware breakpoints on an ARM Cortex-M MCU using the Flash Patch and Breakpoint Unit (**FPB**) and examine a real-world configuration with an example application.



> Note: While the focus of the article will be about breakpoints and how they work for firmware based on ARM Cortex-M MCUs, the
> general ideas presented apply to any compiled language and debugger.
