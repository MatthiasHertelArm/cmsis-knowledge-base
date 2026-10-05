---
id: "drv-can-interface-arm-can-objectgetcapabilities"
type: "concept"
domain: "drivers"
title: "CAN Interface: Remote Frame / ARM_CAN_ObjectGetCapabilities"
summary: "The function ARM_CAN_ObjectGetCapabilities retrieves the capabilities of a CAN object. The structure ARM_CAN_OBJ_CAPABILITIES stores the values."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
license: "Apache-2.0"
mode: "V"
---

_Part of: Remote Frame_

```c
ARM_CAN_OBJ_CAPABILITIES ARM_CAN_ObjectGetCapabilities (uint32_t obj_idx)
```


The function **ARM_CAN_ObjectGetCapabilities** retrieves the capabilities of a CAN object. 
The structure ARM_CAN_OBJ_CAPABILITIES stores the values.

The parameter **obj_idx** is the message object index.

\sa ARM_CAN_ObjectConfigure
\sa ARM_CAN_ObjectSetFilter
*************************************************************************************************************************
