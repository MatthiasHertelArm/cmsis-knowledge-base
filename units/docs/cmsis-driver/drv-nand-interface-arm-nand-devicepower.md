---
id: "drv-nand-interface-arm-nand-devicepower"
type: "concept"
domain: "drivers"
title: "NAND Interface: ARM_NAND_DevicePower"
summary: "The function ARM_NAND_DevicePower controls the power supply of the NAND device."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_NAND_DevicePower (uint32_t voltage)
```


The function **ARM_NAND_DevicePower** controls the power supply of the NAND device.

The parameter **voltage** sets the device supply voltage as defined in the table.

**AMR_NAND_POWER_xxx_xxx** specifies power settings.

Device Power Bits                | Description
:--------------------------------|:--------------------------------------------
ARM_NAND_POWER_VCC_OFF      | Set VCC Power off
ARM_NAND_POWER_VCC_3V3      | Set VCC = 3.3V
ARM_NAND_POWER_VCC_1V8      | Set VCC = 1.8V
ARM_NAND_POWER_VCCQ_OFF     | Set VCCQ I/O Power off
ARM_NAND_POWER_VCCQ_3V3     | Set VCCQ = 3.3V
ARM_NAND_POWER_VCCQ_1V8     | Set VCCQ = 1.8V
ARM_NAND_POWER_VPP_OFF      | Set VPP off
ARM_NAND_POWER_VPP_ON       | Set VPP on

******************************************************************************************************************
