---
id: "txmw-chapter-5-netx-duo-network-drivers-get-error-count"
type: "concept"
domain: "rtos"
title: "Chapter 5 - NetX Duo Network Drivers: Driver Requests / Get Error Count"
summary: "This request is made from within the nx_ip_driver_direct_command service. The driver stores the link's error count in the supplied destination. To support this feature, the driver needs to track operation errors."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter5.md#get-error-count"
license: "MIT"
mode: "V"
---

_Part of: Driver Requests_

This request is made from within the ***nx_ip_driver_direct_command*** service. The driver stores the link's error count in the supplied destination. To support this feature, the driver needs to track operation errors. The following NX_IP_DRIVER members are used for the link error count request.

| NX_IP_DRIVER member   | Meaning                   |
| --------------------------- | -------------------------------|
| nx_ip_driver_command     | NX_LINK_GET_ERROR_COUNT   |
| nx_ip_driver_ptr         | Pointer to IP instance   |
| nx_ip_driver_return_ptr | Pointer to the destination to place the error count |
| nx_ip_driver_interface   | Pointer to the interface instance|
| nx_ip_driver_status      | Completion status. If the driver is not able to get error count, it will return a non-zero error status. |

> **Important:** *This request is not used internally by NetX Duo so its implementation is optional*.
