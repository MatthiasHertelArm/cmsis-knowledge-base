---
id: "spec-algorithm-functions-erasechip"
type: "concept"
domain: "pack"
title: "Algorithm Functions: EraseChip"
summary: "Returns: status information: - 0 on success. - 1 on failure."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/flash_algorithms.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/algorithmFunc.html"
license: "Apache-2.0"
mode: "V"
---

```
int EraseChip (void);
```
Returns: status information:
        - 0 on success.
        - 1 on failure.

The function **EraseChip** deletes the content of the entire Flash memory. It is invoked whenever the uVision menu
**Flash** - **Erase** is used, or whenever an attempt is made to download the program to Flash and the option
**Erase Full Chip** has been set in the **Flash Download Setup** dialog. If this function is missing in the Flash
Programming Algorithm, the EraseSector function is executed until the entire content of the Flash memory area has been
deleted.

**Code Example**
```
int EraseChip (void) {
 
  FLASH->CR |=  FLASH_MER;                      // Mass Erase Enabled
  FLASH->CR |=  FLASH_STRT;                     // Start Erase
 
  while (FLASH->SR & FLASH_BSY) {
    IWDG->KR = 0xAAAA;                          // Reload IWDG
  }
 
  FLASH->CR &= ~FLASH_MER;                      // Mass Erase Disabled
 
  return (0);                                   // Done
}
```
