---
id: "drv-ethernet-phy-interface-arm-eth-phy-getlinkinfo"
type: "concept"
domain: "drivers"
title: "Ethernet PHY Interface: ARM_ETH_PHY_GetLinkInfo"
summary: "The function ARM_ETH_PHY_GetLinkInfo retrieves information about the current established communication mode (half/full duplex) and communication speed. Information is only valid when link is up (see ARM_ETH_PHY_GetLinkState)."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_PHY.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_PHY.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_ETH_LINK_INFO ARM_ETH_PHY_GetLinkInfo (void)
```


The function **ARM_ETH_PHY_GetLinkInfo** retrieves information about the current established communication
mode (half/full duplex) and communication speed. Information is only valid when link is up (see ARM_ETH_PHY_GetLinkState).

**Example:**
 - see eth_interface_gr - Driver Functions
****************************************************************************************************************
