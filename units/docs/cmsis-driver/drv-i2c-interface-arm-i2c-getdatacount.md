---
id: "drv-i2c-interface-arm-i2c-getdatacount"
type: "concept"
domain: "drivers"
title: "I2C Interface: ARM_I2C_GetDataCount"
summary: "The function ARMI2CGetDataCount returns the number of currently transferred data bytes during and after: - ARMI2CMasterTransmit : number of data bytes transmitted and acknowledged - ARMI2CMasterReceive : number of data bytes received - ARMI2CSlaveTransmit : number of data …"
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_I2C.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_I2C.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_I2C_GetDataCount (void)
```


The function **ARM_I2C_GetDataCount** returns the number of currently transferred data bytes during and after:
 - ARM_I2C_MasterTransmit : number of data bytes transmitted and acknowledged
 - ARM_I2C_MasterReceive : number of data bytes received
 - ARM_I2C_SlaveTransmit : number of data bytes transmitted
 - ARM_I2C_SlaveReceive : number of data bytes received and acknowledged

When the Slave is not yet addressed by the Master then `-1` is returned.
****************************************************************************************************************
