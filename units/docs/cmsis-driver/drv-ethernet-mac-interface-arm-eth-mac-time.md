---
id: "drv-ethernet-mac-interface-arm-eth-mac-time"
type: "concept"
domain: "drivers"
title: "Ethernet MAC Interface: ARM_ETH_MAC_TIME"
summary: "The two members of this struct provide fields to encode time values in the order Nano seconds and seconds."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_ETH_MAC_TIME
```


The two members of this struct provide fields to encode time values in the order `Nano seconds` and `seconds`.

The member **ns** is also used as a correction factor for ARM_ETH_MAC_TIMER_ADJUST_CLOCK.

**Used in:**
  - ARM_ETH_MAC_GetRxFrameTime
  - ARM_ETH_MAC_GetTxFrameTime
  - ARM_ETH_MAC_ControlTimer

******************************************************************************************************************
