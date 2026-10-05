---
id: "txmw-chapter-5-netx-duo-network-drivers-get-link-status"
type: "concept"
domain: "rtos"
title: "Chapter 5 - NetX Duo Network Drivers: Driver Requests / Get Link Status"
summary: "The application can query the network interface link status using the NetX Duo service nx_ip_interface_status_check service for any interface on the host. See Chapter 4, \"Description of NetX Duo Services\" on page 149, for more details on these services."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter5.md#get-link-status"
license: "MIT"
mode: "V"
---

_Part of: Driver Requests_

The application can query the network interface link status using the NetX Duo service ***nx_ip_interface_status_check*** service for any interface on the host. See Chapter 4, "Description of NetX Duo Services" on page 149, for more details on these services.

The link status is contained in the *nx_interface_link_up* field in the NX_INTERFACE structure pointed to by *nx_ip_driver_interface* pointer. The following NX_IP_DRIVER members are used for the link status request.

| NX_IP_DRIVER member       | Meaning                  |
| --------------------------- | -------------------------|
| nx_ip_driver_command     | NX_LINK_GET_STATUS    |
| nx_ip_driver_ptr         | Pointer to IP instance   |
| nx_ip_driver_return_ptr | Pointer to the destination to place the status. |
| nx_ip_driver_interface   | Pointer to the interface instance   |
| nx_ip_driver_status      | Completion status. If the driver is not able to get specific status, it will return a non-zero error status. |

> **Note:** ***nx_ip_status_check*** is still available for checking the status of the primary interface. However, application developers are encouraged to use the interface specific service: ***nx_ip_interface_status_check.***
