---
id: "txmw-chapter-3-functional-components-of-creating-ip-instances"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: IPv4 Protocol / Creating IP Instances"
summary: "IP instances are created either during initialization or during runtime by application threads."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#creating-ip-instances"
license: "MIT"
mode: "V"
---

_Part of: IPv4 Protocol_

IP instances are created either during initialization or during runtime by application threads. The initial IPv4 address, network mask, default packet pool, media driver, and memory and priority of the internal IP thread are defined by the ***nx_ip_create***service even if the application intends to use IPv6 networks only. If the application initializes the IP instance with its IPv4 address set to an invalid address(0.0.0.0), it is assumed that the interface address is going to resolved by manual configuration later, via RARP, or through DHCP or similar protocols.

For systems with multiple network interfaces, the primary interface is designated when calling ***nx_ip_create***. Each additional interface can be attached to the same IP instance by calling ***nx_ip_interface_attach***. This service stores information about the network interface (such as IP
address, network mask) in the interface control block, and associates the driver instance with the interface control block in the IP instance. As the driver receives a data packet, it needs to store the
interface information in the NX_PACKET structure before forwarding it to the IP receive logic. Note an IP instance must already be created before attaching any interfaces.

IPv6 services are not started after calling ***nx_ip_create***. Applications wishing to use IPv6 services must call the service ***nx_ipv6_enable*** to start IPv6.

On the IPv6 network, each interface in an IP instance may have multiple IPv6 global addresses. In addition to using DHCPv6 for IPv6 address assignment, a device may also use Stateless Address Autoconfiguration. More information is available in the "IP Control Block" and "IPv6 Address Resolution"
sections later in this chapter.
