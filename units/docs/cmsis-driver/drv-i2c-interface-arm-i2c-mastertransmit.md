---
id: "drv-i2c-interface-arm-i2c-mastertransmit"
type: "concept"
domain: "drivers"
title: "I2C Interface: ARM_I2C_MasterTransmit"
summary: "This function ARMI2CMasterTransmit transmits data as Master to the selected Slave."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_I2C.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_I2C.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_I2C_MasterTransmit (uint32_t addr, const uint8_t *data, uint32_t num, bool xfer_pending)
```


This function **ARM_I2C_MasterTransmit** transmits data as Master to the selected Slave.

The operation consists of:
 - Master generates START condition
 - Master addresses the Slave as Master Transmitter
 - Master transmits data to the addressed Slave
 - Master generates STOP condition (if **xfer_pending** is "false")

The parameter **addr** is the address of the slave to transmit the data to. The value can be ORed with ARM_I2C_ADDRESS_10BIT to 
identify a 10-bit address value. \n
The parameter **data** and **num** specify the address of a data buffer and the number of bytes to transmit. \n
Set the parameter **xfer_pending** to 'true' if another transfer operation follows. With **xfer_pending** set to 'false' a STOP condition is generated.

The function is non-blocking and returns as soon as the driver has started the operation.
During the operation it is not allowed to call any Master function again. Also the data buffer must stay allocated and the contents of data must not be modified. 
When transmit operation has finished the ARM_I2C_EVENT_TRANSFER_DONE event is generated.
When not all the data is transferred then the ARM_I2C_EVENT_TRANSFER_INCOMPLETE flag is set at the same time.

Number of data bytes transmitted and acknowledged is returned by the function ARM_I2C_GetDataCount during and after the operation has finished.

The operation is aborted in the following cases (ARM_I2C_EVENT_TRANSFER_DONE event is generated together with):
 - selected slave has not acknowledged the address: ARM_I2C_EVENT_ADDRESS_NACK event
 - arbitration has been lost: ARM_I2C_EVENT_ARBITRATION_LOST event
 - bus error has been detected: ARM_I2C_EVENT_BUS_ERROR event

Status can be monitored by calling the ARM_I2C_GetStatus and checking the flags.

Transmit operation can be aborted also by calling ARM_I2C_Control with the parameter **control** ARM_I2C_ABORT_TRANSFER.
******************************************************************************************************************
