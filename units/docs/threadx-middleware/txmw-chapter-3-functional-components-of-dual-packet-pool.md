---
id: "txmw-chapter-3-functional-components-of-dual-packet-pool"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: Packet Pools / Dual Packet Pool"
summary: "Typically the payload size of the default IP packet pool is large enough to accommodate frame size up to the network interface MTU."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#dual-packet-pool"
license: "MIT"
mode: "V"
---

_Part of: Packet Pools_

Typically the payload size of the default IP packet pool is large enough to accommodate frame size up to the network interface MTU. During normal operation, the IP thread needs to send messages such as ARP, TCP control messages, IGMP messages, ICMPv6 messages. These messages use the packets allocated from the default packet pool in the IP instance. On a memory-constrained system where the amount of memory available for packet pool is limited, using a single packet pool (with the large payload size to match MTU size) may not be an optimal solution. NetX Duo allows application to install an auxiliary packet pool, where the payload size is smaller. Once the auxiliary packet pool is installed, the IP helper thread would allocate packets from either the default packet pool or the auxiliary pool, depending on the size of the message it transmits. For an auxiliary packet pool, a payload size of 200 bytes would work with most of the messages the IP helper thread transmits.

By default NetX Duo library is built without enabling dual packet pool. To enable the feature, build the library with ***NX_DUAL_PACKET_POOL_ENABLE*** defined. Then the auxiliary packet pool can be set by calling ***nx_ip_auxiliary_packet_pool_set***.

There is also the option of creating more than one packet pool. For example a transmit packet pool is created with optimal payload size for expected message sizes. A receive packet pool is created in the
driver with a payload size set to the driver MTU, since one cannot predict the size of received packets.
