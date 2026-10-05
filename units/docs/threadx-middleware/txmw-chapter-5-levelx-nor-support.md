---
id: "txmw-chapter-5-levelx-nor-support"
type: "concept"
domain: "rtos"
title: "Chapter 5 - LevelX NOR support"
summary: "NOR flash memory is composed of blocks that are typically evenly divisible by 512 bytes. There are no concept of a flash page in NOR flash memory."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter5.md"
license: "MIT"
mode: "V"
---

NOR flash memory is composed of *blocks* that are typically evenly divisible by 512 bytes. There are no concept of a flash *page* in NOR flash memory. Also, there are no *spare* bytes in NOR flash memory, hence LevelX must use the NOR flash memory itself for all management information. Direct read access is possible in NOR flash memory. Write access typically requires a special sequence of operations. NOR flash memory may be written to multiple times, providing that bits are being cleared. Bits in NOR flash memory can only be set once, via the erase block operation.

LevelX divides each NOR flash block into 512-byte logical *sectors*. Furthermore, LevelX uses the first "n" sectors of each NOR flash block to store management information. The format of the LevelX NOR flash memory management information is:

**LevelX NOR Block Format**

| Byte Offset  | Contents                     |
| ------------ | ---------------------------- |
| 0            | [Block Erase Count]          |
| 4            | [Minimum Mapped Sector]      |
| 8            | [Maximum Mapped Sector]      |
| 12           | [Free Sector Bit Map]        |
| m            | [Sector 0 Mapping Entry]     |
|              | …                            |
| m+4*(n-1)    | [Sector "n" Mapping Entry]   |
|              | …                            |
| s            | [Sector 0 Contents]          |
|              | …                            |
| s+512*(n-1) | [Sector "n" Contents]         |

The 32-bit *Block Erase Count* contains the number of times the block has been erased. The main goal of LevelX is to keep the erase count of all blocks relatively close to help prevent any one block from wearing out prematurely. The 32-bit *Minimum Mapped Sector* and *Maximum Mapped Sector* fields are written only when all the logical sectors in the block have been mapped and written to. These fields are useful for optimization of the sector read operation. The *Free Sector Bit Map* entry is a bit map where each set bit corresponds to an unmapped sector in the block. This field is used to make the free sector search more efficient. This is a variable length field that requires one word for every 32 sectors in the block. The *Sector Mapping Entry* array contains mapping information for each sector in the block. Each entry has the following format:

**Sector Mapping Entry**

| Bit(s) | Meaning  |
| ------ | -------- |
| 31     | Valid flag. When set and logical sector not all ones indicates mapping is valid |
| 30     | Obsolete flag. When clear, this mapping is either obsolete or is in the process of becoming obsolete. |
| 29     | Mapping entry write is complete when this bit is 0 |
| 0-28   | Logical sector mapped to this physical sector—when not all ones. |

The upper bit of the 32-bit field (bit 31) is used to indicate the logical sector mapping is valid. If this bit is 0, the information in this entry (and corresponding sector contents) is no longer valid. The next bit - bit 30 - is used to indicate this sector is in the process of becoming obsolete and a new sector is being written. Bit 29 is used to indicate when the mapping entry write is complete. If bit 29 is 0, the mapping entry write is complete. If bit 29 is set, the mapping entry was in the process of being written. Bits 30 and 29 are used in recovering from a potential power loss while updating a new sector mapping. Finally, the lower 29-bits (28-0) contain the logical sector number for the sector. If a sector has not been mapped, all bits will be set, i.e., it will have a value of 0xFFFFFFFF.
