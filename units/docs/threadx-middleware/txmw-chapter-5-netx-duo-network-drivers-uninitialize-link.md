---
id: "txmw-chapter-5-netx-duo-network-drivers-uninitialize-link"
type: "concept"
domain: "rtos"
title: "Chapter 5 - NetX Duo Network Drivers: Driver Requests / Uninitialize Link"
summary: "This request is made by NetX Duo during the deletion of an IP instance by the nx_ip_delete service. This request uninitialized the interface, and release any resources created during initialization phase."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter5.md#uninitialize-link"
license: "MIT"
mode: "V"
---

_Part of: Driver Requests_

This request is made by NetX Duo during the deletion of an IP instance by the ***nx_ip_delete*** service. This request uninitialized the interface, and release any resources created during initialization phase. Typically it is a reverse operation of the ***Initialize Link*** operation. After the interface is uninitialized, the device cannot be used until the interface is initialized again.

The following NX_IP_DRIVER members are used for the disable link request.

| NX_IP_DRIVER member    | Meaning                  |
|------------------------|--------------------------|
| nx_ip_driver_command   | NX_LINK_UNINITIALIZE     |
| nx_ip_driver_ptr       | Pointer to IP instance   |
| nx_ip_driver_interface | Pointer to the interface instance |
| nx_ip_driver_status    | Completion status. If the driver is not able to uninitialize the specified interface to the IP instance, it will return a non-zero error status. |
