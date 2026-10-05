---
id: "txmw-chapter-3-functional-components-of-ipv6-default-routers"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: IPv6 in NetX Duo / IPv6 Default Routers"
summary: "IPv6 uses a default router to forward packets to offlink destinations. The NetX Duo service nxd_ipv6_default_router_addenables an application to add an IPv6 router to the default router table."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#ipv6-default-routers"
license: "MIT"
mode: "V"
---

_Part of: IPv6 in NetX Duo_

IPv6 uses a default router to forward packets to offlink destinations. The NetX Duo service ***nxd_ipv6_default_router_add***enables an application to add an IPv6 router to the default router table. See Chapter 4 "Description of Services" for more default router services offered by NetX Duo.  

When forwarding IPv6 packets, NetX Duo first checks if the packet destination is on-link. If not, NetX Duo checks the default routing table for a valid router to forward the off-link packet to.  

To remove a router from the IPv6 default router table, application shall use the service ***nxd_ipv6_default_router_delete***. To obtain entries of the IPv6 default router table, use the service ***nxd_ipv6_default_router_entry_get***.
