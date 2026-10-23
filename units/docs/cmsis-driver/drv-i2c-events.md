---
id: "drv-i2c-events"
type: "concept"
domain: "drivers"
title: "I2C Events"
summary: "The I2C driver generates call back events that are notified via the function ARM_I2C_SignalEvent."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_I2C.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_I2C.c"
license: "Apache-2.0"
mode: "V"
---

The I2C driver generates call back events that are notified via the function ARM_I2C_SignalEvent.
 
This section provides the event values for the ARM_I2C_SignalEvent callback function.

The following call back notification events are generated:

### ARM_I2C_EVENT_TRANSFER_DONE

```c
ARM_I2C_EVENT_TRANSFER_DONE
```


### ARM_I2C_EVENT_TRANSFER_INCOMPLETE

```c
ARM_I2C_EVENT_TRANSFER_INCOMPLETE
```


### ARM_I2C_EVENT_SLAVE_TRANSMIT

```c
ARM_I2C_EVENT_SLAVE_TRANSMIT
```


### ARM_I2C_EVENT_SLAVE_RECEIVE

```c
ARM_I2C_EVENT_SLAVE_RECEIVE
```


### ARM_I2C_EVENT_ADDRESS_NACK

```c
ARM_I2C_EVENT_ADDRESS_NACK
```


### ARM_I2C_EVENT_GENERAL_CALL

```c
ARM_I2C_EVENT_GENERAL_CALL
```


### ARM_I2C_EVENT_ARBITRATION_LOST

```c
ARM_I2C_EVENT_ARBITRATION_LOST
```


### ARM_I2C_EVENT_BUS_ERROR

```c
ARM_I2C_EVENT_BUS_ERROR
```


### ARM_I2C_EVENT_BUS_CLEAR

```c
ARM_I2C_EVENT_BUS_CLEAR
```
