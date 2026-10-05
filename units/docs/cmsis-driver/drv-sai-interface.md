---
id: "drv-sai-interface"
type: "concept"
domain: "drivers"
title: "SAI Interface"
summary: "Driver API for Serial Audio Interface (%Driver_SAI.h)"
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
license: "Apache-2.0"
mode: "V"
---

Driver API for Serial Audio Interface (%Driver_SAI.h)
 
The **Serial Audio Interface** (SAI) implements a synchronous serial bus interface for connecting digital audio devices. 
It is by far the most common mechanism used to transfer two channels of audio data between devices within a system. **SAI**
can transfer digital audio using various protocols:
- Driver_SAI_I2S
- Driver_SAI_MSB
- Driver_SAI_LSB
- Driver_SAI_PCM
- Driver_SAI_AC97
- Driver_SAI_User


**Block Diagram**


 
 "Simplified SAI Schematic"

 


**SAI API**

The following header files define the Application Programming Interface (API) for the SAI interface:
  - **%Driver_SAI.h** : Driver API for Serial Audio Interface

The driver implementation is a typical part of the
Device Family Pack (DFP) that supports the peripherals of the microcontroller family.


**Driver Functions**

The driver functions are published in the access struct as explained in DriverFunctions
  - ARM_DRIVER_SAI : access struct for SAI driver functions
