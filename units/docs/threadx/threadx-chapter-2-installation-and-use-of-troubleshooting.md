---
id: "threadx-chapter-2-installation-and-use-of-troubleshooting"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and Use of ThreadX: Troubleshooting"
summary: "Each ThreadX port is delivered with a demonstration application. It is always a good idea to first get the demonstration system running—either on actual target hardware or simulated environment."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter2.md#troubleshooting"
license: "MIT"
mode: "V"
---

Each ThreadX port is delivered with a demonstration application. It is always a good idea to first get the demonstration system running—either on actual target hardware or simulated environment.

If the demonstration system does not execute properly, the following are some troubleshooting tips.

1. Determine how much of the demonstration is running.
1. Increase stack sizes (this is more important in actual application code than it is for the demonstration).
1. Rebuild the ThreadX library with TX_ENABLE_STACK_CHECKING defined. This enables the built-in ThreadX stack checking.
1. Temporarily bypass any recent changes to see if the problem disappears or changes.
