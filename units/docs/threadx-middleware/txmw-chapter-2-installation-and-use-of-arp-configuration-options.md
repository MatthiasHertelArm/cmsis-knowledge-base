---
id: "txmw-chapter-2-installation-and-use-of-arp-configuration-options"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and Use of NetX Duo: Configuration Options / ARP Configuration Options"
summary: "Chapter 2 - Installation and Use of NetX Duo: Configuration Options / ARP Configuration Options"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter2.md#arp-configuration-options"
license: "MIT"
mode: "V"
---

_Part of: Configuration Options_

| Option  | Description  |
|---|---|
|NX_ARP_DEFEND_BY_REPLY | Defined, allows NetX Duo to defend its IP address by sending an ARP response.|
|NX_ARP_DEFEND_INTERVAL| Defines the interval, in seconds, the ARP module sends out the next defend packet in response to an incoming ARP message that indicates an address in conflict.|
|NX_ARP_DISABLE_AUTO_ARP_ENTRY|  Renamed to ***NX_DISABLE_ARP_AUTO_ENTRY***. Although it is still being supported, new designs are encouraged to use ***NX_DISABLE_ARP_AUTO_ENTRY***.|
|NX_ARP_EXPIRATION_RATE| Specifies the number of seconds ARP entries remain valid. The default value of zero disables expiration or aging of ARP entries and is defined in ***nx_api.h***. The application can override the default by defining the value before ***nx_api.h*** is included.|
|NX_ARP_MAC_CHANGE_NOTIFICATION_ENABLE | Renamed to ***NX_ENABLE_ARP_MAC_CHANGE_NOTIFICATION***. Although it is still being supported, new designs are encouraged to use ***NX_ENABLE_ARP_MAC_CHANGE_NOTIFICATION***.|
|NX_ARP_MAX_QUEUE_DEPTH | Specifies the maximum number of packets that can be queued while waiting for an ARP response. The default value is 4 and is defined in ***nx_api.h***.|
|NX_ARP_MAXIMUM_RETRIES | Specifies the maximum number of ARP retries made without an ARP response. The default value is 18 and is defined in ***nx_api.h***. The application can override the default by defining the value before ***nx_api.h*** is included.|
|NX_ARP_UPDATE_RATE | Specifies the number of seconds between ARP retries. The default value is 10, which represents 10 seconds, and is defined in ***nx_api.h***. The application can override the default by defining the value before ***nx_api.h*** is included.|
|NX_DISABLE_ARP_AUTO_ENTRY | Defined, disables entering ARP request information in the ARP cache.|
|NX_DISABLE_ARP_INFO | Defined, disables ARP information gathering.|
|NX_ENABLE_ARP_MAC_CHANGE_NOTIFICATION| Defined, allows ARP to invoke a callback notify function on detecting the MAC address is updated.|
