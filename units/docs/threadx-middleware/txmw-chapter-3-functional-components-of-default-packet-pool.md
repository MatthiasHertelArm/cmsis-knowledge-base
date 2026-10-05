---
id: "txmw-chapter-3-functional-components-of-default-packet-pool"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: IPv4 Protocol / Default Packet Pool"
summary: "Each IP instance is given a default packet pool during creation."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#default-packet-pool"
license: "MIT"
mode: "V"
---

_Part of: IPv4 Protocol_

Each IP instance is given a default packet pool during creation. This packet pool is used to allocate packets for ARP, RARP, ICMP, IGMP, various TCP control packets (SYN, ACK, and so on), Neighbor Discovery, Router Discovery, and Duplicate Address Detection. If the default packet pool is empty when NetX Duo needs to allocate a packet, NetX Duo may have to abort the particular operation, and will return an error message if possible.
