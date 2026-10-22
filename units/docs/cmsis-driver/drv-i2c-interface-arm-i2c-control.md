---
id: "drv-i2c-interface-arm-i2c-control"
type: "concept"
domain: "drivers"
title: "I2C Interface: ARM_I2C_Control"
summary: "The function ARM_I2C_Control operates the I2C interface and executes various operations."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_I2C.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_I2C.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_I2C_Control (uint32_t control, uint32_t arg)
```


The function **ARM_I2C_Control** operates the I2C interface and executes various operations. 

The parameter **control** specifies various operations as listed in the table below.  \n
The parameter **arg** provides, depending on the operation,  additional information. \n

Parameter **control**            | Operation
:--------------------------------|:--------------------------------------------
ARM_I2C_OWN_ADDRESS         | Set Own Slave Address; **arg** = slave address
ARM_I2C_BUS_SPEED           | Set Bus Speed; **arg** = bus speed
ARM_I2C_BUS_CLEAR           | Clear the bus by sending nine clock pulses
ARM_I2C_ABORT_TRANSFER      | Aborts the data transfer between Master and Slave for Transmit or Receive 

**Set Own Slave Address**

After initialization, the I2C Device has no slave address assigned and does not accept any requests from 
an I2C Master.

The **control** operation ARM_I2C_OWN_ADDRESS sets the slave address with the parameter **arg.**
The slave address can be ORed with ARM_I2C_ADDRESS_10BIT to indicate a 10-bit address.  

The slave address can be ORed with ARM_I2C_ADDRESS_GC to indicate that the slave accepts a General Call.
If the slave address value is only ARM_I2C_ADDRESS_GC, then the slave only accepts a General Call.

The slave address value `0` disables Slave mode and clears any assigned slave address.

**Examples:**

Set the Slave address value `0x45` as 7-bit address.
```
  I2Cdrv->Control      (ARM_I2C_OWN_ADDRESS, 0x45);
```

Set the Slave address value `0x135` as 10-bit address and accept a General Call.
```
  I2Cdrv->Control      (ARM_I2C_OWN_ADDRESS, 0x135 | ARM_I2C_ADDRESS_10BIT | ARM_I2C_ADDRESS_GC);
```

**Bus Speed**

The **control** operation ARM_I2C_BUS_SPEED sets the bus speed using the parameter **arg.**

Parameter **arg**                | Bus Speed
:--------------------------------|:--------------------------------------------
ARM_I2C_BUS_SPEED_STANDARD  | Standard Speed to (`100 kHz`)
ARM_I2C_BUS_SPEED_FAST      | Fast Speed  (`400kHz`)
ARM_I2C_BUS_SPEED_FAST_PLUS | Fast + Speed (`1MHz`)
ARM_I2C_BUS_SPEED_HIGH      | High Speed  (`3.4MHz`)

**Example:**

```
  I2Cdrv->Control      (ARM_I2C_BUS_SPEED, I2C_BUS_SPEED_FAST);
```
****************************************************************************************************************
