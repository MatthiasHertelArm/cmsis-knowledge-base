---
id: "drv-i2c-interface"
type: "concept"
domain: "drivers"
title: "I2C Interface"
summary: "Driver API for I2C Bus Peripheral (%Driver_I2C.h)"
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_I2C.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_I2C.c"
license: "Apache-2.0"
mode: "V"
---

Driver API for I2C Bus Peripheral (%Driver_I2C.h)


I2C (Inter-Integrated Circuit, referred to as I-squared-C, I-two-C, or IIC) is a multi-master serial single-ended bus and is mostly used 
on single boards, but can also connect to components which are linked via cable. 

Most significant features of the I2C bus include:
 - Only two bus lines are required
 - I2C is a true multi-master bus. Simple master/slave relationships exist between all components
 - A baud rate is not required; the master device determines a bus clock
 - Each connected device is addressable by a unique address
 - Providing arbitration and collision detection

For more information about I2C refer to the following web pages:
  - Wikipedia: I2C
  - www.i2c-bus.org.

Devices can operation in Master or Slave mode:

 - To operate in Master mode call the functions ARM_I2C_MasterTransmit or ARM_I2C_MasterReceive. These functions get as argument a _slave address_. 
 
 - To operate in Slave mode set the _slave address_ using the function ARM_I2C_Control. The functions ARM_I2C_SlaveTransmit or ARM_I2C_SlaveReceive are used to transfer data in Slave mode.

**I2C Slave Address**
 
Depending on the device, I2C supports 7-bit and 10-bit Slaves addresses. 
The element _address_10_bit_ in ARM_I2C_CAPABILITIES indicates that the driver is able to handle 10-bit addresses.
A 10-bit Slave address is ORed with ARM_I2C_ADDRESS_10BIT.
 
I2C also supports a General Call to all Slaves by using the slave address value `0`.
A General Call is recognized by Slaves have a slave address value ARM_I2C_ADDRESS_GC registered with the 
function ARM_I2C_Control.

**Block Diagram**

The I2C driver allows you to connect low-speed peripherals to a motherboard, embedded system, cellphone, or other electronic device. 

  "Master/Slave connected via I2C interface"


**I2C API**

The following header files define the Application Programming Interface (API) for the I2C interface:
  - **%Driver_I2C.h** : Driver API for I2C Bus Peripheral

The driver implementation is a typical part of the Device Family Pack (DFP) that supports the 
peripherals of the microcontroller family.


**Driver Functions**

The driver functions are published in the access struct as explained in DriverFunctions
  - ARM_DRIVER_I2C : access struct for I2C driver functions


 **Example Code**

The following example code shows the usage of the I2C interface in Master mode.

\include I2C_Demo.c

The following example code shows the usage of the I2C interface in Slave mode.

\include I2C_SlaveDemo.c
