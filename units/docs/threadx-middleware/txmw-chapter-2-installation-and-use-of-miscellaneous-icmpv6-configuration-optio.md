---
id: "txmw-chapter-2-installation-and-use-of-miscellaneous-icmpv6-configuration-optio"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and Use of NetX Duo: Configuration Options / Miscellaneous ICMPv6 Configuration Options"
summary: "Chapter 2 - Installation and Use of NetX Duo: Configuration Options / Miscellaneous ICMPv6 Configuration Options"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter2.md#miscellaneous-icmpv6-configuration-options"
license: "MIT"
mode: "V"
---

_Part of: Configuration Options_

| Option  | Description  |
|---|---|
|NX_DISABLE_ICMPV6_ERROR_MESSAGE | Defined, disables NetX Duo from sending an ICMPv6 error message in response to a problem packet (e.g., improperly formatted header or packet header type is deprecated) received from another host.|
|NX_DISABLE_ICMPV6_REDIRECT_PROCESS | Defined, disables ICMPv6 redirect packet processing. NetX Duo by default processes redirect messages and updates the destination table with next hop IP address information.|
|NX_DISABLE_ICMPV6_ROUTER_ADVERTISEMENT_PROCESS | Defined, disables NetX Duo from processing information received in IPv6 router advertisement packets.|
|NX_DISABLE_ICMPV6_ROUTER_SOLICITATION | Defined, disables NetX Duo from sending IPv6 router solicitation messages at regular intervals to the router.|
|NX_DISABLE_ICMPV6_RX_CHECKSUM | Defined, disables ICMPv6 checksum computation on received ICMP packets.|
|NX_DISABLE_ICMPv6_RX_CHECKSUM | Renamed to ***NX_DISABLE_ICMPV6_RX_CHECKSUM***. Although it is still being supported, new designs are encouraged to use ***NX_DISABLE_CMPV6_RX_CHECKSUM***.|
|NX_DISABLE_ICMPV6_TX_CHECKSUM | Defined, disables and ICMPv6 checksum computation on transmitted ICMP packets.|
|NX_DISABLE_ICMPV6_TX_CHECKSUM | Renamed to ***NX_DISABLE_ICMPV6_TX_CHECKSUM***. Although it is still being supported, new designs are encouraged to use ***NX_DISABLE_ICMPV6_TX_CHECKSUM***.|
|NX_ICMPV6_MAX_RTR_SOLICITATIONS | Define the max number of router solicitations a host sends until a router response is received. If no response is received, the host concludes no router is present. The default value is 3.|
|NX_ICMPV6_RTR_SOLICITATION_DELAY | Specifies the maximum delay for the initial router solicitation in seconds.|
|NX_ICMPV6_RTR_SOLICITATION_INTERVAL | Specifies the interval between two router solicitation messages. The default value is 4.|
|NXDUO_DESTINATION_TABLE_SIZE | Renamed to ***NX_IPV6_DESTINATION_TABLE_SIZE***. Although it is still being supported, new designs are encouraged to use ***NX_IPV6_DESTINATION_TABLE_SIZE***.|
|NXDUO_DISABLE_ICMPV6_ERROR_MESSAGE | Renamed to ***NX_DISABLE_ICMPV6_ERROR_MESSAGE***. Although it is still being supported, new designs are encouraged to use ***NX_DISABLE_ICMPV6_ERROR_MESSAGE***.|
|NXDUO_DISABLE_ICMPV6_REDIRECT_PROCESS | Renamed to ***NX_DISABLE_ICMPV6_REDIRECT_PROCESS***. Although it is still being supported, new designs are encouraged to use ***NX_DISABLE_ICMPV6_REDIRECT_PROCESS***|  
|NXDUO_DISABLE_ICMPV6_ROUTER_ADVERTISEMENT_PROCESS| Renamed to ***NX_DISABLE_ICMPV6_ROUTER_ADVERTISEMENT_PROCESS***. Although it is still being supported, new designs are encouraged to use ***NX_DISABLE_ICMPV6_ROUTER_ADVERTISEMENT_PROCESS***.|
|NXDUO_DISABLE_ICMPV6_ROUTER_SOLICITATION | Renamed to ***NX_DISABLE_ICMPV6_ROUTER_SOLICITATION***. Although it is still being supported, new designs are encouraged to use ***NX_DISABLE_ICMPV6_ROUTER_SOLICITATION***.|
|NXDUO_ICMPV6_MAX_RTR_SOLICITATIONS | Renamed to ***NX_ICMPV6_MAX_RTR_SOLICITATIONS***. Although it is still being supported, new designs are encouraged to use ***NX_ICMPV6_MAX_RTR_SOLICITATIONS***.|
|NXDUO_ICMPV6_RTR_SOLICITATION_INTERVAL | Renamed to ***NX_ICMPV6_RTR_SOLICITATION_INTERVAL***. This symbol is being depreciated. Although it is still being supported, new designs are encouraged to use ***NX_ICMPV6_RTR_SOLICITATION_INTERVAL***|
