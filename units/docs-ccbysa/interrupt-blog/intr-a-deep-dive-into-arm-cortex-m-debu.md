---
id: "intr-a-deep-dive-into-arm-cortex-m-debu"
type: "concept"
domain: "debug"
title: "A Deep Dive into ARM Cortex-M Debug Interfaces"
summary: "Ever had issues getting a debugger to flash code? Do your breakpoints not seem to work? Are you hitting weird errors while stepping through your code? Does your debugger seem flaky?"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-08-06-a-deep-dive-into-arm-cortex-m-debug-interfaces.md"
doc_source: "https://interrupt.memfault.com/blog/a-deep-dive-into-arm-cortex-m-debug-interfaces"
license: "CC-BY-SA-4.0"
mode: "V"
---

Ever had issues getting a debugger to flash code? Do your breakpoints not seem to work? Are you hitting weird errors while stepping through your code? Does your debugger seem flaky? Are you confused by all the buzzwords used around embedded debugging (i.e `SWD` vs `JTAG`, `OpenOCD` vs `pyOCD` vs `JLinkGDBServer`, `CMSIS-DAP` vs `ST-Link` vs `J-Link`, etc)

I've run into all of these issues! Having a basic understanding of the technology stack in use can be helpful for working through or around issues you may encounter with your debug setup!



In this article we will walk up through the hardware and software stack that enables debugging on `ARM Cortex-M` devices, demystify what is actually happening and go through a step-by-step example, tracing a basic debugger operation end to end using a logic analyzer.
