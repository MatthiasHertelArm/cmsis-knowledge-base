---
id: "pyocd-semihosting-how-it-works"
type: "concept"
domain: "debug"
title: "Semihosting: How it works"
summary: "To implement semihosting, the debugger intercepts requests from code running on the target and performs the specified action on the target's behalf. Figure 1 below shows how semihosting requests work."
status: "draft"
collection: "pyocd"
source: "pyocd/pyOCD@d1974ff:docs/semihosting.md"
doc_source: "https://github.com/pyocd/pyOCD/blob/d1974ff/docs/semihosting.md#how-it-works"
license: "Apache-2.0"
mode: "V"
---

To implement semihosting, the debugger intercepts requests from code running on the target and performs
the specified action on the target's behalf. Figure 1 below shows how semihosting requests work.

\
**Figure 1**. Semihosting block diagram.

The figure demonstrates and example of how a C standard library call is made to `printf()`. This is routed to a
semihosting handler, which prepares the request parameters and triggers the debugger to perform the request, in this
case writing "hello world" to the console.

For Arm Cortex-M devices, a `BKPT` instruction with a parameter of 0xAB serves as the trigger detected by the debugger.
