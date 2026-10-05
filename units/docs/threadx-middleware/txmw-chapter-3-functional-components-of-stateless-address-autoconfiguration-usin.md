---
id: "txmw-chapter-3-functional-components-of-stateless-address-autoconfiguration-usin"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: IPv6 in NetX Duo / Stateless Address Autoconfiguration Using Router Solicitation"
summary: "NetX Duo devices can configure their interfaces automatically when connected to an IPv6 network with a router that supplies prefix information. Devices that require Stateless Address Autoconfiguration send out router solicitation (RS) messages."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#stateless-address-autoconfiguration-using-router-solicitation"
license: "MIT"
mode: "V"
---

_Part of: IPv6 in NetX Duo_

NetX Duo devices can configure their interfaces automatically when connected to an IPv6 network with a router that supplies prefix information. Devices that require Stateless Address Autoconfiguration send out router solicitation (RS) messages. Routers on the network respond with solicited router advertisement (RA) messages. RA messages advertise prefixes that identify the network addresses associated with a link. Devices then generate a unique identifier for the network the device is attached to. The address is formed by combining the prefix and its unique identifier. In this manner on receiving the RA messages, hosts generate their IP address. Routers may also send periodic unsolicited RA messages. 

> **Warning:** *NetX Duo allows an application to enable or disable Stateless Address Autoconfiguration at run time. To enable this feature, NetX Duo library must be compiled with **NX_IPV6_STATELESS_AUTOCONFIG_CONTROL** defined. Once this feature is enabled, applications may use **nxd_ipv6_stateless_address_autoconfigure_enable** and **nxd_ipv6_stateless_address_autoconfigure_disable** to enable or disable IPv6 stateless address autoconfiguration*.
