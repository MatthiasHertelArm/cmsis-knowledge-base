---
id: "txmw-chapter-3-functional-components-of-pool-statistics-and-errors"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: Packet Pools / Pool Statistics and Errors"
summary: "If enabled, the NetX Duo packet management software keeps track of several statistics and errors that may be useful to the application. The following statistics and error reports are maintained for packet pools:"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#pool-statistics-and-errors"
license: "MIT"
mode: "V"
---

_Part of: Packet Pools_

If enabled, the NetX Duo packet management software keeps track of several statistics and errors that may be useful to the application. The following statistics and error reports are maintained for packet pools:

- Total Packets in Pool
- Free Packets in Pool
- Total Packet Allocations
- Pool Empty Allocation Requests
- Pool Empty Allocation Suspensions
- Invalid Packet Releases

All of these statistics and error reports, except for total and free packet count in pool, are built into NetX Duo library unless ***NX_DISABLE_PACKET_INFO*** is defined. This data is available to the application with the ***nx_packet_pool_info_get*** service.
