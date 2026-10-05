---
id: "txmw-chapter-5-netx-duo-network-drivers-user-commands"
type: "concept"
domain: "rtos"
title: "Chapter 5 - NetX Duo Network Drivers: Driver Requests / User Commands"
summary: "This request is made from within the nx_ip_driver_direct_command service. The driver processes the application specific user commands. The following NX_IP_DRIVER members are used for the user command request."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter5.md#user-commands"
license: "MIT"
mode: "V"
---

_Part of: Driver Requests_

This request is made from within the ***nx_ip_driver_direct_command*** service. The driver processes the application specific user commands. The following NX_IP_DRIVER members are used for the user command request.

| NX_IP_DRIVER member       | Meaning                       |
| --------------------------- | ----------------------------- |
| nx_ip_driver_command     | NX_LINK_USER_COMMAND       |
| nx_ip_driver_ptr         | Pointer to IP instance        |
| nx_ip_driver_return_ptr | User defined       |
| nx_ip_driver_interface   | Pointer to the interface instance    |
| nx_ip_driver_status      | Completion status. If the driver is not able to execute user commands, it will return a non-zero error status. |

> **Important:** *This request is not used internally by NetX Duo so its implementation is optional*.
