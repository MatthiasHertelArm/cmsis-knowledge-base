---
id: "drv-ethernet-mac-interface-arm-eth-mac-getversion"
type: "concept"
domain: "drivers"
title: "Ethernet MAC Interface: ARM_ETH_MAC_GetVersion"
summary: "The function ARMETHMACGetVersion returns version information of the driver implementation in ARMDRIVERVERSION - API version is the version of the CMSIS-Driver specification used to implement this driver. - Driver version is source code version of the actual driver implementation."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_DRIVER_VERSION ARM_ETH_MAC_GetVersion (void);
```


The function **ARM_ETH_MAC_GetVersion** returns version information of the driver implementation in ARM_DRIVER_VERSION
 - API version is the version of the CMSIS-Driver specification used to implement this driver.
 - Driver version is source code version of the actual driver implementation.

Example:
```
extern ARM_DRIVER_ETH_MAC Driver_ETH_MAC0;
ARM_DRIVER_ETH_MAC *mac;
 
void setup_ethernet (void)  {
  ARM_DRIVER_VERSION  version;
 
  mac = &Driver_ETH_MAC0;  
  version = mac->GetVersion ();
  if (version.api < 0x10A)   {      // requires at minimum API version 1.10 or higher
    // error handling
    return;
  }
}
```
******************************************************************************************************************
