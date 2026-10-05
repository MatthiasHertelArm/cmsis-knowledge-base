---
id: "drv-nand-interface"
type: "concept"
domain: "drivers"
title: "NAND Interface"
summary: "Driver API for NAND Flash Device Interface (%Driver_NAND.h)."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
license: "Apache-2.0"
mode: "V"
---

Driver API for NAND Flash Device Interface (%Driver_NAND.h).


**NAND** devices are a type of non-volatile storage and do not require power to hold data. 
Wikipedia offers more information about 
the **Flash Memories**, including NAND.

**Block Diagram**


 
 "Simplified NAND Flash Schematic"

 


**NAND API**

The following header files define the Application Programming Interface (API) for the NAND interface:
  - **%Driver_NAND.h** : Driver API for NAND Flash Device Interface

The driver implementation is a typical part of the Device Family Pack (DFP) that supports the 
peripherals of the microcontroller family.

NAND Flash is organized in pages, grouped into blocks as the smallest erasable unit. The addressing
of data is achieved by `byte_address = block * block_size + page_in_block * page_size + offset_in_page`.
In terms of this NAND API blocks and pages are referred to as `row` and the byte offset within the page as `col`.
Thus one can calculate the `byte_address = row * page_size + col`. The parameters `page_size` and `block_size` 
are device specific and must be handled by the driver user appropriately.

**Driver Functions**

The driver functions are published in the access struct as explained in DriverFunctions
  - ARM_DRIVER_NAND : access struct for NAND driver functions

 **Example Code:**

\include NAND_Demo.c
