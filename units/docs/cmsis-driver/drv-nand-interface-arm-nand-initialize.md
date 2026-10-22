---
id: "drv-nand-interface-arm-nand-initialize"
type: "concept"
domain: "drivers"
title: "NAND Interface: ARM_NAND_Initialize"
summary: "The function ARM_NAND_Initialize initializes the NAND interface. It is called when the middleware component starts operation."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_NAND.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_NAND_Initialize (ARM_NAND_SignalEvent_t  cb_event)
```


The function **ARM_NAND_Initialize** initializes the NAND interface. 
It is called when the middleware component starts operation.

The function performs the following operations:
  - Initializes the resources needed for the NAND interface.
  - Registers the ARM_NAND_SignalEvent callback function.

The parameter **cb_event** is a pointer to the ARM_NAND_SignalEvent callback function; use a NULL pointer 
when no callback signals are required.

**Example:**
 - see nand_interface_gr - Driver Functions

******************************************************************************************************************
