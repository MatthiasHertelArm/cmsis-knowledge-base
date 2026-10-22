---
id: "drv-ethernet-mac-interface-arm-eth-mac-setaddressfilter"
type: "concept"
domain: "drivers"
title: "Ethernet MAC Interface: ARM_ETH_MAC_SetAddressFilter"
summary: "The function ARM_ETH_MAC_SetAddressFilter configures Ethernet MAC receiver address filtering. The Ethernet MAC accepts packets Ethernet frames which contains a MAC destination address of the list supplied with ptr_addr. The parameter ptr_addr provides and array of Ethernet MAC addresses."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_ETH_MAC_SetAddressFilter (const ARM_ETH_MAC_ADDR *ptr_addr, uint32_t num_addr)
```


The function **ARM_ETH_MAC_SetAddressFilter** configures Ethernet MAC receiver address filtering.
The Ethernet MAC accepts packets **Ethernet frames** which contains a MAC destination address of the list supplied with **ptr_addr.**  The parameter **ptr_addr** provides and array of Ethernet MAC addresses.  The number of addresses is supplied by **num_addr.** Specifying **num_adr** = 0 disables address filtering previously set with this function.

The Ethernet MAC receiver will accept packets addressed to its own address and packets with addresses configured by this function.

MAC receiver can be configured to accept also packets with broadcast address, any multicast address or even all packets regardless of address (Promiscuity Mode). 
This is configured by function ARM_ETH_MAC_Control with ARM_ETH_MAC_CONFIGURE as control parameter.
******************************************************************************************************************
