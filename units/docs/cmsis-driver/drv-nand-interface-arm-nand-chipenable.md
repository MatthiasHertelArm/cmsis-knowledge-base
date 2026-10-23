---
id: "drv-nand-interface-arm-nand-chipenable"
type: "concept"
domain: "drivers"
title: "NAND Interface: ARM_NAND_ChipEnable"
summary: "The function ARM_NAND_ChipEnable control the Chip Enable (CEn) pin of a NAND device."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_NAND_ChipEnable (uint32_t dev_num, bool enable)
```


The function **ARM_NAND_ChipEnable** control the Chip Enable (CEn) pin of a NAND device.

The parameter **dev_num** is the device number. \n 
The parameter **enable** specifies whether to enable or disable the device.

This function is optional and supported only when the data field **ce_manual** = `1` in the structure ARM_NAND_CAPABILITIES.
Otherwise, the Chip Enable (CEn) signal is controlled automatically by SendCommand/Address, Read/WriteData and ExecuteSequence 
(for example when the NAND device is connected to a memory bus).
******************************************************************************************************************
