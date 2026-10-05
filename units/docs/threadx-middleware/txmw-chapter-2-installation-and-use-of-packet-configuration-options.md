---
id: "txmw-chapter-2-installation-and-use-of-packet-configuration-options"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and Use of NetX Duo: Configuration Options / Packet Configuration Options"
summary: "Chapter 2 - Installation and Use of NetX Duo: Configuration Options / Packet Configuration Options"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter2.md#packet-configuration-options"
license: "MIT"
mode: "V"
---

_Part of: Configuration Options_

| Option  | Description  |
|---|---|
|NX_DISABLE_PACKET_CHAIN | Defined, disables the packet chain logic. By default this is not defined.|
|NX_DISABLE_PACKET_INFO | Defined, disables packet pool information gathering.|
|NX_ENABLE_LOW_WATERMARK | Defined, enables NetX Duo packet pool low watermark feature. Application sets low watermark value. On receiving TCP packets, if the packet pool low watermark is reached, NetX Duo silently discards the packet by releasing it, preventing the packet pool from starvation. By default this feature is not enabled.|
|NX_ENABLE_PACKET_DEBUG_INFO | Defined, logs packet debug information.|
|NX_PACKET_ALIGNMENT | Defined, specifies the alignment requirement, in bytes, for starting address of the packet payload area. This option deprecates  ***NX_PACKET_HEADER_PAD*** and ***NX_PACKET_HEADER_PAD_SIZE***. By default this option is defined to be 4, making the starting address of the payload area 4-byte aligned.|
|NX_PACKET_HEADER_PAD | Defined, enables padding towards the end of the NX_PACKET control block. The number of ULONG words to pad is defined by  ***NX_PACKET_HEADER_PAD_SIZE***. Note this option is depreciated by ***NX_PACKET_ALIGNMENT***.|
|NX_PACKET_HEADER_PAD_SIZE | Sets the number of ULONG words to be padded to the NX_PACKET structure, allowing the packet payload area to start at the desired alignment. This feature is useful when receive buffer descriptors point directly into NX_PACKET payload area, and the network  interface receive logic or the cache operation logic expects the buffer starting address to meet certain alignment requirements. This value becomes valid only when ***NX_PACKET_HEADER_PAD*** is defined. Note this option is deprecated by ***NX_PACKET_ALIGNMENT***.|
