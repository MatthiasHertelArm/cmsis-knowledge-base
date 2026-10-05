---
id: "txmw-chapter-3-functional-components-of-stop-listening-on-a-server-port"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: Transmission Control Protocol (TCP) / Stop Listening on a Server Port"
summary: "Part of: Transmission Control Protocol (TCP)"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#stop-listening-on-a-server-port"
license: "MIT"
mode: "V"
---

_Part of: Transmission Control Protocol (TCP)_

If the application no longer wishes to listen for client connection requests on a server port that was previously specified by a call to the ***nx_tcp_server_socket_listen*** service, the application simply calls the ***nx_tcp_server_socket_unlisten*** service. This service places any socket waiting for a connection back in the CLOSED state and releases any queued client connection request packets.
