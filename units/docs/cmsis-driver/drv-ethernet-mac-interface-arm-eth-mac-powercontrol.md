---
id: "drv-ethernet-mac-interface-arm-eth-mac-powercontrol"
type: "concept"
domain: "drivers"
title: "Ethernet MAC Interface: ARM_ETH_MAC_PowerControl"
summary: "The function ARM_ETH_MAC_PowerControl allows you to configure the power modes of the Ethernet MAC interface."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_ETH_MAC_PowerControl (ARM_POWER_STATE state)
```

     
The function **ARM_ETH_MAC_PowerControl** allows you to configure the power modes of the Ethernet MAC interface.  

The parameter **state** can be:
 - ARM_POWER_OFF: Ethernet MAC peripheral is turned off.
 - ARM_POWER_FULL: Ethernet MAC peripheral is turned on and fully operational.

If power **state** specifies an unsupported mode, the function returns ARM_DRIVER_ERROR_UNSUPPORTED as status information
and the previous power state of the peripheral is unchanged. Multiple calls with the same **state** generate no
error.

**Example:**
 - see eth_interface_gr - Driver Functions
******************************************************************************************************************
