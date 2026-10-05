---
id: "intr-a-deep-dive-into-arm-cortex-m-debu-the-arm-debugger-stack"
type: "concept"
domain: "debug"
title: "A Deep Dive into ARM Cortex-M Debug Interfaces: The ARM Debugger Stack"
summary: "All Cortex-M's implement a framework known as the Coresight architecture[^1]. This architecture is broken into several major components. Notably,"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-08-06-a-deep-dive-into-arm-cortex-m-debug-interfaces.md"
doc_source: "https://interrupt.memfault.com/blog/a-deep-dive-into-arm-cortex-m-debug-interfaces#the-arm-debugger-stack"
license: "CC-BY-SA-4.0"
mode: "V"
---

All Cortex-M's implement a framework known as the Coresight architecture[^1]. This architecture is broken into several major components. Notably,

- The subsystem used for debug, initial silicon validation, & system bringup known as the **Debug Access Port** (**DAP**)
- A subsystem that allows for traceability known as the Arm **Embedded Trace Macrocell** (**ETM**). This can be used to stream out data & instruction accesses while a system is running.

In this article we will explore the functionality of the **DAP**.
