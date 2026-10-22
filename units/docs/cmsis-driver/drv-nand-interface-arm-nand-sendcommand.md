---
id: "drv-nand-interface-arm-nand-sendcommand"
type: "concept"
domain: "drivers"
title: "NAND Interface: ARM_NAND_SendCommand"
summary: "The function ARM_NAND_SendCommand sends a command to the NAND device."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_NAND_SendCommand (uint32_t dev_num, uint8_t cmd)
```


The function **ARM_NAND_SendCommand** sends a command to the NAND device.

The parameter **dev_num** is the device number. \n
The parameter **cmd** is the command sent to the NAND device.
******************************************************************************************************************
