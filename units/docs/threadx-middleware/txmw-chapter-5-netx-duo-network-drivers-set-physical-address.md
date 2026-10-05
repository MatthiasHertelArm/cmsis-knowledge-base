---
id: "txmw-chapter-5-netx-duo-network-drivers-set-physical-address"
type: "concept"
domain: "rtos"
title: "Chapter 5 - NetX Duo Network Drivers: Driver Requests / Set Physical Address"
summary: "This request is made from within the nx_ip_interface_physical_address_set service. This service allows an application to change the interface physical address at run time."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter5.md#set-physical-address"
license: "MIT"
mode: "V"
---

_Part of: Driver Requests_

This request is made from within the ***nx_ip_interface_physical_address_set*** service. This service allows an application to change the interface physical address at run time. On receiving this command, the driver is required to re-configure the hardware address of the network interface to the supplied physical address. Since the IP instance already has the new address, there is no need to call the ***nx_ip_interface_address_set*** service from this command.

The following NX_IP_DRIVER members are used for the user command request.

| NX_IP_DRIVER member      | Meaning                      |
| -------------------------- | ---------------------------- |
| nx_ip_driver_command    | NX_LINK_SET_PHYSICAL_ADDRESS  |
| nx_ip_driver_ptr        | Pointer to IP instance  |
| nx_ip_driver_interface  | Pointer to the interface instance   |
| nx_ip_driver_physical_ad dress_msw | Most significant 32-bits of the new physical address  |
| nx_ip_driver_physical_ad dress_lsw | Least significant 32-bits of the new physical address  |
| nx_ip_driver_status                  | Completion status. If the driver is not able to reconfigure the physical address, it will return a non-zero error status. |
