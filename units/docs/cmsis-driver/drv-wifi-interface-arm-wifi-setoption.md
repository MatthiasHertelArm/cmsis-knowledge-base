---
id: "drv-wifi-interface-arm-wifi-setoption"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_SetOption"
summary: "The function ARMWIFISetOption sets the value of the specified option of the WiFi module."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_WIFI_SetOption (uint32_t interface, uint32_t option, const void *data, uint32_t len)
```


The function **ARM_WIFI_SetOption** sets the value of the specified option of the WiFi module.

The argument **interface** specifies the interface (0 = Station, 1 = Access Point).

The argument **option** specifies the option that is to be set (see below).

The argument **data** points to a buffer containing the value of the option to be set
and must be aligned to the data type of the corresponding option.

The argument **len** specifies the length of the buffer **data** and must be equal (or higher)
to the length of the corresponding option.
 
Option                                 | Description                            | Data          | Type/Length
:--------------------------------------|:---------------------------------------|:--------------|:-----------
ARM_WIFI_BSSID                    | BSSID of AP to connect or AP           | bssid         | uint8_t[6]
ARM_WIFI_TX_POWER                 | Transmit power                         | power[dbm]    | uint32_t
ARM_WIFI_LP_TIMER                 | Low-power deep-sleep time              | time[seconds] | uint32_t
ARM_WIFI_DTIM                     | DTIM interval                          | dtim[beacons] | uint32_t
ARM_WIFI_BEACON                   | Beacon interval                        | interval[ms]  | uint32_t
ARM_WIFI_MAC                      | MAC address                            | mac           | uint8_t[6]
ARM_WIFI_IP                       | IPv4 address                           | ip            | uint8_t[4]
ARM_WIFI_IP_SUBNET_MASK           | IPv4 subnet mask                       | mask          | uint8_t[4]
ARM_WIFI_IP_GATEWAY               | IPv4 gateway address                   | ip            | uint8_t[4]
ARM_WIFI_IP_DNS1                  | IPv4 primary DNS server address        | ip            | uint8_t[4]
ARM_WIFI_IP_DNS2                  | IPv4 secondary DNS server address      | ip            | uint8_t[4]
ARM_WIFI_IP_DHCP                  | IPv4 DHCP client/server enable/disable | dhcp (0, 1)   | uint32_t
ARM_WIFI_IP_DHCP_POOL_BEGIN       | IPv4 DHCP server begin address         | ip            | uint8_t[4]
ARM_WIFI_IP_DHCP_POOL_END         | IPv4 DHCP server end address           | ip            | uint8_t[4]
ARM_WIFI_IP_DHCP_LEASE_TIME       | IPv4 DHCP server lease time            | time[seconds] | uint32_t
ARM_WIFI_IP6_GLOBAL               | IPv6 global address                    | ip6           | uint8_t[16]
ARM_WIFI_IP6_LINK_LOCAL           | IPv6 link-local address                | ip6           | uint8_t[16]
ARM_WIFI_IP6_SUBNET_PREFIX_LEN    | IPv6 subnet prefix length              | len (1..127)  | uint32_t
ARM_WIFI_IP6_GATEWAY              | IPv6 gateway address                   | ip6           | uint8_t[16]
ARM_WIFI_IP6_DNS1                 | IPv6 primary DNS server address        | ip6           | uint8_t[16]
ARM_WIFI_IP6_DNS2                 | IPv6 secondary DNS server address      | ip6           | uint8_t[16]
ARM_WIFI_IP6_DHCP_MODE            | IPv6 DHCP client mode                  | mode          | uint32_t

**Example:**
```
uint8_t ip[4];
 
ip[0] = 192U;
ip[1] = 168U;
ip[2] = 0U;
ip[3] = 1U;
 
// Set IP static address of the Station
wifi->SetOption (0U, ARM_WIFI_IP, &ip, sizeof(ip));
```
