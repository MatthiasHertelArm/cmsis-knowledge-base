---
id: "spec-algorithm-functions-verify"
type: "concept"
domain: "pack"
title: "Algorithm Functions: Verify"
summary: "The function Verify compares the content of the Flash memory with the program code buf."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/flash_algorithms.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/algorithmFunc.html"
license: "Apache-2.0"
mode: "V"
---

```
unsigned long Verify (unsigned long adr, unsigned long sz, unsigned char *buf);
```
- `adr`: Start address
- `sz`: Size in bytes
- `buf`: Data to be compared
Returns: status information:
        - the sum of (adr+sz) - on success.
        - any other number - on failure, and represents the failing address.


The function **Verify** compares the content of the Flash memory with the program code _*buf._

The argument _adr_ specifies the start address for the verification.

The argument _sz_ specifies the size of the verification.

The argument _buf_ points to the buffer containing the data to be verified.

**Code Example**
```
unsigned long Verify (unsigned long adr, unsigned long sz, unsigned char *buf) {
  unsigned long i, adr_dest, in_page_ofs;
 
  if (adr < block_size) {               // Verifying 2-nd level bootloader data
    adr_dest = adr + page_usr_size;     // skip page 0 of block 0
  } else {                              // Verifying program data
    FindBlock(adr, 0);
    adr_dest  = nand_block_offset + (adr & (block_size-1));
  }
  in_page_ofs = adr_dest & (page_usr_size-1);
 
  if (ReadPage_HW(adr_dest, page_usr_size, data_buf)) return (1);
  for (i=0; i<sz; i++)
    if (buf[i] != data_buf[i+in_page_ofs])
      break;
 
  return (adr+i);
}
```
