---
id: "txmw-chapter-2-installation-and-use-of-neighbor-cache-configuration-options"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and Use of NetX Duo: Configuration Options / Neighbor Cache Configuration Options"
summary: "Chapter 2 - Installation and Use of NetX Duo: Configuration Options / Neighbor Cache Configuration Options"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter2.md#neighbor-cache-configuration-options"
license: "MIT"
mode: "V"
---

_Part of: Configuration Options_

| Option  | Description  |
|---|---|
|NX_DELAY_FIRST_PROBE_TIME | Specifies the delay in seconds before the first solicitation is sent out for a cache entry in the STALE state. Defined in ***nx_nd_cache.h***, the default value is 5.|
|NX_DISABLE_IPV6_DAD | Defined, this option disables Duplicate Address Detection (DAD) during IPv6 address assignment. Addresses are set either by manual configuration or through Stateless Address Auto Configuration.|
|NX_DISABLE_IPV6_PURGE_UNUSED_CACHE_ENTRIES | Defined, this option prevents NetX Duo from removing older cache table entries before their timeout expires to make room for new entries when the table is full. Static and router entries are never purged.|
|NX_IPV6_DAD_TRANSMITS | Specifies the number of Neighbor Solicitation messages to be sent before NetX Duo marks an interface address as valid. If ***NX_DISABLE_IPV6_DAD*** is defined (DAD disabled), setting this option has no effect. Alternatively, a value of zero (0) turns off DAD but leaves the DAD functionality in NetX Duo. Defined in ***nx_api.h***, the default value is 3.|
|NX_IPV6_DISABLE_PURGE_UNUSED_CACHE_ENTRIES | Renamed to ***NX_DISABLE_IPV6_PURGE_UNUSED_CACHE_ENTRIES***. Although it is still being supported, new designs are encouraged to use ***NX_DISABLE_IPV6_PURGE_UNUSED_CACHE_ENTRIES***.|
|NX_IPV6_NEIGHBOR_CACHE_SIZE | Specifies the number of entries in the IPv6 Neighbor Cache table. Defined in ***nx_nd_cache.h***, the default value is 16.|
|NX_MAX_MULTICAST_SOLICIT | Specifies the number of Neighbor Solicitation messages NetX Duo transmits as part of the IPv6 Neighbor Discovery protocol when mapping between IPv6 address and MAC address is required. Defined in ***nx_nd_cache.h***, the default value is 3.|
|NX_MAX_UNICAST_SOLICIT | Specifies the number of Neighbor Solicitation messages NetX Duo transmits to determine a specific neighbor's reachability. Defined in ***nx_nd_cache.h***, the default value is 3.|
|NX_ND_MAX_QUEUE_DEPTH | Symbol that defines the maximum number of packets queued up for ND cache to be resolved. By default this symbol is set to 4.|
|NX_REACHABLE_TIME | Specifies the time out in seconds for a cache entry to exist in the REACHABLE state with no packets received from the cache destination IPv6 address. Defined in ***nx_nd_cache.h***, the default value is 30.|
|NX_RETRANS_TIMER  | Specifies in milliseconds the length of delay between solicitation packets sent by NetX Duo. Defined in ***nx_nd_cache.h***, the default value is 1000.|
| NXDUO_DISABLE_DAD | Renamed to ***NX_DISABLE_IPV6_DAD***. Although it is still being supported, new designs are encouraged to use ***NX_DISABLE_IPV6_DAD***.|
|NXDUO_DUP_ADDR_DETECT_TRANSMITS | Renamed to ***NX_IPV6_DAD_TRANSMITS***. Although it is still being supported, new designs are encouraged to use ***NX_IPV6_DAD_TRANSMITS***.|
