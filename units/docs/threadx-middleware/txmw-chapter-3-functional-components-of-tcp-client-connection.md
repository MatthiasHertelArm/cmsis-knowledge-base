---
id: "txmw-chapter-3-functional-components-of-tcp-client-connection"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: Transmission Control Protocol (TCP) / TCP Client Connection"
summary: "Part of: Transmission Control Protocol (TCP)"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#tcp-client-connection"
license: "MIT"
mode: "V"
---

_Part of: Transmission Control Protocol (TCP)_

As mentioned previously, the client side of the TCP connection initiates a connection request to a TCP server. Before a connection request can be made, TCP must be enabled on the client IP instance. In addition, the client TCP socket must next be created with the ***nx_tcp_socket_create*** service and bound to a port via the ***nx_tcp_client_socket_bind*** service.

After the client socket is bound, the ***nxd_tcp_client_socket_connect*** service is used to establish a connection with a TCP server. Note the socket must be in a CLOSED state to initiate a connection attempt. Establishing the connection starts with NetX Duo issuing a SYN packet and then waiting for a SYN ACK packet back from the server, which signifies acceptance of the connection request. After the SYN ACK is received, NetX Duo responds with an ACK packet and promotes the client socket to the ESTABLISHED state.

(figure: Diagram of the states of the TCP state machine.)   

**FIGURE 14. States of the TCP State Machine**


> **Warning:** *Applications should use **nxd_tcp_client_socket_connect** for either IPv4 and IPv6 TCP connections. Applications can still use **nx_tcp_client_socket_connect** for IPv4 TCP connections, but developers are encouraged to use **nxd_tcp_client_socket_connect** since **nx_tcp_client_socket_connect** will eventually be deprecated*.

*Similarly, **nxd_tcp_socket_peer_info_get** works with either IPv4 or IPv6 TCP connections. However, **nx_tcp_socket_peer_info_get** is still available for legacy applications. Developers are encouraged to use **nxd_tcp_socket_peer_info_get** going forward*.
