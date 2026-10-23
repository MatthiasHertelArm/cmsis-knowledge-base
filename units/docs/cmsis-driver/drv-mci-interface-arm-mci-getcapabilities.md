---
id: "drv-mci-interface-arm-mci-getcapabilities"
type: "concept"
domain: "drivers"
title: "MCI Interface: ARM_MCI_GetCapabilities"
summary: "The function ARM_MCI_GetCapabilities returns information about capabilities in this driver implementation. The data fields of the structure ARM_MCI_CAPABILITIES encode various capabilities, for example supported bus modes ..."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_MCI_CAPABILITIES ARM_MCI_GetCapabilities (void)
```


The function **ARM_MCI_GetCapabilities** returns information about capabilities in this driver implementation.
The data fields of the structure ARM_MCI_CAPABILITIES encode various capabilities, for example
supported bus modes ...
 
Example:
```
extern ARM_DRIVER_MCI Driver_MCI0;
ARM_DRIVER_MCI *drv_info;
  
void read_capabilities (void)  {
  ARM_MCI_CAPABILITIES drv_capabilities;
 
  drv_info = &Driver_MCI0;  
  drv_capabilities = drv_info->GetCapabilities ();
  // interrogate capabilities
 
}
```
******************************************************************************************************************
