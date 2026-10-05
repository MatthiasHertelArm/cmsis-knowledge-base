---
id: "drv-can-interface-arm-can-obj-capabilities"
type: "concept"
domain: "drivers"
title: "CAN Interface: Remote Frame / ARM_CAN_OBJ_CAPABILITIES"
summary: "A CAN object can be implemented with different capabilities encoded in the data fields of this structure."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
license: "Apache-2.0"
mode: "V"
---

_Part of: Remote Frame_

```c
ARM_CAN_OBJ_CAPABILITIES
```


A CAN object can be implemented with different capabilities encoded in the 
data fields of this structure.

**Returned by**:
 - ARM_CAN_ObjectGetCapabilities

\sa ARM_CAN_ObjectConfigure
\sa ARM_CAN_MessageSend
\sa ARM_CAN_MessageRead
\sa ARM_CAN_MSG_INFO
\sa can_filtering
****************************************************************************************************************
