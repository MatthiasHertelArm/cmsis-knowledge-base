---
id: "txmw-chapter-3-functional-components-of-tcp-socket-control-block-nx-tcp-socket"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: Transmission Control Protocol (TCP) / TCP Socket Control Block NX_TCP_SOCKET"
summary: "Part of: Transmission Control Protocol (TCP)"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#tcp-socket-control-block-nx-tcp-socket"
license: "MIT"
mode: "V"
---

_Part of: Transmission Control Protocol (TCP)_

The characteristics of each TCP socket are found in the associated *NX_TCP_SOCKET* control block, which contains useful information such as the link to the IP data structure, the network connection interface, the bound port, and the receive packet queue. This structure is defined in the ***nx_api.h*** file.
