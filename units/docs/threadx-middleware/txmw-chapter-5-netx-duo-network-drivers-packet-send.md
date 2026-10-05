---
id: "txmw-chapter-5-netx-duo-network-drivers-packet-send"
type: "concept"
domain: "rtos"
title: "Chapter 5 - NetX Duo Network Drivers: Driver Requests / Packet Send"
summary: "This request is made during internal IPv4 or IPv6 send processing, which all NetX Duo protocols use to transmit packets (except for ARP, RARP)."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter5.md#packet-send"
license: "MIT"
mode: "V"
---

_Part of: Driver Requests_

This request is made during internal IPv4 or IPv6 send processing, which all NetX Duo protocols use to transmit packets (except for ARP, RARP). On receiving the packet send command, the *nx_packet_prepend_ptr* points to the beginning of the packet to be sent, which is the beginning of the IPv4 or IPv6 header. *nx_packet_length* indicates the total size (in bytes) of the data being transmitted. If *nx_packet_next* is valid, the outgoing IP datagram is stored in multiple packets, the driver is required to follow the chained packet and transmit the entire frame. Note that valid data area in each chained packet is stored between *nx_packet_prepend_ptr* and *nx_packet_append_ptr*.

The driver is responsible for constructing physical header. If physical address to IP address mapping is required (such as Ethernet), the IP layer already resolved the MAC address. The destination MAC address is passed from the IP instance, stored in *nx_ip_driver_physical_address_msw and nx_ip_driver_physical_address_lsw*.

After adding the physical header, the packet send processing then calls the driver's output function to transmit the packet.

The following NX_IP_DRIVER members are used for the packet send request.

| NX_IP_DRIVER member              | Meaning                               |
| -----------------------------------| --------------------------------------|
| nx_ip_driver_command            | NX_LINK_PACKET_SEND                |
| nx_ip_driver_ptr                | Pointer to IP instance                |
| nx_ip_driver_packet             | Pointer to the packet to send         |
| nx_ip_driver_interface          | Pointer to the interface instance.    |
| nx_ip_driver_physical_address_msw | Most significant 32-bits of physical address (only if physical mapping needed) |
| nx_ip_driver_physical_address_lsw | Least significant 32-bits of physical address (only if physical mapping needed) |
| nx_ip_driver_status             | Completion status. If the driver is not able to send the packet, it will return a non-zero error status. |
