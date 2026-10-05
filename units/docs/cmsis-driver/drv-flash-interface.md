---
id: "drv-flash-interface"
type: "concept"
domain: "drivers"
title: "Flash Interface"
summary: "Driver API for Flash Device Interface (%Driver_Flash.h)"
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_Flash.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_Flash.c"
license: "Apache-2.0"
mode: "V"
---

Driver API for Flash Device Interface (%Driver_Flash.h)

Flash devices based on NOR memory cells are the
preferred technology for embedded applications requiring a discrete non-volatile memory device. The low read latency
characteristic of these Flash devices allow a direct code execution
(XIP) and data storage in a single memory
product.

**Flash API**

The Flash API provides a generic API suitable for Flashes with NOR memory cells independent from the actual interface
to the MCU (memory bus, SPI, ...). SPI
flashes are typically not named NOR flashes but have usually same flash cell properties. 

The following header files define the Application Programming Interface (API) for the Flash interface:
  - **%Driver_Flash.h** : Driver API for Flash Device Interface

**Driver Functions**

The driver functions are published in the access struct as explained in DriverFunctions
  - ARM_DRIVER_FLASH : access struct for Flash driver functions

A typical setup sequence for the driver is shown below:

**Example Code:**

\include Flash_Demo.c
