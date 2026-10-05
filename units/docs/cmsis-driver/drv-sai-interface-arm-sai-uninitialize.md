---
id: "drv-sai-interface-arm-sai-uninitialize"
type: "concept"
domain: "drivers"
title: "SAI Interface: User Defined Protocol / ARM_SAI_Uninitialize"
summary: "The function ARMSAIUninitialize de-initializes the resources of SAI interface."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
license: "Apache-2.0"
mode: "V"
---

_Part of: User Defined Protocol_

```c
int32_t ARM_SAI_Uninitialize (void)
```


The function **ARM_SAI_Uninitialize** de-initializes the resources of SAI interface.

It is called when the middleware component stops operation and releases the software resources used by the interface.
****************************************************************************************************************
