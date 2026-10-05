---
id: "txmw-chapter-2-installation-and-use-of-troubleshooting"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and use of FileX: Troubleshooting"
summary: "Each FileX port is delivered with a demonstration application. It is always a good idea to get the demonstration system running first—either on the target hardware or a specific demonstration environment."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/filex/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/filex/chapter2.md#troubleshooting"
license: "MIT"
mode: "V"
---

Each FileX port is delivered with a demonstration application. It is always a good idea to get the demonstration system running first—either on the target hardware or a specific demonstration environment.

If the demonstration system does not work, try the following things to narrow the problem:

1. Determine how much of the demonstration is running.
1. Increase stack sizes (this is more important in actual application code than it is for the demonstration).
1. Ensure there is enough RAM for the 32KBytes default RAM disk size. The basic system will operate on much less RAM; however, as more of the RAM disk is used, problems will surface if there is not enough memory.
1. Temporarily bypass any recent changes to see if the problem disappears or changes.
