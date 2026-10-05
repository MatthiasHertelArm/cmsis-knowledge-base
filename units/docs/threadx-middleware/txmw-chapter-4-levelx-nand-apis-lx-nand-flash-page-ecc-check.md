---
id: "txmw-chapter-4-levelx-nand-apis-lx-nand-flash-page-ecc-check"
type: "concept"
domain: "rtos"
title: "Chapter 4 - LevelX NAND APIs: lx_nand_flash_page_ecc_check"
summary: "Check page for ECC errors with correction"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/levelx/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/levelx/chapter4.md#lx-nand-flash-page-ecc-check"
license: "MIT"
mode: "V"
---

Check page for ECC errors with correction

### Prototype

```c
UINT lx_nand_flash_page_ecc_check(
    LX_NAND_FLASH *nand_flash,  
    UCHAR *page_buffer, 
    UCHAR *ecc_buffer);
```

### Description

This service verifies the integrity of the supplied NAND page buffer with the supplied ECC. Page size (defined in the NAND flash instance pointer) is assumed to be a multiple of 256-bytes and the ECC code supplied is capable of correcting a 1 bit error in each 256-byte portion of the page.

### Input Parameters

- *nand_flash*: NAND flash instance pointer.
- *page_buffer*: Pointer to NAND flash page buffer.
- *ecc_buffer*: Pointer to ECC for NAND flash page. Note that there are 3 ECC bytes per 256-byte portion of the page.

### Return Values

- **LX_SUCCESS**: (0x00) NAND page has no errors.
- **LX_NAND_ERROR_CORRECTED**: (0x06) One or more 1-bit errors were corrected in the NAND page—correction(s) are in the page buffer.
- **LX_NAND_ERROR_NOT_CORRECTED**: (0x07) Too many errors to correct on the NAND page.

### Allowed From

LevelX Driver

### Example

```c
/* Check the NAND page pointed to by "page_pointer" of the NAND flash instance "my_nand_flash" . */
status = lx_nand_flash_page_ecc_check(&my_nand_flash, page_pointer, ecc_pointer);  
  
/* If status is LX_SUCCESS the page is valid. */
```

### See Also

- [levelx NAND Services](#NAND_Services)
