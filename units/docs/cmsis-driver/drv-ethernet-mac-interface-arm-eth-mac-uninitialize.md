---
id: "drv-ethernet-mac-interface-arm-eth-mac-uninitialize"
type: "concept"
domain: "drivers"
title: "Ethernet MAC Interface: ARM_ETH_MAC_Uninitialize"
summary: "The function ARM_ETH_MAC_Uninitialize de-initializes the resources of Ethernet MAC interface."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_ETH_MAC_Uninitialize (void)
```


The function **ARM_ETH_MAC_Uninitialize** de-initializes the resources of Ethernet MAC interface.

It is called when the middleware component stops operation and releases the software resources 
used by the interface.
******************************************************************************************************************
