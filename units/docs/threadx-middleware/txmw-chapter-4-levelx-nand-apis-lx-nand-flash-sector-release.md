---
id: "txmw-chapter-4-levelx-nand-apis-lx-nand-flash-sector-release"
type: "concept"
domain: "rtos"
title: "Chapter 4 - LevelX NAND APIs: lx_nand_flash_sector_release"
summary: "This service releases the logical sector mapping in the NAND flash instance. Releasing a logical sector when not used makes the LevelX wear leveling more efficient."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter4.md#lx-nand-flash-sector-release"
license: "MIT"
mode: "V"
---

Release NAND flash sector

### Prototype

```c
UINT lx_nand_flash_sector_release(
    LX_NAND_FLASH *nand_flash,
    ULONG logical_sector);
```

### Description

This service releases the logical sector mapping in the NAND flash instance. Releasing a logical sector when not used makes the LevelX wear leveling more efficient.

### Input Parameters

- *nand_flash*: NAND flash instance pointer.
- *logical_sector*: Logical sector to release.

### Return Values

- **LX_SUCCESS**: (0x00) Successful request.
- **LX_ERROR**: (0x01) Error NAND flash sector write.

### Allowed From

Threads

### Example

```c
/* Release logical sector 20 of the NAND flash instance "my_nand_flash". */  
status = lx_nand_flash_sector_release(&my_nand_flash, 20);  
  
/* If status is LX_SUCCESS, logical sector 20 has been released. */
```

### See Also

- [levelx NAND Services](#NAND_Services)
