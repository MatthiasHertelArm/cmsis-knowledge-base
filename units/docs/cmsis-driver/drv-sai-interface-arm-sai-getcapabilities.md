---
id: "drv-sai-interface-arm-sai-getcapabilities"
type: "concept"
domain: "drivers"
title: "SAI Interface: User Defined Protocol / ARM_SAI_GetCapabilities"
summary: "The function ARM_SAI_GetCapabilities retrieves information about the capabilities in this driver implementation."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
license: "Apache-2.0"
mode: "V"
---

_Part of: User Defined Protocol_

```c
ARM_SAI_CAPABILITIES ARM_SAI_GetCapabilities (void)
```

The function **ARM_SAI_GetCapabilities** retrieves information about the capabilities in this driver implementation.
The data fields of the struct ARM_SAI_CAPABILITIES encode various capabilities, for example
supported protocols, or if a hardware is capable to create signal events using the ARM_SAI_SignalEvent 
callback function.
 
**Example:**
```
extern ARM_DRIVER_SAI Driver_SAI0;
ARM_DRIVER_SAI *drv_info;
  
void read_capabilities (void)  {
  ARM_SAI_CAPABILITIES drv_capabilities;
 
  drv_info = &Driver_SAI0;  
  drv_capabilities = drv_info->GetCapabilities ();
  // interrogate capabilities
 
}
```
****************************************************************************************************************
