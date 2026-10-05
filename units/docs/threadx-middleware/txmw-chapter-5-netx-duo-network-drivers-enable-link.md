---
id: "txmw-chapter-5-netx-duo-network-drivers-enable-link"
type: "concept"
domain: "rtos"
title: "Chapter 5 - NetX Duo Network Drivers: Driver Requests / Enable Link"
summary: "Next, the IP helper thread enables the physical network by setting the driver command to NX_LINK_ENABLE in the driver request and sending the request to the network driver. This happens shortly after the IP helper thread completes the initialization request."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter5.md#enable-link"
license: "MIT"
mode: "V"
---

_Part of: Driver Requests_

Next, the IP helper thread enables the physical network by setting the driver command to NX_LINK_ENABLE in the driver request and sending the request to the network driver. This happens shortly after the IP helper thread completes the initialization request. Enabling the link may be as simple as setting the *nx_interface_link_up* field in the interface instance. But it may also involve manipulation of the physical hardware. The following NX_IP_DRIVER members are used for the enable link request.

| NX_IP_DRIVER member       | Meaning                      |
| ------------------------- | ---------------------------- |
| nx_ip_driver_command   | NX_LINK_ENABLE   |
| nx_ip_driver_ptr       | Pointer to IP instance  |
| nx_ip_driver_interface | Pointer to the interface instance |
| nx_ip_driver_status    | Completion status. If the driver is not able to enable the specified interface, it will return a non-zero error status. |
