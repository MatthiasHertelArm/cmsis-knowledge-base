---
id: "txmw-chapter-5-netx-duo-network-drivers-arp-response-send"
type: "concept"
domain: "rtos"
title: "Chapter 5 - NetX Duo Network Drivers: Driver Requests / ARP Response Send"
summary: "This request is almost identical to the ARP send packet request. The only difference is the destination physical address fields are passed from the IP instance. The following NX_IP_DRIVER members are used for the ARP response send request."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter5.md#arp-response-send"
license: "MIT"
mode: "V"
---

_Part of: Driver Requests_

This request is almost identical to the ARP send packet request. The only difference is the destination physical address fields are passed from the IP instance. The following NX_IP_DRIVER members are used for the ARP response send request.

| NX_IP_DRIVER member                  | Meaning                                  |
| -------------------------------------- | -----------------------------------------|
| nx_ip_driver_command                | NX_LINK_ARP_RESPONSE_SEND            |
| nx_ip_driver_ptr                    | Pointer to IP instance   |
| nx_ip_driver_packet                 | Pointer to the packet to send          |
| nx_ip_driver_physical_address_msw | Most significant 32-bits of physical address |
| nx_ip_driver_physical_address_lsw | Least significant 32-bits of physical address |
| nx_ip_driver_interface              | Pointer to the interface instance |
| nx_ip_driver_status                 | Completion status. If the driver is not able to send the ARP packet, it will return a non-zero error status. |

> **Important:** *If physical mapping is not needed, implementation of this request is not required*.
