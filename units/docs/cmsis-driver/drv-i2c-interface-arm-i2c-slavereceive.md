---
id: "drv-i2c-interface-arm-i2c-slavereceive"
type: "concept"
domain: "drivers"
title: "I2C Interface: ARM_I2C_SlaveReceive"
summary: "This function ARM_I2C_SlaveReceive receives data as Slave from the Master."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_I2C.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_I2C.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_I2C_SlaveReceive (uint8_t *data, uint32_t num)
```


This function **ARM_I2C_SlaveReceive** receives data as Slave from the Master.

The parameter **data** is a pointer to the data to receive. \n
The parameter **num** specifies the number of bytes to receive.

The function is non-blocking and returns as soon as the driver has registered the operation.
The actual operation will start after being addressed by the master as a Slave Receiver. If the operation has not been registered at that point the ARM_I2C_EVENT_SLAVE_RECEIVE event is generated.

It is not allowed to call this function again if the operation has started until it finishes. Also the data buffer must stay allocated. 
When receive operation has finished the ARM_I2C_EVENT_TRANSFER_DONE event is generated.
When not all the data is transferred then the ARM_I2C_EVENT_TRANSFER_INCOMPLETE flag is set at the same time.

Number of data bytes received and acknowledged is returned by the function ARM_I2C_GetDataCount during and after the operation has finished.

In case that a General call has been detected the ARM_I2C_EVENT_GENERAL_CALL flag is indicated together with the ARM_I2C_EVENT_TRANSFER_DONE event (also with ARM_I2C_EVENT_SLAVE_RECEIVE event).

In case that bus error has been detected then the operation is aborted and the ARM_I2C_EVENT_BUS_ERROR event is generated together with ARM_I2C_EVENT_TRANSFER_DONE.

Slave will only respond to its own address (or General call if enabled) that is specified by calling ARM_I2C_Control with ARM_I2C_OWN_ADDRESS as control parameter. 
Using address `0` disables the slave.

Status can be monitored by calling the ARM_I2C_GetStatus and checking the flags.

Receive operation can be canceled or aborted by calling ARM_I2C_Control with the parameter **control** = ARM_I2C_ABORT_TRANSFER.
******************************************************************************************************************
