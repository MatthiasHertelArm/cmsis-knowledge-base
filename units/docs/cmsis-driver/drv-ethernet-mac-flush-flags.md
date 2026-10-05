---
id: "drv-ethernet-mac-flush-flags"
type: "concept"
domain: "drivers"
title: "Ethernet MAC Flush Flags"
summary: "The function ARMETHMACControl with control = ARMETHMACFLUSH flushes the buffer which is specified with arg listed bellow."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
license: "Apache-2.0"
mode: "V"
---

Specify controls to flush a buffer

The function ARM_ETH_MAC_Control with **control** = ARM_ETH_MAC_FLUSH flushes the buffer
which is specified with **arg** listed bellow.


### ARM_ETH_MAC_FLUSH_RX

```c
ARM_ETH_MAC_FLUSH_RX
```


### ARM_ETH_MAC_FLUSH_TX

```c
ARM_ETH_MAC_FLUSH_TX
```
