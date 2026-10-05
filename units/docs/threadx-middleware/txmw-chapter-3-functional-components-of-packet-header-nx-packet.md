---
id: "txmw-chapter-3-functional-components-of-packet-header-nx-packet"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: Packet Pools / Packet Header NX_PACKET"
summary: "By default, NetX Duo places the packet header immediately before the packet payload area. The packet memory pool is basically a series of packets— headers followed immediately by the packet payload."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#packet-header-nx-packet"
license: "MIT"
mode: "V"
---

_Part of: Packet Pools_

By default, NetX Duo places the packet header immediately before the packet payload area. The packet memory pool is basically a series of packets— headers followed immediately by the
packet payload. The packet header (***NX_PACKET***) and the layout of the packet pool are pictured in Figure 3.

For network devices driver that are able to perform zero copy operations, typically the starting address of the packet payload area is programmed into the DMA logic. Certain DMA engines have alignment
requirement on the payload area. To make the starting address of the payload area align properly for the DMA engine, or the cache operation, the user can define the symbol ***NX_PACKET_ALIGNMENT***.

> **Warning:** *It is important for the network driver to use the **nx_packet_transmit_release** function when transmission of a packet is complete. This function checks to make sure the packet is not part of a TCP output queue before it is actually placed back in the available pool.*

(figure: Packet Header and Packet Pool Layout)

**FIGURE 3. Packet Header and Packet Pool Layout**

The fields of the packet header are defined as follows. Note that this table is not a comprehensive list of all the members in the *NX_PACKET* structure.

|Packet header | Purpose |
|---|---|
|***nx_packet_pool_owner***|This field points to the packet pool that owns this particular packet. When the packet is released, it is released to this particular pool. With the pool ownership inside each packet, it is possible for a datagram to span multiple packets from multiple packet pools.|
|***nx_packet_next***|This field points to the next packet within the same frame. If NULL, there are no additional packets that are part of the frame. This field is also used to hold fragmented packets until the entire packet can be re-assembled. it is removed if ***NX_DISABLE_PACKET_CHAIN***is defined.|
|***nx_packet_last***|This field points to the last packet within the same network packet. If NULL, this packet represents the entire network packet. This field is removed if ***NX_DISABLE_PACKET_CHAIN***is defined.|
|***nx_packet_length***| This field contains the total number of bytes in the entire network packet, including the total of all bytes in all packets chained together by the *nx_packet_next*member.|
|***nx_packet_ip_interface***| This field is the interface control block which is assigned to the packet when it is received by the interface driver, and by NetX Duo for outgoing packets. An interface control block describes the interface e.g. network address, MAC address, IP address and interface status such as link enabled and physical mapping required.|
|***nx_packet_data_start***| This field points to the start of the physical payload area of this packet. It does not have to be immediately following the NX_PACKET header, but that is the default for the ***nx_packet_pool_create*** service.|
|***nx_packet_data_end***|This field points to the end of the physical payload area of this packet. The difference between this field and the *nx_packet_data_start* field represents the payload size.|
|***nx_packet_prepend_ptr***|This field points to the location of where packet data, either protocol header or actual data, is added in front of the existing packet data (if any) in the packet payload area. It must be greater than or equal to the *nx_packet_data_start* pointer location and less than or equal to the *nx_packet_append_ptr* pointer.

**Caution:** *For performance reasons, NetX Duo assumes that when the packet is passed into NetX Duo services for transmission, the prepend pointer points to long word aligned address.*|
|***nx_packet_append_ptr***|This field points to the end of the data currently in the packet payload area. It must be in between the memory location pointed to by *nx_packet_prepend_ptr* and *nx_packet_data_end.* The difference between this field and the *nx_packet_prepend_ptr* field represents the amount of data in this packet.|
|***nx_packet_packet_pad***|This fields defines the length of padding in 4-byte words to achieve the desired alignment requirement. This field is removed if ***NX_PACKET_HEADER_PAD*** is not defined. Alternatively ***NX_PACKET_ALIGNMENT*** can be used instead of defining *nx_packet_header_pad.*|
