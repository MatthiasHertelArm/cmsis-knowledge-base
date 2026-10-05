---
id: "drv-nand-interface-arm-nand-abortsequence"
type: "concept"
domain: "drivers"
title: "NAND Interface: ARM_NAND_AbortSequence"
summary: "The function ARMNANDAbortSequence aborts execution of the current sequence for a NAND device."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_NAND_AbortSequence (uint32_t dev_num)
```


The function **ARM_NAND_AbortSequence** aborts execution of the current sequence for a NAND device.

The parameter **dev_num** is the device number.
******************************************************************************************************************
