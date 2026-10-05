---
id: "drv-i2c-interface-arm-i2c-signalevent"
type: "concept"
domain: "drivers"
title: "I2C Interface: ARM_I2C_SignalEvent"
summary: "The function ARM_I2C_SignalEvent is a callback function registered by the function ARM_I2C_Initialize.. It is called by the I2C driver to notify the application about I2C_events occurred during operation."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_I2C.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_I2C.c"
license: "Apache-2.0"
mode: "V"
---

```c
void ARM_I2C_SignalEvent (uint32_t event)
```


The function **ARM_I2C_SignalEvent** is a callback function registered by the function ARM_I2C_Initialize..
It is called by the I2C driver to notify the application about I2C_events occurred during operation.

The parameter _event_ indicates one or more events that occurred during driver operation.
Each event is encoded in a separate bit and therefore it is possible to signal multiple events within the same call. 

The following events can be generated:

Parameter **event**                       |     Bit   | Description 
:---------------------------------------- |:---------:|:----------------------------------------------------------
ARM_I2C_EVENT_TRANSFER_DONE          | 1UL << 0  | Occurs after Master/Slave Transmit/Receive operation has finished.
ARM_I2C_EVENT_TRANSFER_INCOMPLETE    | 1UL << 1  | Occurs together with ARM_I2C_EVENT_TRANSFER_DONE when less data is transferred then requested.
ARM_I2C_EVENT_SLAVE_TRANSMIT         | 1UL << 2  | Occurs when addressed as Slave Transmitter and ARM_I2C_SlaveTransmit has not been started.
ARM_I2C_EVENT_SLAVE_RECEIVE          | 1UL << 3  | Occurs when addressed as Slave Receiver and ARM_I2C_SlaveReceive has not been started.
ARM_I2C_EVENT_ADDRESS_NACK           | 1UL << 4  | Occurs in master mode when address is not acknowledged from slave.
ARM_I2C_EVENT_GENERAL_CALL           | 1UL << 5  | Indicates General Call in slave mode together with ARM_I2C_EVENT_TRANSFER_DONE, ARM_I2C_EVENT_SLAVE_TRANSMIT and ARM_I2C_EVENT_SLAVE_RECEIVE.
ARM_I2C_EVENT_ARBITRATION_LOST       | 1UL << 6  | Occurs in master mode when arbitration is lost.
ARM_I2C_EVENT_BUS_ERROR              | 1UL << 7  | Occurs when bus error is detected.
ARM_I2C_EVENT_BUS_CLEAR              | 1UL << 8  | Occurs after ARM_I2C_BUS_CLEAR Control operation has finished.

*************************************************************************************************************************
