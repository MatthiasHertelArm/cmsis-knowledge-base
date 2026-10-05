---
id: "spec-algorithm-functions-blankcheck"
type: "concept"
domain: "pack"
title: "Algorithm Functions: BlankCheck"
summary: "Blank Check - adr: Block start address - sz: Block size in bytes - pat: Pattern to compare Returns: status information: - 0 when the block content is equal to the pattern pat."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/flash_algorithms.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/algorithmFunc.html"
license: "Apache-2.0"
mode: "V"
---

```
int BlankCheck (unsigned long adr, unsigned long sz, unsigned char pat);
```
  Blank Check
- `adr`: Block start address
- `sz`:  Block size in bytes
- `pat`: Pattern to compare
Returns: status information:
- 0 when the block content is equal to the pattern pat.
- 1 when the block content differs from the pattern pat.

The function **BlankCheck** can be used to check whether the specified block is empty, or whether the content is equal to a
specific pattern defined in the argument _pat._

The argument _adr_ specifies the start address of the block that is to be verified.

The argument _sz_ specifies the size of the block that is to be verified.

**Code Example**
```
int BlankCheck (unsigned long adr, unsigned long sz, unsigned char pat) {
 
  unsigned long i, j, k;
 
  // Recalculate address for External SDRAM addresses
  if (adr >= SDRAM_START)
    adr = adr - SDRAM_START + USER_OFFSET;
 
  for (i = 0; i < sz; i += 256) {
    // Read 256 bytes
    ReadPage_HW (adr+i, 256, &rd_buf[0]);
 
    // Determine size to compare
    if ((sz-i) >= 256) k = 256;
    else               k = (sz-i);
 
    // Check up to 256 bytes if equal to pattern "pat"
    for (j = 0; j < k; j++)
      if (rd_buf[j] != pat) return (1); // Memory is not blank
  }
 
  return (0);                           // Memory is blank
}
```
