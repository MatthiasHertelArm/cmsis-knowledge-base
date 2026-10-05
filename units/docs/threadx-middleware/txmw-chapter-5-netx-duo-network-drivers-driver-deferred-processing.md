---
id: "txmw-chapter-5-netx-duo-network-drivers-driver-deferred-processing"
type: "concept"
domain: "rtos"
title: "Chapter 5 - NetX Duo Network Drivers: Driver Requests / Driver Deferred Processing"
summary: "This request is made from the IP helper thread in response to the driver calling the nx_ip_driver_deferred_processing routine from a transmit or receive ISR."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter5.md#driver-deferred-processing"
license: "MIT"
mode: "V"
---

_Part of: Driver Requests_

This request is made from the IP helper thread in response to the driver calling the _***nx_ip_driver_deferred_processing*** routine from a transmit or receive ISR. This allows the driver ISR to defer the packet receive and transmit processing to the IP helper thread and thus reduce the amount to process in the ISR. The *nx_interface_additional_link_info* field in the NX_INTERFACE structure pointed to by *nx_ip_driver_interface* may be used by the driver to store information about the deferred processing event from the IP helper thread context. The following  NX_IP_DRIVER members are used for the deferred processing event.

| NX_IP_DRIVER member     | Meaning                           |
| ------------------------- | --------------------------------- |
| nx_ip_driver_command   | NX_LINK_DEFERRED_PROCESSING    |
| nx_ip_driver_ptr       | Pointer to IP instance            |
| nx_ip_driver_interface | Pointer to the interface instance |
