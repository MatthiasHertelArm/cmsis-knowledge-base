---
id: "txmw-chapter-3-functional-components-of-tcp-keepalive"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: Transmission Control Protocol (TCP) / TCP Keepalive"
summary: "Part of: Transmission Control Protocol (TCP)"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#tcp-keepalive"
license: "MIT"
mode: "V"
---

_Part of: Transmission Control Protocol (TCP)_

TCP Keepalive feature allows a socket to detect whether or not its peer disconnects without proper termination (for example, the peer crashed), or to prevent certain network monitoring facilities to terminate a connection for long periods of idle. TCP Keepalive works by periodically sending a TCP frame with no data, and the sequence number set to one less than the current sequence number. On receiving such TCP Keepalive frame, the recipient, if still alive, responses with an ACK for its current sequence number. This completes the keepalive transaction.  

By default the keepalive feature is not enabled. To use this feature, NetX Duo library must be built with ***NX_ENABLE_TCP_KEEPALIVE*** defined. The symbol ***NX_TCP_KEEPALIVE_INITIAL*** specifies the number of seconds of inactivity before the keepalive frame is initiated.
