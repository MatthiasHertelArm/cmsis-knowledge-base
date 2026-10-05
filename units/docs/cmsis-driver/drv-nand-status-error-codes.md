---
id: "drv-nand-status-error-codes"
type: "concept"
domain: "drivers"
title: "NAND Status Error Codes"
summary: "Negative values indicate errors (NAND has specific codes in addition to common execution_status)."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
license: "Apache-2.0"
mode: "V"
---

Negative values indicate errors (NAND has specific codes in addition to common execution_status). 
 
The NAND driver has additional status error codes that are listed below.
Note that the NAND driver also returns the common execution_status. 
  

### ARM_NAND_ERROR_ECC

```c
ARM_NAND_ERROR_ECC
```

ECC generation or correction failed during ARM_NAND_ReadData, ARM_NAND_WriteData or ARM_NAND_ExecuteSequence.
