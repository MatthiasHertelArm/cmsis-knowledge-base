---
id: "abi-semihosting-for-aarch32-and-aarch6-sys-heapinfo-0x16"
type: "concept"
domain: "core"
title: "Semihosting for AArch32 and AArch64: Semihosting operations / `SYS_HEAPINFO (0x16)`"
summary: "Returns the system stack and heap parameters."
status: "draft"
collection: "arm-abi"
source: "ARM-software/abi-aa@a5e86d3:semihosting/semihosting.rst"
doc_source: "https://github.com/ARM-software/abi-aa/blob/a5e86d3/semihosting/semihosting.rst"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Semihosting operations_

Returns the system stack and heap parameters.


#### Entry


On entry, the PARAMETER REGISTER contains the address of a pointer to a four-field data block. The contents of the data block are filled by the function. The following C-like pseudocode describes the layout of the block:

```

struct block {
    void* heap_base;
    void* heap_limit;
    void* stack_base;
    void* stack_limit;
};
```

#### Return


On exit, the PARAMETER REGISTER is unchanged and the data block has been updated.
