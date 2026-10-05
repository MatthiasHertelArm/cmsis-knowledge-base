---
id: "txmw-chapter-2-installation-and-use-of-ip-configuration-options"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and Use of NetX Duo: Configuration Options / IP Configuration Options"
summary: "Chapter 2 - Installation and Use of NetX Duo: Configuration Options / IP Configuration Options"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter2.md#ip-configuration-options"
license: "MIT"
mode: "V"
---

_Part of: Configuration Options_

| Option  | Description  |
|---|---|
|NX_DISABLE_FRAGMENTATION | Defined, disables both IPv4 and IPv6 fragmentation and reassembly logic.|
| NX_DISABLE_IPV4     | Defined, disables IPv4 functionality. This option can be used to build NetX Duo to support IPv6 only. By default this option is not defined. |
| NX_DISABLE_IP_INFO | Defined, disables IP information gathering.|
|NX_DISABLE_IP_RX_CHECKSUM | Defined, disables checksum logic on received IPv4 packets. This is useful if the network device is able to verify the IPv4 checksum, and the application does not expect to use IP fragmentation or IPsec.|
|NX_DISABLE_IP_TX_CHECKSUM | Defined, disables checksum logic on IPv4 packets sent. This is useful in situations in which the underlying network device is capable of generating the IPv4 header checksum, and the application does not expect to use IP fragmentation or IPsec.|
|NX_DISABLE_LOOPBACK_INTERFACE | Defined, disables NetX Duo support for the loopback interface.|
|NX_DISABLE_RX_SIZE_CHECKING | Defined, disables the size checking on received packets.|
|NX_ENABLE_IP_RAW_PACKET_FILTER | Defined, enables the IP raw packet receive filter functionality. Applications requiring more control over the type of raw IP packets to be received can use this feature. The IP raw packet filter feature also supports the raw socket operation in the BSD compatibility layer. By default this option is not defined.|
|NX_ENABLE_IP_STATIC_ROUTING | Defined, enables IPv4 static routing in which a destination address can be assigned a specific next hop address. By default IPv4 static routing is disabled.|
|NX_FRAGMENT_IMMEDIATE_ASSEMBLY | Defined, allows IPv4 and IPv6 reassembly logic to execute right away after receiving an IP fragment. By default this option is not defined.|
|NX_IP_MAX_REASSEMBLY_TIME | Symbol that controls maximum time allowed to reassemble IPv4 fragment and IPv6 fragment. Note the value defined here overwrites both ***NX_IPV4_MAX_REASSEMBLY_TIME*** and ***NX_IPV6_MAX_REASSEMBLY_TIME***.|
|NX_IP_PERIODIC_RATE | Defined, specifies the number of ThreadX timer ticks in one second. The default value is derived from the ThreadX symbol ***TX_TIMER_TICKS_PER_SECOND,*** which by default is set to 100 (10ms timer). Applications shall exercise caution when modifying this value, as the rest of the NetX Duo modules derive timing information from ***NX_IP_PERIODIC_RATE*.**|
|NX_IP_RAW_MAX_QUEUE_DEPTH | Symbol that controls the number of raw IP packets can be queued on the raw packet receive queue. By default value is set to 20.| 
|NX_IP_ROUTING_TABLE_SIZE | Defined, sets the maximum number of entries in the IPv4 static routing table, which is a list of an outgoing interface and the next hop addresses for a given destination address. The default value is 8 and is defined in ***nx_api.h.*** This symbol is used only if ***NX_ENABLE_IP_STATIC_ROUTING*** is defined.|
|NX_IPV4_MAX_REASSEMBLY_TIME | Symbol that controls maximum time allowed to reassemble IPv4 fragment. Note the value defined in NX_IP_MAX_REASSEMBLY_TIME overwrites this value.|
|NX_ENABLE_TCPIP_OFFLOAD | Symbol that enables TCP/IP offload feature. Note NX_ENABLE_INTERFACE_CAPABILITY must be defined to enable this feature.|
