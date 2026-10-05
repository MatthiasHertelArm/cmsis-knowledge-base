---
id: "threadx-chapter-2-installation-use-of-thre-troubleshooting"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation & Use of ThreadX SMP: Troubleshooting"
summary: "Each ThreadX SMP port is delivered with a demonstration application. It is always a good idea to first get the demonstration system running—either on actual target hardware or simulated environment."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/threadx-smp/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/threadx-smp/chapter2.md#troubleshooting"
license: "MIT"
mode: "V"
---

Each ThreadX SMP port is delivered with a demonstration application. It is always a good idea to first get the demonstration system running—either on actual target hardware or simulated environment.

> **Important:** See the **readme_threadx.txt** file supplied with the distribution for more specific details regarding the demonstration system.

If the demonstration system does not execute properly, the following are some troubleshooting tips:

  - Determine how much of the demonstration is running.

  - Increase stack sizes (this is more important in actual application code than it is for the demonstration).

  - Rebuild the ThreadX SMP library with TX_ENABLE_STACK_CHECKING defined. This will enable the built-in ThreadX SMP stack checking.

  - Temporarily bypass any recent changes to see if the problem disappears or changes.
