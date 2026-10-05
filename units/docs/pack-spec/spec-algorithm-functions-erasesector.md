---
id: "spec-algorithm-functions-erasesector"
type: "concept"
domain: "pack"
title: "Algorithm Functions: EraseSector"
summary: "The function EraseSector deletes the content of the sector starting at the address specified by the argument adr."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/flash_algorithms.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/algorithmFunc.html"
license: "Apache-2.0"
mode: "V"
---

```
int EraseSector (unsigned long adr);
```
- `adr`: Sector address
Returns: status information:
        - 0 on success.
        - 1 on failure.


The function **EraseSector** deletes the content of the sector starting at the address specified by the argument _adr._ The
function is invoked whenever the uVision menu **Flash** - **Erase** is used, or whenever an attempt is made to download the
program to Flash and the option **Erase Sectors** has been set in the **Flash Download Setup** dialog.

**Code Example**
```
int EraseSector (unsigned long adr) {
 
  FLASH->CR |=  FLASH_PER;                      // Page Erase Enabled
  FLASH->AR  =  adr;                            // Page Address
  FLASH->CR |=  FLASH_STRT;                     // Start Erase
 
  while (FLASH->SR & FLASH_BSY) {
    IWDG->KR = 0xAAAA;                          // Reload IWDG
  }
 
  FLASH->CR &= ~FLASH_PER;                      // Page Erase Disabled
 
  return (0);                                   // Done
}
```
