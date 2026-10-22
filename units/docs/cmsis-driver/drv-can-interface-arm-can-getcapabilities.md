---
id: "drv-can-interface-arm-can-getcapabilities"
type: "concept"
domain: "drivers"
title: "CAN Interface: Remote Frame / ARM_CAN_GetCapabilities"
summary: "The function ARM_CAN_GetCapabilities returns information about the capabilities in this driver implementation. The data fields of the structure ARM_CAN_CAPABILITIES encode various capabilities."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
license: "Apache-2.0"
mode: "V"
---

_Part of: Remote Frame_

```c
ARM_CAN_CAPABILITIES ARM_CAN_GetCapabilities (void)
```


The function **ARM_CAN_GetCapabilities** returns information about the capabilities in this driver implementation.
The data fields of the structure ARM_CAN_CAPABILITIES encode various capabilities.

Example:
```
extern ARM_DRIVER_CAN Driver_CAN0;
ARM_DRIVER_CAN *drv_info;

void read_capabilities (void)  {
  ARM_CAN_CAPABILITIES drv_capabilities;

  drv_info = &Driver_CAN0;
  drv_capabilities = drv_info->GetCapabilities ();
  // interrogate capabilities

}
```
******************************************************************************************************************
