---
id: "drv-mci-interface"
type: "concept"
domain: "drivers"
title: "MCI Interface"
summary: "Driver API for Memory Card Interface using SD/MMC interface (%DriverMCI.h)"
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
license: "Apache-2.0"
mode: "V"
---

Driver API for Memory Card Interface using SD/MMC interface (%Driver_MCI.h)


The **Memory Card Interface** (MCI) implements the hardware abstraction layer for Secure Digital (SD) and Multi Media Card (MMC)
memory that is typically used as file storage. For embedded systems, SD/MMC devices are available as memory cards in several 
forms (SD, miniSD, microSD, MMC, MMCmicro) or as non-removable device
es that are directly soldered to the PCB (eMMC).  

**References:**
- Wikipedia offers more information about the **Secure Digital** memory.
- Wikipedia offers more information about the **MultiMediaCard**.
- The SD Association provides detailed documentation under www.sdcard.org.
- The MultiMediaCard Association (merged with JEDEC) provides detailed documentation under www.jedec.org.

**Block Diagram**

The MCI driver allows you to exchange data of the SD/MMC memory via SD/MMC interface.

The following modes are supported by SD/MMC memory cards:

- SPI bus mode: Serial Peripheral Interface Bus supported by most microcontrollers.
- 1-bit SD/MMC Bus mode: proprietary data transfer protocol supported by SD/MMC interfaces.
- 4-bit SD/MMC Bus mode: high-speed version of the SD/MMC interface using 4 data I/O pins. 
- 8-bit SD/MMC Bus mode: high-speed version of the SD/MMC interface using 8 data I/O pins. 

  "SD memory connected via SPI interface"

 
  "SD memory connected via 1-bit SD Bus Mode"

 
  "SD memory connected via 4-bit SD Bus Mode"


**MCI API**

The following header files define the Application Programming Interface (API) for the MCI interface:
  - **%Driver_MCI.h** : Driver API for Memory Card Interface using SD/MMC interface

The driver implementation is a typical part of the Device Family Pack (DFP) that supports the 
peripherals of the microcontroller family.

**Note:**
For parameters, the value marked with (default) is the setting after the driver initialization.

 
**Driver Functions**

The driver functions are published in the access struct as explained in DriverFunctions
  - ARM_DRIVER_MCI : access struct for MCI driver functions


**Example Code**

The following example code shows the usage of the MCI interface.

\include MCI_Demo.c
