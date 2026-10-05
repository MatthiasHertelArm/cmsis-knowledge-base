---
id: "drv-spi-interface"
type: "concept"
domain: "drivers"
title: "SPI Interface"
summary: "Driver API for SPI Bus Peripheral (%DriverSPI.h)"
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_SPI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_SPI.c"
license: "Apache-2.0"
mode: "V"
---

Driver API for SPI Bus Peripheral (%Driver_SPI.h)
 
The **Serial Peripheral Interface Bus** (SPI) implements a synchronous serial bus for data exchange. In microcontroller (MCU) applications,
the interface is often used to connect peripheral components at board (PCB) level. SPI devices can operate as Master (SCLK and SS are outputs) or 
Slave (SCLK and SS are inputs). Wikipedia offers more information about 
the **Serial Peripheral Interface Bus**.

**Block Diagram**

The SPI Driver API defines a **SPI** interface for middleware components. The SPI Driver supports multiple
slaves, but if only one slave is connected, then the Slave Select signal can be omitted.


  "SPI Master connected to a single slave"



 
  "SPI Master connected to 3 slaves"

The SPI Driver functions control the following SPI signal lines. 

Signal | Name                                | Description
-------|-------------------------------------|------------------------------------------------------------------------------
SS     | Slave Select (active low)           | Selects the slave. This signal can be part of the SPI peripheral or implemented using a GPIO pin.
MOSI   | Master Out, Slave In | MOSI output of the Master connects to MOSI input of the Slave.
SCLK   | Serial Clock                        | Serial clock output from Master. Controls the transfer speed and when data are sent and read.
MISO   | Master In, Slave Out | MISO input of the Master connects to MISO output of the Slave.


**SPI API**

The following header files define the Application Programming Interface (API) for the SPI interface:
  - **%Driver_SPI.h** : Driver API for SPI Bus Peripheral

The driver implementation is a typical part of the Device Family Pack (DFP) that supports the 
peripherals of the microcontroller family.


**Driver Functions**

The driver functions are published in the access struct as explained in DriverFunctions
  - ARM_DRIVER_SPI : access struct for SPI driver functions

  
**Example Code**

The following example code shows the usage of the SPI interface.

\include SPI_Demo.c
