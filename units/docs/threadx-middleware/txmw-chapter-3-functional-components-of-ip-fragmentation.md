---
id: "txmw-chapter-3-functional-components-of-ip-fragmentation"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: IPv4 Protocol / IP Fragmentation"
summary: "The network device may have limits on the size of outgoing packets. This limit is called the maximum transmission unit (MTU)."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#ip-fragmentation"
license: "MIT"
mode: "V"
---

_Part of: IPv4 Protocol_

The network device may have limits on the size of outgoing packets. This limit is called the maximum transmission unit (MTU). IP MTU is the largest IP frame size a link layer driver is able to transmit without fragmenting the IP packet. During a device driver initialization phase, the driver module must configure its IP MTU size via the service ***nx_ip_interface_mtu_set.***

Although not recommended, the application may generate datagrams larger than the underlying IP MTU supported by the device. Before transmitting such IP datagram, the IP layer must fragment these packets. On receiving fragmented IP frames, the receiving end must store all fragmented IP frames with the same fragmentation ID, and reassemble them in order. If the IP receive logic is unable to collect all the fragments to restore the original IP frame in time, all the fragments are released. It is up to the upper layer protocol to detect such packet loss and recover from it.

The IP fragmentation applies to both IPv4 and IPv6 packets.

In order to support IP fragmentation and reassembly operation, the system designer must enable the IP fragmentation feature in NetX Duo using the ***nx_ip_fragment_enable*** service. If this feature is 
not enabled, incoming fragmented IP packets are discarded, as well as packets that exceed the network driver's MTU.

> **Note:** *The IP Fragmentation logic can be removed completely by defining ***NX_DISABLE_FRAGMENTATION*** when building the NetX Duo library. Doing so helps reduce the code size of NetX Duo. Note that in this situation, both the IPv4 and IPv6 fragmentation/reassembly functions are disabled.*

> **Note:** *If **NX_DISABLE_CHAINED_PACKET** is defined, IP fragmentation must be disabled.*

> **Note:** *In an IPv6 network, routers do not fragment a datagram if the size of the datagram exceeds its minimum MTU size. Therefore, it is up to the sending device to determine the minimum MTU between the source and the destination, and to ensure the IP datagram size does not exceed the path MTU. In NetX Duo, IPv6 PATH MTU discovery can be enabled by building NetX Duo library with the symbol **NX_ENABLE_IPV6_PATH_MTU_DISCOVERY** defined.*
