---
id: "txmw-chapter-2-installation-and-use-of-target-considerations-2"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and Use of NetX Duo: Target Considerations"
summary: "NetX Duo requires between 5 KBytes and 45 KBytes of Read-Only Memory (ROM) on the target. Another 1 to 5KBytes of the target's Random Access Memory (RAM) are required for the NetX Duo thread stack and other global data structures."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter2.md#target-considerations"
license: "MIT"
mode: "V"
---

NetX Duo requires between 5 KBytes and 45 KBytes of Read-Only Memory (ROM) on the target. Another 1 to 5KBytes of the target's Random Access Memory (RAM) are required for the NetX Duo thread stack and other global data structures.

In addition, NetX Duo requires the use of two ThreadX timer objects and one ThreadX mutex object. These facilities are used for periodic processing needs and thread protection inside the NetX Duo protocol stack.
