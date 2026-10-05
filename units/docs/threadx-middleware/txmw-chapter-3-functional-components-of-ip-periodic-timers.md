---
id: "txmw-chapter-3-functional-components-of-ip-periodic-timers"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: Execution Overview / IP Periodic Timers"
summary: "There are two ThreadX periodic timers used for each IP instance. The first one is a one-second timer for ARP, IGMP, TCP timeout, and it also drives IP fragment reassemble processing."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#ip-periodic-timers"
license: "MIT"
mode: "V"
---

_Part of: Execution Overview_

There are two ThreadX periodic timers used for each IP instance. The first one is a one-second timer for ARP, IGMP, TCP timeout, and it also drives IP fragment reassemble processing. The second timer is a 100ms timer to drive the TCP retransmission timeout and IPv6-related operations.
