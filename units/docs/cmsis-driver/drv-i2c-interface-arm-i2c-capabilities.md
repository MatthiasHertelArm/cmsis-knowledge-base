---
id: "drv-i2c-interface-arm-i2c-capabilities"
type: "concept"
domain: "drivers"
title: "I2C Interface: ARM_I2C_CAPABILITIES"
summary: "An I2C driver can be implemented with different capabilities. The data fields of this struct encode the capabilities implemented by this driver."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_I2C.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_I2C.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_I2C_CAPABILITIES
```


An I2C driver can be implemented with different capabilities.
The data fields of this struct encode the capabilities implemented by this driver.

The element **address_10_bit** indicates that the driver is able to handle 10-bit addressing natively.
User can still emulate the 10-bit addressing in software if the driver does not support it.

**Returned by:**
  - ARM_I2C_GetCapabilities
******************************************************************************************************************
