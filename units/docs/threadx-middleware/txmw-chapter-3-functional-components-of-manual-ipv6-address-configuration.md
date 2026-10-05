---
id: "txmw-chapter-3-functional-components-of-manual-ipv6-address-configuration"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: IPv6 in NetX Duo / Manual IPv6 Address Configuration"
summary: "If a specific IPv6 address is needed, the application may use nxd_ipv6_address_set to manually configure an IPv6 address. A network interface may have multiple IPv6 addresses."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#manual-ipv6-address-configuration"
license: "MIT"
mode: "V"
---

_Part of: IPv6 in NetX Duo_

If a specific IPv6 address is needed, the application may use ***nxd_ipv6_address_set*** to manually configure an IPv6 address. A network interface may have multiple IPv6 addresses. However keep in mind that the total number of IPv6 addresses in a system, either obtained through Stateless Address 
Autoconfiguration, or through the Manual Configuration, cannot exceed ***NX_MAX_IPV6_ADDRESSES***.

The following example illustrates how to manually configure a global address on the primary interface (device 0) in ip_0:

```c
NXD_ADDRESS global_address;
global_address.nxd_ip_version = NX_IP_VERSION_V6;
global_address.nxd_ip_address.v6[0] = 0x20010000;
global_address.nxd_ip_address.v6[1] = 0x00000000;
global_address.nxd_ip_address.v6[2] = 0x00000000;
global_address.nxd_ip_address.v6[3] = 0x0000ABCD;
```

The host then calls the following NetX Duo service to assign this address as its global IP address:

```c
status = nxd_ipv6_address_set(&ip_0, 0,  
                              &global_address, 64
                              NX_NULL);
```
