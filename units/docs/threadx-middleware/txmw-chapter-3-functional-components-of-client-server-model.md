---
id: "txmw-chapter-3-functional-components-of-client-server-model"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: Transmission Control Protocol (TCP) / Client-Server Model"
summary: "Part of: Transmission Control Protocol (TCP)"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#client-server-model"
license: "MIT"
mode: "V"
---

_Part of: Transmission Control Protocol (TCP)_

To use TCP for data transfer, a connection must first be established between the two TCP sockets. The establishment of the connection is done in a client-server fashion. The client side of the connection is the side that initiates the connection, while the server side simply waits for client connection requests before any processing is done.

> **Important:** *For multihome devices, NetX Duo automatically determines the source address to use for the connection, and the next hop address based on the destination IP address of the connection. Because TCP is limited to sending packets to unicast (e.g.nonbroadcast) destination addresses, NetX Duo does not require a "hint" for choosing the source IPv6 address*.
