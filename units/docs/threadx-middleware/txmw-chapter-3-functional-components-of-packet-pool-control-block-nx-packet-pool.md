---
id: "txmw-chapter-3-functional-components-of-packet-pool-control-block-nx-packet-pool"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: Packet Pools / Packet Pool Control Block NX_PACKET_POOL"
summary: "The characteristics of each packet memory pool are found in its control block. It contains useful information such as the linked list of free packets, the number of free packets, and the payload size for packets in this pool."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#packet-pool-control-block-nx-packet-pool"
license: "MIT"
mode: "V"
---

_Part of: Packet Pools_

The characteristics of each packet memory pool are found in its control block. It contains useful information such as the linked list of free packets, the number of free packets, and the payload size for packets in this pool. This structure is defined in the ***nx_api.h*** file.

Packet pool control blocks can be located anywhere in memory, but it is most common to make the control block a global structure by defining it outside the scope of any function.
