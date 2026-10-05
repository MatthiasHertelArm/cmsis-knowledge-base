---
id: "txmw-chapter-2-installation-and-use-of-igmp-configuration-options"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and Use of NetX Duo: Configuration Options / IGMP Configuration Options"
summary: "Chapter 2 - Installation and Use of NetX Duo: Configuration Options / IGMP Configuration Options"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter2.md#igmp-configuration-options"
license: "MIT"
mode: "V"
---

_Part of: Configuration Options_

| Option  | Description  |
|---|---|
|NX_DISABLE_IGMP_INFO | Defined, disables IGMP information gathering.|
|NX_DISABLE_IGMPV2 | Defined, disables IGMPv2 support, and NetX Duo supports IGMPv1 only. By default this option is not set and is defined in ***nx_api.h***.|
|NX_MAX_MULTICAST_GROUPS | Specifies the maximum number of multicast groups that can be joined. The default value is 7 and is defined in ***nx_api.h***. The application can override the default by defining the value before ***nx_api.h*** is included.|
