---
id: "txmw-chapter-5-netx-duo-network-drivers-detach-interface"
type: "concept"
domain: "rtos"
title: "Chapter 5 - NetX Duo Network Drivers: Driver Requests / Detach Interface"
summary: "This request is invoked by NetX Duo to the device driver, allowing the driver to disassociate the driver instance with the corresponding IP instance and the physical interface instance within the IP."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter5.md#detach-interface"
license: "MIT"
mode: "V"
---

_Part of: Driver Requests_

This request is invoked by NetX Duo to the device driver, allowing the driver to disassociate the driver instance with the corresponding IP instance and the physical interface instance within the IP. The following NX_IP_DRIVER members are used for the attach interface request.

| NX_IP_DRIVER member    | Meaning                                                                                                                                    |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| nx_ip_driver_command   | NX_LINK_INTERFACE_DETACH                                                                                                                   |
| nx_ip_driver_ptr       | Pointer to IP instance                                                                                                                     |
| nx_ip_driver_interface | Pointer to the interface instance.                                                                                                         |
| nx_ip_driver_status    | Completion status. If the driver is not able to attach the specified interface to the IP instance, it will return a non-zero error status. |
