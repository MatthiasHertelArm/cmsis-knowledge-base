---
id: "spec-flash-programming-creating-a-new-algorithm"
type: "concept"
domain: "pack"
title: "Flash Programming: Creating a new Algorithm"
summary: "Flash programming algorithms are defined with functions to erase and program the Flash device. Special compiler and linker settings are required."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/flash_algorithms.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/flashAlgorithm.html"
license: "Apache-2.0"
mode: "V"
---

Flash programming algorithms are defined with functions to erase and program the Flash device. Special compiler and linker
settings are required. Follow these steps to create and configure a new Flash programming algorithm:
-# Copy the content from the **ARM:CMSIS** Pack folder (usually
   ${CMSIS_PACK_ROOT}/ARM/Cortex_DFP/_version_/Device/Template/Flash) to a new folder.
-# Rename the project file **NewDevice.uvprojx** to represent the new Flash ROM device name, for example **MyDevice.uvprojx.**
-# Open the project with uVision. From the toolbar, use the drop-down **Select Target** to define the processor
   architecture. **Cortex-M** fits for all Cortex-M0/M0+, M3, and M4 devices. The configuration assumes a little-endian
   microcontroller. In case of a big-endian microcontroller, select the correct processor core with **Project** -
   **Options for Target** - **Device.**
-# Open the dialog **Project** - **Options for Target** - **Output** and change the content of the field
   **Name of Executable** to represent the device, for example **MyDevice.**
-# Adapt the programming algorithms in the file FlashPrg.
-# Adapt the device parameters in the file FlashDev.
-# Use **Project** - **Build Target** to generate the new Flash programming algorithm. The output file (for example
   **MyDevice.FLM)** has to be added to the **DFP.**

**Note:**
- Creating a Flash programming algorithm with
  MDK-Lite is not supported.
- Flash programming algorithms use **Read-Only Position Independent** and **Read-Write Position Independent** program
  code. These options are set in the dialogs **Project** - **Options for Target** - **C/C++** and **Project** -
  **Options for Target** - **Asm.**
- The dialog **Project** - **Options for Target** - **Linker** defines the linker scatter file **Target.lin.** The error
  L6305 is disabled with `--diag_suppress` `L6305.`
- The Flash Algorithm Functions section contains reference for all the available functions.


FlashPrg.c
----------
The file **FlashPrg.c** contains the mandatory Flash programming functions Init, UnInit, EraseSector, and
ProgramPage. Optionally, depending on the device features (or to speed-up execution), the functions EraseChip,
BlankCheck, and Verify can be implemented.


FlashDev.c
----------
The file **FlashDev.c** contains parameter definitions for:
-# the Flash programming functions.
-# the **FlashDevice** structure:
```
struct FlashDevice const FlashDevice  =  {
   FLASH_DRV_VERS,             // Driver Version, do not modify!
   "New Device 256kB Flash",   // Device Name 
   ONCHIP,                     // Device Type
   0x00000000,                 // Device Start Address
   0x00040000,                 // Device Size in Bytes (256kB)
   1024,                       // Programming Page Size
   0,                          // Reserved, must be 0
   0xFF,                       // Initial Content of Erased Memory
   100,                        // Program Page Timeout 100 mSec
   3000,                       // Erase Sector Timeout 3000 mSec
 
// Specify Size and Address of Sectors
   0x002000, 0x000000,         // Sector Size  8kB (8 Sectors)
   0x010000, 0x010000,         // Sector Size 64kB (2 Sectors) 
   0x002000, 0x030000,         // Sector Size  8kB (8 Sectors)
   SECTOR_END
};
```

**Note:**
The **Device Name** is usually be shown in tools to identify the Flash algorithm. Make sure that this name reflects the device name.

**Note:**
The **Programming Page Size** specifies the block size for programming using the function ProgramPage.  For devices with small block sizes
it might be better to specify a multiple of the physical block size as this reduces the communication overhead to the target.
An optimal block size for fast programming is 1024 bytes, however the system itself does not restrict this size value.
