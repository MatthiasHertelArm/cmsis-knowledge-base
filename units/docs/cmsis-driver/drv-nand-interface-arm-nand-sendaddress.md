---
id: "drv-nand-interface-arm-nand-sendaddress"
type: "concept"
domain: "drivers"
title: "NAND Interface: ARM_NAND_SendAddress"
summary: "Send an address to the NAND device. The parameter dev_num is the device number. The parameter addr is the address."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_NAND_SendAddress (uint32_t dev_num, uint8_t addr)
```


Send an address to the NAND device.
The parameter **dev_num** is the device number.
The parameter **addr** is the address.
******************************************************************************************************************
