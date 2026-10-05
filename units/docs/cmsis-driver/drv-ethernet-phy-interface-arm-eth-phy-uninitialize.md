---
id: "drv-ethernet-phy-interface-arm-eth-phy-uninitialize"
type: "concept"
domain: "drivers"
title: "Ethernet PHY Interface: ARM_ETH_PHY_Uninitialize"
summary: "The function ARMETHPHYUninitialize de-initializes the resources of Ethernet PHY interface."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_PHY.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_PHY.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_ETH_PHY_Uninitialize (void)
```


The function **ARM_ETH_PHY_Uninitialize** de-initializes the resources of Ethernet PHY interface.

It is called when the middleware component stops operation and releases the software resources used by the interface.
****************************************************************************************************************
