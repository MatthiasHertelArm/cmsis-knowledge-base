---
id: "drv-flash-interface-arm-flash-initialize"
type: "concept"
domain: "drivers"
title: "Flash Interface: ARM_Flash_Initialize"
summary: "The function ARM_Flash_Initialize initializes the Flash interface. It is called when the middleware component starts operation."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_Flash.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_Flash.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_Flash_Initialize (ARM_Flash_SignalEvent_t cb_event)
```


The function **ARM_Flash_Initialize** initializes the Flash interface.
It is called when the middleware component starts operation.

The function performs the following operations:
  - Initializes the resources needed for the Flash interface.
  - Registers the ARM_Flash_SignalEvent callback function.

The parameter **cb_event** is a pointer to the ARM_Flash_SignalEvent callback function; use a NULL pointer 
when no callback signals are required.

**Example:**
 - see flash_interface_gr - Driver Functions

******************************************************************************************************************
