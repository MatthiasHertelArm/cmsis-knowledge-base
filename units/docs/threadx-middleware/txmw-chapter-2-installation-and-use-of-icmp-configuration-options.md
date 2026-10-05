---
id: "txmw-chapter-2-installation-and-use-of-icmp-configuration-options"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and Use of NetX Duo: Configuration Options / ICMP Configuration Options"
summary: "Chapter 2 - Installation and Use of NetX Duo: Configuration Options / ICMP Configuration Options"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter2.md#icmp-configuration-options"
license: "MIT"
mode: "V"
---

_Part of: Configuration Options_

| Option  | Description  |
|---|---|
|NX_DISABLE_ICMP_INFO| Defined, disables ICMP information gathering.|
|NX_DISABLE_ICMP_RX_CHECKSUM| Defined, disables both ICMPv4 and ICMPv6 checksum computation on received ICMP packets. This option is useful when the network interface driver is able to verify the ICMPv4 and ICMPv6 checksum, and the application does not use the IP fragmentation feature or the IPsec feature. By default this option is not defined.|
|NX_DISABLE_ICMP_TX_CHECKSUM | Defined, disables both ICMPv4 and ICMPv6 checksum computation on transmitted ICMP packets. This option is useful where the network interface driver is able to compute the ICMPv4 and ICMPv6 checksum, and the application does not use the IP fragmentation feature or IPsec feature. By default this option is not defined.|
|NX_DISABLE_ICMPV4_ERROR_MESSAGE | Defined, NetX Duo does not send ICMPv4 Error Messages in response to error conditions such as improperly formatted IPv4 header. By default this option is not defined.|
|NX_DISABLE_ICMPV4_RX_CHECKSUM | Defined, disables ICMPv4 checksum computation on received ICMP packets. This option is defined automatically if ***NX_DISABLE_ICMP_RX_CHECKSUM*** is defined. By default this option is not defined.|
|NX_DISABLE_ICMPv4_RX_CHECKSUM | Renamed to ***NX_DISABLE_ICMPV4_RX_CHECKSUM***. Although it is still being supported, new designs are encouraged to use ***NX_DISABLE_ICMPV4_RX_CHECKSUM***.|
|NX_DISABLE_ICMPV4_TX_CHECKSUM | Defined, disables ICMPv4 checksum computation on transmitted ICMP packets. This option is defined automatically if ***NX_DISABLE_ICMP_TX_CHECKSUM*** is defined. By default this option is not defined.|
|NX_DISABLE_ICMPv4_TX_CHECKSUM | Renamed to ***NX_DISABLE_ICMPV4_TX_CHECKSUM***.`</br>`Although it is still being supported, new designs are encouraged to use ***NX_DISABLE_ICMPV4_TX_CHECKSUM***.|
|NX_ENABLE_ICMP_ADDRESS_CHECK | Defined, the destination address of ICMP packet is checked. The default is disabled. An ICMP Echo Request destined to an IP broadcast or IP multicast address will be silently discarded.|
