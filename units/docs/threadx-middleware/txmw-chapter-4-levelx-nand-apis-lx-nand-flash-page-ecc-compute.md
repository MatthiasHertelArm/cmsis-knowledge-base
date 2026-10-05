---
id: "txmw-chapter-4-levelx-nand-apis-lx-nand-flash-page-ecc-compute"
type: "concept"
domain: "rtos"
title: "Chapter 4 - LevelX NAND APIs: lx_nand_flash_page_ecc_compute"
summary: "This service computes the ECC of the supplied NAND page buffer and returns the ECC in the supplied ECC buffer. Page size is assume to be a multiple of 256-bytes (defined in the NAND flash instance pointer)."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter4.md#lx-nand-flash-page-ecc-compute"
license: "MIT"
mode: "V"
---

Compute ECC for page

### Prototype

```c
UINT lx_nand_flash_page_ecc_compute(
    LX_NAND_FLASH *nand_flash,  
    UCHAR *page_buffer, 
    UCHAR *ecc_buffer);
```

### Description

This service computes the ECC of the supplied NAND page buffer and returns the ECC in the supplied ECC buffer. Page size is assume to be a multiple of 256-bytes (defined in the NAND flash instance pointer). The ECC code is used to verify the integrity of the page when it is read at a later time.

### Input Parameters

- *nand_flash*: NAND flash instance pointer.
- *page_buffer*: Pointer to NAND flash page buffer.
- *ecc_buffer*: Pointer to destination for ECC of the NAND flash page. Note that must be 3 bytes of ECC storage per 256-byte portion of the page. For example, a 2048 byte page would require 24 bytes for the ECC.

### Return Values

- **LX_SUCCESS**: (0x00) ECC successfully calculated.
- **LX_ERROR**: (0x01) Error calculating ECC.

### Allowed From

LevelX Driver

### Example

```c
/* Compute ECC for the NAND page pointed to by "page_pointer" of the NAND flash instance "my_nand_flash". */  
status = lx_nand_flash_page_ecc_compute(&my_nand_flash, page_pointer, ecc_pointer);  
  
/* If status is LX_SUCCESS the ECC was calculated and Can be found in the memory pointed to by "ecc_pointer." */
```

### See Also

- [levelx NAND Services](#NAND_Services)
