---
id: "txmw-chapter-3-functional-components-of-ipv6-header"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: IPv6 in NetX Duo / IPv6 Header"
summary: "The IPv6 header has been modified from the IPv4 header. When allocating a packet, the caller specifies the application protocol (e.g., UDP, TCP), buffer size in bytes, and hop limit."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#ipv6-header"
license: "MIT"
mode: "V"
---

_Part of: IPv6 in NetX Duo_

The IPv6 header has been modified from the IPv4 header. When allocating a packet, the caller specifies the application protocol (e.g., UDP, TCP), buffer size in bytes, and hop limit.   

Figure 9 shows the format of the IPv6 header and the table lists the header components.

(figure: Diagram of the IPv6 header format.)

**FIGURE 9. IPv6 Header Format**

|IP header | Purpose |
|---|---|
|Version |4-bit field for IP version. For IPv6 networks, the value in this field must be 6; For IPv4 networks it must be 4.|
|Traffic Class |8-bit field that stores the traffic class information. This field is not used by NetX Duo.|
|Flow Label |20-bit field to uniquely identify the flow, if any, that a packet is associated with. A value of zero indicates the packet does not belong to a particular flow. This field replaces the *TOS*field in IPv4.|
|Payload Length |16-bit field indicating the amount of data in bytes of the IPv6 packet following the IPv6 base header. This includes all encapsulated protocol header and data.|
|Next Header | 8-bit field indicating the type of the extension header that follows the IPv6 base header. This field replaces the *Protocol*field in IPv4.|
|Hop Limit |8-bit field that limits the number of routers the packet is allowed to go through. This field replaces the *TTL*field in IPv4.|
|Source Address |128-bit field that stores the IPv6 address of the sender.|
|Destination Address |128-bit field that sores the IPv6 address of the destination.|
