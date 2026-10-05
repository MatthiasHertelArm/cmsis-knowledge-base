---
id: "txmw-chapter-3-functional-components-of-tcp-receive-notify"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: Transmission Control Protocol (TCP) / TCP Receive Notify"
summary: "Part of: Transmission Control Protocol (TCP)"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#tcp-receive-notify"
license: "MIT"
mode: "V"
---

_Part of: Transmission Control Protocol (TCP)_

If the application thread needs to process received data from more than one socket, the ***nx_tcp_socket_receive_notify*** function should be used. This function registers a receive packet callback function for the socket. Whenever a packet is received on the socket, the callback function is executed.  

The contents of the callback function are application specific; however, the function would most likely contain logic to inform the processing thread that a packet is available on the corresponding socket.
