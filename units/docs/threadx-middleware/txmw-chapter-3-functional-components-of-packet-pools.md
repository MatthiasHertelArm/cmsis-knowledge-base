---
id: "txmw-chapter-3-functional-components-of-packet-pools"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: Packet Pools"
summary: "Allocating packets in a fast and deterministic manner is always a challenge in real-time networking applications. With this in mind, NetX Duo provides the ability to create and manage multiple pools of fixed-size network packets."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#packet-pools"
license: "MIT"
mode: "V"
---

Allocating packets in a fast and deterministic manner is always a challenge in real-time networking applications. With this in mind, NetX Duo provides the ability to create and manage multiple pools of
fixed-size network packets.

Because NetX Duo packet pools consist of fixed-size memory blocks, there are never any internal fragmentation problems. Of course, fragmentation causes behavior that is inherently nondeterministic. In addition, the time required to allocate and free a NetX Duo packet amounts to simple linked-list manipulation. Furthermore, packet allocation and deallocation is done at the head of the available list. This provides the fastest possible linked list processing.

(figure: UDP Data Encapsulation)

**FIGURE 2. UDP Data Encapsulation**

Lack of flexibility is typically the main drawback of fixed-size packet pools. Determining the optimal packet payload size that also handles the worst-case incoming packet is a difficult task. NetX Duo packets address this problem with an optional feature called packet chaining. An actual network packet can be made of one or more NetX Duo packets linked together. In addition, the packet header maintains a pointer to the top of the packet. As additional protocols are added, this pointer is simply moved backwards and the new header is written directly in front of the data. Without the flexible packet technology, the stack would have to allocate another buffer and copy the data into a new buffer with the new header, which is processing intensive.

Since each packet payload size is fixed for a given packet pool, application data larger than the payload size would require multiple packets chained together. When filling a packet with user data, the
application shall use the service ***nx_packet_data_append***. This service moves application data into a packet. In situations where a packet is not enough to hold user data, additional packets are
allocated to store user data. To use packet chaining, the driver must be able to receive into or transmit from chained packets.

For embedded systems that do not need to use the packet chaining feature, the NetX Duo library can
be built with ***NX_DISABLE_PACKET_CHAIN*** to remove the packet chaining logic. Note that the IP fragmentation and reassembly feature may need to utilize the chained packet feature. Therefore defining ***NX_DISABLE_PACKET_CHAIN*** requires ***NX_DISABLE_FRAGMENTATION*** also be defined. 

Each NetX Duo packet memory pool is a public resource. NetX Duo places no constraints on how packet pools are used.
