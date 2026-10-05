---
id: "txmw-chapter-2-installation-and-use-of-udp-configuration-options"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and Use of NetX Duo: Configuration Options / UDP Configuration Options"
summary: "Chapter 2 - Installation and Use of NetX Duo: Configuration Options / UDP Configuration Options"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter2.md#udp-configuration-options"
license: "MIT"
mode: "V"
---

_Part of: Configuration Options_

| Option  | Description  |
|---|---|
|NX_DISABLE_UDP_INFO | Defined, disables UDP information gathering.|
|NX_DISABLE_UDP_RX_CHECKSUM | Defined, disables the UDP checksum computation on incoming UDP packets. This is useful if the network interface driver is able to verify UDP header checksum in hardware, and the application does not enable IPsec or IP fragmentation logic.|
|NX_DISABLE_UDP_TX_CHECKSUM | Defined, disables the UDP checksum computation on outgoing UDP packets. This is useful if the network interface driver is able to compute UDP header checksum and insert the value in the IP head before transmitting the data, and the application does not enable IPsec or IP fragmentation logic.|
