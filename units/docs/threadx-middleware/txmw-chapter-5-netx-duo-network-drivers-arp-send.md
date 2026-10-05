---
id: "txmw-chapter-5-netx-duo-network-drivers-arp-send"
type: "concept"
domain: "rtos"
title: "Chapter 5 - NetX Duo Network Drivers: Driver Requests / ARP Send"
summary: "This request is also similar to the IP packet send request. The only difference is that the Ethernet header specifies an ARP packet instead of an IP packet, and destination physical address fields are set to MAC broadcast address."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter5.md#arp-send"
license: "MIT"
mode: "V"
---

_Part of: Driver Requests_

This request is also similar to the IP packet send request. The only difference is that the Ethernet header specifies an ARP packet instead of an IP packet, and destination physical address fields are set to MAC broadcast address. The following NX_IP_DRIVER members are used for the ARP send request.

| NX_IP_DRIVER member                | Meaning                                                                                                      |
|------------------------------------|--------------------------------------------------------------------------------------------------------------|
| nx_ip_driver_command               | NX_LINK_ARP_SEND                                                                                             |
| nx_ip_driver_ptr                   | Pointer to IP instance                                                                                       |
| nx_ip_driver_packet                | Pointer to the packet to send                                                                                |
| nx_ip_driver_physical_address_ms w | 0x0000FFFF (broadcast)                                                                                       |
| nx_ip_driver_physical_address_lsw  | 0xFFFFFFFF (broadcast)                                                                                       |
| nx_ip_driver_interface             | Pointer to the interface instance.                                                                           |
| nx_ip_driver_status                | Completion status. If the driver is not able to send the ARP packet, it will return a non-zero error status. |

> **Important:** *If physical mapping is not needed, implementation of this request is not required*.

*Although ARP has been replaced with the Neighbor Discovery Protocol and the Router Discovery Protocol in IPv6, Ethernet network drivers must still be compatible with IPv4 peers and routers. Therefore, drivers must still handle ARP packets*.
