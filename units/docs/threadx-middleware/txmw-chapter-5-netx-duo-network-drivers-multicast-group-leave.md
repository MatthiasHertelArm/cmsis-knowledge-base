---
id: "txmw-chapter-5-netx-duo-network-drivers-multicast-group-leave"
type: "concept"
domain: "rtos"
title: "Chapter 5 - NetX Duo Network Drivers: Driver Requests / Multicast Group Leave"
summary: "This request is invoked by explicitly calling the nx_igmp_multicast_interface_leave or nx_ipv4_multicast_interface_leave services in IPv4, nxd_ipv6_multicast_interface_leave service in IPv6, or by various internal NetX Duo operations required for IPv6. The driver removes the supplied Ethernet multicast address from the multicast list."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter5.md#multicast-group-leave"
license: "MIT"
mode: "V"
---

_Part of: Driver Requests_

This request is invoked by explicitly calling the ***nx_igmp_multicast_interface_leave*** or ***nx_ipv4_multicast_interface_leave*** services in IPv4, ***nxd_ipv6_multicast_interface_leave*** service in IPv6, or by various internal NetX Duo operations required for IPv6. The driver removes the supplied Ethernet multicast address from the multicast list. After a host has left a multicast group, packets on the network with this Ethernet multicast address are no longer received by this IP instance. The following NX_IP_DRIVER members are used for the multicast group leave request.

| NX_IP_DRIVER member              | Meaning                              |
| -----------------------------------| -------------------------------------|
| nx_ip_driver_command            | NX_LINK_MULTICAST_LEAVE           |
| nx_ip_driver_ptr                | Pointer to IP instance   |
| nx_ip_driver_physical_address_msw | Most significant 32 bits of physical multicast address |
| nx_ip_driver_physical_address_lsw | Least significant 32 bits of physical multicast address |
| nx_ip_driver_interface              | Pointer to the interface instance |
| nx_ip_driver_status                 | Completion status. If the driver is not able to leave the multicast group, it will return a non-zero error status. |

> **Important:** *If multicast capabilities are not required by either IPv4 or IPv6, implementation of this request is not required*.
