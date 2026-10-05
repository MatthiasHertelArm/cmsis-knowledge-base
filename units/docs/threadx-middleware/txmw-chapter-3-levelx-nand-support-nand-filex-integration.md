---
id: "txmw-chapter-3-levelx-nand-support-nand-filex-integration"
type: "concept"
domain: "rtos"
title: "Chapter 3 - LevelX NAND support: NAND FileX Integration"
summary: "As mentioned earlier, LevelX does not rely on FileX for operation. All the LevelX APIs may be called directly by the application software to store/retrieve raw data to the logical sectors provided by LevelX. However, LevelX also supports FileX."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter3.md#nand-filex-integration"
license: "MIT"
mode: "V"
---

As mentioned earlier, LevelX does not rely on FileX for operation. All the LevelX APIs may be called directly by the application software to store/retrieve raw data to the logical sectors provided by LevelX. However, LevelX also supports FileX.

The file ***fx_nand_flash_simulated_driver.c*** contains an example FileX driver for use with the NAND flash simulation. An interesting aspect of this driver is that it combines 512-byte logical sectors typically used by FileX into single logical sector read/write requests to the LevelX simulator using 2048-byte pages. This results in more efficient use of the NAND flash memory. The NAND flash FileX driver for LevelX provides a good starting point for writing custom FileX drivers.  
  
> **Note:** The FileX NAND flash format should be one full block size of sectors less than the NAND flash provides. This will help ensure best performance during the wear level processing. Additional techniques to improve write performance in the LevelX wear leveling algorithm include the following.
> 
> 1. Ensure that all writes are exactly one or more clusters in size and start on exact cluster boundaries.
> 1. Pre-allocate clusters before performing large file write operations via the FileX ***fx_file_allocate*** class of APIs.
> 1. Ensure the FileX driver is enabled to receive release sector information and requests made to the driver to release sectors are handled in the driver by calling ***lx_nor_flash_sector_release***.
