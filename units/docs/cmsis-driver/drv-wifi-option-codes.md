---
id: "drv-wifi-option-codes"
type: "concept"
domain: "drivers"
title: "WiFi Option Codes"
summary: "WiFi Option Codes for ARM_WIFI_SetOption or ARM_WIFI_GetOption function."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

WiFi Option Codes for ARM_WIFI_SetOption or ARM_WIFI_GetOption function.
 
Many parameters of the WiFi module are configured using the ARM_WIFI_SetOption or ARM_WIFI_GetOption function.

### ARM_WIFI_BSSID

```c
ARM_WIFI_BSSID
```

 Specifies the BSSID of the access point to connect or the access point itself.
\sa WiFi_option

### ARM_WIFI_TX_POWER

```c
ARM_WIFI_TX_POWER
```

 Specifies the transmit power in dBm.
\sa WiFi_option

### ARM_WIFI_LP_TIMER

```c
ARM_WIFI_LP_TIMER
```

 Specifies the low-power deep-sleep time in seconds for station (disabled when 0 - default).
\sa WiFi_option

### ARM_WIFI_DTIM

```c
ARM_WIFI_DTIM
```

 Specifies the DTIM interval in number of beacons.
\sa WiFi_option

### ARM_WIFI_BEACON

```c
ARM_WIFI_BEACON
```

 Specifies the beacon interval in milliseconds for access point.
\sa WiFi_option

### ARM_WIFI_MAC

```c
ARM_WIFI_MAC
```

 Specifies the MAC address.
\sa WiFi_option

### ARM_WIFI_IP

```c
ARM_WIFI_IP
```

 Specifies the IP address.
\sa WiFi_option

### ARM_WIFI_IP_SUBNET_MASK

```c
ARM_WIFI_IP_SUBNET_MASK
```

 Specifies the subnet mask.
\sa WiFi_option

### ARM_WIFI_IP_GATEWAY

```c
ARM_WIFI_IP_GATEWAY
```

 Specifies the gateway IP address.
\sa WiFi_option

### ARM_WIFI_IP_DNS1

```c
ARM_WIFI_IP_DNS1
```

 Specifies the IP address of the primary DNS server.
\sa WiFi_option

### ARM_WIFI_IP_DNS2

```c
ARM_WIFI_IP_DNS2
```

 Specifies the IP address of the secondary DNS server.
\sa WiFi_option

### ARM_WIFI_IP_DHCP

```c
ARM_WIFI_IP_DHCP
```

 Enables or disables the DHCP client for station or DHCP server for access point.
\sa WiFi_option

### ARM_WIFI_IP_DHCP_POOL_BEGIN

```c
ARM_WIFI_IP_DHCP_POOL_BEGIN
```

 Specifies the start IP address for DHCP server (access point).
\sa WiFi_option

### ARM_WIFI_IP_DHCP_POOL_END

```c
ARM_WIFI_IP_DHCP_POOL_END
```

 Specifies the end IP address for DHCP server (access point).
\sa WiFi_option

### ARM_WIFI_IP_DHCP_LEASE_TIME

```c
ARM_WIFI_IP_DHCP_LEASE_TIME
```

 Specifies the lease time for DHCP server (access point).
\sa WiFi_option

### ARM_WIFI_IP6_GLOBAL

```c
ARM_WIFI_IP6_GLOBAL
```

 Specifies the global IPv6 address.
\sa WiFi_option

### ARM_WIFI_IP6_LINK_LOCAL

```c
ARM_WIFI_IP6_LINK_LOCAL
```

 Specifies the link-local IPv6 address.
\sa WiFi_option

### ARM_WIFI_IP6_SUBNET_PREFIX_LEN

```c
ARM_WIFI_IP6_SUBNET_PREFIX_LEN
```

 Specifies the address prefix length.
\sa WiFi_option

### ARM_WIFI_IP6_GATEWAY

```c
ARM_WIFI_IP6_GATEWAY
```

 Specifies the gateway IPv6 address.
\sa WiFi_option

### ARM_WIFI_IP6_DNS1

```c
ARM_WIFI_IP6_DNS1
```

 Specifies the IPv6 address of the primary DNS server.
\sa WiFi_option

### ARM_WIFI_IP6_DNS2

```c
ARM_WIFI_IP6_DNS2
```

 Specifies the IPv6 address of the secondary DNS server.
\sa WiFi_option

### ARM_WIFI_IP6_DHCP_MODE

```c
ARM_WIFI_IP6_DHCP_MODE
```

 Specifies the operation mode of the DHCPv6 client.
\sa WiFi_option
