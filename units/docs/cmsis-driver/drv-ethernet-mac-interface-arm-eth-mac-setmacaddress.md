---
id: "drv-ethernet-mac-interface-arm-eth-mac-setmacaddress"
type: "concept"
domain: "drivers"
title: "Ethernet MAC Interface: ARM_ETH_MAC_SetMacAddress"
summary: "The function ARMETHMACSetMacAddress configures Ethernet MAC own address. The Ethernet MAC accepts packets Ethernet frames which contains a MAC destination address that matches the address specified with ptraddr."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_ETH_MAC_SetMacAddress (const ARM_ETH_MAC_ADDR *ptr_addr)
```


The function **ARM_ETH_MAC_SetMacAddress** configures Ethernet MAC own address.
The Ethernet MAC accepts packets **Ethernet frames** which contains a MAC destination address that matches the address specified with **ptr_addr.**

The Ethernet MAC receiver will accept also packets with addresses configured by ARM_ETH_MAC_SetAddressFilter function.

MAC receiver can be configured to accept also packets with broadcast address, any multicast address or even all packets regardless of address (Promiscuity Mode). 
This is configured by function ARM_ETH_MAC_Control with ARM_ETH_MAC_CONFIGURE as control parameter.
******************************************************************************************************************
