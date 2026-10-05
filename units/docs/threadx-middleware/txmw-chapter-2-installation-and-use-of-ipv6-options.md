---
id: "txmw-chapter-2-installation-and-use-of-ipv6-options"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and Use of NetX Duo: Configuration Options / IPv6 Options"
summary: "Chapter 2 - Installation and Use of NetX Duo: Configuration Options / IPv6 Options"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter2.md#ipv6-options"
license: "MIT"
mode: "V"
---

_Part of: Configuration Options_

| Option  | Description  |
|---|---|
| NX_DISABLE_IPV6 | Disables IPv6 functionality when the NetX Duo library is built. For applications that do not need IPv6, this avoids pulling in code and additional storage space needed to support IPv6.|
|NX_DISABLE_IPV6_PATH_MTU_DISCOVERY | Defined, disables path MTU discovery, which is used to determine the maximum MTU in the path to a target in the NetX Duo host destination table. This enables the NetX Duo host to send the largest possible packet that will not require fragmentation. By default, this option is defined (path MTU is disabled).|
|NX_ENABLE_IPV6_ADDRESS_CHANGE_NOTIFY | Defined, allows a callback function to be invoked when the IPv6 address is changed. By default this option is not enabled.|
|NX_ENABLE_IPV6_MULTICAST | Defined, enables IPv6 multicast join/leave function. By default this option is not enabled.|
|NX_ENABLE_IPV6_PATH_MTU_DISCOVERY | Defined, enables the IPv6 path MTU discovery feature. By default this option is not enabled.|
|NX_IPV6_ADDRESS_CHANGE_NOTIFY_ENABLE | Renamed to ***NX_ENABLE_IPV6_ADDRESS_CHANGE_NOTIFY***. Although it is still being supported, new designs are encouraged to use ***NX_ENABLE_IPV6_ADDRESS_CHANGE_NOTIFY***.|
|NX_IPV6_DEFAULT_ROUTER_TABLE_SIZE | Specifies the number of entries in the IPv6 routing table. At least onS entry is needed for the default router. Defined in ***nx_api.h***, the default value is 8.|
|NX_IPV6_DESTINATION_TABLE_SIZE | Specifies the number of entries in the IPv6 destination table. This stores information about next hop addresses for IPv6 addresses. Defined in ***nx_api.h***, the default value is 8.|
|NX_IPV6_MAX_REASSEMBLY_TIME | Symbol that controls the maximum time allowed to reassemble IPv6 fragment.|
|NX_IPV6_MULTICAST_ENABLE | Renamed to ***NX_ENABLE_IPV6_MULTICAST***. Although it is still being supported, new designs are encouraged to use ***NX_ENABLE_IPV6_MULTICAST***.|
|NX_IPV6_PREFIX_LIST_TABLE_SIZE | Specifies the size of the prefix table. Prefix information is obtained from router advertisements and is part of the IPv6 address configuration. Defined in ***nx_api.h***, the default value is 8.|
|NX_IPV6_STATELESS_AUTOCONFIG_CONTROL | Defined, allows NetX Duo to disable stateless address autoconfiguration feature. By default this option is not enabled.|
|NX_MAX_IPV6_ADDRESSES | Specifies the number of entries in the IPv6 address pool. During interface configuration, NetX Duo uses IPv6 entries from the pool. It is defaulted to (NX_MAX_PHYSICAL_INTERFACES \* 3) to allow each interface to have at least one link local address and two global addresses. Note that all interfaces share the IPv6 address pool.|
|NX_PATH_MTU_INCREASE_WAIT_INTERVAL | Specifies the wait interval in timer ticks to reset the path MTU for a specific target in the destination table. If ***NX_DISABLE_IPV6_PATH_MTU_DISCOVERY*** is defined, defining this symbol has no effect.|
|NX_PATH_MTU_INCREASE_WAIT_INTERVAL | Symbol that specifies the wait interval (in seconds) to reset the path MTU value for a destination table entry. It is valid only if ***NX_ENABLE_IPV6_PATH_MTU_DISCOVERY*** is defined. By default this value is set to 600 (seconds).|
