---
id: "txmw-chapter-3-functional-components-of-ip-control-block-nx-ip"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: IPv4 Protocol / IP Control Block NX_IP"
summary: "The characteristics of each IP instance are found in its control block. It contains useful information such as the IP addresses and network masks of each network device, and a table of neighbor IP and physical hardware address mapping."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#ip-control-block-nx-ip"
license: "MIT"
mode: "V"
---

_Part of: IPv4 Protocol_

The characteristics of each IP instance are found in its control block. It contains useful information such as the IP addresses and network masks of each network device, and a table of neighbor IP and physical hardware address mapping. This structure is defined in the ***nx_api.h***file. If IPv6 is enabled, it also contains an array of IPv6 address, the number of which is specified by the user configurable option ***NX_MAX_IPV6_ADDRESSES***. The default value allows each physical network
interface to have three IPv6 addresses.

IP instance control blocks can be located anywhere in memory, but it is most common to make the control block a global structure by defining it outside the scope of any function.
