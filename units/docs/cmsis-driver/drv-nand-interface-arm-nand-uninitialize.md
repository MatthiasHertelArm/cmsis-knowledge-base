---
id: "drv-nand-interface-arm-nand-uninitialize"
type: "concept"
domain: "drivers"
title: "NAND Interface: ARM_NAND_Uninitialize"
summary: "The function ARM_NAND_Uninitialize de-initializes the resources of NAND interface."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_NAND_Uninitialize (void)
```


The function **ARM_NAND_Uninitialize** de-initializes the resources of NAND interface.

It is called when the middleware component stops operation and releases the software resources used by the interface.
******************************************************************************************************************
