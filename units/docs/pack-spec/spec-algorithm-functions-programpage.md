---
id: "spec-algorithm-functions-programpage"
type: "concept"
domain: "pack"
title: "Algorithm Functions: ProgramPage"
summary: "The function ProgramPage is used to write code into the Flash memory. It is invoked to download a program to Flash."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/flash_algorithms.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/algorithmFunc.html"
license: "Apache-2.0"
mode: "V"
---

```
int ProgramPage (unsigned long adr, unsigned long sz, unsigned char *buf);
```
- `adr`: Page start address
- `sz`: Page size
- `buf`: Data to be written
Returns: status information:
        - 0 on success.
        - 1 on failure.


The function **ProgramPage** is used to write code into the Flash memory. It is invoked  to
download a program to Flash. As Flash memory is typically organized in blocks or pages, the parameters to the function **ProgramPage** 
must not cross alignment boundaries of these flash pages.  The page size is specified in the struct FlashDevice with the value
**Program Page Size**.

The argument _adr_ specifies the start address of the page that is to be programmed. It is aligned by the host programming system to a start address
of a flash page.

The argument _sz_ specifies the data size in the data buffer.  The host programming system ensures that page boundaries are not crossed.

The argument _buf_ points to the data buffer containing the data to be programmed.

**Note:**
The host programming system ensures that the argument _adr_ + _sz_ never crosses any page boundary.  The function **ProgramPage** does therefore not
require any provisions for that.

**Code Example**
```
int ProgramPage (unsigned long adr, unsigned long sz, unsigned char *buf) {
 
  sz = (sz + 1) & ~1;                           // Adjust size for Half Words
 
  while (sz) {
 
    FLASH->CR |=  FLASH_PG;                     // Programming Enabled
 
    M16(adr) = *((unsigned short *)buf);        // Program Half Word
    while (FLASH->SR & FLASH_BSY);
 
    FLASH->CR &= ~FLASH_PG;                     // Programming Disabled
 
    // Check for Errors
    if (FLASH->SR & (FLASH_PGERR | FLASH_WRPRTERR)) {
      FLASH->SR |= FLASH_PGERR | FLASH_WRPRTERR;
      return (1);                               // Failed
    }
 
    // Go to next Half Word
    adr += 2;
    buf += 2;
    sz  -= 2;
 
  }
 
  return (0);                                   // Done
}
```
