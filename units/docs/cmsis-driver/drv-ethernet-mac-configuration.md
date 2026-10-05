---
id: "drv-ethernet-mac-configuration"
type: "concept"
domain: "drivers"
title: "Ethernet MAC Configuration"
summary: "Specifies speed mode, link mode, checksum, and frame filtering modes."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
license: "Apache-2.0"
mode: "V"
---

Specifies speed mode, link mode, checksum, and frame filtering modes.

The function ARM_ETH_MAC_Control with **control** = ARM_ETH_MAC_CONFIGURE configures the Ethernet MAC interface
as specified with **arg** listed bellow.


### ARM_ETH_MAC_SPEED_10M

```c
ARM_ETH_MAC_SPEED_10M
```


### ARM_ETH_MAC_SPEED_100M

```c
ARM_ETH_MAC_SPEED_100M
```


### ARM_ETH_MAC_SPEED_1G

```c
ARM_ETH_MAC_SPEED_1G
```


### ARM_ETH_MAC_DUPLEX_HALF

```c
ARM_ETH_MAC_DUPLEX_HALF
```


### ARM_ETH_MAC_DUPLEX_FULL

```c
ARM_ETH_MAC_DUPLEX_FULL
```


### ARM_ETH_MAC_LOOPBACK

```c
ARM_ETH_MAC_LOOPBACK
```


### ARM_ETH_MAC_CHECKSUM_OFFLOAD_RX

```c
ARM_ETH_MAC_CHECKSUM_OFFLOAD_RX
```


### ARM_ETH_MAC_CHECKSUM_OFFLOAD_TX

```c
ARM_ETH_MAC_CHECKSUM_OFFLOAD_TX
```


### ARM_ETH_MAC_ADDRESS_BROADCAST

```c
ARM_ETH_MAC_ADDRESS_BROADCAST
```


### ARM_ETH_MAC_ADDRESS_MULTICAST

```c
ARM_ETH_MAC_ADDRESS_MULTICAST
```


### ARM_ETH_MAC_ADDRESS_ALL

```c
ARM_ETH_MAC_ADDRESS_ALL
```
