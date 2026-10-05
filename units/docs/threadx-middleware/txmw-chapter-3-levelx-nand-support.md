---
id: "txmw-chapter-3-levelx-nand-support"
type: "concept"
domain: "rtos"
title: "Chapter 3 - LevelX NAND support"
summary: "NAND flash memory is commonly utilized for large data storage, which is typical of file systems. NAND memory consists of blocks. Within each NAND block is a series of pages."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter3.md"
license: "MIT"
mode: "V"
---

NAND flash memory is commonly utilized for large data storage, which is typical of file systems. NAND memory consists of *blocks*. Within each NAND block is a series of *pages*. NAND blocks are erasable, which means that all pages within the NAND block are erased (set to all ones). Each NAND block page has a set of *spare bytes* that are utilized by LevelX for bookkeeping, bad block management, and error detection. NAND block pages are available in a variety of sizes. The most common page sizes are: 

| **Page Size** | **Spare Bytes** |
| ------------- | --------------- |
| 256           | 8               |
| 512           | 16              |
| 2048          | 64              |

NAND memory differs from NOR memory in that there is no direct access, i.e., NAND memory cannot be read directly from the processor like NOR memory. NAND memory can only be written to after an erase a limited number of times. Again, this differs from NOR memory that can be written an unlimited number of times providing the write request is clearing set bits. Finally, the spare bytes associated with each page are unique to NAND flash. Typical spare byte configurations are as shown in the table below.

| **Spare Bytes** | **Byte numbers** | **Configuration**     |
| ------------------------- | -------------- | --------------------- |
| 8                         | Bytes 0-2:     | ECC bytes             |
|                           | Bytes 3,4,6,7: | LevelX Metadata       |
|                           | Byte 5:        | Bad block flag        |
| 16                        | Bytes 0-3,6-7: | ECC bytes             |
|                           | Bytes 8-11:    | LevelX Metadata       |
|                           | Bytes 12-15:   | Unused                |
|                           | Byte 5:        | Bad block flag        |
| 64                        | Byte 0:        | Bad block flag        |
|                           | Bytes 2-5:     | LevelX Metadata       |
|                           | Bytes 6-39:    | Unused                |
|                           | Bytes 40-63:   | ECC bytes             |

LevelX Utilizes 4 of the spare bytes of each NAND page for keeping track of the data stored in the each page. These 4 bytes are used to implement a 32-bit unsigned integer with a LevelX proprietary format. The upper 4 bits of the 32-bit field (bit 31 to bit 28) are used to indicate the data type stored in the page. The data type can be user sector data and metadata. If the data type indicate it as user sector data, the bit 28-0 of this field stores the logic sector number. If the data type indicate it as metadata, the bit 7-0 of this field stores the metadata page number. The format of the spare bytes is shown below.

**LevelX Spare Bytes Format**

| Bit(s) | Meaning |
| ------ | ------- |
| 31-29  | Data type. Specify the data type of the data stored in the page. It can be LevelX metadata or user sector data.  |
| 28-0   | Logical sector number, if the data type is user sector data. |
| 7-0    | Metadata page number if data type is metadata. |

LevelX utilizes a few NAND blocks for the metadata. The metadata blocks are used to store the mapping information between the logical block and the physical block and other tables used to keep track of the blocks and pages.
