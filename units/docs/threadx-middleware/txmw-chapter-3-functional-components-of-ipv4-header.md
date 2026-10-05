---
id: "txmw-chapter-3-functional-components-of-ipv4-header"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: IPv4 Protocol / IPv4 Header"
summary: "For any IPv4 packet to be sent on the Internet, it must have an IPv4 header."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#ipv4-header"
license: "MIT"
mode: "V"
---

_Part of: IPv4 Protocol_

For any IPv4 packet to be sent on the Internet, it must have an IPv4 header. When higher-level protocols (UDP, TCP, ICMP, or IGMP) call the IP component to send a packet, the IPv4 transmit 
module places an IPv4 header in front of the data. Conversely, when IP packets are received from the network, the IP component removes the IPv4 header from the packet before delivery to the higher-level protocols. Figure 5 shows the format of the IP header.

(figure: IPv4 Header Format)

**FIGURE 5. IPv4 Header Format**

> **Important:** *All headers in the TCP/IP implementation are expected to be in **big endian** format. In this format, the most significant byte of the word resides at the lowest byte address. For example, the 4-bit version and the 4-bit header length of the IP header must be located on the first byte of the header.*

The fields of the IPv4 header are defined as follows:

|IPv4 Header Field |Purpose |
|---|---|
|***4-bit version*** |This field contains the version of IP this header represents. For IP version 4, which is what NetX Duo supports, the value of this field is 4. |
|***4-bit header length*** |This field specifies the number of 32-bit words in the IP header. If no option words are present, the value for this field is 5. |
|***8-bit type of service (TOS)*** |This field specifies the type of service requested for this IP packet. Valid requests are as follows:
- Normal: 0x00 
- Minimum Delay: 0x00
- Maximum Data: 0x08
- Maximum Reliability: 0x04
- Minimum Cost: 0x02 |
|***16-bit total length*** |This field contains the total length of the IP datagram in bytes, including the IP header. An IP datagram is the basic unit of information found on a TCP/IP Internet. It contains a destination and source address in addition to data. Because it is a 16-bit field, the maximum size of an IP datagram is 65,535 bytes.|
|***16-bit identification*** |The field is a number used to uniquely identify each IP datagram sent from a host. This number is typically incremented after an IP datagram is sent. It is especially useful in assembling received IP packet fragments.|
|***3-bit flags*** |This field contains IP fragmentation information. Bit 14 is the "don't fragment" bit. If this bit is set, the outgoing IP datagram will not be fragmented. Bit 13 is the "more fragments" bit. If this bit is set, there are more fragments. If this bit is clear, this is the last fragment of the IP packet.|
|***13-bit fragment offset*** |This field contains the upper 13-bits of the fragment offset. Because of this, fragment offsets are only allowed on 8-byte boundaries. The first fragment of a fragmented IP datagram will have the "more fragments" bit set and have an offset of 0.|
|***8-bit time to live (TTL)*** |This field contains the number of routers this datagram can pass, which basically limits the lifetime of the datagram.|
|***8-bit protocol***|This field specifies which protocol is using the IP datagram. The following is a list of valid protocols and their values:
- ICMP: 0x01 
- IGMP: 0x02
- TCP: 0X06
- UDP: 0X11 |
|***16-bit checksum*** |This field contains the 16-bit checksum that covers the IP header only. There are additional checksums in the higher level protocols that cover the IP payload. |
|***32-bit source IP address*** |This field contains the IP address of the sender and is always a host address. |
|***32-bit destination IP address*** |This field contains the IP address of the receiver or receivers if the address is a broadcast or multicast address. |
