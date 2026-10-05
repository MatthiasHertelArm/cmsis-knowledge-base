---
id: "drv-wifi-dhcpv6-mode"
type: "concept"
domain: "drivers"
title: "WiFi DHCPv6 Mode"
summary: "Specifies IPv6 Dynamic Host Configuration Protocol (DHCP) Mode."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

Specifies IPv6 Dynamic Host Configuration Protocol (DHCP) Mode.

The WiFi DHCPv6 mode defines the DHCP mode in IPv6.

### ARM_WIFI_IP6_DHCP_OFF

```c
ARM_WIFI_IP6_DHCP_OFF
```


In the static host configuration mode, the IPv6 address, the default gateway address,
and the addresses of DNS servers are statically configured from the preset values.
\sa wifi_dhcp_v6_mode

### ARM_WIFI_IP6_DHCP_STATELESS

```c
ARM_WIFI_IP6_DHCP_STATELESS
```


In the stateless DHCP configuration mode, the client obtains only extended information
from a DHCPv6 server, such as DNS server addresses. Stateless auto-configuration of
IPv6 allows the client device to self configure it's IPv6 addresses and routing based
on the router advertisements.
\sa wifi_dhcp_v6_mode

### ARM_WIFI_IP6_DHCP_STATEFULL

```c
ARM_WIFI_IP6_DHCP_STATEFULL
```


In the stateful DHCP configuration mode, the client connects to a DHCPv6 server for
a leased IPv6 address and DNS server addresses.
\sa wifi_dhcp_v6_mode
