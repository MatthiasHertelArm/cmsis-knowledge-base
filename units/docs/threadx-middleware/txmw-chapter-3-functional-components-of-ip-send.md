---
id: "txmw-chapter-3-functional-components-of-ip-send"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: IPv4 Protocol / IP Send"
summary: "The IP send processing in NetX Duo is very streamlined. The prepend pointer in the packet is moved backwards to accommodate the IP header."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#ip-send"
license: "MIT"
mode: "V"
---

_Part of: IPv4 Protocol_

The IP send processing in NetX Duo is very streamlined. The prepend pointer in the packet is moved backwards to accommodate the IP header. The IP header is completed (with all the options specified by the calling protocol layer), the IP checksum is computed in-line (for IPv4 packets only), and the packet is dispatched to the associated network driver. In addition, outgoing fragmentation is also coordinated from within the IP send processing.

For IPv4, NetX Duo initiates ARP requests if physical mapping is needed for the destination IP address. IPv6 uses Neighbor Discovery for IPv6-address-to-physical-address mapping.

> **Note:** *For IPv4 connectivity, packets that require IP address resolution (i.e., physical mapping) are enqueued on the ARP queue until the number of packets queued exceeds the ARP queue depth (defined by the symbol **NX_ARP_MAX_QUEUE_DEPTH**). If the queue depth is reached, NetX Duo will remove the oldest packet on the queue and continue waiting for address resolution for the remaining packets enqueued. On the other hand, if an ARP entry is not resolved, the pending packets on the ARP entry are released upon ARP entry timeout.*

For systems with multiple network interfaces, NetX Duo chooses an interface based on the destination IP address. The following procedure applies to the selection process:

1. If the sender specifies an outgoing interface and the interface is valid, use that interface.
2. If a destination address is IPv4 broadcast or multicast, the first enabled physical interface is used.
3. If the destination address is found in the static routing table, the interface associated with the gateway is used.
4. If the destination is on-link, the on-link interface is used.
5. If the destination address is a link-local address (169.254.0.0/16), the first valid interface is used.
6. If the default gateway is configured, use the interface associated with the default gateway to transmit the packet.
7. Finally, if one of the valid interface IP address is link-local address (169.254.0.0/16), this interface is used as source address for the transmission.
8. The output packet is dropped if all above fails.
