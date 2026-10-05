---
id: "txmw-chapter-5-netx-duo-network-drivers-driver-capability"
type: "concept"
domain: "rtos"
title: "Chapter 5 - NetX Duo Network Drivers: Driver Capability"
summary: "Some network interfaces offer checksum offload features. Device drivers may take advantage of the hardware accelerations to free up CPU time from running various checksum computations."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter5.md#driver-capability"
license: "MIT"
mode: "V"
---

Some network interfaces offer checksum offload features. Device drivers may take advantage of the hardware accelerations to free up CPU time from running various checksum computations.

Depending the level of hardware checksum support from the hardware, the device driver needs to inform the IP instance which hardware feature is enabled. This way, the IP instance is aware of the hardware feature, and offload as much computation to the hardware as possible. The driver should use the API ***nx_ip_interface_capability_set*** to set all the features the physical interface is able to handle.

The following features can be used:

- NX_INTERFACE_CAPABILITY_IPV4_TX_CHECKSUM
- NX_INTERFACE_CAPABILITY_IPV4_RX_CHECKSUM
- NX_INTERFACE_CAPABILITY_TCP_TX_CHECKSUM
- NX_INTERFACE_CAPABILITY_TCP_RX_CHECKSUM
- NX_INTERFACE_CAPABILITY_UDP_TX_CHECKSUM
- NX_INTERFACE_CAPABILITY_UDP_RX_CHECKSUM
- NX_INTERFACE_CAPABILITY_ICMPV4_TX_CHECKSUM
- NX_INTERFACE_CAPABILITY_ICMPV4_RX_CHECKSUM
- NX_INTERFACE_CAPABILITY_ICMPV6_TX_CHECKSUM
- NX_INTERFACE_CAPABILITY_ICMPV6_RX_CHECKSUM
- NX_INTERFACE_CAPABILITY_IGMP_TX_CHECKSUM
- NX_INTERFACE_CAPABILITY_IGMP_RX_CHECKSUM

For a checksum computation that can be performed in hardware, the driver must set up the hardware or the buffer descriptors correctly so the checksum for an out-going packet can be generated and inserted into the header by the hardware. On receiving a packet, the hardware checksum logic should be able to verify the checksum value. If the checksum value is incorrect, the received frame should be discarded.

Even with the capability of performing checksum computation in hardware, the IP instance still maintains the checksum capability. In certain scenarios, for example a UDP datagram going through IPsec protection, the UDP checksum must be computed in software before passing the UDP frame down the stack. Most hardware checksum feature does not support checksum computation for a segment of data protected by IPsec. For a UDP or ICMP frame that needs to be fragmented, the UDP or ICMP checksum needs to be computed in software. Most hardware checksum logic does not handle the case where the data is split into multiple frames.
