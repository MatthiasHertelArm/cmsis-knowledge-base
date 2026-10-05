---
id: "txmw-chapter-3-functional-components-of-tcp-checksum"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: Transmission Control Protocol (TCP) / TCP Checksum"
summary: "Part of: Transmission Control Protocol (TCP)"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#tcp-checksum"
license: "MIT"
mode: "V"
---

_Part of: Transmission Control Protocol (TCP)_

TCP specifies a one's complement 16-bit checksum that covers the IP pseudo header, (consisting of the source IP address, destination IP address, and the protocol/length IP word), the TCP header, and the TCP packet data. The only difference between IPv4 and IPv6 TCP packet header checksums is that the source and destination IP addresses are 32 bit in IPv4 and 128 bit in IPv6. 

Certain network controllers are able to perform TCP checksum computation and validation in hardware. For such systems, applications may want to use hardware checksum logic as much as possible to reduce runtime overhead. Applications may disable TCP checksum computation logic from the NetX Duo library altogether at build time by defining ***NX_DISABLE_TCP_TX_CHECKSUM*** and ***NX_DISABLE_TCP_RX_CHECKSUM***. This way, the TCP checksum code is not compiled in. However one should exercise caution if the optional NetX Duo IPsec package is installed, and the TCP connection may need to traverse through a secure channel. In this case, data in packets belonging to the TCP connection is already encrypted, and most hardware TCP checksum modules present in the network driver are unable to generate correct checksum value from the encrypted TCP payload.

To address this issue, application shall keep the TCP checksum logic available in the library and use the interface capability feature. With interface capability feature enabled, the TCP module knows how to
properly handle the TCP checksum if the driver is also able to compute the checksum value:

1) If the TCP packet is not subject to IPsec process, the network interface hardware is able to compute the checksum. Therefore the TCP module does not attempt to compute the checksum;

2) If IPsec package is installed, and the TCP packet is subject to IPsec process, the TCP module computes checksum in software before sending the packet to IPsec layer.
