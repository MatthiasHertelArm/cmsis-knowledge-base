---
id: "intr-how-to-debug-a-hardfault-on-an-arm-determining-what-caused-the-fault"
type: "concept"
domain: "debug"
title: "How to debug a HardFault on an ARM Cortex-M MCU: Determining What Caused The Fault"
summary: "All MCUs in the Cortex-M series have several different pieces of state which can be analyzed when a fault takes place to trace down what went wrong."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-20-cortex-m-hardfault-debug.md"
doc_source: "https://interrupt.memfault.com/blog/cortex-m-hardfault-debug#determining-what-caused-the-fault"
license: "CC-BY-SA-4.0"
mode: "V"
---

All MCUs in the Cortex-M series have several different pieces of state which can be analyzed when a fault takes place to trace down what went wrong.

First we will explore the dedicated fault status registers that are present on all Cortex-M MCUs except the Cortex-M0.

If you are trying to debug a Cortex-M0, you can skip ahead to the [next section](#registers-prior-to-exception) where we discuss how to recover the core register state and instruction being executed at the time of the exception.

> NOTE: If you already know the state to inspect when a fault occurs, you may want to skip ahead to the section about how to [automate the analysis](#automating-the-analysis).
