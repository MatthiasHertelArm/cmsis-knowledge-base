---
id: "txmw-chapter-3-functional-components-of-raw-ip-receive"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: IPv4 Protocol / Raw IP Receive"
summary: "If raw IP packet processing is enabled, the application may receive raw IP packets through the nx_ip_raw_packet_receive service. All incoming packets are processed according to the protocol specified in the IP header."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#raw-ip-receive"
license: "MIT"
mode: "V"
---

_Part of: IPv4 Protocol_

If raw IP packet processing is enabled, the application may receive raw IP packets through the ***nx_ip_raw_packet_receive*** service. All incoming packets are processed according to the protocol specified in the IP header. If the protocol specifies UDP, TCP, IGMP or ICMP, NetX Duo will process the packet using the appropriate handler for the packet protocol type. If the protocol is not one of these protocols, and raw IP receive is enabled, the incoming packet will be put into the raw packet queue waiting for the application to receive it via the ***nx_ip_raw_packet_receive*** service. In addition, application threads may suspend with an optional timeout while waiting for a raw
IP packet. The number of packets that can be queued on the raw packet queue is limited. The maximum value is defined in ***NX_IP_RAW_MAX_QUEUE_DEPTH***, whose default value is 20. An application may change the maximum value by calling the ***nx_ip_raw_receive_queue_max_set*** service.

Alternatively, the NetX Duo library may be built with ***NX_ENABLE_IP_RAW_PACKET_FILTER*.** In this mode of operation, the application provides a callback function that is invoked every time a packet with an unhandled protocol type is received. The IP receive logic forwards the packet to the user-defined raw packet receive filter routine. The filter routine decides whether or not to keep the raw packet for future process. The return value from the callback routine indicates whether the packet has been processed by the raw packet receive filter. If the packet is processed by the callback function, the packet should be released after the application is done with the packet. Otherwise, NetX Duo is responsible for releasing the packet. Refer to the ***nx_ip_raw_packet_filter_set*** for more information on how to use the raw packet filter function.

> **Note:** *The BSD wrapper function for NetX Duo relies on the raw packet filter function to handle BSD raw sockets. Therefore, to support raw socket in the BSD wrapper, the NetX Duo library must be built with ***NX_ENABLE_IP_RAW_PACKET_FILTER*** defined, and the application should not use the ***nx_ip_raw_packet_filter_set*** to install its own raw packet filter functions.*
