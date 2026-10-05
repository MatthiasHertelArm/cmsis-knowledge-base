---
id: "txmw-chapter-3-functional-components-of-raw-ip-send"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: IPv4 Protocol / Raw IP Send"
summary: "A raw IP packet is an IP frame that contains upper layer protocol payload not directly supported (and processed) by NetX Duo. A raw packet allows developers to define their own IP-based applications."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#raw-ip-send"
license: "MIT"
mode: "V"
---

_Part of: IPv4 Protocol_

A raw IP packet is an IP frame that contains upper layer protocol payload not directly supported (and processed) by NetX Duo. A raw packet allows developers to define their own IP-based applications. An application may send raw IP packets directly using the ***nxd_ip_raw_packet_send*** service if raw IP packet processing has been enabled with the ***nx_ip_raw_packet_enabled*** service. When transmitting a unicast packet on an IPv6 network, NetX Duo automatically determines the best source IPv6 address to use to send the packets out on, based on the destination address. If the destination address is a multicast (or broadcast for IPv4) address, however, NetX Duo will default to the first (primary) interface. Therefore, to send such packets out on secondary interfaces, the application must use the ***nx_ip_raw_packet_source_send*** service to specify the source address to use for the outgoing packet.
