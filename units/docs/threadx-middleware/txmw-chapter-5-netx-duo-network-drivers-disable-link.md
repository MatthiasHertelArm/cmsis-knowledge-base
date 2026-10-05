---
id: "txmw-chapter-5-netx-duo-network-drivers-disable-link"
type: "concept"
domain: "rtos"
title: "Chapter 5 - NetX Duo Network Drivers: Driver Requests / Disable Link"
summary: "This request is made by NetX Duo during the deletion of an IP instance by the nx_ip_delete service. Or an application may issue this command in order to temporarily disable the link in order to save power."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter5.md#disable-link"
license: "MIT"
mode: "V"
---

_Part of: Driver Requests_

This request is made by NetX Duo during the deletion of an IP instance by the ***nx_ip_delete*** service. Or an application may issue this command in order to temporarily disable the link in order to save power. This service disables the physical network interface on the IP instance. The processing to disable the link may be as simple as clearing the *nx_interface_link_up* flag in the interface instance. But it may also involve manipulation of the physical hardware. Typically it is a reverse operation of the ***Enable Link*** operation. After the link is disabled, the application request ***Enable Link*** operation to enable the interface.

The following NX_IP_DRIVER members are used for the disable link request.

| NX_IP_DRIVER member     | Meaning                      |
| ------------------------- | ---------------------------- |
| nx_ip_driver_command   | NX_LINK_DISABLE    |
| nx_ip_driver_ptr       | Pointer to IP instance   |
| nx_ip_driver_interface | Pointer to the interface instance   |
| nx_ip_driver_status    | Completion status. If the driver is not able to disable the specified interface in the IP instance, it will return a non-zero error status. |
