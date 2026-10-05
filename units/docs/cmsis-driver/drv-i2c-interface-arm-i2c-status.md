---
id: "drv-i2c-interface-arm-i2c-status"
type: "concept"
domain: "drivers"
title: "I2C Interface: ARM_I2C_STATUS"
summary: "Structure with information about the status of the I2C."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_I2C.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_I2C.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_I2C_STATUS
```


Structure with information about the status of the I2C.

The flag **busy** indicates that the driver is busy executing Master/Slave Transmit/Receive operation.

It is set:
 - when Master operation starts: after calling ARM_I2C_MasterTransmit or ARM_I2C_MasterReceive
 - when Slave operation starts: after calling ARM_I2C_SlaveTransmit or ARM_I2C_SlaveReceive and after being addressed by a Master as the Slave

It is cleared when Master/Slave operation has finished.

The flag **mode** indicates the current mode which is Master when Master Transmit/Receive is active or Slave otherwise.

The flag **direction** indicates either Transmitter or Receiver mode. It is updated during Master/Slave operation when the Slave is addressed by a Master.

The flag **general_call** indicates a General call (address `0`) when in Slave mode.

The flag **arbitration_lost** indicates that the Master has lost arbitration. The current Master operation is aborted.

The flag **bus_error** indicates that a bus error has been detected. The current Master/Slave operation is aborted.

**Returned by:**
  - ARM_I2C_GetStatus
******************************************************************************************************************
