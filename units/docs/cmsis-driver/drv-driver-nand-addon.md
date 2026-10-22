---
id: "drv-driver-nand-addon"
type: "concept"
domain: "drivers"
title: "Driver NAND AddOn"
summary: "Stores the characteristics of a NAND Flash device. This includes the page layout configuration, NAND type, device number (chip select), number of blocks, pages, sectors, and error correction code."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND_AddOn.txt"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND_AddOn.txt"
license: "Apache-2.0"
mode: "V"
---

### ARM_NAND_DEVICE

```c
ARM_NAND_DEVICE
```


Stores the characteristics of a NAND Flash device. This includes the page layout configuration, NAND type, 
device number (chip select), number of blocks, pages, sectors, and error correction code.

**Parameter for:**
  - ARM_NAND_Initialize

******************************************************************************************************************


### ARM_NAND_ECC_INFO_x

```c
ARM_NAND_ECC_INFO_x
```

 
Stores the default NAND page layout definition (with spare_size and spare_offset),
which contains a **Spare** area after each sector. The struct **ARM_NAND_ECC_INFO** defines the **Spare** area.

The page size is defined as the sum of **User** area plus **Spare** area. 
Each page has a small number of associated "spare" bytes (typically 1/32 of the data size) to store the Error Correction Algorithms (ECC). 

The following standard page sizes are available:

Page Size| User + Spare Area
---------|-------------------
528      |  512 +  16 bytes
2112     | 2048 +  64 bytes
4224     | 4096 + 128 bytes
8448     | 8192 + 256 bytes


 "Default Page Layout"


 
 "Organization of the default 16-byte Spare area"

NAND devices require bad block management by the driver software or by a separate controller chip. 
For example, SD cards have mechanisms that execute wear leveling and  bad block management.
The memory capacity shrinks as more blocks are marked bad.
The block size is a value specified as amount of flash pages. 

The following block sizes are available:

Block Size| Pages
----------|-------------------
  8       |   8
 16       |  16
 32       |  32
 64       |  64
128       | 128
256       | 256

**Note:**
NAND chip manufacturers document the order in which pages can be written. 
Typically, single pages of an erase block must be written in sequential order starting from the first. Random-order writes are prohibited or unspecified.

**Parameter for:**
  - ARM_NAND_DEVICE structure
******************************************************************************************************************
