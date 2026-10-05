---
id: "txmw-chapter-3-functional-components-of-ip-receive"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: IPv4 Protocol / IP Receive"
summary: "The IP receive processing is either called from the network driver or the internal IP thread (for processing packets on the deferred received packet queue)."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#ip-receive"
license: "MIT"
mode: "V"
---

_Part of: IPv4 Protocol_

The IP receive processing is either called from the network driver or the internal IP thread (for processing packets on the deferred received packet queue). The IP receive processing examines the protocol field and attempts to dispatch the packet to the proper protocol component. Before the packet is actually dispatched, the IP header is removed by advancing the prepend pointer past the IP header.

IP receive processing also detects fragmented IP packets and performs the necessary steps to reassemble them if fragmentation is enabled. If fragmentation is needed but not enabled, the packet is dropped.

NetX Duo determines the appropriate network interface based on the interface specified in the packet. If the packet interface is NULL, NetX Duo defaults to the primary interface. This is done to guarantee compatibility with legacy NetX Duo Ethernet drivers.
