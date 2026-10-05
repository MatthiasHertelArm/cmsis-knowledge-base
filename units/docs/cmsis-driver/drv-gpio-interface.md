---
id: "drv-gpio-interface"
type: "concept"
domain: "drivers"
title: "GPIO Interface"
summary: "Driver API for GPIO Interface (%DriverGPIO.h)"
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_GPIO.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_GPIO.c"
license: "Apache-2.0"
mode: "V"
---

Driver API for GPIO Interface (%Driver_GPIO.h)
 
The **General-purpose Input/Output Interface** (GPIO) features Input/Output operations on pin level (does not support simultaneous operations on multiple pins belonging to the same port).

Features:
 - basic pin configuration (direction, output mode, pull-resistor, event trigger) excluding advanced settings (drive strength or speed, input filter, ...),
 - events on edge detection,
 - setting outputs,
 - reading inputs.

Each function operates on a pin level and uses a pin identification as the first parameter. Pin identification is a virtual number which is mapped to an actual pin.

**GPIO API**

The following header files define the Application Programming Interface (API) for the GPIO interface:
  - **%Driver_GPIO.h** : Driver API for GPIO Interface

The driver implementation is a typical part of the Device Family Pack (DFP) that supports the 
peripherals of the microcontroller family.


**Driver Functions**

The driver functions are published in the access struct as explained in DriverFunctions
  - ARM_DRIVER_GPIO : access struct for GPIO driver functions

  
**Example Code**

The following example code shows the usage of the GPIO interface.

\include GPIO_Demo.c
