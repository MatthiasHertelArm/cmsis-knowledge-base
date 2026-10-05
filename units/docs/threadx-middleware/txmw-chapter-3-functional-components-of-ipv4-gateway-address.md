---
id: "txmw-chapter-3-functional-components-of-ipv4-gateway-address"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: IPv4 Protocol / IPv4 Gateway Address"
summary: "Network gateways assist hosts on their networks to relay packets destined to destinations outside the local domain."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#ipv4-gateway-address"
license: "MIT"
mode: "V"
---

_Part of: IPv4 Protocol_

Network gateways assist hosts on their networks to relay packets destined to destinations outside the local domain. Each node has some knowledge of which next hop to send to, either the destination 
one of its neighbors, or through a pre-programmed static routing table. However if these approaches fail, the node should forward the packet to its default gateway which has better knowledge on how to
route the packet to its destination. Note that the default gateway must be directly accessible through one of the physical interfaces attached to the IP instance. The application calls ***nx_ip_gateway_address_set*** to configure IPv4 default gateway address. Use the service ***nx_ip_gateway_address_get*** to retrieve the current IPv4 gateway settings. Application shall use the service ***nx_ip_gateway_address_clear*** to clear the gateway setting.
