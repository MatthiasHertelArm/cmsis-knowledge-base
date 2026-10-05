---
id: "txmw-chapter-3-functional-components-of-ipv6-multicast-support-in-netx-duo"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: IPv6 in NetX Duo / IPv6 Multicast Support In NetX Duo"
summary: "Multicast addresses specify a dynamic group of hosts on the Internet. Members of the multicast group may join and leave whenever they wish."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#ipv6-multicast-support-in-netx-duo"
license: "MIT"
mode: "V"
---

_Part of: IPv6 in NetX Duo_

Multicast addresses specify a dynamic group of hosts on the Internet. Members of the multicast group may join and leave whenever they wish. NetX Duo implements several ICMPv6 protocols, including Duplicate Address Detection, Neighbor Discovery, and Router Discovery, which require IP multicast capability. Therefore, NetX Duo expects the underlying device driver to support multicast operations.

When NetX Duo needs to join or leave a multicast group (such as the all-node multicast address, and the *solicited-node* multicast address), it issues a driver command to the device driver to join or leave a multicast MAC address. The driver command for joining the multicast address is ***NX_LINK_MULTICAST_JOIN***. To leave a multicast address, NetX Duo issues the driver command ***NX_LINK_MULTICAST_LEAVE***. The device driver must implement these two commands for ICMPv6 protocols to work properly.

Applications may join an IPv6 multicast group by using the service ***nxd_ipv6_multicast_interface_join*.** This service registers the multicast address with the IP stack, and then notifies the specified device driver of the IPv6 multicast address. To leave a
multicast group, applications use the service ***nxd_ipv6_multicast_interface_leave.***
