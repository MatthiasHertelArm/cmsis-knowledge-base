---
id: "drv-mci-interface-arm-mci-uninitialize"
type: "concept"
domain: "drivers"
title: "MCI Interface: ARM_MCI_Uninitialize"
summary: "The function ARMMCIUninitialize de-initializes the resources of I2C interface."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_MCI_Uninitialize (void)
```


The function **ARM_MCI_Uninitialize** de-initializes the resources of I2C interface.

It is called when the middleware component stops operation and releases the software resources used by the interface.
******************************************************************************************************************
