---
id: "drv-nand-interface-arm-nand-getstatus"
type: "concept"
domain: "drivers"
title: "NAND Interface: ARM_NAND_GetStatus"
summary: "The function ARM_NAND_GetStatus returns the current NAND device status."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_NAND_STATUS ARM_NAND_GetStatus (uint32_t dev_num)
```


The function **ARM_NAND_GetStatus** returns the current NAND device status.

The parameter **dev_num** is the device number.
******************************************************************************************************************
