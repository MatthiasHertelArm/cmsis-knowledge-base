---
id: "drv-ethernet-interface-arm-eth-interface"
type: "concept"
domain: "drivers"
title: "Ethernet Interface: ARM_ETH_INTERFACE"
summary: "Encodes the supported media interface between Ethernet MAC and Ethernet PHY."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_ETH_INTERFACE
```


Encodes the supported media interface between Ethernet MAC and Ethernet PHY. 

The function ARM_ETH_MAC_GetCapabilities retrieves the media interface type encoded in the data field **media_interface** of the struct
 ARM_ETH_MAC_CAPABILITIES. 

**Parameter for:**
- ARM_ETH_PHY_SetInterface
