---
id: "drv-ethernet-mac-interface-arm-eth-mac-getcapabilities"
type: "concept"
domain: "drivers"
title: "Ethernet MAC Interface: ARM_ETH_MAC_GetCapabilities"
summary: "The function ARM_ETH_MAC_GetCapabilities retrieves information about capabilities in this driver implementation."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_ETH_MAC_CAPABILITIES ARM_ETH_MAC_GetCapabilities (void)
```


The function **ARM_ETH_MAC_GetCapabilities** retrieves information about capabilities in this driver implementation.
The data fields of the struct ARM_ETH_MAC_CAPABILITIES encode various capabilities, for example
if a hardware is capable to create checksums in hardware or signal events using the ARM_ETH_MAC_SignalEvent 
callback function.
 
Example:
```
extern ARM_DRIVER_ETH_MAC Driver_ETH_MAC0;
ARM_DRIVER_ETH_MAC *mac;
  
void read_capabilities (void)  {
  ARM_ETH_MAC_CAPABILITIES mac_capabilities;
 
  mac = &Driver_ETH_MAC0;  
  mac_capabilities = mac->GetCapabilities ();
  // interrogate capabilities
 
}
```
******************************************************************************************************************
