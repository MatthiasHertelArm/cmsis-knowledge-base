---
id: "drv-sai-interface-arm-sai-getrxcount"
type: "concept"
domain: "drivers"
title: "SAI Interface: User Defined Protocol / ARM_SAI_GetRxCount"
summary: "The function ARMSAIGetRxCount returns the number of the currently received data items during an ARMSAIReceive operation."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
license: "Apache-2.0"
mode: "V"
---

_Part of: User Defined Protocol_

```c
uint32_t ARM_SAI_GetRxCount (void)
```


The function **ARM_SAI_GetRxCount** returns the number of the currently received data items during an ARM_SAI_Receive
operation.
****************************************************************************************************************
