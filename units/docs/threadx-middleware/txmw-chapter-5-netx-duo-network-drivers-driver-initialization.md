---
id: "txmw-chapter-5-netx-duo-network-drivers-driver-initialization"
type: "concept"
domain: "rtos"
title: "Chapter 5 - NetX Duo Network Drivers: Driver Requests / Driver Initialization"
summary: "Although the actual driver initialization processing is application specific, it usually consists of data structure and physical hardware initialization."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter5.md#driver-initialization"
license: "MIT"
mode: "V"
---

_Part of: Driver Requests_

Although the actual driver initialization processing is application specific, it usually consists of data structure and physical hardware initialization. The information required from NetX Duo for driver initialization is the IP Maximum Transmission Unit (MTU), which is the number of bytes available to the IP-layer payload, including IPv4 or IPv6 header) and if the physical interface needs logical-to-physical mapping. The driver configures the interface MTU value by calling ***nx_ip_interface_mtu_set***.

The device driver needs to call ***nx_ip_interface_address_mapping_configure*** to inform NetX Duo whether or not interface address mapping is required. If address mapping is needed, the driver is responsible for configuring the interface with valid MAC address, and supply the MAC address to NetX via ***nx_ip_interface_physical_address_set***.

When the network driver receives the NX_LINK INITIALIZE request from NetX Duo, it receives a pointer to the IP control block as part of the NX_IP_DRIVER request control block shown above.

After the application calls ***nx_ip_create***, the IP helper thread sends a driver request with the command set to NX_LINK_INITIALIZE to the driver to initialize its physical network interface. The following NX_IP_DRIVER members are used for the initialize request.

| NX_IP_DRIVER member | Meaning    |
| ------------------------- | ----------------------------- |
| nx_ip_driver_command   | NX_LINK_INITIALIZE    |
| nx_ip_driver_ptr       | Pointer to the IP instance. This value should be saved by the driver so that the driver function can find the IP instance to operate on.    |
| nx_ip_driver_interface | Pointer to the network interface structure within the IP instance. This information should be saved by the driver. On receiving packets, the driver shall use the interface structure information when sending the packet up the stack. The interface index (device index) can be obtained by reading the member nx_interface_index inside this data structure. |
| nx_ip_driver_status    | Completion status. If the driver is not able to initialize the specified interface to the IP instance, it will return a nonzero error status. |


> **Note:** *The driver is actually called from the IP helper thread that was created for the IP instance. Therefore the driver routine should avoid performing blocking operations, or the IP helper thread could stall, causing unbounded delays to applications that rely on the IP thread*.
