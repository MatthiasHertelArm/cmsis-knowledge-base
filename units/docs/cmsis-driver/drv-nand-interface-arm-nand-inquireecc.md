---
id: "drv-nand-interface-arm-nand-inquireecc"
type: "concept"
domain: "drivers"
title: "NAND Interface: ARM_NAND_InquireECC"
summary: "The function ARM_NAND_InquireECC reads error correction code information."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_NAND_InquireECC (int32_t index, ARM_NAND_ECC_INFO *info)
```


The function **ARM_NAND_InquireECC** reads error correction code information.

The parameter **index** is the ECC index and is used to retrieve different ECC configurations. \n
The parameter **info** is a pointer of type ARM_NAND_ECC_INFO. The data fields store the information.

When multiple different ECC configurations exist, ARM_NAND_ECC_INFO structure exists for each configuration. Parameter
**index** denotes which configuration will be retrieved. Value of index should start with zero to retrieve first ECC
configuration and should be incremented in order to retrieve next ECC configuration. When index is out of range function
ARM_NAND_InquireECC returns with error.

Parameter **index** is used by ARM_NAND_ECC(n) in ARM_NAND_ReadData, ARM_NAND_WriteData and
ARM_NAND_ExecuteSequence to select suitable ECC configuration.

**Example**
```
extern ARM_DRIVER_NAND Driver_NAND0; 

ARM_NAND_ECC_INFO ecc;
int32_t idx;
 
idx = 0;
while (Driver_NAND0.InquireECC (idx, &ecc) == ARM_DRIVER_OK) {
  // Examine retrieved ECC configuration
  if (ecc.type == 2) {
    // Algorithm ECC0 protects Main+Spare
  }
  // ..
  idx++;
}
```
******************************************************************************************************************
