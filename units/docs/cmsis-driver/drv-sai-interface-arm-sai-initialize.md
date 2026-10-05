---
id: "drv-sai-interface-arm-sai-initialize"
type: "concept"
domain: "drivers"
title: "SAI Interface: User Defined Protocol / ARM_SAI_Initialize"
summary: "The function ARM_SAI_Initialize initializes the SAI interface. It is called when the middleware component starts operation."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
license: "Apache-2.0"
mode: "V"
---

_Part of: User Defined Protocol_

```c
int32_t ARM_SAI_Initialize (ARM_SAI_SignalEvent_t cb_event)
```


The function **ARM_SAI_Initialize** initializes the SAI interface. It is called when the middleware component starts
operation.

The function performs the following operations:
  - Initializes the required resources of the SAI interface.
  - Registers the ARM_SAI_SignalEvent callback function.

The parameter **cb_event** is a pointer to the ARM_SAI_SignalEvent callback function; use a NULL pointer 
when no callback signals are required.
****************************************************************************************************************
