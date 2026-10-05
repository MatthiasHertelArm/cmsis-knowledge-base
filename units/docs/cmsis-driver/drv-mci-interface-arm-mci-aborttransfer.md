---
id: "drv-mci-interface-arm-mci-aborttransfer"
type: "concept"
domain: "drivers"
title: "MCI Interface: ARM_MCI_AbortTransfer"
summary: "The function ARMMCIAbortTransfer aborts the active data transfer operation initiated with ARMMCISendCommand."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_MCI_AbortTransfer (void)
```


The function **ARM_MCI_AbortTransfer** aborts the active data transfer operation initiated with ARM_MCI_SendCommand.
******************************************************************************************************************
