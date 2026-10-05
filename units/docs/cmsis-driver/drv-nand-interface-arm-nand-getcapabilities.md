---
id: "drv-nand-interface-arm-nand-getcapabilities"
type: "concept"
domain: "drivers"
title: "NAND Interface: ARM_NAND_GetCapabilities"
summary: "The function ARMNANDGetCapabilities retrieves information about capabilities in this driver implementation. The data fields of the structure ARMNANDCAPABILITIES encode various capabilities, for example if a hardware is able to create signal events using the ARMNANDSignalEvent callback function."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_NAND_CAPABILITIES ARM_NAND_GetCapabilities (void)
```


The function **ARM_NAND_GetCapabilities** retrieves information about capabilities in this driver implementation.
The data fields of the structure ARM_NAND_CAPABILITIES encode various capabilities, for example
if a hardware is able to create signal events using the ARM_NAND_SignalEvent 
callback function.
 
Example:
```
extern ARM_DRIVER_NAND Driver_NAND0;
ARM_DRIVER_NAND *drv_info;
  
void read_capabilities (void)  {
  ARM_NAND_CAPABILITIES drv_capabilities;
 
  drv_info = &Driver_NAND0;  
  drv_capabilities = drv_info->GetCapabilities ();
  // interrogate capabilities
 
}
```
******************************************************************************************************************
