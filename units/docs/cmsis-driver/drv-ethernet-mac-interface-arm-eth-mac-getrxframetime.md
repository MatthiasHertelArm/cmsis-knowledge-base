---
id: "drv-ethernet-mac-interface-arm-eth-mac-getrxframetime"
type: "concept"
domain: "drivers"
title: "Ethernet MAC Interface: ARM_ETH_MAC_GetRxFrameTime"
summary: "Retrieve time stamp of a received Ethernet frame. This function must be called before the frame is read using ARM_ETH_MAC_ReadFrame."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_ETH_MAC_GetRxFrameTime (ARM_ETH_MAC_TIME *time)
```


Retrieve time stamp of a received **Ethernet frame**.
This function must be called before the frame is read using ARM_ETH_MAC_ReadFrame.
******************************************************************************************************************
