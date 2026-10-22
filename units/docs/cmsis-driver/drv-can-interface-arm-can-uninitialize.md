---
id: "drv-can-interface-arm-can-uninitialize"
type: "concept"
domain: "drivers"
title: "CAN Interface: Remote Frame / ARM_CAN_Uninitialize"
summary: "The function ARM_CAN_Uninitialize de-initializes the resources of the CAN interface. It is called to release the software resources used by the interface such as deallocate any RTOS objects, dynamic memory and pin de-configuration."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
license: "Apache-2.0"
mode: "V"
---

_Part of: Remote Frame_

```c
int32_t ARM_CAN_Uninitialize (void)
```


The function **ARM_CAN_Uninitialize** de-initializes the resources of the CAN interface.
It is called to release the software resources used by the interface such as deallocate any RTOS objects, dynamic memory and pin de-configuration.
******************************************************************************************************************
