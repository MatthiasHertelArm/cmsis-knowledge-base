---
id: "drv-mci-interface-arm-mci-initialize"
type: "concept"
domain: "drivers"
title: "MCI Interface: ARM_MCI_Initialize"
summary: "The function ARM_MCI_Initialize initializes the MCI interface. It is called when the middleware component starts operation."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_MCI_Initialize (ARM_MCI_SignalEvent_t cb_event)
```


The function **ARM_MCI_Initialize** initializes the MCI interface. 
It is called when the middleware component starts operation.

The function performs the following operations:
  - Initializes the resources needed for the MCI interface.
  - Registers the ARM_MCI_SignalEvent callback function.

The parameter **cb_event** is a pointer to the ARM_MCI_SignalEvent callback function; use a NULL pointer 
when no callback signals are required.

**Example:**
 - see mci_interface_gr - Driver Functions

******************************************************************************************************************
