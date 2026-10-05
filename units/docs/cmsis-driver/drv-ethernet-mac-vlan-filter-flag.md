---
id: "drv-ethernet-mac-vlan-filter-flag"
type: "concept"
domain: "drivers"
title: "Ethernet MAC VLAN Filter Flag"
summary: "Specify whether to compare only the VLAN Identifier"
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
license: "Apache-2.0"
mode: "V"
---

Specify whether to compare only the VLAN Identifier

The function ARM_ETH_MAC_Control with **control** = ARM_ETH_MAC_VLAN_FILTER configures the VLAN Filter for received frames as specified with **arg.**

By default the complete VLAN Tag (16-bit) is compared. When ARM_ETH_MAC_VLAN_FILTER_ID_ONLY is specified then only the VLAN Identifier (12-bit) is compared.

Specifying **arg=0** disables the VLAN Filter. 


### ARM_ETH_MAC_VLAN_FILTER_ID_ONLY

```c
ARM_ETH_MAC_VLAN_FILTER_ID_ONLY
```
