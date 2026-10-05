---
id: "txmw-chapter-3-functional-components-of-network-driver"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: Execution Overview / Network Driver"
summary: "Each IP instance in NetX Duo has a primary interface, which is identified by its device driver specified in the nx_ip_create service."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#network-driver"
license: "MIT"
mode: "V"
---

_Part of: Execution Overview_

Each IP instance in NetX Duo has a primary interface, which is identified by its device driver specified in the ***nx_ip_create*** service. The network driver is responsible for handling various NetX Duo requests, including packet transmission, packet reception, and requests for status and control. 

For a multi-home system, the IP instance has multiple interfaces, each with an associated network driver that performs these tasks for the respective interface.

The network driver must also handle asynchronous events occurring on the media. Asynchronous events from the media include packet reception, packet transmission completion, and status changes. NetX Duo provides the network driver with several access functions to handle various events. These functions are designed to be called from the  interrupt service routine portion of the network driver. For IPv4 networks, the network driver should forward all ARP packets received to the ***_nx_arp_packet_deferred_receive*** internal function. All RARP packets should be forwarded to
***_nx_rarp_packet_deferred_receive*** internal function. There are two options for IP packets. If fast dispatch of IP packets is required, incoming IP packets should be forwarded to ***_nx_ip_packet_receive*** for immediate processing. This greatly improves NetX Duo performance in handling IP packets. Otherwise, forwarding IP packets to ***_nx_ip_packet_deferred_receive*** should be done. This service places the IP packet in the deferred processing queue where it is then
handled by the internal IP thread, which results in the least amount of ISR processing time.

The network driver can also defer interrupt processing to run out of the context of the IP thread. In this mode, the ISR shall save the necessary information, call the internal function ***_nx_ip_driver_deferred_processing***, and acknowledge the interrupt controller. This service notifies IP thread to schedule a callback to the device driver to complete the process of the event that causes the interrupt.

Some network controllers are capable of performing TCP/IP header checksum computation and validation in hardware, without taking up valuable CPU resources. To take advantage of the hardware capability feature, NetX Duo provides options to enable or disable various software checksum computation at compilation time, as well as turning on or off checksum computation at run time, if the device driver is able to communicate with the IP layer about is hardware capabilities. See [Chapter 5 - NetX Duo Network Drivers](https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter5.md) for more detailed information on writing NetX Duo network drivers.
