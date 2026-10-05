---
id: "txmw-chapter-3-functional-components-of-multihome-support"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: Execution Overview / Multihome Support"
summary: "NetX Duo supports systems connected to multiple physical devices using a single IP instance. Each physical interface is assigned to an interface control block in the IP instance."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#multihome-support"
license: "MIT"
mode: "V"
---

_Part of: Execution Overview_

NetX Duo supports systems connected to multiple physical devices using a single IP instance. Each physical interface is assigned to an interface control block in the IP instance. Applications wishing to use a multihome system must define the value for ***NX_MAX_PHYSICAL_INTERFACES*** to the number of physical devices attached to the system, and rebuild NetX Duo library. By default ***NX_MAX_PHYSICAL_INTERFACES*** is set to one, creating one interface control block in the IP instance.

The NetX Duo application creates a single IP instance for the primary device using the ***nx_ip_create*** service. For each additional network devices, the application attaches the device to the IP instance using the ***nx_ip_interface_attach*** service.

Each network interface structure contains a subset of network information about the network interface that is contained in the IP control block, including interface IPv4 address, subnet mask, IP MTU size, and MAC-layer address information.

> **Note:** *NetX Duo with multihome support is backward compatible with earlier versions of NetX Duo. Services that do not take explicit interface information default to the primary network device.*

The primary interface has index zero in the IP instance list. Each subsequent device attached to the IP instance is assigned the next index.

All upper layer protocol services for which the IP instance is enabled, including TCP, UDP, ICMP, and IGMP, are available to all the attached devices.

In most cases, NetX Duo can determine the best source address to use when transmitting a packet. The source address selection is based on the destination address. NetX Duo services are added to allow applications to specify a specific source address to use, in cases where the most suitable one cannot be determined by the destination
address. An example would be in a multihome system, an application needs to send a packet to an IPv4 broadcast or multicast destination addresses.

Services specifically for developing multihome applications include the following:

- *nx_igmp_multicast_interface_join*
- *nx_igmp_multicast_interface_leave*
- *nx_ip_driver_interface_direct_command*
- *nx_ip_interface_address_get*
- *nx_ip_interface_address_mapping_configure*
- *nx_ip_interface_address_set*  
- *nx_ip_interface_attach*
- *nx_ip_interface_capability_get* 
- *nx_ip_interface_capability_set*
- *nx_ip_interface_detach*
- *nx_ip_interface_info_get*
- *nx_ip_interface_mtu_set*
- *nx_ip_interface_physical_address_get*
- *nx_ip_interface_physical_address_set*
- *nx_ip_interface_status_check*
- *nx_ip_raw_packet_source_send*
- *nx_ipv4_multicast_interface_join*
- *nx_ipv4_multicast_interface_leave*
- *nx_udp_socket_source_send*
- *nxd_ipv6_multicast_interface_join*
- *nxd_ipv6_multicast_interface_leave* 
- *nxd_udp_socket_source_send*
- *nxd_icmp_source_ping*
- *nxd_ip_raw_packet_source_send*
- *nxd_udp_socket_source_send*

These services are explained in greater detail in [Description of NetX Duo Services](https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter4.md).
