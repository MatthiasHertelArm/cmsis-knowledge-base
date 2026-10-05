---
id: "drv-ethernet-mac-interface-arm-eth-mac-getrxframesize"
type: "concept"
domain: "drivers"
title: "Ethernet MAC Interface: ARM_ETH_MAC_GetRxFrameSize"
summary: "The function ARMETHMACGetRxFrameSize returns the size of a received Ethernet frame. This function is called before ARMETHMACReadFrame and supplies the value len."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t ARM_ETH_MAC_GetRxFrameSize (void)
```


The function **ARM_ETH_MAC_GetRxFrameSize** returns the size of a received 
**Ethernet frame**.
This function is called before ARM_ETH_MAC_ReadFrame and supplies the value **len.**

The frame size includes MAC destination and ends with the last Payload data byte.
Value **0** indicates that no Ethernet frame is available in the receive buffer.
Values smaller than minimum size of Ethernet frame or larger than maximum size of Ethernet frame
indicate an invalid frame which needs to be discarded by calling ARM_ETH_MAC_ReadFrame.

**Example:**
  - see ARM_ETH_MAC_ReadFrame

******************************************************************************************************************
