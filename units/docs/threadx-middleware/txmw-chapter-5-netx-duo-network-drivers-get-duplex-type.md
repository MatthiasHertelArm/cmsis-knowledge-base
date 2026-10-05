---
id: "txmw-chapter-5-netx-duo-network-drivers-get-duplex-type"
type: "concept"
domain: "rtos"
title: "Chapter 5 - NetX Duo Network Drivers: Driver Requests / Get Duplex Type"
summary: "This request is made from within the nx_ip_driver_direct_command service. The driver stores the link's duplex type in the supplied destination. The following NX_IP_DRIVER members are used for the duplex type request."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter5.md#get-duplex-type"
license: "MIT"
mode: "V"
---

_Part of: Driver Requests_

This request is made from within the ***nx_ip_driver_direct_command*** service. The driver stores the link's duplex type in the supplied destination. The following NX_IP_DRIVER members are used for the duplex type request.

| NX_IP_DRIVER member   | Meaning                                                                                                    |
| --------------------------- | -------------------------------------------------------------------------------------------------------------- |
| nx_ip_driver_command     | NX_LINK_GET_DUPLEX_TYPE                                                                                    |
| nx_ip_driver_ptr         | Pointer to IP instance                                                                                         |
| nx_ip_driver_return_ptr | Pointer to the destination to place the duplex type                                                            |
| nx_ip_driver_interface   | Pointer to the interface instance                                                                              |
| nx_ip_driver_status      | Completion status. If the driver is not able to get duplex information, it will return a nonzero error status. |

> **Important:** *This request is not used internally by NetX Duo so its implementation is optional*.
