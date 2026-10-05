---
id: "txmw-chapter-5-netx-duo-network-drivers-packet-broadcast-ipv4-packets-only"
type: "concept"
domain: "rtos"
title: "Chapter 5 - NetX Duo Network Drivers: Driver Requests / Packet Broadcast(IPv4 packets only)"
summary: "This request is almost identical to the send packet request. The only difference is that the destination physical address fields are set to the Ethernet broadcast MAC address. The following NX_IP_DRIVER members are used for the packet broadcast request."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter5.md#packet-broadcast-ipv4-packets-only"
license: "MIT"
mode: "V"
---

_Part of: Driver Requests_

This request is almost identical to the send packet request. The only difference is that the destination physical address fields are set to the Ethernet broadcast MAC address. The following NX_IP_DRIVER members are used for the packet broadcast request.

| NX_IP_DRIVER member                | Meaning                                                                                                  |
|------------------------------------|----------------------------------------------------------------------------------------------------------|
| nx_ip_driver_command               | NX_LINK_PACKET_BROADCAST                                                                                 |
| nx_ip_driver_ptr                   | Pointer to IP instance                                                                                   |
| nx_ip_driver_packet                | Pointer to the packet to send                                                                            |
| nx_ip_driver_physical_address_ms w | 0x0000FFFF (broadcast)                                                                                   |
| nx_ip_driver_physical_address_lsw  | 0xFFFFFFFF (broadcast)                                                                                   |
| nx_ip_driver_interface             | Pointer to the interface instance.                                                                       |
| nx_ip_driver_status                | Completion status. If the driver is not able to send the packet, it will return a non-zero error status. |
