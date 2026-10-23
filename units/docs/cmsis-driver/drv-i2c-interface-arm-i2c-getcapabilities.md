---
id: "drv-i2c-interface-arm-i2c-getcapabilities"
type: "concept"
domain: "drivers"
title: "I2C Interface: ARM_I2C_GetCapabilities"
summary: "The function ARM_I2C_GetCapabilities returns information about capabilities of this driver implementation. The data fields of the struct ARM_I2C_CAPABILITIES encodes the driver capabilities."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_I2C.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_I2C.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_I2C_CAPABILITIES ARM_I2C_GetCapabilities (void)
```


The function **ARM_I2C_GetCapabilities** returns information about capabilities of this driver implementation.
The data fields of the struct ARM_I2C_CAPABILITIES encodes the driver capabilities.
 
Example:
```
extern ARM_DRIVER_I2C Driver_I2C0;
ARM_DRIVER_I2C *drv_info;
  
void read_capabilities (void)  {
  ARM_I2C_CAPABILITIES drv_capabilities;
 
  drv_info = &Driver_I2C0;  
  drv_capabilities = drv_info->GetCapabilities ();
  // interrogate capabilities
 
}
```
******************************************************************************************************************
