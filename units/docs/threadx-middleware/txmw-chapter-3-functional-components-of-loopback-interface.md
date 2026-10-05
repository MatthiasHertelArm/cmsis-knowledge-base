---
id: "txmw-chapter-3-functional-components-of-loopback-interface"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: Execution Overview / Loopback Interface"
summary: "The loopback interface is a special network interface without an physical link attached to."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#loopback-interface"
license: "MIT"
mode: "V"
---

_Part of: Execution Overview_

The loopback interface is a special network interface without an physical link attached to. The loopback interface allows applications to communicate using the IPv4 loopback address 127.0.0.1 To utilize a logical loopback interface, ensure the configurable option ***NX_DISABLE_LOOPBACK_INTERFACE*** is not set.
