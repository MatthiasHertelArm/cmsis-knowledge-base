---
id: "txmw-chapter-5-netx-duo-network-drivers-multicast-group-join"
type: "concept"
domain: "rtos"
title: "Chapter 5 - NetX Duo Network Drivers: Driver Requests / Multicast Group Join"
summary: "This request is made with the nx_igmp_multicast_interface join and nx_ipv4_multicast_interface_join service in IPv4, nxd_ipv6_multicast_interface_join service in IPv6, and various operation required by IPv6."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter5.md#multicast-group-join"
license: "MIT"
mode: "V"
---

_Part of: Driver Requests_

This request is made with the ***nx_igmp_multicast_interface join*** and ***nx_ipv4_multicast_interface_join*** service in IPv4, ***nxd_ipv6_multicast_interface_join*** service in IPv6, and various operation required by IPv6. The network driver takes the supplied multicast group address and sets up the physical media to accept incoming packets from that multicast group address. Note that for drivers that don't support multicast filter, the driver receive logic may have to be in promiscuous mode. In this case, the driver may need to filter incoming frames based on destination MAC address, thus reducing the amount of traffic passed into the IP instance. The following NX_IP_DRIVER members are used for the multicast group join request.

| NX_IP_DRIVER member                  | Meaning                                 |
| -------------------------------------- | --------------------------------------- |
| nx_ip_driver_command                | NX_LINK_MULTICAST_JOIN               |
| nx_ip_driver_ptr                    | Pointer to IP instance  |
| nx_ip_driver_physical_address_msw | Most significant 32-bits of physical multicast address |
| nx_ip_driver_physical_address_lsw | Least significant 32-bits of physical multicast address |
| nx_ip_driver_interface              | Pointer to the interface instance |
| nx_ip_driver_status                 | Completion status. If the driver is not able to join the multicast group, it will return a non-zero error status. |

> **Note:** *IPv6 applications will require multicast to be implemented in the driver for ICMPv6 based protocols such as address configuration. However, for IPv4 applications, implementation of this request is not necessary if multicast capabilities are not required*.

> **Important:** *If IPv6 is not enabled, and multicast capabilities are not required by IPv4, implementation of this request is not required*.
