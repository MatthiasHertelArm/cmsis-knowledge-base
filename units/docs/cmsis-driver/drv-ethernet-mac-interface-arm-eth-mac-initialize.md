---
id: "drv-ethernet-mac-interface-arm-eth-mac-initialize"
type: "concept"
domain: "drivers"
title: "Ethernet MAC Interface: ARM_ETH_MAC_Initialize"
summary: "The function ARMETHMACInitialize initializes the Ethernet MAC interface. It is called when the middleware component starts operation."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_ETH_MAC_Initialize (ARM_ETH_MAC_SignalEvent_t cb_event)
```

 
The function **ARM_ETH_MAC_Initialize** initializes the Ethernet MAC interface. 
It is called when the middleware component starts operation.

The ARM_ETH_MAC_Initialize function performs the following operations:
  - Initializes the resources needed for the Ethernet MAC peripheral.
  - Registers the ARM_ETH_MAC_SignalEvent callback function.

The parameter **cb_event** is a pointer to the ARM_ETH_MAC_SignalEvent callback function; use a NULL pointer 
when no callback signals are required.

**Example:**
 - see eth_interface_gr - Driver Functions
******************************************************************************************************************
