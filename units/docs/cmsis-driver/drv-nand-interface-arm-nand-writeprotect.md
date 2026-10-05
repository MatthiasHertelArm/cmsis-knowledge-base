---
id: "drv-nand-interface-arm-nand-writeprotect"
type: "concept"
domain: "drivers"
title: "NAND Interface: ARM_NAND_WriteProtect"
summary: "The function ARMNANDWriteProtect controls the Write Protect (WPn) pin of a NAND device."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_NAND_WriteProtect (uint32_t dev_num, bool enable)
```


The function **ARM_NAND_WriteProtect** controls the Write Protect (WPn) pin of a NAND device.

The parameter **dev_num** is the device number. \n 
The parameter **enable** specifies whether to enable or disable write protection.
******************************************************************************************************************
