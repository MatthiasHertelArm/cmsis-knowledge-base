---
id: "txmw-chapter-3-functional-components-of-ipv4-addresses"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: IPv4 Protocol / IPv4 Addresses"
summary: "Each host on the Internet has a unique 32-bit identifier called an IP address. There are five classes of IPv4 addresses as described in Figure 4. The ranges of the five IPv4 address classes are as follows:"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#ipv4-addresses"
license: "MIT"
mode: "V"
---

_Part of: IPv4 Protocol_

Each host on the Internet has a unique 32-bit identifier called an IP address. There are five classes of IPv4 addresses as described in Figure 4. The ranges of the five IPv4 address classes are as follows:

|Class|Range|
|---|---|
|A |0.0.0.0 to 127.255.255.255|
|B |128.0.0.0 to 191.255.255.255|
|C |192.0.0.0 to 223.255.255.255|
|D |224.0.0.0 to 239.255.255.255|
|E |240.0.0.0 to 247.255.255.255|

(figure: Diagram of the IPv4 Address Structure.)

**FIGURE 4. IPv4 Address Structure**

There are also three types of address specifications: *unicast*, *broadcast*, and *multicast*. Unicast addresses are those IPv4 addresses that identify a specific host on the Internet. Unicast addresses can be either a source or a destination IPv4 address. A broadcast address identifies all hosts on a specific network or sub-network and can only be used as destination addresses. Broadcast addresses are specified by having the host ID portion of the address set to ones. Multicast addresses (Class D) specify a dynamic group of hosts on the Internet. Members of the multicast group may join and leave whenever they wish.

> **Important:** *Only connectionless protocols like UDP over IPv4 can utilize broadcast and the limited broadcast capability of the multicast group.*

> **Important:** *The macro *IP_ADDRESS* is defined in ***nx_api.h***. It allows easy specification of IPv4 addresses using commas instead of a periods. For example, *IP_ADDRESS(128,0,0,0)* specifies the first class B address shown in Figure 4.*
