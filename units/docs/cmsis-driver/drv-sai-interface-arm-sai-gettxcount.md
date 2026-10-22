---
id: "drv-sai-interface-arm-sai-gettxcount"
type: "concept"
domain: "drivers"
title: "SAI Interface: User Defined Protocol / ARM_SAI_GetTxCount"
summary: "The function ARM_SAI_GetTxCount returns the number of the currently transmitted data items during an ARM_SAI_Send operation."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
license: "Apache-2.0"
mode: "V"
---

_Part of: User Defined Protocol_

```c
uint32_t ARM_SAI_GetTxCount (void)
```


The function **ARM_SAI_GetTxCount** returns the number of the currently transmitted data items during an ARM_SAI_Send
operation.
****************************************************************************************************************
