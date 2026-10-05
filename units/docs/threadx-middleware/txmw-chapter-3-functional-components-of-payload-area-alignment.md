---
id: "txmw-chapter-3-functional-components-of-payload-area-alignment"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: Packet Pools / Payload Area Alignment"
summary: "Packet pool design in NetX Duo supports zero-copy. At the device driver level, the driver is able to assign the payload area directly into buffer descriptors for data reception."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#payload-area-alignment"
license: "MIT"
mode: "V"
---

_Part of: Packet Pools_

Packet pool design in NetX Duo supports zero-copy. At the device driver level, the driver is able to assign the payload area directly into buffer descriptors for data reception. Sometimes the DMA engine or the cache synchronization mechanism requires the starting address of the payload area to have a certain alignment requirement. This can be achieved by defining the desired alignment requirement (in bytes) in ***NX_PACKET_ALIGNMENT***. When creating a packet pool, the starting address of the payload area will aligned to this value. By default, starting address is 4-byte aligned.
