---
id: "drv-ethernet-mac-interface-arm-eth-mac-phy-write"
type: "concept"
domain: "drivers"
title: "Ethernet MAC Interface: ARM_ETH_MAC_PHY_Write"
summary: "The function ARMETHMACPHYWrite writes to a Ethernet PHY register through the Management Interface. The function is passed to ARMETHPHYInitialize. The Ethernet PHY driver uses this function to write data to PHY registers."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_ETH_MAC_PHY_Write (uint8_t phy_addr, uint8_t reg_addr, uint16_t data)
```


The function **ARM_ETH_MAC_PHY_Write** writes to a Ethernet PHY register through the Management Interface.  The function is passed to ARM_ETH_PHY_Initialize.
The Ethernet PHY driver uses this function to write data to PHY registers.

**Example:**
 - see eth_interface_gr - Driver Functions

******************************************************************************************************************
