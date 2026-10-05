---
id: "drv-ethernet-phy-interface-arm-eth-phy-initialize"
type: "concept"
domain: "drivers"
title: "Ethernet PHY Interface: ARM_ETH_PHY_Initialize"
summary: "The function ARMETHPHYInitialize initializes the Ethernet PHY interface. It is called when the middleware component starts operation."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_PHY.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_PHY.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_ETH_PHY_Initialize (ARM_ETH_PHY_Read_t fn_read, ARM_ETH_PHY_Write_t fn_write)
```


The function **ARM_ETH_PHY_Initialize** initializes the Ethernet PHY interface. 
It is called when the middleware component starts operation.

The ARM_ETH_PHY_Initialize function performs the following operations:
  - Initializes the resources needed for Ethernet PHY peripheral.
  - Registers the ARM_ETH_MAC_PHY_Read register read access function.
  - Registers the ARM_ETH_MAC_PHY_Write register write access function.

**Example:**
 - see eth_interface_gr - Driver Functions

****************************************************************************************************************
