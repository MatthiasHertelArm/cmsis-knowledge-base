---
id: "txmw-chapter-3-functional-components-of-enabling-ipv6-in-netx-duo"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: IPv6 in NetX Duo / Enabling IPv6 in NetX Duo"
summary: "By default IPv6 is enabled in NetX Duo. IPv6 services are enabled in NetX Duo if the configurable option NX_DISABLE_IPV6 in nx_user.h is not defined."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#enabling-ipv6-in-netx-duo"
license: "MIT"
mode: "V"
---

_Part of: IPv6 in NetX Duo_

By default IPv6 is enabled in NetX Duo. IPv6 services are enabled in NetX Duo if the configurable option ***NX_DISABLE_IPV6*** in *nx_user.h* is not defined. If ***NX_DISABLE_IPV6*** is defined, NetX Duo will only offer IPv4 services, and all the IPv6-related modules and services are not built into NetX Duo library.

The following service is provided for applications to configure the device IPv6 address: ***nxd_ipv6_address_set***

In addition to manually setting the device's IPv6 addresses, the system may also use Stateless Address Autoconfiguration. To use this option, the application must call ***nxd_ipv6_enable*** to start IPv6 services on the device. In addition, ICMPv6 services must be started by calling ***nxd_icmp_enable***, which enables NetX Duo to perform services such as Router Solicitation, Neighbor Discovery, and Duplicate Address Detection. Note that ***nx_icmp_enable*** only starts ICMP for IPv4 services. ***nxd_icmp_enable*** starts ICMP services for both IPv4 and IPv6. If the system does not need ICMPv6 services, then ***nx_icmp_enable*** can be used so the ICMPv6 module is not linked into the system.

The following example shows a typical NetX Duo IPv6 initialization procedure.

```c
/* Assume ip_0 has been created and IPv4 services (such as ARP,
   ICMP, have been enabled. */
#define SECONDARY_INTERFACE 1

/* Enable IPv6 */
status = nxd_ipv6_enable(&ip_0);

if(status != NX_SUCCESS)
{
    /* nxd_ipv6_enable failed. */
}

/* Enable ICMPv6 */
status = nxd_icmp_enable(&ip_0);
if(status != NX_SUCCESS)
{
    /* nxd_icmp_enable failed. */
}

/* Configure the link local address on the primary interface. */
status = nxd_ipv6_address_set(&ip_0, 0, NX_NULL, 10, NX_NULL);

/* Configure ip_0 primary interface global address. */
ip_address.nxd_ip_version = NX_IP_VERSION_V6
ip_address.nxd_ip_address.v6[0] = 0x20010db8;
ip_address.nxd_ip_address.v6[1] = 0x0000f101;
ip_address.nxd_ip_address.v6[2] = 0;
ip_address.nxd_ip_address.v6[3] = 0x202;

/* Configure global address of the primary interface. */
status = nxd_ipv6_address_set(&ip_0, SECONDARY_INTERFACE,
                              &ip_address, 64, NX_NULL);
```                              

Upper layer protocols (such as TCP and UDP) can be enabled either before or after IPv6 starts.

> **Important:** *IPv6 services are available only after IP thread is initialized and the device is enabled.*

After the interface is enabled (i.e.,the interface device driver is ready to send and receive data, and a valid link local address has been obtained), the device may obtain global IPv6 addresses by one of
the these methods:

- Stateless Address Auto Configuration;  
- Manual IPv6 address configuration;  
- Address configuration via DHCPv6 (with optional DHCPv6 package)

The first two methods are described below. The 3rd method (DHCPv6) is described in the DHCP package.
